import os
import re
import unittest
from typing import Optional, Callable

from rdflib import Graph, Namespace, OWL
from rdflib.compare import to_isomorphic, graph_diff

from biolinkml import METAMODEL_NAMESPACE, MODULE_DIR
from biolinkml.utils.generator import Generator
from tests.test_scripts.clicktestcase import ClickTestCase
from tests.utils.compare_directories import are_dir_trees_equal
from tests.utils.dirutils import make_and_clear_directory

BIOLINK_NS = Namespace("https://w3id.org/biolink/vocab/")

# ShEx validation of the biolink model takes a loooong time, so we only do it on rare occasions
DO_SHEX_VALIDATION = False


class GeneratorTestCase(unittest.TestCase):
    source_path: str = None
    target_path: str = None
    model_path: str = None
    model_name: str = None
    output_name: str = None             # If different than model name

    @classmethod
    def setUpClass(cls) -> None:
        assert cls.source_path and cls.target_path and cls.model_path and cls.model_name, "Paths must be set"

    @staticmethod
    def _print_triples(g: Graph):
        """ Pretty print the contents of g, removing the prefix declarations """
        g.bind('BIOLINK', BIOLINK_NS)
        g.bind('meta', METAMODEL_NAMESPACE)
        g.bind('owl', OWL)
        g_text = re.sub(r'@prefix.*\n', '', g.serialize(format="turtle").decode())
        print(g_text)

    def _default_comparator(self, old_data: str, new_data: str, new_file: str, msg: Optional[str] = None) -> None:
        """ Simple file comparator.  Compare old to new and, if they don't match, save an image of new in
        new_file and raise an error

        :param old_data: Expected data
        :param new_data: Actual data
        :param new_file: Save actual data here if mismatch
        :param msg: If present add to the assert message
        :return:
        """
        self.maxDiff = None
        if old_data != new_data:
            if msg:
                print(msg)
            with open(new_file, 'w') as newf:
                newf.write(new_data)
            if len(new_data) > 20000:
                print(ClickTestCase.closein_comparison(old_data, new_data))
            self.assertEqual(old_data, new_data)

    def rdf_comparator(self, old_data: str, new_data: str, new_file: str, msg: Optional[str] = None) -> None:
        """
        RDF comparator.  Compare two graphs and, if they don't match, save a turtle image of new_data in
        new_file and raise an error
        :param old_data: Turtle representation of expected RDF
        :param new_data: Turtle representation of actual RDF
        :param new_file: Save actual RDF here if mismatch
        :param msg: If present, add to assert message
        :return:
        """
        old_graph = Graph()
        new_graph = Graph()
        old_graph.parse(data=old_data, format="turtle")
        new_graph.parse(data=new_data, format="turtle")
        old_iso = to_isomorphic(old_graph)
        # Remove the metadata specific triples
        for t in list(old_iso.triples((None, METAMODEL_NAMESPACE.generation_date, None))):
            old_iso.remove(t)
        for t in list(old_iso.triples((None, METAMODEL_NAMESPACE.source_file_date, None))):
            old_iso.remove(t)
        new_iso = to_isomorphic(new_graph)
        for t in list(new_iso.triples((None, METAMODEL_NAMESPACE.generation_date, None))):
            new_iso.remove(t)
        for t in list(new_iso.triples((None, METAMODEL_NAMESPACE.source_file_date, None))):
            new_iso.remove(t)

        in_both, in_old, in_new = graph_diff(old_iso, new_iso)
        # Graph compare takes a Looong time
        # if old_iso != new_iso:
        #     in_both, in_old, in_new = graph_diff(old_iso, new_iso)
        old_len = len(list(in_old))
        new_len = len(list(in_new))
        if old_len or new_len:
            if old_len:
                print("----- Old graph only -----")
                self._print_triples(in_old)
            if new_len:
                print("----- New Grapn Only -----")
                self._print_triples(in_new)
            with open(new_file, 'w') as newf:
                newf.write(new_data)
            self.assertTrue(False, "RDF file mismatch" if not msg else msg)

    def single_file_generator(self, suffix: str, gen: type(Generator), *,
                              format: Optional[str] = None,
                              generator_args: Optional[dict] = None,
                              serialize_args: Optional[dict] = None,
                              filtr: Optional[Callable[[str], str]] = None,
                              comparator: Callable[[type(unittest.TestCase), str, str, str], None] = None,
                              preserve_metadata: bool = False) -> None:
        """ Invoke Generator gen.  If

        :param suffix: File suffix (without '.')
        :param gen: Generator to invoke
        :param format: Generator format argument
        :param generator_args: Additional arguments to the generator
        :param serialize_args: Arguments to serializer.
        :param filtr: Filter to remove metadata specific info from the output.  Default: identity
        :param comparator: Comparison method to use.  Default: GeneratorTestCase._default_comparator
        :param preserve_metadata: True means metadata is to preserved in old_file
        """
        if serialize_args is None:
            serialize_args = {}
        if generator_args is None:
            generator_args = {}
        if format:
            generator_args["format"] = format
        if filtr is None:
            def filtr(s): return s
        if comparator is None:
            comparator = GeneratorTestCase._default_comparator
        output_base = self.output_name if self.output_name else self.model_name
        old_file = os.path.join(self.source_path, output_base + '.' + suffix)
        new_file = os.path.join(self.target_path, output_base + '.' + suffix)
        message = \
            f"\n***** Move {os.path.relpath(new_file, MODULE_DIR)} to {os.path.relpath(old_file, MODULE_DIR)} *****\n"
        yaml_file = os.path.join(self.model_path, self.model_name + '.yaml')
        if os.path.exists(new_file):
            os.remove(new_file)

        new_data = str(gen(yaml_file, **generator_args).serialize(**serialize_args))

        if not os.path.exists(old_file):
            with open(old_file, 'w') as oldf:
                oldf.write(new_data if preserve_metadata else filtr(new_data))
            self.assertTrue(False, f"Created {old_file} - run again")

        with open(old_file) as oldf:
            old_data = filtr(oldf.read())
        comparator(self, old_data, filtr(new_data), new_file, message)

    def directory_generator(self, dirname: str, gen: type(Generator), gen_args: Optional[dict] = None,
                            serialize_args: Optional[dict] = None):
        if gen_args is None:
            gen_args = {}
        if serialize_args is None:
            serialize_args = {}

        source_dir = os.path.join(self.source_path, dirname)
        if not os.path.exists(source_dir):
            make_and_clear_directory(source_dir)
            target_dir = source_dir
        else:
            target_dir = os.path.join(self.target_path, dirname)
            make_and_clear_directory(target_dir)
        yaml_file = os.path.join(self.model_path, self.model_name + '.yaml')
        gen(yaml_file, **gen_args).serialize(directory=target_dir, **serialize_args)
        if source_dir == target_dir:
            self.assertTrue(False, f"{dirname} created - rerun test")

        diffs = are_dir_trees_equal(target_dir, source_dir)
        if diffs:
            print(diffs)
            self.assertTrue(False, f"{dirname} mismatch")
        make_and_clear_directory(target_dir)

import os
import re
import unittest
from typing import Optional, Callable, Union, Dict

from rdflib import Graph, Namespace, OWL
from rdflib.compare import to_isomorphic, graph_diff, IsomorphicGraph

from biolinkml import METAMODEL_NAMESPACE, MODULE_DIR
from biolinkml.utils.generator import Generator
from biolinkml.utils.context_utils import parse_import_map
from tests import sourcedir, USE_LOCAL_IMPORT_MAP
from tests.test_scripts.clicktestcase import ClickTestCase
from tests.utils.compare_directories import are_dir_trees_equal
from tests.utils.dirutils import make_and_clear_directory
from tests.utils.rdf_comparator import compare_rdf, to_graph

BIOLINK_NS = Namespace("https://w3id.org/biolink/vocab/")

# ShEx validation of the biolink model takes a loooong time, so we only do it on rare occasions
DO_SHEX_VALIDATION = False

# Normally we import mappings and types directly from the URL, but for testing we use local maps
BIOLINK_IMPORT_MAP_FNAME = os.path.join(sourcedir, 'local_import_map.json' if USE_LOCAL_IMPORT_MAP else 'biolink_import_map.json')
BIOLINK_IMPORT_MAP = parse_import_map(BIOLINK_IMPORT_MAP_FNAME,
                                      os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))



class GeneratorTestCase(unittest.TestCase):
    source_path: str = None             # Path to expected output
    target_path: str = None             # Path to actual output
    model_path: str = None              # Path for yaml
    model_name: str = None              # yaml name (sans '.yaml')
    output_name: str = None             # If different than model name
    importmap: Dict[str, str] = None   # Location of the import mappings if any

    def verify_paths(self) -> None:
        assert self.source_path and self.target_path and self.model_path and self.model_name, "Paths must be set"

    @staticmethod
    def _print_triples(g: Graph):
        """ Pretty print the contents of g, removing the prefix declarations """
        g.bind('BIOLINK', BIOLINK_NS)
        g.bind('meta', METAMODEL_NAMESPACE)
        g.bind('owl', OWL)
        g_text = re.sub(r'@prefix.*\n', '', g.serialize(format="turtle").decode())
        print(g_text)

    def _default_comparator(self, old_data: str, new_data: str, new_file: str, msg: Optional[str] = None,
                            filtr: Optional[Callable[[str], str]] = None) -> None:
        """ Simple file comparator.  Compare old to new and, if they don't match, save an image of new in
        file_name_for_actual and raise an error

        :param old_data: Expected data
        :param new_data: Actual data
        :param new_file: Save actual data here if mismatch
        :param msg: If present add to the assert message
        :param filtr: data filter
        :return:
        """
        self.maxDiff = None
        old_data_filtered = filtr(old_data) if filtr is not None else old_data
        new_data_filtered = filtr(new_data) if filtr is not None else new_data
        if old_data_filtered != new_data_filtered:
            if msg:
                print(msg)
            with open(new_file, 'w') as newf:
                newf.write(new_data)
            if len(new_data) > 20000:
                print(ClickTestCase.closein_comparison(old_data_filtered, new_data_filtered))
            self.maxDiff = None
            self.assertEqual(old_data_filtered, new_data_filtered)

    def rdf_comparator(self, expected_rdf: Union[Graph, str], actual_rdf: Union[Graph, str],
                       file_name_for_actual: Optional[str] = None, msg: Optional[str] = None,
                       filtr: Optional[Callable[[str], str]] = None) -> None:
        """
        RDF comparator.  Compare two graphs and, if they don't match, save a turtle image of new_data in
        new_file and raise an error
        :param expected_rdf: Turtle representation of expected RDF
        :param actual_rdf: Turtle representation of actual RDF
        :param file_name_for_actual: Save actual RDF here if mismatch
        :param msg: If present, add to assert message
        :param filtr: data filter
        :return:
        """
        error_msg = compare_rdf(expected_rdf, actual_rdf)
        if error_msg:
            if file_name_for_actual:
                to_graph(actual_rdf).serialize(file_name_for_actual, format="turtle")
                print(f"***** New graph saved in {file_name_for_actual} *****")
            print(error_msg)
            self.fail("RDF file mismatch" if not msg else msg)

    def single_file_generator(self, suffix: str, gen: type(Generator), *,
                              format: Optional[str] = None,
                              generator_args: Optional[dict] = None,
                              serialize_args: Optional[dict] = None,
                              filtr: Optional[Callable[[str], str]] = None,
                              comparator: Callable[[type(unittest.TestCase), str, str, str, Optional[Callable[[str], str]]], None] = None,
                              preserve_metadata: bool = False,
                              fail_if_expected_missing: bool = True) -> str:
        """ Invoke generator specified in gen

        :param suffix: File suffix (without '.')
        :param gen: Generator to invoke
        :param format: Generator format argument
        :param generator_args: Additional arguments to the generator
        :param serialize_args: Arguments to serializer.
        :param filtr: Filter to remove metadata specific info from the output.  Default: identity
        :param comparator: Comparison method to use.  Default: GeneratorTestCase._default_comparator
        :param preserve_metadata: True means metadata is to preserved in old_file
        :param fail_if_expected_missing: True means return error message rather than fail
        :return: Empty string if success else error message if fail_if_expected_missing is false
        """
        self.verify_paths()
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
        if self.importmap is not None and 'importmap' not in generator_args:
            generator_args['importmap'] = self.importmap
        output_base = self.output_name if self.output_name is not None else self.model_name
        old_file = os.path.join(self.source_path, output_base + ('.' if output_base else '') + suffix)
        new_file = os.path.join(self.target_path, output_base + ('.' if output_base else '') + suffix)
        message = \
            f"\n***** Expected output is in {os.path.relpath(old_file, MODULE_DIR)} " \
            f"and actual is in {os.path.relpath(new_file, MODULE_DIR)} *****\n" \
            f"***** Remove {os.path.relpath(old_file, MODULE_DIR)} and re-run to update"
        yaml_file = os.path.join(self.model_path, self.model_name + '.yaml')
        if os.path.exists(new_file):
            os.remove(new_file)

        new_data = str(gen(yaml_file, **generator_args).serialize(**serialize_args))
        if not os.path.exists(old_file):
            with open(old_file, 'w') as oldf:
                oldf.write(new_data if preserve_metadata else filtr(new_data))
            msg = f"Created {old_file} - run again"
            if fail_if_expected_missing:
                self.fail(msg)
            return msg + '\n'

        with open(old_file) as oldf:
            old_data = filtr(oldf.read())
        comparator(self, old_data, new_data, new_file, message, filtr=filtr)
        return ''

    def directory_generator(self, dirname: str, gen: type(Generator), gen_args: Optional[dict] = None,
                            serialize_args: Optional[dict] = None):
        self.verify_paths()
        if gen_args is None:
            gen_args = {}
        if serialize_args is None:
            serialize_args = {}
        if self.importmap is not None and 'importmap' not in gen_args:
            gen_args['importmap'] = self.importmap
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

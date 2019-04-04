import os
import re
import unittest
from types import ModuleType
from typing import Optional, Callable, List

from biolinkml import METAMODEL_NAMESPACE, LOCAL_SHEX_PATH, LOCAL_CONTEXT_PATH
from biolinkml.generators.csvgen import CsvGenerator
from biolinkml.generators.dotgen import DotGenerator
from biolinkml.generators.golrgen import GolrSchemaGenerator
from biolinkml.generators.graphqlgen import GraphqlGenerator
from biolinkml.generators.jsonldcontextgen import ContextGenerator
from biolinkml.generators.jsonldgen import JSONLDGenerator
from biolinkml.generators.jsonschemagen import JsonSchemaGenerator
from biolinkml.generators.markdowngen import MarkdownGenerator
from biolinkml.generators.owlgen import OwlSchemaGenerator
from biolinkml.generators.protogen import ProtoGenerator
from biolinkml.generators.pythongen import PythonGenerator
from biolinkml.generators.rdfgen import RDFGenerator
from biolinkml.generators.shexgen import ShExGenerator
from biolinkml.utils.generator import Generator
from pyshex import ShExEvaluator
from pyshex.shex_evaluator import EvaluationResult
from rdflib import Graph, Namespace
from rdflib.compare import to_isomorphic, graph_diff
from tests.test_scripts.clicktestcase import ClickTestCase, metadata_filter
from tests.utils.compare_directories import are_dir_trees_equal
from tests.utils.dirutils import make_and_clear_directory

BIOLINK_NS = Namespace("https://w3id.org/biolink/vocab/")

# ShEx validation of the biolink model takes a loooong time, so we only do it on rare occasions
DO_SHEX_VALIDATION = False

class CurrentBiolinkModelTestCase(unittest.TestCase):
    cwd = os.path.abspath(os.path.dirname(__file__))

    source_path = os.path.join(cwd, 'source')
    target_path = os.path.join(cwd, 'target')
    biolink_model_path = os.path.join(cwd, 'yaml', 'biolink-model.yaml')

    @staticmethod
    def _print_triples(g: Graph):
        g.bind('BIOLINK', BIOLINK_NS)
        g.bind('meta', METAMODEL_NAMESPACE)
        g_text = re.sub(r'@prefix.*\n', '', g.serialize(format="turtle").decode())
        print(g_text)

    def _default_comparator(self, old_data: str, new_data:str, new_file:str) -> None:
        self.maxDiff = None
        if old_data != new_data:
            with open(new_file, 'w') as newf:
                newf.write(new_data)
            print(ClickTestCase.closein_comparison(old_data, new_data))
            self.assertEqual(old_data, new_data)

    def rdf_comparator(self, old_data: str, new_data: str, new_file:str) -> None:
        old_graph = Graph()
        new_graph = Graph()
        old_graph.parse(data=old_data, format="turtle")
        new_graph.parse(data=new_data, format="turtle")
        old_iso = to_isomorphic(old_graph)
        # Remove the metadata specific triples
        for t in list(old_iso.triples((None, METAMODEL_NAMESPACE.generation_date, None))):
            old_iso.remove(t)
        new_iso = to_isomorphic(new_graph)
        for t in list(new_iso.triples((None, METAMODEL_NAMESPACE.generation_date, None))):
            new_iso.remove(t)
        # Graph compare takes a Looong time
        in_both, in_old, in_new = graph_diff(old_iso, new_iso)
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
            self.assertTrue(False, "RDF file mismatch")

    def single_file_generator(self, suffix: str, gen: type(Generator), gen_args: Optional[dict] = None,
                              serialize_args: Optional[dict] = None,
                              filtr: Optional[Callable[[str], str]] = None,
                              comparator: Callable[[type(unittest.TestCase), str, str, str], None] = None) -> None:
        """

        :param suffix: File suffix (without '.')
        :param gen: Generator to use
        :param gen_args: Arguments to generator
        :param serialize_args: Arguments to serializer
        :param filtr: Filter to remove metadata specific info from the file
        :param comparator: Comparison method to use
        :return:
        """
        if gen_args is None:
            gen_args = {}
        if serialize_args is None:
            serialize_args = {}
        if filtr is None:
            def filtr(s): return s
        if comparator is None:
            comparator = CurrentBiolinkModelTestCase._default_comparator
        old_file = os.path.join(self.source_path, 'biolink_model.' + suffix)
        new_file = os.path.join(self.target_path, 'biolink_model.' + suffix)
        if os.path.exists(new_file):
            os.remove(new_file)
        new_data = filtr(str(gen(self.biolink_model_path, **gen_args).serialize(**serialize_args)))

        if not os.path.exists(old_file):
            with open(old_file, 'w') as oldf:
                oldf.write(new_data)
            self.assertTrue(False, f"Created {old_file} - run again")

        # Note: we assume old file (source) is pre-filtered.  This prevents unnecessary git updates
        with open(old_file) as oldf:
            old_data = oldf.read()
        comparator(self, old_data, new_data, new_file)

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
        gen(self.biolink_model_path, **gen_args).serialize(directory=target_dir, **serialize_args)
        if source_dir == target_dir:
            self.assertTrue(False, f"{dirname} created - rerun test")

        diffs = are_dir_trees_equal(target_dir, source_dir)
        if diffs:
            print(diffs)
            self.assertTrue(False, f"{dirname} mismatch")
        make_and_clear_directory(target_dir)

    def test_biolink_python(self):
        """ Test the python generator for the biolink model """
        self.single_file_generator('py', PythonGenerator, {'emit_metadata': True}, filtr=metadata_filter)
        with open(os.path.join(self.source_path, 'biolink_model.py')) as f:
            pydata = f.read()
        # Make sure the python is valid
        spec = compile(pydata, 'test', 'exec')
        module = ModuleType('test')
        exec(spec, module.__dict__)

    def test_biolink_markdown(self):
        """ Test the markdown generator for the biolink model """
        self.directory_generator('markdown', MarkdownGenerator)

    def test_biolink_tsv(self):
        """ Test the tsv generator for the biolink model """
        def filtr(s: str) -> str:
            return s.replace('\r\n', '\n')
        self.single_file_generator('tsv', CsvGenerator, {'fmt':'tsv'}, filtr=filtr)

    def test_biolink_graphviz(self):
        """ Test the dotty generator for the biolink model """
        self.directory_generator('graphviz', DotGenerator)

    def test_biolink_golr(self):
        """ Test the golr schema generator for the biolink model """
        self.directory_generator('golr', GolrSchemaGenerator)

    def test_biolink_graphql(self):
        """ Test the graphql schema generator for the biolink model """
        self.single_file_generator('graphql', GraphqlGenerator)

    def test_biolink_jsonld(self):
        """ Test the jsonld schema generator for the biolink model """
        def filtr(s: str) -> str:
            return re.sub(r'"generation_date": ".*?",', '"generation_date": "2019-01-01 12:00",', s)
        self.single_file_generator('jsonld', JSONLDGenerator, filtr=filtr)

    def test_biolink_context(self):
        """ Test the jsonld context generator for the biolink model """
        def filtr(s: str) -> str:
            return re.sub(r'Generation date: .*?\\n', r'Generation date: \\n',
                          re.sub(r' version: .*?\\n', r' version: \\n', s))
        self.single_file_generator('context.jsonld', ContextGenerator, filtr=filtr)

    def test_biolink_json_schema(self):
        """ Test the jsonld context generator for the biolink model """
        self.single_file_generator('json.schema', JsonSchemaGenerator)

    @unittest.expectedFailure
    def test_biolink_owl_schema(self):
        """ Test the owl schema generator for the biolink model """
        self.single_file_generator('owl', OwlSchemaGenerator)

    def test_biolink_proto(self):
        """ Test the proto schema generator for the biolink model """
        self.single_file_generator('proto', ProtoGenerator)

    def _evaluate_shex_results(self, results: List[EvaluationResult]) -> bool:
        """
        Check the results of the ShEx evaluation
        :param results: evaluate output
        :return: success indicator
        """
        success = all(r.result for r in results)
        if not success:
            for r in results:
                if not r.result:
                    print(r.reason)
        return success

    def test_biolink_rdf(self):
        """ Test the rdf generator for the biolink model """
        self.single_file_generator('ttl', RDFGenerator, serialize_args={"context": LOCAL_CONTEXT_PATH},
                                   comparator=CurrentBiolinkModelTestCase.rdf_comparator)

        # Validate the RDF against the Biolink ShEx
        if DO_SHEX_VALIDATION:
            g = Graph()
            rdf_file = os.path.join(self.source_path, 'biolink_model.ttl')
            g.load(rdf_file, format='ttl')
            focus = BIOLINK_NS.biolink_model
            start = METAMODEL_NAMESPACE.SchemaDefinition
            results = ShExEvaluator(g, LOCAL_SHEX_PATH, focus, start).evaluate(debug=False)
            self.assertTrue(self._evaluate_shex_results(results))

        else:
            print("*** RDF Model validation step was skipped. See: test_biolink_model.DO_SHEX_VALIDATION to run it")

    def test_biolink_shex(self):
        """ Test the shex generator for the biolink model """
        self.single_file_generator('shex', ShExGenerator)
        shex_file = os.path.join(self.source_path, 'biolink_model.shex')
        g = Graph()
        rdf_file = os.path.join(self.source_path, 'statements.ttl')
        g.load(rdf_file, format='ttl')
        focus = "http://identifiers.org/drugbank:DB00005"
        start = BIOLINK_NS.Drug
        results = ShExEvaluator(g, shex_file, focus, start).evaluate()
        self.assertTrue(self._evaluate_shex_results(results))


if __name__ == '__main__':
    unittest.main()

import os
import re
import unittest
from types import ModuleType
from typing import List

from pyshex import ShExEvaluator
from pyshex.shex_evaluator import EvaluationResult
from rdflib import Graph, Namespace, URIRef

from biolinkml import METAMODEL_NAMESPACE, LOCAL_SHEXJ_FILE_NAME, LOCAL_METAMODEL_LDCONTEXT_FILE, MODULE_DIR
from biolinkml.generators.csvgen import CsvGenerator
from biolinkml.generators.dotgen import DotGenerator
from biolinkml.generators.golrgen import GolrSchemaGenerator
from biolinkml.generators.graphqlgen import GraphqlGenerator
from biolinkml.generators.jsonldcontextgen import ContextGenerator
from biolinkml.generators.jsonldgen import JSONLDGenerator
from biolinkml.generators.jsonschemagen import JsonSchemaGenerator
from biolinkml.generators.markdowngen import MarkdownGenerator
from biolinkml.generators.namespacegen import NamespaceGenerator
from biolinkml.generators.owlgen import OwlSchemaGenerator
from biolinkml.generators.protogen import ProtoGenerator
from biolinkml.generators.pythongen import PythonGenerator
from biolinkml.generators.rdfgen import RDFGenerator
from biolinkml.generators.shexgen import ShExGenerator
from biolinkml.utils.formatutils import shex_results_as_string
from biolinkml.utils.context_utils import parse_import_map
from tests.utils.metadata_filters import metadata_filter
from tests.utils.generator_utils import GeneratorTestCase

BIOLINK_NS = Namespace("https://w3id.org/biolink/vocab/")

# ShEx validation of the biolink model takes a loooong time, so we only do it on rare occasions
DO_SHEX_VALIDATION = False


class CurrentBiolinkModelTestCase(GeneratorTestCase):
    cwd = os.path.abspath(os.path.dirname(__file__))

    source_path = os.path.join(cwd, 'source')
    target_path = os.path.join(cwd, 'target')
    model_path = os.path.join(cwd, 'yaml')
    model_name = 'biolink-model'
    importmap = parse_import_map(os.path.join(model_path, 'biolink-model-map.json'), MODULE_DIR)

    def tearDown(self) -> None:
        self.output_name = None

    def test_biolink_python(self):
        """ Test the python generator for the biolink model """
        self.output_name = 'model'
        self.single_file_generator('py', PythonGenerator, generator_args={'emit_metadata': True}, filtr=metadata_filter)

        # Make sure the python is valid
        with open(os.path.join(self.source_path, f'{self.output_name}.py')) as f:
            pydata = f.read()
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
        self.single_file_generator('tsv', CsvGenerator, format="tsv", filtr=filtr)

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
            return re.sub(r'"source_file_date": ".*?",', '"source_file_date": "2019-01-01-12:00",',
                          re.sub(r'"generation_date": ".*?",', '"generation_date": "2019-01-01 12:00",', s))
        self.single_file_generator('jsonld', JSONLDGenerator, filtr=filtr)

    def test_biolink_context(self):
        """ Test the jsonld context generator for the biolink model """
        def filtr(s: str) -> str:
            return re.sub(r'Generation date: .*?\\n', r'Generation date: \\n',
                          re.sub(r' version: .*?\\n', r' version: \\n', s))
        self.single_file_generator('context.jsonld', ContextGenerator, filtr=filtr)
        # Generate a second copy with native identifiers
        self.single_file_generator('context.native.jsonld', ContextGenerator, filtr=filtr,
                                   generator_args=dict(useuris=False))

    def test_biolink_json_schema(self):
        """ Test the jsonld context generator for the biolink model """
        self.single_file_generator('json.schema', JsonSchemaGenerator)

    def test_biolink_owl_schema(self):
        """ Test the owl schema generator for the biolink model """
        self.single_file_generator('owl', OwlSchemaGenerator, comparator=GeneratorTestCase.rdf_comparator)
        # Generate a second copy with native identifiers
        self.single_file_generator('native.owl', OwlSchemaGenerator, comparator=GeneratorTestCase.rdf_comparator,
                                   generator_args=dict(useuris=False))

    def test_biolink_proto(self):
        """ Test the proto schema generator for the biolink model """
        self.single_file_generator('proto', ProtoGenerator)

    def test_biolink_namespaces(self):
        """ Test the python generator for the biolink model """
        self.output_name = 'namespaces'
        self.single_file_generator('py', NamespaceGenerator, generator_args={'emit_metadata': True}, filtr=metadata_filter)

        # Make sure the python is valid
        with open(os.path.join(self.source_path, f'{self.output_name}.py')) as f:
            pydata = f.read()
        spec = compile(pydata, 'test', 'exec')
        module = ModuleType('test')
        exec(spec, module.__dict__)

    @staticmethod
    def _evaluate_shex_results(results: List[EvaluationResult], printit: bool=True) -> bool:
        """
        Check the results of the ShEx evaluation
        :param results: evaluate output
        :return: success indicator
        """
        success = all(r.result for r in results)
        if not success and printit:
            for r in results:
                if not r.result:
                    print(r.reason)
        return success

    def test_biolink_rdf(self):
        """ Test the rdf generator for the biolink model """
        self.single_file_generator('ttl', RDFGenerator, serialize_args={"context": LOCAL_METAMODEL_LDCONTEXT_FILE},
                                   comparator=GeneratorTestCase.rdf_comparator)

        # Validate the RDF against the Biolink ShEx
        if DO_SHEX_VALIDATION:
            g = Graph()
            rdf_file = os.path.join(self.source_path, 'biolink_model.ttl')
            g.load(rdf_file, format='ttl')
            focus = BIOLINK_NS.biolink_model
            start = METAMODEL_NAMESPACE.SchemaDefinition
            results = ShExEvaluator(g, LOCAL_SHEXJ_FILE_NAME, focus, start).evaluate(debug=False)
            self.assertTrue(self._evaluate_shex_results(results))

        else:
            print("*** RDF Model validation step was skipped. See: test_biolink_model.DO_SHEX_VALIDATION to run it")

    def test_biolink_shex(self):
        """ Just Generate the ShEx file untested """
        self.single_file_generator('shex', ShExGenerator)
        self.single_file_generator('shexj', ShExGenerator, format='json')
        # Generate native ShEx
        self.single_file_generator('native.shex', ShExGenerator, generator_args=dict(useuris=False))
        self.single_file_generator('native.shexj', ShExGenerator, format='json',
                                   generator_args=dict(useuris=False))

    def test_biolink_shex_incorrect_rdf(self):
        """ Test some non-conforming RDF  """
        self.single_file_generator('shexj', ShExGenerator, format='json')
        shex_file = os.path.join(self.source_path, 'biolink-model.shexj')
        data_dir = os.path.join(self.cwd, 'data')

        focus = "http://identifiers.org/drugbank:DB00005"
        start = BIOLINK_NS.Drug
        evaluator = ShExEvaluator(None, shex_file, focus, start)

        # incorrect.ttl has 16 error lines (more or less).
        rdf_file = os.path.join(data_dir, 'incorrect.ttl')
        errs_file = os.path.join(data_dir, 'incorrect.errs')
        results = evaluator.evaluate(rdf_file)
        self.assertFalse(self._evaluate_shex_results(results, printit=False))
        self.assertEqual(1, len(results))
        self.assertTrue('Unmatched triples in CLOSED shape' in results[0].reason)
        ntabs = results[0].reason.count('\n\t')
        self.assertEqual(13, ntabs)
        if not os.path.exists(errs_file):
            with open(errs_file, 'w') as f:
                f.write(shex_results_as_string(results[0]))
        # TODO:
        #     self.assertTrue(False, f"{errs_file} created - run test again")
        # else:
        #     with open(errs_file) as f:
        #         expected = f.read()
        #     self.assertEqual(expected, shex_results_as_string(results[0]))

    @unittest.skipIf(not DO_SHEX_VALIDATION, "Skipping ShEx Validation")
    def test_biolink_correct_rdf(self):
        """ Test some conforming RDF  """
        self.single_file_generator('shexj', ShExGenerator, format='json')    # Make sure ShEx is current

        shex_file = os.path.join(self.source_path, 'biolink-model.shexj')
        data_dir = os.path.join(self.cwd, 'data')

        focus = "http://identifiers.org/drugbank:DB00005"
        start = BIOLINK_NS.Drug
        evaluator = ShExEvaluator(None, shex_file, focus, start)

        rdf_file = os.path.join(data_dir, 'probe.ttl')
        results = evaluator.evaluate(rdf_file, debug=False)
        self.assertTrue(self._evaluate_shex_results(results))


if __name__ == '__main__':
    unittest.main()

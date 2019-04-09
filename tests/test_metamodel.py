import os
import unittest
from types import ModuleType
from typing import List

from pyshex.shex_evaluator import EvaluationResult, ShExEvaluator
from rdflib import Graph

from biolinkml import LOCAL_YAML_PATH, meta, LOCAL_TYPES_PATH, LOCAL_CONTEXT_PATH, METAMODEL_NAMESPACE, LOCAL_SHEX_PATH, \
    LOCAL_RDF_PATH
from biolinkml.generators.markdowngen import MarkdownGenerator
from biolinkml.generators.owlgen import OwlSchemaGenerator
from biolinkml.generators.rdfgen import RDFGenerator
from biolinkml.generators.shexgen import ShExGenerator
from includes import types
from biolinkml.generators.pythongen import PythonGenerator
from tests import targetdir
from tests.test_scripts.clicktestcase import metadata_filter
from tests.utils.generator_utils import GeneratorTestCase

DO_SHEX_VALIDATION: bool = True

class MetaModelTestCase(GeneratorTestCase):
    root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))

    source_path = root
    target_path = targetdir
    model_path = root
    model_name = 'meta'

    def test_meta_markdown(self):
        """ Test the markdown generator for the biolink model """
        self.directory_generator('docs', MarkdownGenerator)

    def test_meta_owl_schema(self):
        """ Test the owl schema generator for the biolink model """
        self.single_file_generator('owl', OwlSchemaGenerator, comparator=GeneratorTestCase.rdf_comparator)

    @staticmethod
    def _evaluate_shex_results(results: List[EvaluationResult]) -> bool:
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

    def test_meta_rdf(self):
        """ Test the rdf generator for the biolink model """
        self.single_file_generator('ttl', RDFGenerator, serialize_args={"context": LOCAL_CONTEXT_PATH},
                                   comparator=GeneratorTestCase.rdf_comparator)

        # Validate the RDF against the Biolink ShEx
        if DO_SHEX_VALIDATION:
            g = Graph()
            rdf_file = LOCAL_RDF_PATH
            g.load(rdf_file, format='turtle')
            focus = METAMODEL_NAMESPACE.metamodel
            start = METAMODEL_NAMESPACE.SchemaDefinition
            results = ShExEvaluator(g, LOCAL_SHEX_PATH, focus, start).evaluate(debug=False)
            self.assertTrue(self._evaluate_shex_results(results))
        else:
            print("*** RDF Model validation step was skipped. See: test_meta_model.DO_SHEX_VALIDATION to run it")


if __name__ == '__main__':
    unittest.main()

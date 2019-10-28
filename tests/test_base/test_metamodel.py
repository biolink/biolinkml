import os
import unittest
from typing import List

from pyshex.shex_evaluator import EvaluationResult, ShExEvaluator
from rdflib import Graph

from biolinkml import LOCAL_METAMODEL_LDCONTEXT_FILE, METAMODEL_NAMESPACE, LOCAL_SHEXJ_FILE_NAME, \
    LOCAL_RDF_FILE_NAME, MODULE_DIR
from biolinkml.generators.jsonldgen import JSONLDGenerator
from biolinkml.generators.markdowngen import MarkdownGenerator
from biolinkml.generators.owlgen import OwlSchemaGenerator
from biolinkml.generators.rdfgen import RDFGenerator
from biolinkml.generators.shexgen import ShExGenerator
from tests import targetdir, DO_SHEX_VALIDATION, sourcedir
from tests.utils.generator_utils import GeneratorTestCase, BIOLINK_IMPORT_MAP
from tests.utils.metadata_filters import json_metadata_filter


class MetaModelTestCase(GeneratorTestCase):
    source_path = MODULE_DIR
    target_path = targetdir
    model_path = MODULE_DIR
    model_name = 'meta'
    importmap = BIOLINK_IMPORT_MAP

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

    def test_meta_shexc(self):
        """ Test the shex ShExC generation """
        self.single_file_generator('shex', ShExGenerator, format="shex")

    def test_meta_shecj(self):
        """ Test the shex ShExJ generation """
        self.single_file_generator('shexj', ShExGenerator, format="json")

    def test_meta_rdf(self):
        """ Test the rdf generator for the biolink model """
        # Make sure the ShEx is good
        self.single_file_generator('shexj', ShExGenerator, format="json")

        # Make a fresh copy of the RDF and validate it as well
        self.single_file_generator('ttl', RDFGenerator, serialize_args={"context": LOCAL_METAMODEL_LDCONTEXT_FILE},
                                   comparator=GeneratorTestCase.rdf_comparator)

        # Validate the RDF against the Biolink ShEx
        if DO_SHEX_VALIDATION:
            g = Graph()
            rdf_file = LOCAL_RDF_FILE_NAME
            g.load(rdf_file, format='turtle')
            focus = METAMODEL_NAMESPACE.metamodel
            start = METAMODEL_NAMESPACE.SchemaDefinition
            results = ShExEvaluator(g, LOCAL_SHEXJ_FILE_NAME, focus, start).evaluate(debug=False)
            self.assertTrue(self._evaluate_shex_results(results))
        else:
            print("*** RDF Model validation step was skipped. Set: tests.__init__.DO_SHEX_VALIDATION to run it")


if __name__ == '__main__':
    unittest.main()

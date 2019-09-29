import os
import unittest
from types import ModuleType
from typing import List

from pyshex import ShExEvaluator, PrefixLibrary
from pyshex.shex_evaluator import EvaluationResult
from rdflib import Graph, Namespace

from biolinkml import INCLUDES_DIR, MODULE_DIR, METAMODEL_FILE_NAME, LOCAL_CONTEXT_PATH, METAMODEL_NAMESPACE, \
    LOCAL_SHEXJ_PATH
from biolinkml.generators.markdowngen import MarkdownGenerator
from biolinkml.generators.pythongen import PythonGenerator
from biolinkml.generators.rdfgen import RDFGenerator
from biolinkml.generators.shexgen import ShExGenerator
from tests import targetdir, sourcedir, DO_SHEX_VALIDATION
from tests.test_scripts.clicktestcase import metadata_filter
from tests.utils.generator_utils import GeneratorTestCase


class MappingsTestCase(GeneratorTestCase):
    """ Validate that mappings are available on both a meta and a model level basis """

    source_path = sourcedir
    target_path = targetdir
    model_path = sourcedir
    model_name = 'meta_mappings'

    def test_mappings_in_metamodel(self):
        """ Make sure that mappings can be specified in a metamodel """
        self.single_file_generator('py', PythonGenerator, filtr=metadata_filter)

        # Make sure the python is valid
        with open(os.path.join(self.source_path, 'meta_mappings.py')) as f:
            pydata = f.read()
        spec = compile(pydata, 'test', 'exec')
        module = ModuleType('test')
        exec(spec, module.__dict__)

    def test_mappings_markdown(self):
        """ Test mappings markdown for  """
        self.directory_generator('meta_mappings_docs', MarkdownGenerator)

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

    def test_mappings_rdf(self):
        """ Test the rdf generator for the biolink model """
        # Make a fresh copy of the RDF and validate it as well
        self.single_file_generator('ttl', RDFGenerator, serialize_args={"context": LOCAL_CONTEXT_PATH},
                                   comparator=GeneratorTestCase.rdf_comparator)

        g = Graph()
        rdf_file = os.path.join(sourcedir, 'meta_mappings.ttl')
        g.load(rdf_file, format='turtle')
        ns = PrefixLibrary()
        ns.add_rdf(g)
        ns['FULL'] = "http://example.org/fulluri/"
        ns['EX'] = "http://example.org/mappings/"
        # Make sure that the expected triples got added
        # skos:closeMatch <ex:slot1_close>,
        #         <http://example.org/fulluri/slot1_close> ;
        #     skos:exactMatch <ex:slot1>,
        #         <http://example.org/fulluri/slot1> ;
        #     skos:inScheme <http://example.org/mappings/> ;
        #     skos:relatedMatch <ex:slot1_related>,
        #         <http://example.org/fulluri/slot1_related> ;
        #     :deprecated_element_has_exact_replacement <http://example.org/mappings/['s3']> ;
        #     :deprecated_element_has_possible_replacement <http://example.org/mappings/['s4']> ;
        self.assertEqual({ns.EX.slot1_close, ns.FULL.slot1_close}, set(g.objects(ns.EX.s1, ns.SKOS.closeMatch)))
        self.assertEqual({ns.EX.slot1, ns.FULL.slot1}, set(g.objects(ns.EX.s1, ns.SKOS.exactMatch)))
        if DO_SHEX_VALIDATION:
            EX = Namespace("http://example.org/mappings/")
            focus = EX.testMetamodelMappings
            start = METAMODEL_NAMESPACE.SchemaDefinition
            results = ShExEvaluator(g, LOCAL_SHEXJ_PATH, focus, start).evaluate(debug=False)
            self.assertTrue(self._evaluate_shex_results(results))
        else:
            print("*** RDF Model validation step was skipped. Set: tests.__init__.DO_SHEX_VALIDATION to run it")



if __name__ == '__main__':
    unittest.main()

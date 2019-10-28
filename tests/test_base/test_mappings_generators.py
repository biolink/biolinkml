import os
import unittest
from types import ModuleType
from typing import List

from pyshex import ShExEvaluator, PrefixLibrary
from pyshex.shex_evaluator import EvaluationResult
from rdflib import Graph, Namespace

from biolinkml import METAMODEL_NAMESPACE, LOCAL_SHEXJ_FILE_NAME, LOCAL_METAMODEL_LDCONTEXT_FILE
from biolinkml.generators.jsonldcontextgen import ContextGenerator
from biolinkml.generators.jsonldgen import JSONLDGenerator
from biolinkml.generators.markdowngen import MarkdownGenerator
from biolinkml.generators.pythongen import PythonGenerator
from biolinkml.generators.rdfgen import RDFGenerator
from tests import targetdir, sourcedir, DO_SHEX_VALIDATION
from tests.utils.generator_utils import GeneratorTestCase, BIOLINK_IMPORT_MAP
from tests.utils.metadata_filters import metadata_filter, ldcontext_metadata_filter, json_metadata_filter


class MappingsGeneratorTestCase(GeneratorTestCase):
    """ Validate that mappings are available on both a meta and a model level basis """

    source_path = sourcedir
    target_path = targetdir
    model_path = sourcedir
    model_name = 'meta_mappings'
    importmap = BIOLINK_IMPORT_MAP

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
        """ Test the imported mappings in the biolink metamodel """

        # Generate context and use it to create the RDF
        self.single_file_generator('jsonld', ContextGenerator, filtr=ldcontext_metadata_filter)

        # Generate a copy of the JSON representation of the model
        context_loc = os.path.join(self.source_path, self.model_name + ".jsonld")
        context_args = {"context": [LOCAL_METAMODEL_LDCONTEXT_FILE, context_loc]}
        self.single_file_generator('json', JSONLDGenerator,  serialize_args=context_args,  filtr=json_metadata_filter)

        # Make a fresh copy of the RDF and validate it as well
        self.single_file_generator('ttl', RDFGenerator, serialize_args=context_args,
                                   comparator=GeneratorTestCase.rdf_comparator)

        g = Graph()
        rdf_file = os.path.join(sourcedir, 'meta_mappings.ttl')
        g.load(rdf_file, format='turtle')
        ns = PrefixLibrary()
        ns.add_rdf(g)
        ns['FULL'] = "http://example.org/fulluri/"
        ns['EX'] = "http://example.org/mappings/"
        ns['META'] = "https://w3id.org/biolink/biolinkml/meta/"
        # Make sure that the expected triples got added

        self.assertEqual({ns.EX.slot1_close, ns.FULL.slot1_close}, set(g.objects(ns.EX.s1, ns.SKOS.closeMatch)))
        self.assertEqual({ns.EX.slot1, ns.FULL.slot1}, set(g.objects(ns.EX.s1, ns.SKOS.exactMatch)))
        self.assertEqual(ns.EX.s3, g.value(ns.EX.s1, ns.META.deprecated_element_has_exact_replacement, any=False))
        self.assertEqual(ns.EX.s4, g.value(ns.EX.s1, ns.META.deprecated_element_has_possible_replacement, any=False))

        self.assertEqual({ns.EX.class1_close, ns.FULL.class1_close}, set(g.objects(ns.EX.C1, ns.SKOS.closeMatch)))
        self.assertEqual({ns.EX.class1, ns.FULL.class1}, set(g.objects(ns.EX.C1, ns.SKOS.exactMatch)))
        self.assertEqual(ns.EX.c2, g.value(ns.EX.C1, ns.META.deprecated_element_has_exact_replacement, any=False))
        self.assertEqual(ns.EX.c3, g.value(ns.EX.C1, ns.META.deprecated_element_has_possible_replacement, any=False))
        if DO_SHEX_VALIDATION:
            EX = Namespace("http://example.org/mappings/")
            focus = EX.testMetamodelMappings
            start = METAMODEL_NAMESPACE.SchemaDefinition
            results = ShExEvaluator(g, LOCAL_SHEXJ_FILE_NAME, focus, start).evaluate(debug=False)
            self.assertTrue(self._evaluate_shex_results(results))
        else:
            print("*** RDF Model validation step was skipped. Set: tests.__init__.DO_SHEX_VALIDATION to run it")


if __name__ == '__main__':
    unittest.main()

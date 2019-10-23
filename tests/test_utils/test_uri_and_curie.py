import os
import unittest
from types import ModuleType

from jsonasobj import loads

from biolinkml.generators.jsonldcontextgen import ContextGenerator
from biolinkml.generators.jsonldgen import JSONLDGenerator
from biolinkml.generators.pythongen import PythonGenerator
from biolinkml.utils.yamlutils import as_rdf
from tests.utils.metadata_filters import ldcontext_metadata_filter, metadata_filter, json_metadata_filter
from tests.test_utils import inputdir
from tests.test_utils import outputdir

from tests.utils.generator_utils import GeneratorTestCase

expected_rdf = """
@prefix : <http://example.org/test/uriandcurie> .
@prefix ex: <http://example.org/test/inst#> .
@prefix test: <http://example.org/test/> .
@prefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
@prefix xml: <http://www.w3.org/XML/1998/namespace> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

ex:obj1 a test:uriandcurieC1 ;
    test:uriandcuriehasCurie ex:curie ;
    test:uriandcuriehasNcName "A123" ;
    test:uriandcuriehasURI <http://example.org/test/uri> ;
    test:uriandcurieid2 ex:id2 .
"""


# Note: GeneratorTestCase is the
class URIAndCurieTestCase(GeneratorTestCase):
    source_path: str = inputdir
    target_path: str = outputdir
    model_path: str = inputdir
    model_name: str = 'uriandcurie'
    output_name: str = 'uriandcurie'
    
    def test_uriÎ_and_curie(self):
        """ Compile a model of URI's and Curies and then test the various types """
        self.single_file_generator('py', PythonGenerator, filtr=metadata_filter)

        # Make sure the python is valid
        with open(os.path.join(self.source_path, self.model_name + '.py')) as f:
            model = f.read()
        spec = compile(model, 'test', 'exec')
        module = ModuleType('test')
        exec(spec, module.__dict__)

        # Check that the interpretations are correct
        msg = self.single_file_generator('jsonld', ContextGenerator, filtr=ldcontext_metadata_filter,
                                         fail_if_expected_missing=False)
        msg = self.single_file_generator('json', JSONLDGenerator, filtr=json_metadata_filter,
                                         fail_if_expected_missing=False)
        if msg:
            self.fail(msg)

        curie_obj = module.C1("ex:obj1",
                              hasCurie="ex:curie",
                              hasURI="http://example.org/test/uri",
                              hasNcName="A123",
                              id2="ex:id2")
        instance_jsonld = loads('{ "ex": "http://example.org/test/inst#" }')

        g = as_rdf(curie_obj, [os.path.join(self.source_path, self.model_name + '.jsonld'), instance_jsonld])
        self.rdf_comparator(expected_rdf, g, os.path.join(self.target_path, self.model_name + '.jsonld'))


if __name__ == '__main__':
    unittest.main()

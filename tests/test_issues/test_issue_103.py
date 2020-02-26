import os
import unittest
from types import ModuleType

from jsonasobj import as_json

from biolinkml.generators.jsonldcontextgen import ContextGenerator
from biolinkml.generators.pythongen import PythonGenerator
from biolinkml.utils.yamlutils import as_rdf
from tests.test_issues import sourcedir
from rdflib import Graph, Literal, URIRef


class Issue103TestCase(unittest.TestCase):

    def header(self, txt: str) -> str:
        return '\n' + ("=" * 20) + f" {txt} " + ("=" * 20)

    def test_issue_103(self):
        """ Make sure that types are generated as part of the output """
        yaml_fname = os.path.join(sourcedir, 'issue_103.yaml')
        python = PythonGenerator(yaml_fname).serialize()
        print(self.header("Python"))
        print(python)
        spec = compile(python, 'test', 'exec')
        module = ModuleType('test')
        exec(spec, module.__dict__)
        example = module.ChemicalSubstance("http://example.org/compound/13", "benzene")

        # JSON Representation
        print(self.header("JSON"))
        print(as_json(example))

        # Generate a context for this particular model
        print(self.header("Context"))
        context = ContextGenerator(yaml_fname).serialize()

        print(context)

        with open(os.path.join(sourcedir, 'context.jsonld'), 'r') as f:
            context = f.read()

        # RDF Representation
        print(self.header("RDF"))
        print(as_rdf(example, contexts=context).serialize(format="turtle").decode())

    def test_jsonld_prefix(self):
        test_json = '''
        {
            "@context": {
                "dc": "http://purl.org/dc/terms_",
                "rdf": "http://www.w3.org/1999/02/22-rdf-syntax-ns#",
                "rdfs": "http://www.w3.org/2000/01/rdf-schema#"
            },
            "@id": "http://example.org/about",
            "dc:title": {
                "@language": "en",
                "@value": "Someone's Homepage"
            }
        }
        '''
        g = Graph().parse(data=test_json, format='json-ld')
        print(g.serialize(format='turtle').decode())
        assert list(g) == [(
            URIRef('http://example.org/about'),
            URIRef('http://purl.org/dc/terms_title'),
            Literal("Someone's Homepage", lang='en'))]

    def test_mondo(self):
        g = Graph()
        g.load("https://raw.githubusercontent.com/prefixcommons/biocontext/master/registry/monarch_context.jsonld",
               format="json-ld")
        print(g.serialize(format="turtle").decode())

if __name__ == '__main__':
    unittest.main()

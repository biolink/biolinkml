import os
import unittest
from types import ModuleType

from jsonasobj import as_json
from rdflib.plugins.serializers.turtle import TurtleSerializer

from biolinkml.generators.jsonldcontextgen import ContextGenerator
from biolinkml.generators.pythongen import PythonGenerator
from biolinkml.utils.yamlutils import as_rdf
from tests.test_issues import sourcedir
from rdflib import Graph, Literal, URIRef

TurtleSerializer.roundtrip_prefixes = True


class Issue103TestCase(unittest.TestCase):

    def test_jsonld_prefix(self):
        test_json = '''
        {
            "@context": {
                "CHEBI": "http://purl.obolibrary.org/obo/CHEBI_",
                "rdf": "http://www.w3.org/1999/02/22-rdf-syntax-ns#",
                "@vocab": "http://example.org"
            },
            "CHEBI:33709": {
                "rdf:label": "Amino Acid"
            }
        }
        '''

        g = Graph().parse(data=test_json, format="json-ld", prefix=True)
        assert '@prefix CHEBI: <http://purl.obolibrary.org/obo/CHEBI_>' in g.serialize(format="turtle").decode()

        g = Graph().parse(data=test_json, format="json-ld", prefix=False)
        assert '@prefix CHEBI: <http://purl.obolibrary.org/obo/CHEBI_>' not in g.serialize(format="turtle").decode()


if __name__ == '__main__':
    unittest.main()

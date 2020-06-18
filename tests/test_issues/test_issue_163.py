import os
import unittest
from rdflib import URIRef
from rdflib.namespace import OWL, RDFS, RDF

from biolinkml.generators.owlgen import OwlSchemaGenerator
from tests.test_issues import sourcedir


class IssueOWLNamespaceTestCase(unittest.TestCase):

    def header(self, txt: str) -> str:
        return '\n' + ("=" * 20) + f" {txt} " + ("=" * 20)

    def test_issue_owl_namespace(self):
        """ Make sure that types are generated as part of the output """
        yaml_fname = os.path.join(sourcedir, 'issue_163.yaml')
        gen = OwlSchemaGenerator(yaml_fname)
        out = gen.serialize()
        print(self.header("OWL"))
        print(out)
        g = gen.graph
        A = URIRef('http://example.org/A')
        assert (A, RDF.type, OWL.Class) in g
        NAME = URIRef('http://example.org/name')
        assert (NAME, RDF.type, OWL.ObjectProperty) in g


    def test_issue_no_default(self):
        """ Make sure that types are generated as part of the output """
        yaml_fname = os.path.join(sourcedir, 'issue_163b.yaml')
        gen = OwlSchemaGenerator(yaml_fname)
        out = gen.serialize()
        print(self.header("OWL"))
        print(out)
        g = gen.graph
        A = URIRef('http://example.org/sample/example1#A')
        assert (A, RDF.type, OWL.Class) in g
        NAME = URIRef('http://example.org/sample/example1#name')
        assert (NAME, RDF.type, OWL.ObjectProperty) in g

if __name__ == '__main__':
    unittest.main()

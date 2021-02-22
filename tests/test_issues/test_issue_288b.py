import os
import unittest

from rdflib import URIRef, Graph
from rdflib.namespace import OWL, RDFS, RDF

from biolinkml.generators.yamlgen import YAMLGenerator
from tests.utils.compare_rdf import compare_rdf
from tests.utils.test_environment import TestEnvironmentTestCase
from biolinkml.utils.yamlutils import as_yaml
from tests.test_issues.environment import env


class IssueYamlGenTestCase(TestEnvironmentTestCase):
    env = env

    def test_yaml(self):
        yaml_fname = env.input_path('issue_288.yaml')
        gen = YAMLGenerator(yaml_fname, mergeimports=False)
        s = gen.serialize()
        print(s)

if __name__ == '__main__':
    unittest.main()

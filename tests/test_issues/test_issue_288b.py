import os
import unittest

from rdflib import URIRef, Graph
from rdflib.namespace import OWL, RDFS, RDF

from biolinkml.generators.yamlgen import YAMLGenerator
from tests.utils.compare_rdf import compare_rdf
from tests.utils.test_environment import TestEnvironmentTestCase
from biolinkml.utils.yamlutils import as_yaml
from tests.test_issues.environment import env


class IssueSQLGenTestCase(TestEnvironmentTestCase):
    env = env

    def test_transform(self):
        yaml_fname = env.input_path('issue_288.yaml')
        gen = YAMLGenerator(yaml_fname, mergeimports=False)
        #yaml_str = as_yaml(gen.schema)
        s = gen.serialize()
        print(s)
        #print(yaml_str)


if __name__ == '__main__':
    unittest.main()

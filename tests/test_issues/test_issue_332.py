import unittest

from biolinkml.generators.jsonldgen import JSONLDGenerator
from tests.test_issues.environment import env


class JSONContextTestCase(unittest.TestCase):
    def test_context(self):
        """ Test no context in the argument"""
        self.assertIn('''"@context": [
    [
      "https://w3id.org/biolink/biolinkml/context.jsonld"
    ],''', JSONLDGenerator(env.input_path('issue_332.yaml')).serialize())

    def test_context_2(self):
        """ Test a single context argument """
        self.assertIn('''"@context": [
    [
      "http://some.org/nice/context.jsonld"
    ],''', JSONLDGenerator(env.input_path('issue_332.yaml')).serialize(context="http://some.org/nice/context.jsonld"))

    def test_context_3(self):
        """ Test multi context arguments """
        self.assertIn('''"@context": [
    [
      "http://some.org/nice/context.jsonld",
      "http://that.org/context.jsonld"
    ],''', JSONLDGenerator(env.input_path('issue_332.yaml')).
              serialize(context=["http://some.org/nice/context.jsonld", "http://that.org/context.jsonld"]))


if __name__ == '__main__':
    unittest.main()

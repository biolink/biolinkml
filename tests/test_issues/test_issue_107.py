import unittest
from biolinkml.generators.pythongen import PythonGenerator

yaml_txt = """
id: https://issue_test/107/schema
name: schema

default_curi_maps:
    - semweb_context

types:
  string:
    uri: xsd:string
    base: str
    description: A character string

prefixes:
  ICD-9: http://test.org/prefix/ICD9

emit_prefixes:
    - ICD-9
"""


class PrefixTestCase(unittest.TestCase):
    def test_prefix(self):
        python = PythonGenerator(yaml_txt).serialize()
        compile(python, 'test', 'exec')
        self.assertTrue(True, "Passed the generate")


if __name__ == '__main__':
    unittest.main()

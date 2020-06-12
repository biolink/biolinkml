import os
import unittest

from biolinkml.generators.pythongen import PythonGenerator
from biolinkml.utils.yamlutils import as_yaml
from tests.test_issues import sourcedir
import yaml


class IssueYamlSerializerTestCase(unittest.TestCase):
    def test_roundtrip(self):
        yaml_fname = os.path.join(sourcedir, 'issue_134.yaml')

        gen = PythonGenerator(yaml_fname)
        schema = gen.schema
        yaml_str = as_yaml(schema)
        generated = yaml.safe_load(yaml_str)
        with open(yaml_fname) as yaml_file:
            original = yaml.safe_load(yaml_file)

        # The generated YAML contains many added fields. Some with default values. Therefore, we can't directly
        # compare it to the original.
        for key in original:
            self.assertEqual(len(original[key]), len(generated[key]))
            if isinstance(original[key], dict):
                for subkey in original[key]:
                    self.assertTrue(subkey in generated[key])


if __name__ == '__main__':
    unittest.main()

import os
import unittest

from biolinkml.generators.shexgen import ShExGenerator
from biolinkml.utils.yamlutils import as_yaml
from tests.test_issues import sourcedir


class MyTestCase(unittest.TestCase):
    def test_roundtrip(self):
        yaml_fname = os.path.join(sourcedir, 'issue_134.yaml')

        # we don't actually want json schema - this
        # is just to get a schemaobj
        gen = ShExGenerator(yaml_fname)

        schema = gen.schema
        print(schema)
        yaml = as_yaml(schema)

        print(f'YAML={yaml}')


if __name__ == '__main__':
    unittest.main()

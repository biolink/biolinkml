import unittest

from biolinkml.utils.schemaloader import SchemaLoader
from biolinkml.utils.yamlutils import as_yaml
from tests.test_issues.environment import env
from tests.utils.test_environment import TestEnvironmentTestCase


class Issue18TestCase(TestEnvironmentTestCase):
    env = env

    def test_issue_177(self):
        env.generate_single_file('issue_177.yaml',
                                 lambda: as_yaml(SchemaLoader(env.input_path('issue_177.yaml')).resolve()),
                                 value_is_returned=True)


if __name__ == '__main__':
    unittest.main()
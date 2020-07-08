import unittest

from biolinkml.generators.pythongen import PythonGenerator
from tests.utils.filters import metadata_filter
from tests.utils.python_comparator import compare_python
from tests.utils.test_environment import TestEnvironmentTestCase
from tests.test_issues.environment import env


class InheritedPhenotypicFeatureTestCase(TestEnvironmentTestCase):
    env = env

    def test_inheritence(self):
        env.generate_single_file('issue_14.py',
                                 lambda: PythonGenerator(env.input_path('issue_14.yaml')).serialize(),
                                 comparator=compare_python, filtr=metadata_filter, value_is_returned=True)


if __name__ == '__main__':
    unittest.main()

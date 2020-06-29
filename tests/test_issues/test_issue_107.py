import unittest
from biolinkml.generators.pythongen import PythonGenerator
from tests.utils.python_comparator import compare_python
from tests.utils.test_environment import TestEnvironmentTestCase
from tests.test_issues.environment import env


class PrefixTestCase(TestEnvironmentTestCase):
    env = env

    def test_prefix(self):
        env.generate_single_file('issue_107.py',
                                 lambda: PythonGenerator(env.input_path('issue_107.yaml')).serialize(),
                                 comparator=compare_python, value_is_returned=True)


if __name__ == '__main__':
    unittest.main()

import os
import unittest

from biolinkml.generators.pythongen import PythonGenerator
from tests.test_issues.environment import env
from tests.utils.python_comparator import compare_python
from tests.utils.test_environment import TestEnvironmentTestCase


class Issue260TestCase(TestEnvironmentTestCase):
    env = env

    def test_local_imports(self):
        """ Check the local import behavior """
        dir = 'issue_260'

        # Useful to have an __init__.py available
        init_path = env.actual_path(dir, '__init__.py')
        if not os.path.exists(init_path):
            with open(init_path, 'w'):
                pass

        env.generate_single_file('issue_260/issue_260a.py',
                                 lambda: PythonGenerator(env.input_path(dir, 'issue_260a.yaml'),
                                                         importmap=env.import_map, mergeimports=False).serialize(),
                                 comparator=compare_python, value_is_returned=True)
        env.generate_single_file('issue_260/issue_260b.py',
                                 lambda: PythonGenerator(env.input_path(dir, 'issue_260b.yaml'),
                                                         importmap=env.import_map, mergeimports=False).serialize(),
                                 comparator=compare_python, value_is_returned=True)
        env.generate_single_file('issue_260/issue_260c.py',
                                 lambda: PythonGenerator(env.input_path(dir, 'issue_260c.yaml'),
                                                         importmap=env.import_map, mergeimports=False).serialize(),
                                 comparator=compare_python, value_is_returned=True)
        env.generate_single_file('issue_260/issue_260.py',
                                 lambda: PythonGenerator(env.input_path(dir, 'issue_260.yaml'),
                                                         importmap=env.import_map, mergeimports=False).serialize(),
                                 comparator=compare_python, value_is_returned=True)


if __name__ == '__main__':
    unittest.main()

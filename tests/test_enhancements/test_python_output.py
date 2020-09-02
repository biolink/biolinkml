import unittest

from biolinkml.generators.pythongen import PythonGenerator
from tests.test_enhancements.environment import env
from tests.utils.python_comparator import compare_python
from tests.utils.test_environment import TestEnvironmentTestCase


class PythonOutputTestCase(TestEnvironmentTestCase):
    env = env

    def test_python_types(self):
        """ description """
        test_dir = 'python_generation'
        test_name = 'python_types'

        env.generate_single_file(f'{test_dir}/{test_name}.py',
                                 lambda: PythonGenerator(env.input_path(test_dir, f'{test_name}.yaml'),
                                                         importmap=env.import_map, mergeimports=False).serialize(),
                                 comparator=compare_python, value_is_returned=True)

    def test_python_complex_ranges(self):
        """ description """
        test_dir = 'python_generation'
        test_name = 'python_complex_ranges'

        env.generate_single_file(f'{test_dir}/{test_name}.py',
                                 lambda: PythonGenerator(env.input_path(test_dir, f'{test_name}.yaml'),
                                                         importmap=env.import_map, mergeimports=False).serialize(),
                                 comparator=compare_python, value_is_returned=True)

    def test_python_lists_and_keys(self):
        """ description """
        test_dir = 'python_generation'
        test_name = 'python_lists_and_keys'

        env.generate_single_file(f'{test_dir}/{test_name}.py',
                                 lambda: PythonGenerator(env.input_path(test_dir, f'{test_name}.yaml'),
                                                         importmap=env.import_map, mergeimports=False).serialize(),
                                 comparator=compare_python, value_is_returned=True)


if __name__ == '__main__':
    unittest.main()

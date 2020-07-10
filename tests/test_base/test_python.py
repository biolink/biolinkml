import unittest

from biolinkml.generators.pythongen import PythonGenerator
from tests.test_base.environment import env
from tests.utils.filters import metadata_filter
from tests.utils.python_comparator import compare_python
from tests.utils.test_environment import TestEnvironmentTestCase


class PythonTestCase(TestEnvironmentTestCase):
    """ Generate python for all of the models, compare them against what has been published
     and verify that they compile"""
    env = env

    @classmethod
    def setUpClass(cls) -> None:
        env.make_testing_directory(env.root_temp_file_path('includes'))

    def test_types_python(self):
        env.generate_single_file('includes/types.py', lambda: PythonGenerator(env.types_yaml).serialize(),
                                 value_is_returned=True, filtr=metadata_filter, comparator=compare_python,
                                 use_testing_root=True)

    def test_mapping_python(self):
        env.generate_single_file('includes/mappings.py', lambda: PythonGenerator(env.mapping_yaml).serialize(),
                                 value_is_returned=True, filtr=metadata_filter, comparator=compare_python,
                                 use_testing_root=True)

    def test_metamodel_python(self):
        env.generate_single_file('meta.py', lambda: PythonGenerator(env.meta_yaml).serialize(), value_is_returned=True,
                                 filtr=metadata_filter, comparator=compare_python, use_testing_root=True)


if __name__ == '__main__':
    unittest.main()

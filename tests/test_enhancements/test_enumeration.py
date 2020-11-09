import unittest

from biolinkml.generators.pythongen import PythonGenerator
from tests.test_enhancements.environment import env
from tests.utils.python_comparator import compare_python
from tests.utils.test_environment import TestEnvironmentTestCase


class EnumerationTestCase(TestEnvironmentTestCase):
    env = env
    testdir = 'enumeration'

    def test_evidence(self):
        """ Test evidence enumeration  """
        file = "evidence"
        env.generate_single_file(f'{self.testdir}/{file}.py',
                                 lambda: PythonGenerator(env.input_path(self.testdir, f'{file}.yaml'),
                                                         importmap=env.import_map, mergeimports=False).serialize(),
                                 comparator=lambda exp, act: compare_python(exp, act, self.env.expected_path(f'{self.testdir}/{file}.py')),
                                 value_is_returned=True)


if __name__ == '__main__':
    unittest.main()

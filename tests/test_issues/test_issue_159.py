import unittest

from tests.test_issues.environment import env
from tests.utils.test_environment import TestEnvironmentTestCase
import tests.test_issues.output.issue_159 as module


class Issue159TestCase(TestEnvironmentTestCase):
    env = env

    def test_string_template(self):
        """ Validate that a string template works """
        python_file = 'issue_159.py'
        python_file_path = env.expected_path(python_file)
        # env.generate_single_file(python_file,
        #                          lambda: PythonGenerator(env.input_path('issue_159.yaml'),
        #                                                  importmap=env.import_map, mergeimports=False).serialize(),
        #                          comparator=compare_python, value_is_returned=True)

        # module = compile_python(python_file_path)
        import tests.test_issues.input.issue_159 as module
        example1 = module.C1(value=117.43, units="acres/fortnight")
        self.assertEqual("117.43:acres/fortnight", str(example1))

        example2 = module.C1(value=-12.3)
        self.assertEqual("-12.3:", str(example2))
        example3 = module.C1.parse("1000: hectares")
        self.assertEqual('1000: hectares', str(example3))


if __name__ == '__main__':
    unittest.main()

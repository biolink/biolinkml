import unittest

from biolinkml.generators.pythongen import PythonGenerator
from tests.test_issues.environment import env
from tests.utils.python_comparator import validate_python


class Issue39UnitTest(unittest.TestCase):
    def test_python_import(self):
        """ Import generates for biolink-model """
        python = PythonGenerator(env.input_path('issue_38.yaml')).serialize()
        msg = validate_python(python)
        if msg:
            self.fail(msg)


if __name__ == '__main__':
    unittest.main()

import os
import unittest

from biolinkml.generators.pythongen import PythonGenerator

sourcedir = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'source')


class Issue39UnitTest(unittest.TestCase):
    def test_python_import(self):
        """ Import generates for biolink-model """
        python = PythonGenerator(os.path.join(sourcedir, 'issue_38.yaml')).serialize()
        print(python)
        # We never get here if the imports fails
        self.assertEqual(True, True)


if __name__ == '__main__':
    unittest.main()

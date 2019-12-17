import os
import unittest

from biolinkml.generators.pythongen import PythonGenerator
from tests.test_issues import sourcedir


class Issue5084TestCase(unittest.TestCase):
    def test_issue_84(self):
        yaml_fname = os.path.join(sourcedir, 'issue_84.yaml')
        PythonGenerator(yaml_fname).serialize()

    def test_issue_50(self):
        yaml_fname = os.path.join(sourcedir, 'issue_50.yaml')
        PythonGenerator(yaml_fname).serialize()



if __name__ == '__main__':
    unittest.main()

import os
import unittest

from biolinkml.generators.pythongen import PythonGenerator
from tests.test_issues import sourcedir


class SlotSubclassTestCase(unittest.TestCase):
    def test_slot_subclass_good(self):
        """ Test slot domain as superclass of parent """

        yaml_fname = os.path.join(sourcedir, 'issue_56_good.yaml')
        PythonGenerator(yaml_fname).serialize()
        self.assertTrue(True, "Didn't throw an error - we good")
        yaml_fname = os.path.join(sourcedir, 'issue_56_bad.yaml')
        PythonGenerator(yaml_fname).serialize()

    @unittest.skipIf(True, "We still need to figure out what to do here")
    def test_slot_subclass_bad(self):
        """ Test slot domain as superclass of parent """

        yaml_fname = os.path.join(sourcedir, 'issue_56_bad.yaml')
        with self.assertRaises(ValueError):
            PythonGenerator(yaml_fname).serialize()


if __name__ == '__main__':
    unittest.main()

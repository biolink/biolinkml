import os
import unittest

from biolinkml import LOCAL_YAML_PATH, meta, LOCAL_TYPES_PATH
from includes import types
from biolinkml.generators.pythongen import PythonGenerator
from tests import targetdir
from tests.test_scripts.clicktestcase import metadata_filter


class PythonGenTestCase(unittest.TestCase):
    cwd = os.path.abspath(os.path.dirname(__file__))

    def gen_and_test(self, yaml_path: str, target_python: str, master_python: str) -> None:
        pydata = str(PythonGenerator(yaml_path, "py", emit_metadata=True).serialize())
        with open(target_python, 'w') as pyfile:
            pyfile.write(pydata)

        with open(target_python) as newf:
            newdat = metadata_filter(newf.read())
            with open(master_python) as oldf:
                olddat = metadata_filter(oldf.read())
                self.maxDiff = None
        if olddat != newdat:
            print("-" * 80)
            print(pydata)
            print('-' * 80)
        self.assertEqual(olddat, newdat, f'\n{master_python} does not match output -- run "make regen-mm"?')

    def test_metamodel(self):
        """ Generate a new metamodel and verify that it matches what we used to build it """

        # Test the types file
        self.gen_and_test(LOCAL_TYPES_PATH, os.path.join(targetdir, 'types.py'), types.__file__)

        # Test the metamodel
        self.gen_and_test(LOCAL_YAML_PATH, os.path.join(targetdir, 'meta.py'), meta.__file__)


if __name__ == '__main__':
    unittest.main()

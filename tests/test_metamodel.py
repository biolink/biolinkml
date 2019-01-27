import os
import unittest

from biolinkml import LOCAL_YAML_PATH, meta
from biolinkml.generators.pythongen import PythonGenerator
from tests import targetdir
from tests.test_scripts.clicktestcase import metadata_filter

class PythonGenTestCase(unittest.TestCase):
    cwd = os.path.abspath(os.path.dirname(__file__))

    def test_metamodel(self):
        """ Generate a new metamodel and verify that it matches what we used to build it """
        pydata = str(PythonGenerator(LOCAL_YAML_PATH, "py", emit_metadata=True).serialize())
        target_python = os.path.join(targetdir, 'meta.py')
        master_python = meta.__file__
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


if __name__ == '__main__':
    unittest.main()

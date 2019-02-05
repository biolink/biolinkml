import unittest

import os
import unittest

from biolinkml import LOCAL_YAML_PATH, meta, LOCAL_TYPES_PATH
from includes import types
from biolinkml.generators.pythongen import PythonGenerator
from tests import targetdir
from tests.test_scripts.clicktestcase import metadata_filter

cwd = os.path.abspath(os.path.join(os.path.dirname(__file__)))
default_yaml_path = os.path.join(cwd, 'source')
default_target_path = os.path.join(cwd, 'target')
default_master_path = os.path.join(cwd, 'biolink_metamodel')


class BiolinkModelTestCase(unittest.TestCase):
    cwd = os.path.abspath(os.path.dirname(__file__))

    def gen_and_test(self, filename: str, yaml_path: str = default_yaml_path, target_path: str = default_target_path,
                     master_path: str = default_master_path) -> None:
        yaml = os.path.join(yaml_path, f"{filename}.yaml")
        target_python = os.path.join(target_path, f"{filename}.py")
        master_python = os.path.join(master_path, f"{filename}.py")
        pydata = str(PythonGenerator(yaml, "py", emit_metadata=True).serialize())
        # TODO: figure this bit out
        pydata = pydata.\
            replace('from biolink_types ', 'from tests.test_biolink_model.biolink_metamodel.includes.biolink_types ').\
            replace('from biolink_named_thing ', 'from tests.test_biolink_model.biolink_metamodel.biolink_named_thing ').\
            replace('from biolink_association', 'from tests.test_biolink_model.biolink_metamodel.biolink_association ')
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

    def test_biolink_types(self):
        """ Test biolink_types generator """
        self.gen_and_test('biolink_types', master_path=os.path.join(default_master_path, 'includes'))

    def test_biolink_named_thing(self):
        self.gen_and_test('biolink_named_thing')

    def test_biolink_association(self):
        self.gen_and_test('biolink_association')

    def test_biolink_metamodel(self):
        self.gen_and_test('biolink_metamodel')

if __name__ == '__main__':
    unittest.main()

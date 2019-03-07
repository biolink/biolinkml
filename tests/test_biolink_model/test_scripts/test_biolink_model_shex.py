import os
import unittest

from biolinkml.generators.shexgen import cli
from tests.test_biolink_model.test_scripts.mmclicktestcase import MMClickTestCase
from tests.test_biolink_model import yaml_dir


class GenMetamodelShex(MMClickTestCase):
    testdir = "genshex"
    click_ep = cli
    prog_name = "gen-shex"
    dirname = 'biolinkmodel'

    def do_it(self, fname: str) -> None:
        outfile = os.path.join(self.testdir_path, 'biolink-model.shex')
        yaml_path = os.path.join(yaml_dir, 'orig', 'biolink-model.yaml')
        self.do_test(yaml_path, testfile=outfile)

    def test_biolink_metamodel(self):
        self.do_it('biolink_metamodel')



if __name__ == '__main__':
    unittest.main()

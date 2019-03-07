import os
import unittest

from biolinkml.generators.summarygen import cli
from tests import source_yaml_path
from tests.test_scripts.clicktestcase import ClickTestCase

# This has to occur post ClickTestCase
import click

@unittest.skipIf(True, "Pending update in model")
class SummaryGenTestCase(ClickTestCase):
    testdir = "gensummary"
    click_ep = cli
    prog_name = "gen-summary"

    def test_help(self):
        self.do_test("--help", 'help')

    def test_meta(self):
        self.do_test(source_yaml_path, 'meta.tsv')

    def test_biolink_named_thing(self):
        yaml_path = os.path.join(self.test_base_dir, '..', '..', 'test_biolink_model', 'yaml', 'metamodel',
                                 'biolink_named_thing.yaml')
        self.do_test(yaml_path, 'biolink_named_thing.tsv')

    def test_biolink_association(self):
        yaml_path = os.path.join(self.test_base_dir, '..', '..', 'test_biolink_model', 'yaml', 'metamodel',
                                 'biolink_association.yaml')
        self.do_test(yaml_path, 'biolink_association.tsv')

    def test_biolink_metamodel(self):
        yaml_path = os.path.join(self.test_base_dir, '..', '..', 'test_biolink_model', 'yaml', 'metamodel',
                                 'biolink_metamodel.yaml')
        self.do_test(yaml_path, 'biolink_metamodel.tsv')


if __name__ == '__main__':
    unittest.main()

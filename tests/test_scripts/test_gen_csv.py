import unittest

from biolinkml.generators.csvgen import cli
from tests import source_yaml_path
from tests.test_scripts.clicktestcase import ClickTestCase

# This has to occur post ClickTestCase
import click


class GenCSVTestCase(ClickTestCase):
    testdir = "gencsv"
    click_ep = cli
    prog_name = "gen-csv"

    def test_help(self):
        self.do_test("--help", 'help')

    def test_meta(self):
        self.do_test(source_yaml_path, 'meta.csv')
        self.do_test(source_yaml_path + ' -f tsv', 'meta.tsv')
        self.do_test(source_yaml_path + ' -f xsv', 'meta_error', error=click.exceptions.BadParameter)
        self.do_test([source_yaml_path, "-r", "schema_definition"], 'meta_sd')
        self.do_test([source_yaml_path, "-r", "schema_definition", "-r", "slot_definition"], 'meta_sd_sd')
        self.do_test([source_yaml_path, "-r", "nada"], 'meta_sd', error=ValueError)


if __name__ == '__main__':
    unittest.main()

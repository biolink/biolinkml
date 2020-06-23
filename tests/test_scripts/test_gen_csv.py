import unittest

from biolinkml.generators.csvgen import cli
from tests.test_scripts import meta_yaml
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
        self.do_test(meta_yaml, 'meta.csv')
        self.do_test(meta_yaml + ' -f tsv', 'meta.tsv')
        self.do_test(meta_yaml + ' -f xsv', 'meta_error', expected_error=click.exceptions.BadParameter)
        self.do_test([meta_yaml, "-r", "schema_definition"], 'meta_sd')
        self.do_test([meta_yaml, "-r", "schema_definition", "-r", "slot_definition"], 'meta_sd_sd')
        self.do_test([meta_yaml, "-r", "nada"], 'meta_sd', expected_error=ValueError)


if __name__ == '__main__':
    unittest.main()

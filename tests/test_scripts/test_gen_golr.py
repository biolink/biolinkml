import unittest

# This has to occur post ClickTestCase
import click

from biolinkml.generators.golrgen import cli
from tests import source_yaml_path
from tests.test_scripts.clicktestcase import ClickTestCase


class GolrViewTestCase(ClickTestCase):
    testdir = "gengolr"
    click_ep = cli
    prog_name = "gen-golr-views"

    def test_help(self):
        self.do_test("--help", 'help')

    def test_meta(self):
        outdir = self.temp_directory('meta')
        self.do_test(source_yaml_path + f" -d {outdir}", dirbase='meta')
        self.do_test(source_yaml_path + f' -f xsv -d {outdir}', error=click.exceptions.BadParameter)


if __name__ == '__main__':
    unittest.main()

import unittest

# This has to occur post ClickTestCase
import click

from biolinkml.generators.golrgen import cli
from tests.test_scripts import meta_yaml
from tests.test_scripts.clicktestcase import ClickTestCase


class GolrViewTestCase(ClickTestCase):
    testdir = "gengolr"
    click_ep = cli
    prog_name = "gen-golr-views"

    def test_help(self):
        self.do_test("--help", 'help')

    def test_meta(self):
        self.do_test(meta_yaml, 'meta', is_directory=True)
        self.do_test(meta_yaml + f' -f xsv', 'error', is_directory=True, expected_error=click.exceptions.BadParameter)


if __name__ == '__main__':
    unittest.main()

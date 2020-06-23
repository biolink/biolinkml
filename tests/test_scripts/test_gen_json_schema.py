import unittest

# This has to occur post ClickTestCase
import click
from biolinkml.generators.jsonschemagen import cli
from tests.test_scripts import meta_yaml
from tests.test_scripts.clicktestcase import ClickTestCase


class GenJSONSchemaTestCase(ClickTestCase):
    testdir = "genjsonschema"
    click_ep = cli
    prog_name = "gen-json-schema"

    def test_help(self):
        self.do_test("--help", 'help')

    def test_meta(self):
        self.maxDiff = None
        self.do_test(meta_yaml, 'meta.jsonld')
        self.do_test(meta_yaml + ' -f json', 'meta.jsonld')
        self.do_test(meta_yaml + ' -f xsv', 'meta_error', expected_error=click.exceptions.BadParameter)
        self.do_test(meta_yaml + " -i", 'meta_inline.json')


if __name__ == '__main__':
    unittest.main()

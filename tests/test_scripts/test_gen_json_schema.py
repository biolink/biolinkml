import unittest

# This has to occur post ClickTestCase
import click
from biolinkml.generators.jsonschemagen import cli
from tests import source_yaml_path
from tests.test_scripts.clicktestcase import ClickTestCase


class GenJSONSchemaTestCase(ClickTestCase):
    testdir = "genjsonschema"
    click_ep = cli
    prog_name = "gen-json-schema"

    def test_help(self):
        self.do_test("--help", 'help', tox_wrap_fix=True)

    def test_meta(self):
        self.maxDiff = None
        self.do_test(source_yaml_path, 'meta.jsonld')
        self.do_test(source_yaml_path + ' -f json', 'meta.jsonld')
        self.do_test(source_yaml_path + ' -f xsv', 'meta_error', error=click.exceptions.BadParameter)
        self.do_test(source_yaml_path + " -i", 'meta_inline.json')


if __name__ == '__main__':
    unittest.main()

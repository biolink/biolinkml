import unittest

import click
from biolinkml.generators.jsonschemagen import cli

from tests.test_scripts.environment import env
from tests.utils.clicktestcase import ClickTestCase


class GenJSONSchemaTestCase(ClickTestCase):
    testdir = "genjsonschema"
    click_ep = cli
    prog_name = "gen-json-schema"
    env = env

    def test_help(self):
        self.do_test("--help", 'help')

    def test_meta(self):

        self.do_test([], 'meta.jsonld')
        self.do_test('-f json', 'meta.jsonld')
        self.do_test('-f xsv', 'meta_error', expected_error=click.exceptions.BadParameter)
        self.do_test('-i', 'meta_inline.json')


if __name__ == '__main__':
    unittest.main()

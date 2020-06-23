import unittest

# This has to occur post ClickTestCase
import click

from biolinkml.generators.graphqlgen import cli
from tests.test_scripts import meta_yaml
from tests.test_scripts.clicktestcase import ClickTestCase


class GenGraphqlTestCase(ClickTestCase):
    testdir = "gengraphql"
    click_ep = cli
    prog_name = "gen-graphql"

    def test_help(self):
        self.do_test("--help", 'help')

    def test_meta(self):
        self.do_test(meta_yaml, 'meta.graphql')
        self.do_test(meta_yaml + ' -f xsv', 'meta_error', expected_error=click.exceptions.BadParameter)


if __name__ == '__main__':
    unittest.main()

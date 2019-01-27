import unittest

# This has to occur post ClickTestCase
import click

from biolinkml.generators.graphqlgen import cli
from tests import source_yaml_path
from tests.test_scripts.clicktestcase import ClickTestCase


class GenGraphqlTestCase(ClickTestCase):
    testdir = "gengraphql"
    click_ep = cli
    prog_name = "gen-graphql"

    def test_help(self):
        self.do_test("--help", 'help')

    def test_meta(self):
        self.do_test(source_yaml_path, 'meta.graphql')
        self.do_test(source_yaml_path + ' -f xsv', 'meta_error', error=click.exceptions.BadParameter)


if __name__ == '__main__':
    unittest.main()

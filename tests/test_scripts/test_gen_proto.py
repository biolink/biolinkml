import unittest

# This has to occur post ClickTestCase
import click

from biolinkml.generators.protogen import cli
from tests.test_scripts import meta_yaml
from tests.test_scripts.clicktestcase import ClickTestCase


class GenProtoTestCase(ClickTestCase):
    testdir = "genproto"
    click_ep = cli
    prog_name = "gen-proto"

    def test_help(self):
        self.do_test("--help", 'help')

    def test_meta(self):
        self.do_test(meta_yaml, 'meta.proto')
        self.do_test(meta_yaml + ' -f proto', 'meta.proto')
        self.do_test(meta_yaml + ' -f xsv', 'meta_error', expected_error=click.exceptions.BadParameter)


if __name__ == '__main__':
    unittest.main()

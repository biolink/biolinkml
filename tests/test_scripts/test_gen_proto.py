import unittest

# This has to occur post ClickTestCase
import click

from biolinkml.generators.protogen import cli
from tests import source_yaml_path
from tests.test_scripts.clicktestcase import ClickTestCase


class GenProtoTestCase(ClickTestCase):
    testdir = "genproto"
    click_ep = cli
    prog_name = "gen-proto"

    def test_help(self):
        self.do_test("--help", 'help')

    def test_meta(self):
        self.do_test(source_yaml_path, 'meta.proto')
        self.do_test(source_yaml_path + ' -f proto', 'meta.proto')
        self.do_test(source_yaml_path + ' -f xsv', 'meta_error', error=click.exceptions.BadParameter)


if __name__ == '__main__':
    unittest.main()

import unittest

# This has to occur post ClickTestCase
import click

from biolinkml.generators.yumlgen import cli, YumlGenerator
from tests import source_yaml_path
from tests.test_scripts.clicktestcase import ClickTestCase


class GenYUMLTestCase(ClickTestCase):
    testdir = "genyuml"
    click_ep = cli
    prog_name = "gen-yuml"

    def test_help(self):
        self.do_test("--help", 'help')

    def test_meta(self):
        self.maxDiff = None

        self.do_test(source_yaml_path, 'meta.yuml')
        self.do_test(source_yaml_path + ' -f yuml', 'meta.yuml')
        self.do_test(source_yaml_path + ' -f xsv', 'meta_error', error=click.exceptions.BadParameter)
        self.do_test(source_yaml_path + ' -c definition', 'definition.yuml')
        self.do_test(source_yaml_path + ' -c definition -c element', 'definition_element.yuml')
        self.do_test(source_yaml_path + ' -c noclass', 'definition.yuml', error=ValueError)

        tmp_dir = self.temp_directory('meta')
        self.do_test([source_yaml_path, '-c', 'schema_definition', '-d', tmp_dir], dirbase='meta')
        tmp_dir = self.temp_directory('meta1')
        self.do_test([source_yaml_path, '-c', 'definition', '-d', tmp_dir], dirbase='meta1')
        tmp_dir = self.temp_directory('meta2')
        self.do_test([source_yaml_path, '-c', 'element', '-d', tmp_dir], dirbase='meta2')

        # Directory tests
        for fmt in YumlGenerator.valid_formats:
            if fmt != 'yuml':
                tmp_dir = self.temp_directory('meta_' + fmt)
                self.do_test([source_yaml_path, '-f', fmt, '-c', 'schema_definition', '-d', tmp_dir],
                             dirbase='meta_' + fmt)


if __name__ == '__main__':
    unittest.main()

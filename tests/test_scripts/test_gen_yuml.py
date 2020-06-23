import unittest

# This has to occur post ClickTestCase
import click

from biolinkml.generators.yumlgen import cli, YumlGenerator
from tests.test_scripts import meta_yaml
from tests.test_scripts.clicktestcase import ClickTestCase


class GenYUMLTestCase(ClickTestCase):
    testdir = "genyuml"
    click_ep = cli
    prog_name = "gen-yuml"

    def test_help(self):
        self.do_test("--help", 'help')

    def test_meta(self):

        self.do_test(meta_yaml, 'meta.yuml')
        self.do_test(meta_yaml + ' -f yuml', 'meta.yuml')
        self.do_test(meta_yaml + ' -f xsv', 'meta_error', expected_error=click.exceptions.BadParameter)
        self.do_test(meta_yaml + ' -c definition', 'definition.yuml')
        self.do_test(meta_yaml + ' -c definition -c element', 'definition_element.yuml')
        self.do_test(meta_yaml + ' -c noclass', 'definition.yuml', expected_error=ValueError)

        self.do_test([meta_yaml, '-c', 'schema_definition'], 'meta', is_directory=True)
        self.do_test([meta_yaml, '-c', 'definition'], 'meta1', is_directory=True)
        self.do_test([meta_yaml, '-c', 'element'], 'meta2', is_directory=True)

        # Directory tests
        for fmt in YumlGenerator.valid_formats:
            if fmt != 'yuml':
                self.do_test([meta_yaml, '-f', fmt, '-c', 'schema_definition'],
                             'meta_' + fmt, is_directory=True)


if __name__ == '__main__':
    unittest.main()

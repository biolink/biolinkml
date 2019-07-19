import os
import re
import unittest

# This has to occur post ClickTestCase
import click

from biolinkml.generators.jsonldcontextgen import cli
from tests import sourcedir, source_yaml_path
from tests.test_scripts.clicktestcase import ClickTestCase


def json_metadata_filter(s: str) -> str:
    ...
    return re.sub(r'Auto generated from .*? by', 'Auto generated from ... by',
                  re.sub(r'Generation date: .*?\\n', 'Generation date: \n', s))


class GenContextTestCase(ClickTestCase):
    testdir = "gencontext"
    click_ep = cli
    prog_name = "gen-jsonld-context"

    def test_help(self):
        self.do_test("--help", 'help')

    def test_meta(self):
        self.maxDiff = None
        self.do_test(source_yaml_path, 'meta_context.jsonld', filtr=json_metadata_filter)
        self.do_test(source_yaml_path + ' --metauris', 'meta_contextn.jsonld', filtr=json_metadata_filter)
        self.do_test(source_yaml_path + ' -f xsv', 'meta_error', error=click.exceptions.BadParameter)
        self.do_test(source_yaml_path + ' --niggles', 'meta2_error', error=click.exceptions.NoSuchOption)

    def test_slot_class_uri(self):
        uri_tests_yaml = os.path.join(sourcedir, 'uri_tests.yaml')
        self.do_test(uri_tests_yaml, 'uri_tests.jsonld', filtr=json_metadata_filter)


if __name__ == '__main__':
    unittest.main()

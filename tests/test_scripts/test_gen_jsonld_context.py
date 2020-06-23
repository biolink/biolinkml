import os
import unittest

# This has to occur post ClickTestCase
import click

from biolinkml.generators.jsonldcontextgen import cli
from tests.test_scripts import meta_yaml, env
from tests.test_scripts.clicktestcase import ClickTestCase
from tests.utils.metadata_filters import ldcontext_metadata_filter


class GenContextTestCase(ClickTestCase):
    testdir = "gencontext"
    click_ep = cli
    prog_name = "gen-jsonld-context"

    def test_help(self):
        self.do_test("--help", 'help')

    def test_meta(self):
        self.maxDiff = None
        self.do_test(meta_yaml, 'meta_context.jsonld', filtr=ldcontext_metadata_filter)
        self.do_test(meta_yaml + ' --metauris', 'meta_contextn.jsonld', filtr=ldcontext_metadata_filter)
        self.do_test(meta_yaml + ' -f xsv', 'meta_error', expected_error=click.exceptions.BadParameter)
        self.do_test(meta_yaml + ' --niggles', 'meta2_error', expected_error=click.exceptions.NoSuchOption)

    def test_slot_class_uri(self):
        self.do_test(env.input_path('uri_tests.yaml'), 'uri_tests.jsonld', filtr=ldcontext_metadata_filter)


if __name__ == '__main__':
    unittest.main()

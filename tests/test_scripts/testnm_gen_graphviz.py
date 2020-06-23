import unittest

# This has to occur post ClickTestCase
import click

from biolinkml.generators.dotgen import cli
from tests.test_scripts import meta_yaml
from tests.test_scripts.clicktestcase import ClickTestCase


class GraphvizTestCase(ClickTestCase):
    testdir = "gengraphviz"
    click_ep = cli
    prog_name = "gen-graphviz"

    def test_help(self):
        self.do_test("--help", 'help')

    @unittest.skipIf(False, 'Determine whether we need graphviz before moving further')
    def test_meta(self):

        # 'ALL' may be useful, but it is very time consuming
        self.do_test(meta_yaml + f" -o all", 'meta', is_directory=True)
        self.do_test(meta_yaml + f" -f svg -o all", 'meta1', is_directory=True)
        self.do_test(meta_yaml + f' -f xyz -o all', 'nada', is_directory=True,
                     expected_error=click.exceptions.BadParameter)
        self.do_test(meta_yaml + f" -c definition", 'meta2', is_directory=True)
        self.do_test([meta_yaml, "-c", "class_definition", "-c", "element"], 'meta3', is_directory=True)
        self.do_test([meta_yaml, "-c", "nada"], "nada", is_directory=True, expected_error=ValueError)


if __name__ == '__main__':
    unittest.main()

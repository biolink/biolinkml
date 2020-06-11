import os
import unittest

# This has to occur post ClickTestCase
import click

from biolinkml.generators.dotgen import cli
from tests import source_yaml_path
from tests.test_scripts.clicktestcase import ClickTestCase


class GraphvizTestCase(ClickTestCase):
    testdir = "gengraphviz"
    click_ep = cli
    prog_name = "gen-graphviz"

    def test_help(self):
        self.do_test("--help", 'help')

    @unittest.skipIf(True, 'Determine whether we need graphviz before moving further')
    def test_meta(self):

        # ALL may be useful, but it is very time consuming
        # NOTE: Because the GraphViz output binaries can vary considerably, we don't try to compare them
        outdir = self.temp_directory('meta')
        self.do_test(source_yaml_path + f" -d {outdir} -o all", dirbase='meta', comparator=self.always_pass_comparator)
        outdir = self.temp_directory('meta1')
        self.do_test(source_yaml_path + f" -f svg -d {outdir} -o all", dirbase='meta1',
                     comparator=self.always_pass_comparator)
        self.do_test(source_yaml_path + f' -f xyz -d {outdir} -o all', error=click.exceptions.BadParameter)
        outdir = os.path.join(self.tmpdir_path, 'meta2')
        self.do_test(source_yaml_path + f" -d {outdir} -c definition", dirbase='meta2',
                     comparator=self.always_pass_comparator)
        outdir = os.path.join(self.tmpdir_path, 'meta3')
        self.do_test([source_yaml_path, "-d", outdir, "-c", "class_definition", "-c", "element"], dirbase='meta3',
                     comparator=self.always_pass_comparator)
        self.do_test([source_yaml_path, "-c", "nada"], error=ValueError)

if __name__ == '__main__':
    unittest.main()

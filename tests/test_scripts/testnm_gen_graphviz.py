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

    def test_meta(self):

        # ALL may be useful, but it is very time consuming
        outdir = self.temp_directory('meta')
        self.do_test(source_yaml_path + f" -d {outdir} -o all", dirbase='meta')
        outdir = self.temp_directory('meta1')
        self.do_test(source_yaml_path + f" -f svg -d {outdir} -o all", dirbase='meta1')
        self.do_test(source_yaml_path + f' -f xyz -d {outdir} -o all', error=click.exceptions.BadParameter)
        outdir = os.path.join(self.tmpdir_path, 'meta2')
        self.do_test(source_yaml_path + f" -d {outdir} -c definition", dirbase='meta2')
        outdir = os.path.join(self.tmpdir_path, 'meta3')
        self.do_test([source_yaml_path, "-d", outdir, "-c", "class_definition", "-c", "element"], dirbase='meta3')
        self.do_test([source_yaml_path, "-c", "nada"], error=ValueError)


if __name__ == '__main__':
    unittest.main()

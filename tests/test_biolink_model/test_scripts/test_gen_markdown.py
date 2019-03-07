import os
import unittest

from biolinkml.generators.markdowngen import cli
from tests.test_biolink_model.test_scripts.mmclicktestcase import MMClickTestCase
from tests.test_biolink_model import metamodel_yaml_path

class GenMarkdownTestCase(MMClickTestCase):
    testdir = "genmarkdown"
    click_ep = cli
    prog_name = "gen-markdown"
    dirname = 'metamodel'

    def do_it(self, fname: str) -> None:
        outdir = self.temp_directory(self.dirname)
        yaml_path = os.path.join(metamodel_yaml_path, f'{fname}.yaml')
        self.do_test(yaml_path + f" -d {outdir}", dirbase=self.dirname)

    def test_biolink_metamodel(self):
        self.do_it('biolink_metamodel')



if __name__ == '__main__':
    unittest.main()

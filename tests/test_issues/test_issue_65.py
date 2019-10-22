import os
import unittest

from biolinkml.generators.markdowngen import MarkdownGenerator
from tests.test_issues import sourcedir, outputdir
from tests.utils.dirutils import make_and_clear_directory


class Issue65TestCase(unittest.TestCase):

    def test_issue_65(self):
        """ Make sure that types are generated as part of the output """
        outdir = os.path.join(outputdir, 'issue65')
        make_and_clear_directory(outdir)
        yaml_fname = os.path.join(sourcedir, 'issue_65.yaml')
        MarkdownGenerator(yaml_fname).serialize(directory=outdir)


if __name__ == '__main__':
    unittest.main()

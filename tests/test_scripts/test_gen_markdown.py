import os
import unittest

from biolinkml.generators.markdowngen import cli
from tests.test_scripts import meta_yaml
from tests.test_scripts.clicktestcase import ClickTestCase


class GenMarkdownTestCase(ClickTestCase):
    testdir = "genmarkdown"
    click_ep = cli
    prog_name = "gen-markdown"

    def test_help(self):
        self.do_test("--help", 'help')

    def test_meta(self):
        outdir = self.temp_directory('meta')
        self.do_test(meta_yaml, 'meta', is_directory=True)

    def _exists(self, *path: str) -> None:
        expected = self.expected_file_path(*path)
        self.assertTrue(os.path.exists(expected), f"Failed to create {expected}")

    def test_issue_2(self):
        self.do_test(meta_yaml + f"  -c example -i ", 'issue2', is_directory=True)
        self._exists('issue2', 'images', 'Example.svg')
        self.assertFalse(os.path.exists(self.expected_file_path('issue2', 'abstract.md')))


if __name__ == '__main__':
    unittest.main()

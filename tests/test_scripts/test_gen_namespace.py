import unittest
from biolinkml.generators import namespacegen
from tests.test_scripts.environment import env
from tests.utils.clicktestcase import ClickTestCase
from tests.utils.filters import metadata_filter
from tests.utils.python_comparator import compare_python


class GenNamespaceTestCase(ClickTestCase):
    testdir = "gennamespace"
    click_ep = namespacegen.cli
    prog_name = "gen-namespace"
    env = env

    def test_help(self):
        self.do_test("--help", 'help')

    def test_meta(self):
        self.maxDiff = None
        self.do_test([], 'meta_namespaces.py', filtr=metadata_filter, comparator=compare_python)


if __name__ == '__main__':
    unittest.main()

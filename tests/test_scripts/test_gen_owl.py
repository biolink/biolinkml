import re
import unittest

# This has to occur post ClickTestCase
from functools import reduce
from typing import List, Tuple

import click

from biolinkml.generators.owlgen import cli
from tests import source_yaml_path
from tests.test_scripts.clicktestcase import ClickTestCase

repl: List[Tuple[str, str]] = [
    (r'\s*meta:generation_date ".*" ;', 'meta:generation_date "Fri Jan 25 14:22:29 2019" ;'),
    (r'\s*meta:source_file_date ".*" ;', 'meta:source_file_date "Fri Jan 25 14:22:29 2019" ;')
]


def filtr(txt: str) -> str:
    return reduce(lambda s, expr: re.sub(expr[0], expr[1], s, flags=re.MULTILINE), repl, txt)


class GenOWLTestCase(ClickTestCase):
    testdir = "genowl"
    click_ep = cli
    prog_name = "gen-owl"

    def test_help(self):
        self.do_test("--help", 'help', bypass_soft_compare=True)

    def test_meta(self):
        self.maxDiff = None
        self.do_test(source_yaml_path, 'meta_owl.ttl', filtr=filtr, comparator=ClickTestCase.rdf_comparator)
        self.soft_compare = "Files differ but json-ld OWL representations have bnodes and ordering issues"
        self.do_test(source_yaml_path + ' -f json-ld', 'meta_owl.jsonld')
        self.soft_compare = None
        self.do_test(source_yaml_path + ' -f n3', 'meta_owl.n3', filtr=filtr, comparator=ClickTestCase.n3_comparator)
        self.do_test(source_yaml_path + ' -f xsv', 'meta_error', error=click.exceptions.BadParameter)


if __name__ == '__main__':
    unittest.main()

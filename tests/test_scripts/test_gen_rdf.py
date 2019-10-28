import os
import re
import unittest

# This has to occur post ClickTestCase
from functools import reduce
from typing import List, Tuple
from urllib.parse import urljoin

import click

from biolinkml.generators.rdfgen import cli
from tests import source_yaml_path
from tests.test_scripts.clicktestcase import ClickTestCase
from tests import source_context_path


repl1: List[Tuple[str, str]] = [
    (r'(\s*):generation_date\s*".*"\^\^xsd:dateTime', r'\1:generation_date "2019-01-25 12:34"^^xsd:dateTime'),
    (r'(\s*):source_file_date\s*".*"\^\^xsd:dateTime', r'\1:source_file_date "2019-01-25 12:34"^^xsd:dateTime'),
    (r'(\s*):source_file_size\s*[0-9]+', r'\1:source_file_size 10000'),
]


def filtr(txt: str) -> str:
    return reduce(lambda s, expr: re.sub(expr[0], expr[1], s, flags=re.MULTILINE), repl1, txt)


class GenRDFTestCase(ClickTestCase):
    testdir = "genrdf"
    click_ep = cli
    prog_name = "gen-rdf"

    def test_help(self):
        self.do_test("--help", 'help', bypass_soft_compare=True)

    def test_meta(self):
        """ Test the RDF generator on the metamodel """
        meta_context_path = urljoin('file:', os.path.join(self.test_base_dir, 'gencontext', 'meta_context.jsonld'))
        meta_contextn_path = urljoin('file:', os.path.join(self.test_base_dir, 'gencontext', 'meta_contextn.jsonld'))
        self.maxDiff = None
        self.do_test(source_yaml_path + f" --context {meta_context_path}", 'meta.ttl', filtr=filtr,
                     comparator=ClickTestCase.rdf_comparator)
        self.do_test(source_yaml_path + f" --context {meta_contextn_path} --metauris", 'metan.ttl', filtr=filtr,
                     comparator=ClickTestCase.rdf_comparator)
        self.do_test(source_yaml_path + f' -f n3  --context {meta_context_path}', 'meta.n3', filtr=filtr,
                     comparator=ClickTestCase.rdf_comparator)
        self.do_test(source_yaml_path + f' -f xsv  --context {meta_context_path}', 'meta_error',
                     error=click.exceptions.BadParameter)

    def test_make_script(self):
        """ Test a relative file path in JSON """
        self.do_test(source_yaml_path + f" --context {source_context_path}",
                     'make_output.ttl', filtr=filtr, comparator=ClickTestCase.rdf_comparator)


if __name__ == '__main__':
    unittest.main()

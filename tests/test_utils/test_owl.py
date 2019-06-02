import os
import re
import unittest

from functools import reduce
from typing import List, Tuple

from rdflib import Graph

from biolinkml.generators.owlgen import OwlSchemaGenerator
from tests.test_utils import inputdir
from tests.test_utils.support.base import Base

repl: List[Tuple[str, str]] = [
    (r'\s*meta:generation_date ".*" ;', 'meta:generation_date "Fri Jan 25 14:22:29 2019" ;'),
    (r'\s*meta:source_file_date ".*" ;', 'meta:source_file_date "Fri Jan 25 14:22:29 2019" ;')
]


def filtr(txt: str) -> str:
    return reduce(lambda s, expr: re.sub(expr[0], expr[1], s, flags=re.MULTILINE), repl, txt)


class OWLTestCase(Base):

    def assertOwlEqual(self, s1: str, s2: str) -> None:
        g1 = Graph()
        g2 = Graph()
        g1.parse(data=s1, format="turtle")
        g2.parse(data=s2, format="turtle")
        self.assertTrue(g1.isomorphic(g2))

    def test_cardinalities(self):
        owl_txt = OwlSchemaGenerator(os.path.join(inputdir, 'owl1.yaml')).serialize()
        self.eval_output(owl_txt, 'owl1.owl', filtr, self.assertOwlEqual)

    def test_pred_types(self):
        owl_txt = OwlSchemaGenerator(os.path.join(inputdir, 'owl2.yaml')).serialize()
        self.eval_output(owl_txt, 'owl2.owl', filtr, self.assertOwlEqual)


if __name__ == '__main__':
    unittest.main()

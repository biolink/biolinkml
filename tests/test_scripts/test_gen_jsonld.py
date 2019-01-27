import os
import re
import unittest
# This has to occur post ClickTestCase
from functools import reduce
from typing import List, Tuple
from urllib.parse import urljoin

import click
from rdflib import Graph, URIRef
from rdflib.collection import Collection

from biolinkml import METAMODEL_NAMESPACE
from biolinkml.generators.jsonldcontextgen import ContextGenerator
from biolinkml.generators.jsonldgen import cli, JSONLDGenerator
from tests import source_yaml_path
from tests.test_scripts import testscriptstempdir
from tests.test_scripts.clicktestcase import ClickTestCase

cwd = os.path.dirname(__file__)
meta_context = urljoin('file:', os.path.join(cwd, 'output', 'gencontext', 'meta.jsonld'))

repl: List[Tuple[str, str]] = [
    (r'"source_file_size": [0-9]+', ''),
    (r'"source_file_date": "[^"]+"', ''),
    (r'"generation_date": "[^"]+"', ''),
    (r'"source_file": "[^"]+"', '')
]


def filtr(txt: str) -> str:
    return reduce(lambda s, expr: re.sub(expr[0], expr[1], s), repl, txt)


class GenJSONLDTestCase(ClickTestCase):
    testdir = "genjsonld"
    click_ep = cli
    prog_name = "gen-jsonld"

    def test_help(self):
        self.do_test("--help", 'help')

    def test_meta(self):
        self.maxDiff = None
        self.do_test(source_yaml_path + f" --context {meta_context}", 'meta.jsonld', filtr=filtr)
        self.do_test(source_yaml_path + f' -f jsonld --context {meta_context}', 'meta.jsonld', filtr=filtr)
        self.do_test(source_yaml_path + f' -f xsv --context {meta_context}', 'meta_error',
                     error=click.exceptions.BadParameter)

    def check_size(self, g: Graph, g2: Graph, root: URIRef, expected_classes: int,
                   expected_slots: int, expected_types: int, model: str) -> None:
        for graph in [g, g2]:
            class_bnode = graph.value(root, METAMODEL_NAMESPACE.classes)
            slot_bnode = graph.value(root, METAMODEL_NAMESPACE.slots)
            type_bnode = graph.value(root, METAMODEL_NAMESPACE.types)
            self.assertEqual(expected_classes, len(list(Collection(graph, class_bnode))),
                             f"Expected {expected_classes} classes in {model}")
            self.assertEqual(expected_slots, len(list(Collection(graph, slot_bnode))),
                             f"Expected {expected_slots} slots in {model}")
            self.assertEqual(expected_types, len(list(Collection(graph, type_bnode))),
                             f"Expected {expected_types} types in {model}")

    def test_meta_output(self):
        """ Generate a context AND a jsonld for the metamodel and make sure it parses as RDF """
        jsonld_path = os.path.join(testscriptstempdir, 'metajson.jsonld')
        rdf_path = os.path.join(testscriptstempdir, 'metardf.ttl')
        meta_context_path = os.path.join(self.testdir_path, 'metacontext.jsonld')

        # Generate an image of the metamodel
        gen = ContextGenerator(source_yaml_path)
        root = gen.schema.id
        with open(meta_context_path, 'w') as tfile:
            tfile.write(gen.serialize())
        with open(jsonld_path, 'w') as tfile:
            tfile.write(JSONLDGenerator(source_yaml_path, fmt=JSONLDGenerator.valid_formats[0])\
                .serialize(context=meta_context_path))
        g = Graph()
        g.load(jsonld_path, format="json-ld")
        g.serialize(rdf_path, format="ttl")
        g.bind('meta', METAMODEL_NAMESPACE)
        new_ttl = g.serialize(format="turtle").decode()
        new_g = Graph()
        new_g.parse(data=new_ttl, format="turtle")
        self.check_size(g, new_g, URIRef(root), 9, 68, 10, "meta")


if __name__ == '__main__':
    unittest.main()

import os
import sys
import unittest
from dataclasses import dataclass
from typing import List, Optional, Union, Tuple

import requests

from rdflib import Namespace, URIRef

W3ID_SERVER = "https://w3id.org/"
DEFAULT_SERVER = W3ID_SERVER
# DEFAULT_SERVER = "http://localhost:8091/"

# Taken from Firefox network.http.accept.default
default_header = "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8"
github_io = "https://biolink.github.io/"


@dataclass
class TestEntry:
    input_url: Union[str, URIRef, Namespace]
    expected_url: str
    accept_header: Optional[str] = None


class TestLists:
    def __init__(self, server: str) -> None:
        if not server.endswith(('#', '/')):
            server += '/'
        self.biolink = server + 'biolink/'
        self.biolinkml = self.biolink + 'biolinkml/'
        self.types = Namespace(self.biolinkml + 'types')
        self.mappings = Namespace(self.biolinkml + 'mappings')
        self.metas = Namespace(self.biolinkml + 'meta')
        self.type = Namespace(self.biolinkml + 'type/')
        self.mapping = Namespace(self.biolinkml + 'mapping/')
        self.meta = Namespace(self.biolinkml + 'meta/')

        self.biolink_general: List[TestEntry] = [
            TestEntry(self.biolink, 'biolink-model/'),
            TestEntry(self.biolink + 'foo', 'biolink-model/foo')
        ]

        self.model_entries: List[TestEntry] = [
            TestEntry(self.types, 'biolinkml/includes/types'),
            TestEntry(self.types, 'biolinkml/includes/types.yaml', 'text/yaml'),
            TestEntry(self.types, 'biolinkml/includes/types.ttl', 'text/turtle'),
            TestEntry(self.types, 'biolinkml/includes/types.jsonld', 'application/json'),
            TestEntry(self.types, 'biolinkml/includes/types.shex', 'text/shex'),
            TestEntry(self.types['.owl'], 'biolinkml/includes/types.owl'),
            TestEntry(self.biolinkml + 'includes/context.jsonld', 'biolinkml/includes/context.jsonld'),
            TestEntry(self.types['/'], 'biolinkml/includes/types/'),
            TestEntry(self.mappings, 'biolinkml/includes/mappings'),
            TestEntry(self.mappings, 'biolinkml/includes/mappings.yaml', 'text/yaml'),
            TestEntry(self.mappings, 'biolinkml/includes/mappings.ttl', 'text/turtle'),
            TestEntry(self.mappings, 'biolinkml/includes/mappings.jsonld', 'application/json'),
            TestEntry(self.mappings, 'biolinkml/includes/mappings.shex', 'text/shex'),
            TestEntry(self.mappings['.owl'], 'biolinkml/includes/mappings.owl'),
            # TestEntry(self.mappings, 'biolinkml/includes/mappings.context.jsonld', 'application.jsonld'),
            TestEntry(self.mappings['/'], 'biolinkml/includes/mappings/')
        ]

        self.vocab_entries: List[TestEntry] = [
            TestEntry(self.type['index'], 'biolinkml/docs/types/index'),
            TestEntry(self.type.Element, 'biolinkml/docs/types/Element.yaml', 'text/yaml'),
            TestEntry(self.type.Element, 'biolinkml/docs/types/Element.ttl', 'text/turtle'),
            TestEntry(self.type.slots, 'biolinkml/docs/types/slots.jsonld', 'application/json'),
            TestEntry(self.mapping['index'], 'biolinkml/docs/mappings/index')
        ]

        self.meta_model_entries: List[TestEntry] = [
            TestEntry(self.metas, 'biolinkml/meta'),
            TestEntry(self.metas, 'biolinkml/meta.yaml', 'text/yaml'),
            TestEntry(self.metas, 'biolinkml/meta.ttl', 'text/turtle'),
            TestEntry(self.metas, 'biolinkml/meta.jsonld', 'application/json'),
            TestEntry(self.metas, 'biolinkml/meta.shex', 'text/shex'),
            TestEntry(self.metas['.owl'], 'biolinkml/meta.owl'),
            TestEntry(self.metas['.foo'], 'biolinkml/meta.foo'),
            TestEntry(self.biolinkml + 'context.jsonld', 'biolinkml/context.jsonld'),
            TestEntry(self.biolinkml + 'contextn.jsonld', 'biolinkml/contextn.jsonld')
        ]
        self.meta_vocab_entries: List[TestEntry] = [
            TestEntry(self.meta.Element, 'biolinkml/docs/Element'),
            TestEntry(self.meta.slot, 'biolinkml/docs/slot'),
            TestEntry(self.meta.Element, 'biolinkml/docs/Element.yaml', 'text/yaml'),
            TestEntry(self.meta.Element, 'biolinkml/docs/Element.ttl', 'text/turtle'),
            TestEntry(self.meta.Element, 'biolinkml/docs/Element.jsonld', 'application/json'),
            TestEntry(self.meta.Element, 'biolinkml/docs/Element.shex', 'text/shex'),
            TestEntry(self.meta.Element, 'biolinkml/docs/Element', 'text/foo'),
        ]

        self.biolinkmodel_entries: List[TestEntry] = [
            TestEntry(self.biolink + 'vocab/Element', 'biolink-model/docs/Element'),
            TestEntry(self.biolink + 'vocab', 'biolink-model/docs'),
            TestEntry(self.biolink + 'context.jsonld', 'biolink-model/context.jsonld'),
            TestEntry(self.biolink + 'contextn.jsonld', 'biolink-model/contextn.jsonld'),
            TestEntry(self.biolink + 'biolink-model.yaml', 'biolink-model/biolink-model.yaml')
        ]


FAIL_ON_ERROR = True


@unittest.skipIf(True, "Rewrite rules test bypassed except when new rules are submitted to w3id.org")
class RewriteRuleTestCase(unittest.TestCase):
    SERVER = DEFAULT_SERVER         # Can be overwritten with a startup parameter

    @classmethod
    def setUpClass(cls):
        cls.tests = TestLists(cls.SERVER)
        print(f"Server: {cls.SERVER}")
        cls.results: Tuple[str, str, str] = set()   # from, to, format

    @classmethod
    def tearDownClass(cls):
        print()
        for from_url, to_url, hdr in sorted(list(cls.results)):
            fmt = '' if hdr == 'text/html' else f" ({hdr})"
            if DEFAULT_SERVER != W3ID_SERVER:
                from_url = from_url.replace(DEFAULT_SERVER, W3ID_SERVER)
            print(f"{from_url}{fmt} - {to_url}")

    def record_results(self, from_url: str, accept_header, to_url: str) -> None:
        self.results.add( (from_url, to_url, accept_header.split(',')[0]))

    def rule_test(self, entries: List[TestEntry]) -> None:

        def test_it(e: TestEntry, accept_header: str) -> bool:
            expected = github_io + e.expected_url
            resp = requests.head(e.input_url, headers={'accept': accept_header}, verify=False)

            # w3id.org uses a 301 to go from http: to https:
            if resp.status_code == 301 and 'location' in resp.headers:
                resp = requests.head(resp.headers['location'], headers={'accept': accept_header}, verify=False)
            actual = resp.headers['location'] \
                if resp.status_code == 302 and 'location' in resp.headers \
                else f"Error: {resp.status_code}"
            if FAIL_ON_ERROR:
                self.assertEqual(expected, actual, f"redirect for: {resp.url}")
                self.record_results(e.input_url, accept_header, actual)
                return True
            elif expected != actual:
                print(f"{e.input_url} ({accept_header}):\n expected {expected} - got {actual}")
                return False
            self.record_results(e.input_url, accept_header, actual)
            return True

        def ev_al(entry: TestEntry) -> bool:
            if not entry.accept_header:
                return test_it(entry, default_header)
            else:
                r1 = test_it(entry, entry.accept_header)
                return test_it(entry, entry.accept_header + ',' + default_header) and r1

        self.assertTrue(all([ev_al(entry) for entry in entries]))

    def test_type_model(self):
        self.rule_test(self.tests.model_entries)

    def test_type_entry(self):
        self.rule_test(self.tests.vocab_entries)

    def test_meta_model(self):
        self.rule_test(self.tests.meta_model_entries)

    def test_meta_entry(self):
        self.rule_test(self.tests.meta_vocab_entries)

    def test_general(self):
        self.rule_test(self.tests.biolink_general)

    def test_biolink_model(self):
        self.rule_test(self.tests.biolinkmodel_entries)


if __name__ == '__main__':
    RewriteRuleTestCase.SERVER = os.environ.get('SERVER', RewriteRuleTestCase.SERVER)
    unittest.main()

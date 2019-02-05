import os
import unittest
from dataclasses import dataclass
from typing import List, Optional, Union

import requests

from rdflib import Namespace, URIRef

# DEFAULT_SERVER = "http://w3id.org/"
DEFAULT_SERVER = "http://localhost:8084/"

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
            server += '/pipenv run python ../test_rewrite_rules/test_rewrite_rules.pypipenv run python ../test_rewrite_rules/test_rewrite_rules.py'
        self.biolink = server + 'biolink/'
        self.biolinkml = self.biolink + 'biolinkml/'
        self.types = Namespace(self.biolinkml + 'types')
        self.metas = Namespace(self.biolinkml + 'meta')
        self.type = Namespace(self.biolinkml + 'type/')
        self.meta = Namespace(self.biolinkml + 'meta/')

        self.biolink_general: List[TestEntry] = [
            TestEntry(self.biolink, ''),
            TestEntry(self.biolink + 'foo', 'foo')
        ]

        self.model_entries: List[TestEntry] = [
            TestEntry(self.types, 'biolinkml/includes/types'),
            TestEntry(self.types, 'biolinkml/includes/types.yaml', 'text/yaml'),
            TestEntry(self.types, 'biolinkml/includes/types.ttl', 'text/turtle'),
            TestEntry(self.types, 'biolinkml/includes/types.jsonld', 'application/json'),
            TestEntry(self.types, 'biolinkml/includes/types.shex', 'text/shex'),
            TestEntry(self.types['.owl'], 'biolinkml/includes/types.owl'),
            TestEntry(self.biolinkml + 'includes/context.jsonld', 'biolinkml/includes/context.jsonld'),
            TestEntry(self.types['/'], 'biolinkml/includes/types/')
        ]

        self.vocab_entries: List[TestEntry] = [
            TestEntry(self.type['index'], 'biolinkml/docs/types/index'),
            TestEntry(self.type.Element, 'biolinkml/docs/types/Element.yaml', 'text/yaml'),
            TestEntry(self.type.Element, 'biolinkml/docs/types/Element.ttl', 'text/turtle'),
            TestEntry(self.type.slots, 'biolinkml/docs/types/slots.jsonld', 'application/json')
        ]

        self.meta_model_entries: List[TestEntry] = [
            TestEntry(self.metas, 'biolinkml/meta'),
            TestEntry(self.metas, 'biolinkml/meta.yaml', 'text/yaml'),
            TestEntry(self.metas, 'biolinkml/meta.ttl', 'text/turtle'),
            TestEntry(self.metas, 'biolinkml/meta.jsonld', 'application/json'),
            TestEntry(self.metas, 'biolinkml/meta.shex', 'text/shex'),
            TestEntry(self.metas['.owl'], 'biolinkml/meta.owl'),
            TestEntry(self.metas['.foo'], 'biolinkml/meta.foo'),
            TestEntry(self.biolinkml + 'context.jsonld', 'biolinkml/context.jsonld')
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
            TestEntry(self.biolink + '/vocab/Element', 'biolink-model/docs/Element'),
            TestEntry(self.biolink + '/vocab', 'vocab'),
            TestEntry(self.biolink + 'biolink-model.yaml', 'biolink-model.yaml')
        ]


FAIL_ON_ERROR = True


@unittest.skipIf(True, "Only works if the server is up and running")
class RewriteRuleTestCase(unittest.TestCase):
    SERVER = DEFAULT_SERVER         # Can be overwritten with a startup parameter

    @classmethod
    def setUpClass(cls):
        cls.tests = TestLists(cls.SERVER)

    def rule_test(self, entries: List[TestEntry]) -> None:

        def test_it(e: TestEntry, accept_header: str) -> bool:
            expected = github_io + e.expected_url
            resp = requests.head(e.input_url, headers={'accept': accept_header})
            actual = resp.headers['location'] \
                if resp.status_code == 302 and 'location' in resp.headers \
                else f"Error: {resp.status_code}"
            if FAIL_ON_ERROR:
                self.assertEqual(expected, actual)
                return True
            elif expected != actual:
                print(f"{e.input_url} ({accept_header}):\n expected {expected} - got {actual}")
                return False
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

import unittest
from http.client import HTTP_PORT, HTTPS_PORT
from typing import cast
import os

from rdflib import Namespace, SKOS, Literal

from biolinkml.dumpers import yaml_dumper, json_dumper, rdf_dumper
from tests.test_loaders_dumpers import LD_11_DIR, LD_11_SSL_SVR, LD_11_SVR
from tests.test_loaders_dumpers.models.termci_schema import ConceptReference, ConceptSystem, Package
from tests.utils.clicktestcase import ClickTestCase
from tests.utils.test_environment import TestEnvironmentTestCase

OBO = Namespace("http://purl.obolibrary.org/obo/")
NCIT = Namespace("http://purl.obolibrary.org/obo/NCI_")

from tests.test_loaders_dumpers.environment import env


class DumpersTestCase(TestEnvironmentTestCase):
    env = env

    @classmethod
    def setUpClass(cls) -> None:
        """ Generate a small sample TermCI instance for testing purposes """
        e1 = ConceptReference(OBO.NCI_C147796, code="C147796", defined_in=OBO,
                              designation="TSCYC - Being Frightened of Men",
                              definition="Trauma Symptom Checklist for Young Children (TSCYC) Please indicate how often"
                                         " the child has done, felt, or experienced each of the following things in the "
                                         "last month: Being frightened of men.", narrower_than=OBO.NCI_C147557, reference=OBO.NCI_C147796)
        e2 = ConceptReference(OBO.NCI_C147557, code="C147557", defined_in=OBO,
                              designation="TSCYC Questionnaire Question",
                              definition="A question associated with the TSCYC questionnaire.", narrower_than=OBO.NCI_C91102)
        c1 = ConceptSystem(OBO, "OBO", contents=[e1, e2])
        cls.test_package = Package([c1])

    def test_yaml_dumper(self):
        """ Test the yaml emitter """
        # TODO: Once this is entered into the BiolinkML test package, compare this to input/obo_test.yaml
        expected_fname = env.input_path('obo_sample.yaml')
        actual_fname = env.actual_path('obo_sample.yaml')

        yaml_dumper.dump(self.test_package, actual_fname)
        with open(actual_fname) as f:
            actual = f.read()
        self.env.eval_single_file(expected_fname, actual)

        obo_yaml = yaml_dumper.dumps(self.test_package)
        self.env.eval_single_file(expected_fname, obo_yaml)

    def test_json_dumper(self):
        """ Test the json emitter """
        # TODO: Same as test_yaml_dumper
        expected_fname = env.input_path('obo_sample.json')
        output_fname = env.actual_path('obo_sample.json')

        json_dumper.dump(self.test_package, output_fname)
        with open(output_fname) as f:
            actual = f.read().strip()
        self.env.eval_single_file(expected_fname, actual)

        obo_json_obj = cast(Package, json_dumper.as_json_object(self.test_package))
        self.assertEqual(OBO, obo_json_obj.system[0].namespace)
        self.assertEqual('C147796', obo_json_obj.system[0].contents[0].code)

        obo_json = json_dumper.dumps(self.test_package)
        self.env.eval_single_file(expected_fname, obo_json)

    def test_rdf_dumper(self):
        """ Test the rdf dumper """
        contexts = os.path.join(LD_11_DIR, 'termci_schema_inlined.context.jsonld')
        expected_fname = env.input_path('obo_sample.ttl')
        output_fname = env.actual_path('obo_sample.ttl')

        rdf_dumper.dump(self.test_package, output_fname, contexts)
        with open(output_fname) as f:
            actual = f.read()
        self.env.eval_single_file(expected_fname, actual, comparator=ClickTestCase.rdf_comparator)

        g = rdf_dumper.as_rdf_graph(self.test_package, contexts)
        self.assertIn(OBO[''], g.subjects())
        self.assertIn(NCIT.C147796, g.subjects())
        self.assertIn(Literal('C147796'), g.objects(NCIT.C147796, SKOS.notation))

        obo_ttl = rdf_dumper.dumps(self.test_package, contexts)
        self.env.eval_single_file(expected_fname, obo_ttl, comparator=ClickTestCase.rdf_comparator)

        # Build a vanilla jsonld image for subsequent testing
        expected_fname = env.expected_path('obo_sample.jsonld')
        output_fname = env.actual_path('obo_sample.jsonld')
        rdf_dumper.dump(self.test_package, output_fname, contexts, fmt='json-ld')
        with open(output_fname) as f:
            actual = f.read()
        self.env.eval_single_file(expected_fname, actual,
                                  comparator=lambda expected, actual: ClickTestCase.rdf_comparator(expected, actual, fmt='json-ld'))

    def test_nested_contexts(self):

        def is_listening(port):
            import socket
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                return s.connect_ex(('localhost', port)) == 0

        use_http = is_listening(HTTP_PORT)
        use_https = is_listening(HTTPS_PORT)
        if not (use_http or use_https):
            print(f"Nested contexts test skipped - no servers found on sockets {HTTP_PORT} or {HTTPS_PORT}")

        expected_fname = env.input_path('obo_sample.ttl')
        output_fname = env.actual_path('obo_sample.ttl')

        nested_context_base = LD_11_SSL_SVR if use_https else LD_11_SVR
        nested_context = LD_11_SSL_SVR + "termci_schema_inlined.context.jsonld"
        output_fname = env.actual_path('obo_sample_nested.ttl')
        rdf_dumper.dump(self.test_package, output_fname, nested_context)
        with open(output_fname) as f:
            actual = f.read()
        self.env.eval_single_file(expected_fname, actual, comparator=ClickTestCase.rdf_comparator)


if __name__ == '__main__':
    unittest.main()

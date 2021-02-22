import os
import unittest

from biolinkml.loaders import yaml_loader, json_loader, rdf_loader
from tests.test_loaders_dumpers import LD_11_SVR, LD_10_SVR
from tests.test_loaders_dumpers.environment import env
from tests.test_loaders_dumpers.ldtestcase import LDTestCase
from tests.test_loaders_dumpers.models.termci_schema import Package


class LoadersUnitTest(LDTestCase):
    env = env

    def test_yaml_loader(self):
        self.loader_test('obo_sample.yaml', Package, yaml_loader)

    def test_json_loader(self):
        self.loader_test('obo_sample.json', Package, json_loader)

    def test_rdf_loader(self):
        contexts = os.path.join(LD_10_SVR, 'termci_schema.context.jsonld')
        fmt = 'turtle'

        class loader_wrapper:
            @staticmethod
            def load(source, base, target, metadata):
                return rdf_loader.load(source, base, target, contexts, fmt, metadata)

            @staticmethod
            def loads(source, target, metadata):
                return rdf_loader.loads(source, target, contexts, fmt, metadata)

        self.loader_test('obo_sample.ttl', Package, loader_wrapper)
        fmt = 'json-ld'
        self.loader_test('obo_sample.jsonld', Package, loader_wrapper)


if __name__ == '__main__':
    unittest.main()

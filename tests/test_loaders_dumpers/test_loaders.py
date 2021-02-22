import unittest

from biolinkml.loaders import yaml_loader, json_loader
from tests.test_loaders_dumpers.environment import env
from tests.test_loaders_dumpers.ldtestcase import LDTestCase
from tests.test_loaders_dumpers.models.termci_schema import Package


class LoadersUnitTest(LDTestCase):
    env = env

    def test_yaml_loader(self):
        self.loader_test('obo_sample.yaml', Package, yaml_loader)

    def test_json_loader(self):
        self.loader_test('obo_sample.json', Package, json_loader)

    # def test_load_rdf(self):
    #     contexts = os.path.join(CONTEXT_SVR, 'termci_schema_inlined.context.jsonld')
    #     fmt = 'turtle'
    #
    #     def rdf_load(source, base_dir, target_class, metadata):
    #         """ Wrapper for loader to include the context """
    #         return rdf_loader.load(source, base_dir, target_class, contexts=contexts, fmt=fmt, metadata=metadata)
    #
    #     def rdf_loads(source, target_class, metadata):
    #         return rdf_loader.loads(source, target_class, contexts=contexts, fmt=fmt, metadata=metadata)
    #
    #     self.do_load_test('obo_sample.ttl', rdf_load, rdf_loads)
    #
    # def test_load_rdf_jsonld(self):
    #     contexts = os.path.join(CONTEXT_SVR, 'termci_schema_inlined.context.jsonld')
    #     test_file = os.path.join(INPUT_DIR, 'obo_sample.jsonld')
    #     obj = rdf_loader.load(test_file, None, Package, contexts=contexts, fmt='json-ld')
    #     print(obj)


if __name__ == '__main__':
    unittest.main()

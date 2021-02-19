import os
import unittest
from typing import Callable

from hbreader import FileInfo

from biolinkml.dumpers import yaml_dumper, CONTEXT_SVR
from biolinkml.loaders import yaml_loader, json_loader, rdf_loader
from tests.test_loaders_dumpers.models.termci_schema import Package
from tests.utils.test_environment import TestEnvironmentTestCase

from tests.test_loaders_dumpers.environment import env

class LoadersUnitTest(TestEnvironmentTestCase):
    env = env

    @classmethod
    def setUpClass(cls) -> None:
        cls.expected_file_name = env.input_path('obo_sample.yaml')
        with open(cls.expected_file_name) as f:
            cls.expected = f.read().strip()

    def do_load_test(self, fname: str, loader: Callable, sloader: Callable) -> None:
        # Load from a file
        inp_file = env.input_path(fname)
        with open(inp_file) as f:
            inp_text = f.read()

        metadata = FileInfo()
        obo_sample = loader(fname, env.indir, Package, metadata=metadata)
        print(metadata)
        self.env.eval_single_file(self.expected_file_name, yaml_dumper.dumps(obo_sample))

        # Load from a string
        obo_sample = sloader(inp_text, Package, metadata=metadata)
        print(metadata)
        self.assertEqual(self.expected, yaml_dumper.dumps(obo_sample).strip())

        # Load from a URL
        metadata = Metadata()
        obo_sample = loader(fname, GITHUB_INPUT_DIR, Package, metadata=metadata)
        print(metadata)
        self.assertEqual(self.expected, yaml_dumper.dumps(obo_sample).strip())

        # Load from an open file
        metadata = Metadata()
        with open(inp_file) as f:
            obo_sample = loader(f, None, target_class=Package, metadata=metadata)
            print(metadata)
        self.assertEqual(self.expected, yaml_dumper.dumps(obo_sample).strip())

    def test_load_yaml(self):
        self.do_load_test('obo_sample.yaml', yaml_loader.load, yaml_loader.loads)

    def test_load_json(self):
        self.do_load_test('obo_sample.json', json_loader.load, json_loader.loads)

    def test_load_rdf(self):
        contexts = os.path.join(CONTEXT_SVR, 'termci_schema_inlined.context.jsonld')
        fmt = 'turtle'

        def rdf_load(source, base_dir, target_class, metadata):
            """ Wrapper for loader to include the context """
            return rdf_loader.load(source, base_dir, target_class, contexts=contexts, fmt=fmt, metadata=metadata)

        def rdf_loads(source, target_class, metadata):
            return rdf_loader.loads(source, target_class, contexts=contexts, fmt=fmt, metadata=metadata)

        self.do_load_test('obo_sample.ttl', rdf_load, rdf_loads)

    def test_load_rdf_jsonld(self):
        contexts = os.path.join(CONTEXT_SVR, 'termci_schema_inlined.context.jsonld')
        test_file = os.path.join(INPUT_DIR, 'obo_sample.jsonld')
        obj = rdf_loader.load(test_file, None, Package, contexts=contexts, fmt='json-ld')
        print(obj)


if __name__ == '__main__':
    unittest.main()

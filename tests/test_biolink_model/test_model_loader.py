import os
import unittest

from jsonasobj import as_json

from tests.test_biolink_model.biolink_metamodel.biolink_metamodel import Model
from tests.test_biolink_model.model_loader import load_raw_schema


class ModelLoaderTestCase(unittest.TestCase):
    def do_it(self, base_name: str) -> Model:
        yaml = os.path.join(os.path.dirname(__file__), 'yaml', 'model', f'{base_name}.yaml')
        return load_raw_schema(yaml)

    def test_model_subsets(self):
        print(as_json(self.do_it("biolink_subsets")))

    def test_model_types(self):
        print(as_json(self.do_it("biolink_types")))

    def test_model_relations(self):
        """ Test the biolink model relation definitions """
        print(as_json(self.do_it("biolink_relations")))

    def test_model_nodes(self):
        """ Test the biolink model node definitions """
        print(as_json(self.do_it("biolink_nodes")))

    def test_model_associations(self):
        """ Test the biolink model node definitions """
        print(as_json(self.do_it("biolink_associations")))

if __name__ == '__main__':
    unittest.main()

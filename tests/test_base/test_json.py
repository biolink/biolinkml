import os
import unittest

from biolinkml import INCLUDES_DIR, MODULE_DIR, LOCAL_METAMODEL_LDCONTEXT_FILE
from biolinkml.generators.jsonldgen import JSONLDGenerator
from tests import targetdir
from tests.utils.generator_utils import GeneratorTestCase, BIOLINK_IMPORT_MAP
from tests.utils.metadata_filters import json_metadata_filter


class JsonLDTestCase(GeneratorTestCase):
    """ Generate the JSON LD for all of the models and compare them against what has been published """
    target_path = targetdir

    def test_types_json(self):
        self.source_path = INCLUDES_DIR
        self.model_path = INCLUDES_DIR
        self.model_name = 'types'
        self.single_file_generator('jsonld', JSONLDGenerator, filtr=json_metadata_filter)

    def test_mappings_json(self):
        self.source_path = INCLUDES_DIR
        self.model_path = INCLUDES_DIR
        self.model_name = 'mappings'
        self.importmap = BIOLINK_IMPORT_MAP
        self.single_file_generator('jsonld', JSONLDGenerator, filtr=json_metadata_filter)

    def test_metamodel_json(self):
        self.source_path = MODULE_DIR
        self.model_path = MODULE_DIR
        self.model_name = 'meta'
        self.importmap = BIOLINK_IMPORT_MAP
        self.single_file_generator('jsonld', JSONLDGenerator, filtr=json_metadata_filter)


if __name__ == '__main__':
    unittest.main()

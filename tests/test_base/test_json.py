import unittest

from biolinkml import META_BASE_URI
from biolinkml.generators.jsonldgen import JSONLDGenerator
from tests.test_base.environment import env
from tests.utils.generatortestcase import GeneratorTestCase
from tests.utils.filters import json_metadata_filter


class JsonLDTestCase(GeneratorTestCase):
    """ Generate the JSON for all of the models and compare them against what has been published """
    env = env

    def test_types_context(self):
        """ Build an image of types.jsonld in the local includes directory """
        self.model_name = 'types'
        self.single_file_generator('jsonld', JSONLDGenerator, subdir='includes',
                                   serialize_args=dict(base=META_BASE_URI), filtr=json_metadata_filter)

    def test_mappings_context(self):
        self.model_name = 'mappings'
        self.single_file_generator('jsonld', JSONLDGenerator, serialize_args=dict(base=META_BASE_URI),
                                   filtr=json_metadata_filter, subdir='includes')

    def test_metamodel_context(self):
        self.model_name = 'meta'
        self.single_file_generator('jsonld', JSONLDGenerator, serialize_args=dict(base=META_BASE_URI),
                                   filtr=json_metadata_filter)


if __name__ == '__main__':
    unittest.main()

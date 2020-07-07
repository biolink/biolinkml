import unittest

from biolinkml import META_BASE_URI
from biolinkml.generators.jsonldcontextgen import ContextGenerator
from tests.test_base.environment import env
from tests.utils.generatortestcase import GeneratorTestCase
from tests.utils.filters import ldcontext_metadata_filter


class ContextTestCase(GeneratorTestCase):
    """ Generate the context.jsonld for all of the models and compare them against what has been published """
    env = env

    def test_types_context(self):
        """ Build an image of types.jsonld in the local includes directory """
        self.model_name = 'types'
        self.single_file_generator('context.jsonld', ContextGenerator, subdir='includes',
                                   serialize_args=dict(base=META_BASE_URI), filtr=ldcontext_metadata_filter)

    def test_mappings_context(self):
        self.model_name = 'mappings'
        self.single_file_generator('context.jsonld', ContextGenerator, subdir='includes',
                                   serialize_args=dict(base=META_BASE_URI), filtr=ldcontext_metadata_filter)

    def test_metamodel_context(self):
        self.model_name = 'meta'
        self.single_file_generator('jsonld', ContextGenerator, serialize_args=dict(base=META_BASE_URI),
                                   filtr=ldcontext_metadata_filter, output_name='context')


if __name__ == '__main__':
    unittest.main()

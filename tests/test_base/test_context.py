import unittest

from biolinkml import INCLUDES_DIR, META_BASE_URI, MODULE_DIR
from biolinkml.generators.jsonldcontextgen import ContextGenerator
from tests import targetdir
from tests.utils.generator_utils import GeneratorTestCase, BIOLINK_IMPORT_MAP
from tests.utils.metadata_filters import ldcontext_metadata_filter


class ContextTestCase(GeneratorTestCase):
    """ Generate the context.jsonld for all of the models and compare them against what has been published """
    target_path = targetdir

    def test_types_context(self):
        self.source_path = INCLUDES_DIR
        self.model_path = INCLUDES_DIR
        self.model_name = 'types'
        self.single_file_generator('context.jsonld', ContextGenerator, filtr=ldcontext_metadata_filter)

    def test_mappings_context(self):
        self.source_path = INCLUDES_DIR
        self.model_path = INCLUDES_DIR
        self.model_name = 'mappings'
        self.importmap = BIOLINK_IMPORT_MAP
        self.single_file_generator('context.jsonld', ContextGenerator, filtr=ldcontext_metadata_filter)

    def test_metamodel_context(self):
        self.source_path = MODULE_DIR
        self.model_path = MODULE_DIR
        self.model_name = 'meta'
        self.output_name = ''
        self.importmap = BIOLINK_IMPORT_MAP
        self.single_file_generator('context.jsonld', ContextGenerator, serialize_args=dict(base=META_BASE_URI),
                                   filtr=ldcontext_metadata_filter)


if __name__ == '__main__':
    unittest.main()

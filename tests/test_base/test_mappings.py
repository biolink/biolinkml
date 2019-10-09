import os
import unittest
from types import ModuleType

from biolinkml import INCLUDES_DIR
from biolinkml.generators.pythongen import PythonGenerator
from tests import targetdir
from tests.utils.metadata_filters import metadata_filter
from tests.utils.generator_utils import GeneratorTestCase


class MappingsTestCase(GeneratorTestCase):
    """ Validate that mappings.py matches the YAML and compiles """

    source_path = INCLUDES_DIR
    target_path = targetdir
    model_path = INCLUDES_DIR
    model_name = 'mappings'

    # Note: mappings.yaml imports "types", while ../meta.yaml imports "includes/types".  To do this test we need
    # to figure out a way to pass a base directory one up to the ganerator
    @unittest.skipIf(True, "Need to resolve base directory issue")
    def test_mappings_python(self):
        """ Make sure the python is current for mappings.yaml """
        self.single_file_generator('py', PythonGenerator, filtr=metadata_filter)

        # Make sure the python is valid
        with open(os.path.join(self.source_path, 'mappings.py')) as f:
            pydata = f.read()
        spec = compile(pydata, 'test', 'exec')
        module = ModuleType('test')
        exec(spec, module.__dict__)


if __name__ == '__main__':
    unittest.main()

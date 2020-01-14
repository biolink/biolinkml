import os
import unittest
from types import ModuleType

from biolinkml import INCLUDES_DIR, MODULE_DIR
from biolinkml.generators.pythongen import PythonGenerator
from tests import targetdir
from tests.utils.generator_utils import GeneratorTestCase, BIOLINK_IMPORT_MAP
from tests.utils.metadata_filters import metadata_filter


class PythonTestCase(GeneratorTestCase):
    """ Generate python for all of the models, compare them against what has been published
     and verify that they compile"""

    target_path = targetdir

    def check_python(self) -> None:
        # Make sure the python is valid
        with open(os.path.join(self.source_path, self.model_name + '.py')) as f:
            pydata = f.read()
        spec = compile(pydata, 'test', 'exec')
        module = ModuleType('test')
        exec(spec, module.__dict__)

    def test_types_python(self):
        self.source_path = INCLUDES_DIR
        self.model_path = INCLUDES_DIR
        self.model_name = 'types'
        self.single_file_generator('py', PythonGenerator, filtr=metadata_filter)
        self.check_python()

    def test_mappings_python(self):
        self.source_path = INCLUDES_DIR
        self.model_path = INCLUDES_DIR
        self.model_name = 'mappings'
        self.importmap = BIOLINK_IMPORT_MAP
        self.single_file_generator('py', PythonGenerator, filtr=metadata_filter)
        self.check_python()

    def test_metamodel_python(self):
        self.source_path = os.path.join(MODULE_DIR, 'biolinkml')
        self.model_path = MODULE_DIR
        self.model_name = 'meta'
        self.importmap = BIOLINK_IMPORT_MAP
        self.single_file_generator('py', PythonGenerator, filtr=metadata_filter)
        self.check_python()


if __name__ == '__main__':
    unittest.main()

import os
import unittest
from types import ModuleType

from biolinkml import INCLUDES_DIR
from biolinkml.generators.pythongen import PythonGenerator
from tests import targetdir
from tests.test_scripts.clicktestcase import metadata_filter
from tests.utils.generator_utils import GeneratorTestCase


class TypesTestCase(GeneratorTestCase):
    """ Validate that types.py matches the YAML and compiles """

    source_path = INCLUDES_DIR
    target_path = targetdir
    model_path = INCLUDES_DIR
    model_name = 'types'

    def test_types_python(self):
        """ Make sure the python is current for types.yaml """
        self.single_file_generator('py', PythonGenerator, filtr=metadata_filter)

        # Make sure the python is valid
        with open(os.path.join(self.source_path, 'types.py')) as f:
            pydata = f.read()
        spec = compile(pydata, 'test', 'exec')
        module = ModuleType('test')
        exec(spec, module.__dict__)


if __name__ == '__main__':
    unittest.main()

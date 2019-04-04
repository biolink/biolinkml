import os
import unittest
from types import ModuleType

from biolinkml.generators.pythongen import PythonGenerator
from tests import targetdir
from tests.test_scripts.clicktestcase import metadata_filter
from tests.utils.generator_utils import GeneratorTestCase


class TypesTestCase(GeneratorTestCase):
    root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'includes'))

    source_path = root
    target_path = targetdir
    model_path = root
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

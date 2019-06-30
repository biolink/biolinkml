import os
import unittest
from types import ModuleType

from biolinkml.generators.pythongen import PythonGenerator
from tests.test_scripts.clicktestcase import metadata_filter
from tests.test_utils import inputdir, outputdir
from tests.utils.generator_utils import GeneratorTestCase


class IfAbsentTestCase(GeneratorTestCase):
    root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))

    source_path: str = inputdir
    target_path: str = outputdir
    model_path: str = source_path
    model_name: str = "ifabsents"
    output_name: str = None

    def test_good_ifabsent(self):
        IfAbsentTestCase.model_name = "ifabsents"

        """ Test the metadata options"""
        self.single_file_generator('py', PythonGenerator, filtr=metadata_filter)

        # Make sure the python is valid
        with open(os.path.join(self.source_path, 'ifabsents.py')) as f:
            pydata = f.read()
        spec = compile(pydata, 'test', 'exec')
        module = ModuleType('test')
        exec(spec, module.__dict__)

    def test_bad_ifabsent(self):
        IfAbsentTestCase.model_name = "ifabsents_error"
        with self.assertRaises(ValueError):
            self.single_file_generator('py', PythonGenerator, filtr=metadata_filter)


if __name__ == '__main__':
    unittest.main()

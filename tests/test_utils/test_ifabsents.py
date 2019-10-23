import os
import unittest
from types import ModuleType

from biolinkml.generators.pythongen import PythonGenerator
from tests.utils.metadata_filters import metadata_filter
from tests.test_utils import inputdir, outputdir
from tests.utils.generator_utils import GeneratorTestCase


class IfAbsentTestCase(GeneratorTestCase):
    root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))

    source_path: str = inputdir
    target_path: str = outputdir
    model_path: str = source_path
    model_name: str = "ifabsents"
    output_name: str = None

    def do_test(self):
        """ Test the metadata options"""
        self.single_file_generator('py', PythonGenerator, filtr=metadata_filter)

        # Make sure the python is valid
        with open(os.path.join(self.source_path, f'{IfAbsentTestCase.model_name}.py')) as f:
            pydata = f.read()
        spec = compile(pydata, 'test', 'exec')
        module = ModuleType('test')
        exec(spec, module.__dict__)

    def test_good_ifabsent(self):
        """ Test isabsent with no default_prefix """
        IfAbsentTestCase.model_name = "ifabsents"
        self.do_test()

    def test_good_ifabsent2(self):
        """ Test isabsents with default_prefix specified """
        IfAbsentTestCase.model_name = "ifabsents2"
        self.do_test()

    def test_good_ifabsent3(self):
        """ Test isabsent with no default_prefix, but prefix specified that matches the module id """
        IfAbsentTestCase.model_name = "ifabsents3"
        self.do_test()

    def test_bad_ifabsent(self):
        IfAbsentTestCase.model_name = "ifabsents_error"
        with self.assertRaises(ValueError):
            self.single_file_generator('py', PythonGenerator, filtr=metadata_filter)

    def test_ifabsent_uri(self):
        IfAbsentTestCase.model_name = "ifabsent_uri"
        self.do_test()


if __name__ == '__main__':
    unittest.main()

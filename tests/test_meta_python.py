import os
import unittest
from types import ModuleType

from biolinkml.generators.pythongen import PythonGenerator
from tests import targetdir
from tests.test_scripts.clicktestcase import metadata_filter
from tests.utils.generator_utils import GeneratorTestCase


class MetaModelTestCase(GeneratorTestCase):
    root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))

    source_path = os.path.join(root, 'biolinkml')
    target_path = targetdir
    model_path = root
    model_name = 'meta'

    def test_meta_python(self):
        """ Test the python generator for the biolink model """
        self.single_file_generator('py', PythonGenerator, {'emit_metadata': True}, filtr=metadata_filter,
                                   preserve_metadata=True)

        # Make sure the python is valid
        with open(os.path.join(self.source_path, 'meta.py')) as f:
            pydata = f.read()
        spec = compile(pydata, 'test', 'exec')
        module = ModuleType('test')
        exec(spec, module.__dict__)


if __name__ == '__main__':
    unittest.main()

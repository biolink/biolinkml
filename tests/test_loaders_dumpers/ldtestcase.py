import os
from typing import Callable, Type, Union, TextIO, Optional

from hbreader import FileInfo, hbread

from biolinkml.dumpers import yaml_dumper
from biolinkml.utils.yamlutils import YAMLRoot
from tests.utils.test_environment import TestEnvironment, TestEnvironmentTestCase
import tests.environment as test_base


class LDTestCase(TestEnvironmentTestCase):
    env = TestEnvironment(__file__)

    def dump_test(self, filename: str,  dumper: Callable[[str], None], comparator: Callable[[str], str] = None)\
            -> bool:
        """
        Invoke the dumper passing it the output file name and then compare the result to an expected output
        :param filename: non-pathed file name to dump to and test
        :param dumper: when called with pathed file name, creates the output
        :param comparator: content comparator
        :returns: Success indicator
        """
        actual_file = self.env.actual_path(filename)
        expected_file = self.env.expected_path(filename.replace('.', '_d.'))

        dumper(actual_file)

        with open(actual_file) as actual_f:
            actual = actual_f.read()
        return self.env.eval_single_file(expected_file, actual, comparator=comparator)

    def dumps_test(self, filename: str, dumper: Callable[[], str], comparator: Callable[[], str] = None) -> bool:
        """
        Invoke the string dumper and evaluate the results
        :param filename: filename to test
        :param dumper: function that produces
        :param comparator: content comparator
        """
        actual = dumper()
        expected_file = self.env.expected_path(filename.replace('.', '_ds.'))

        return self.env.eval_single_file(expected_file, actual, comparator=comparator)

    def loader_test(self, filename: str, model: Type[YAMLRoot], loader) -> None:
        """
        Test the various permutations of the supplied loader using the input file 'filename' -- both load and loads

        :param filename: un-pathed file name to load
        :param model: model to load the file name into
        :param loader: package that contains 'load' and 'loads' operations
        """
        metadata = FileInfo()
        expected_yaml = self.env.input_path(filename.rsplit('.', 1)[0] + ".yaml")
        python_obj: YAMLRoot = loader.load(filename, self.env.indir, model, metadata)
        self.env.eval_single_file(expected_yaml, yaml_dumper.dumps(python_obj))

        # Make sure metadata gets filled out properly
        rel_path = os.path.abspath(os.path.join(test_base.env.cwd, '..'))
        self.assertEqual('tests/test_loaders_dumpers/input', os.path.relpath(metadata.base_path, rel_path))
        self.assertEqual(f'tests/test_loaders_dumpers/input/{filename}', os.path.relpath(metadata.source_file, rel_path))
        self.assertIsNotNone(metadata.source_file_date)
        self.assertEqual(899, metadata.source_file_size)

        # Load from a string
        expected_yaml_str = hbread(expected_yaml, base_path=self.env.indir)
        python_obj: YAMLRoot = loader.loads(expected_yaml_str, model, metadata)
        self.env.eval_single_file(expected_yaml, yaml_dumper.dumps(python_obj))

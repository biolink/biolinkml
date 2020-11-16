import logging
import unittest
from typing import Union, List

from biolinkml.generators.pythongen import PythonGenerator
from biolinkml.generators.yamlgen import YAMLGenerator
from tests.test_enhancements.environment import env
from tests.utils.filters import yaml_filter
from tests.utils.python_comparator import compare_python, compile_python
from tests.utils.test_environment import TestEnvironmentTestCase


class EnumerationTestCase(TestEnvironmentTestCase):
    env = env
    testdir = 'enumeration'

    def _check_error(self, file: str, error: str) -> None:
        with self.assertRaises(ValueError, msg=error) as e:
            YAMLGenerator(env.input_path(self.testdir, f'{file}.yaml'),
                          mergeimports=False, log_level=logging.INFO).serialize(validateonly=True)
        # print(str(e.exception))
        self.assertIn(error, str(e.exception), error)

    def _check_warns(self, file: str, msgs: Union[str, List[str]]) -> None:
        with self.redirect_logstream() as logger:
            YAMLGenerator(env.input_path(self.testdir, f'{file}.yaml'),
                          mergeimports=False, log_level=logging.INFO, logger=logger).serialize(validateonly=True)
        for msg in msgs if isinstance(msgs, list) else [msgs]:
            self.assertIn(msg, logger.result, msg)


    def test_evidence(self):
        """ Test evidence enumeration  """
        file = "evidence"
        env.generate_single_file(f'{self.testdir}/{file}.py',
                                 lambda: PythonGenerator(env.input_path(self.testdir, f'{file}.yaml'),
                                                         importmap=env.import_map, mergeimports=False).serialize(),
                                 comparator=lambda exp, act: compare_python(exp, act, self.env.expected_path(f'{self.testdir}/{file}.py')),
                                 value_is_returned=True)

    def test_enum_constraints(self):
        """ Test the various enum constraints """
        self._check_error("enum_name_error", '":" not allowed in identifier')

        self._check_error("enum_class_name_error", "Overlapping enum and class names: test1, test2")

        self._check_error("enum_type_name_error", "Overlapping type and enum names: test2")

        self._check_warns("enum_name_overlaps", ['Overlapping subset and slot names: a random name',
                                                 'Overlapping enum and slot names: a random name, a slot',
                                                 'Overlapping subset and enum names: a random name, a subset'])

    def test_enum_errors(self):
        """ Test the other invariants """
        self._check_error("enum_error_1", 'Enum: "error1" needs a code set to have a version')

        self._check_error("enum_error_2", 'Enum: "error2" cannot have both version and tag')

        self._check_error("enum_error_3", 'Enum: "error3" needs a code set to have a tag')

        self._check_error("enum_error_4", 'Enum: "error4" needs a code set to have a formula')

        self._check_error("enum_error_5", 'Enum: "error5" can have a formula or permissible values but not both')

        self._check_error("enum_error_6a", 'Slot: "classError1__slot_1" enumerations cannot be inlined')

        self._check_error("enum_error_6b", 'Slot: "classError1__slot_1" enumerations cannot be inlinedz')

        self._check_error("enum_error_7", 'Slot: "Unknown PvFormulaOptions value: LABEL')

    @unittest.skipIf(True, "Enable this when we get the emitter updated to include the location of the error")
    def test_enum_valueerror(self):
        """ Make sure that the link to the error is included in the output """
        self._check_error("enum_error_7", 'alternatives.yaml", line ')

    def test_enum_alternatives(self):
        """ test various variants on enum constraints """
        file = "alternatives"
        env.generate_single_file(env.expected_path(self.testdir, f'{file}.yaml'),
                                 lambda: YAMLGenerator(env.input_path(self.testdir, f'{file}.yaml')).serialize(),
                                 filtr=yaml_filter, value_is_returned=True)

        python_name = f'{self.testdir}/{file}.py'
        YAMLGenerator(env.input_path(self.testdir, f'{file}.yaml'),
                      mergeimports=False, log_level=logging.INFO).serialize()
        env.generate_single_file(python_name,
                                 lambda: PythonGenerator(env.input_path(self.testdir, f'{file}.yaml'),
                                                         importmap=env.import_map, mergeimports=False).serialize(),
                                 comparator=lambda exp, act: compare_python(exp, act, self.env.expected_path(python_name)),
                                 value_is_returned=True)

        module = compile_python(env.expected_path(python_name))

if __name__ == '__main__':
    unittest.main()

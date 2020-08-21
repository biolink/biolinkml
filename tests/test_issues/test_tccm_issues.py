import unittest

from biolinkml.generators.pythongen import PythonGenerator
from biolinkml.generators.yamlgen import YAMLGenerator
from biolinkml.utils.schemaloader import SchemaLoader
from tests.utils.python_comparator import compare_python
from tests.utils.test_environment import TestEnvironmentTestCase
from tests.test_issues.environment import env


class TCCMTestCase(TestEnvironmentTestCase):
    env = env

    """ Unit tests for issues encountered in the TCCM model generation """
    def test_references_typeerror(self):
        """  TypeError: sequence item 0: expected str instance, NoneType found is generated from schemasynopsis """
        SchemaLoader(env.input_path('issue_tccm', 'resourcedescription.yaml'), mergeimports=False).resolve()

    def test_slot_usage_only(self):
        """ Slot_usages without parents don't generate slots period. """
        env.generate_single_file('issue_ttcm_1.py',
                                 lambda: PythonGenerator(env.input_path('issue_tccm', 'resourcedescription.yaml'),
                                                         importmap=env.import_map, mergeimports=False).serialize(),
                                 comparator=compare_python, value_is_returned=True)

    def test_mapping_prefix(self):
        """ Prefix validation fails in  """
        with self.redirect_logstream() as logger:
            YAMLGenerator(env.input_path('issue_tccm', 'illegal_mapping_prefix.yaml'),
                          mergeimports=False, logger=logger).serialize(validateonly=True)
        self.assertIn('Unrecognized prefix: DO', logger.result, "Basic slot mapping validation failure")
        self.assertIn('Unrecognized prefix: RE', logger.result, "Basic class mapping validation failure")
        self.assertIn('Unrecognized prefix: MI', logger.result, "Solo slot usage mapping validation failure")
        self.assertIn('Unrecognized prefix: FA', logger.result, "Slot usage specialization validation failure")
        self.assertIn('Unrecognized prefix: SO', logger.result, "Slot usage variant validation failure")
        self.assertIn('Unrecognized prefix: LA', logger.result, "Inherited slot mapping validation failure")
        self.assertIn('Unrecognized prefix: TI', logger.result, "Inherited class mapping mapping validation failure")


if __name__ == '__main__':
    unittest.main()

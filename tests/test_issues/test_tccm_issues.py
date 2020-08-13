import unittest

from biolinkml.utils.schemaloader import SchemaLoader
from tests.utils.test_environment import TestEnvironmentTestCase
from tests.test_issues.environment import env


class TCCMTestCase(TestEnvironmentTestCase):
    env = env

    """ Unit tests for issues encountered in the TCCM model generation """
    def test_references_typeerror(self):
        """  TypeError: sequence item 0: expected str instance, NoneType found is generated from schemasynopsis """
        SchemaLoader(env.input_path('issue_tccm', 'resourcedescription.yaml'), mergeimports=False).resolve()



if __name__ == '__main__':
    unittest.main()

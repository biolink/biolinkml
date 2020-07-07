import unittest

from biolinkml.generators.csvgen import CsvGenerator
from tests import DEFAULT_LOG_LEVEL
from tests.test_issues.environment import env


class Issue38UnitTest(unittest.TestCase):
    def test_domain_slots(self):
        """ Subsets need to be imported as well """
        CsvGenerator(env.input_path('issue_38.yaml'), log_level=DEFAULT_LOG_LEVEL).serialize()
        # We never get here if the imports fails
        self.assertEqual(True, True)


if __name__ == '__main__':
    unittest.main()

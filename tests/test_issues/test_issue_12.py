import os
import unittest

from biolinkml.generators.yumlgen import YumlGenerator
from tests.test_issues import sourcedir


class Issue12UnitTest(unittest.TestCase):
    def test_domain_slots(self):
        """ has_phenotype shouldn't appear in the UML graph """
        yuml = YumlGenerator(os.path.join(sourcedir, 'issue_12.yaml')).serialize()
        self.assertEqual('http://yuml.me/diagram/nofunky;dir:TB/class/', yuml)


if __name__ == '__main__':
    unittest.main()

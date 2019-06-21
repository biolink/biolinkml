import os
import unittest

from biolinkml.generators.yumlgen import YumlGenerator

sourcedir = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'source')


class Issue10UnitTest(unittest.TestCase):
    def test_domain_slots(self):
        """ has_phenotype shouldn't appear in the UML graph """
        yuml = YumlGenerator(os.path.join(sourcedir, 'issue_12.yaml')).serialize()
        self.assertEqual('http://yuml.me/diagram/nofunky;dir:TB/class/'
                         '[BiologicalEntity]++- required thing 0..1>[PhenotypicFeature]', yuml)


if __name__ == '__main__':
    unittest.main()

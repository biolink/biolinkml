import os
import unittest

from jsonasobj import loads
from rdflib import Namespace

from biolinkml.generators.shexgen import ShExGenerator

sourcedir = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'source')
DCT = Namespace("http://purl.org/dc/terms/")

class DefinedPrefixTestCase(unittest.TestCase):
    def test_dct_prefix(self):
        """ Make sure prefixes are handled correctly """
        with self.assertRaises(ValueError, msg="A colon in an identifier is illegal"):
            shex = loads(ShExGenerator(os.path.join(sourcedir, 'Issue_6.yaml')).serialize(format='json'))
        shex = loads(ShExGenerator(os.path.join(sourcedir, 'Issue_6_fixed.yaml')).serialize(format='json'))
        company_shape = [s for s in shex.shapes if 'Company' in s.id][0]
        self.assertEqual(str(DCT.created), company_shape.expression.predicate, )



if __name__ == '__main__':
    unittest.main()

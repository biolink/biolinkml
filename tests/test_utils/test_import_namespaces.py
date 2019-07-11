import os
import unittest

from biolinkml.generators.shexgen import ShExGenerator
from tests.test_utils import inputdir


class URLImportTestCase(unittest.TestCase):

    @unittest.skipIf(True, "Finish implementing this")
    def test_import_from_url(self):
        """ Validate namespace bindings """
        shex = ShExGenerator(os.path.join(inputdir, 'import_test_l2.yaml')).serialize()
        print(shex)
        self.assertTrue(False, "Finish implementing this")


if __name__ == '__main__':
    unittest.main()

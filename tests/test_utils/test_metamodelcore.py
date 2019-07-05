import unittest

from biolinkml.utils.metamodelcore import NCName, Bool, URIorCURIE, URI
from biolinkml.utils.strictness import lax, strict


class MetamodelCoreTest(unittest.TestCase):
    def tearDown(self) -> None:
        strict()

    def test_ncname(self):
        self.assertEqual('A123', NCName('A123'))
        x = NCName('A1.B_C-')
        self.assertEqual('A1.B_C-', x)
        self.assertIsInstance(x, str)
        self.assertIsInstance(x, NCName)
        self.assertEqual(x, NCName(x))
        x = str(x)
        self.assertIsInstance(x, str)
        self.assertFalse(isinstance(x, NCName))
        with self.assertRaises(ValueError):
            NCName('1')
        with self.assertRaises(ValueError):
            NCName('A12!')

    def test_uris(self):
        """ Test the URI and URIorCURIE types """
        str1 = "https://google.com/test#file?abc=1&def=4"
        self.assertEqual(str1, URIorCURIE(str1))
        self.assertEqual(str1, URI(str1))
        str2 = "abc:123"
        self.assertEqual(str2, URIorCURIE(str2))
        str3 = ":123"
        self.assertEqual(str3, URIorCURIE(str3))
        with self.assertRaises(ValueError):
            URI(str2)
        with self.assertRaises(ValueError):
            URIorCURIE("1abc:def")
        with self.assertRaises(ValueError):
            URIorCURIE("1:def")

    def test_bool(self):
        self.assertTrue(Bool(True))
        self.assertTrue(Bool("True"))
        self.assertTrue(Bool("true"))
        self.assertTrue(Bool(1))
        self.assertTrue(Bool("1"))
        self.assertTrue(Bool(Bool(True)))
        self.assertFalse(Bool(False))
        self.assertFalse(Bool("False"))
        self.assertFalse(Bool("false"))
        self.assertFalse(Bool(0))
        self.assertFalse(Bool("0"))
        self.assertFalse(Bool(Bool(0)))
        # Strict mode
        with self.assertRaises(ValueError):
            x = Bool(17)
        with self.assertRaises(ValueError):
            x = Bool("a")
        lax()
        x = Bool(17)
        print(str(x))
        x = Bool("a")


if __name__ == '__main__':
    unittest.main()

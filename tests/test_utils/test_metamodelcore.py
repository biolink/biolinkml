import unittest

from biolinkml.utils.metamodelcore import NCName, Bool


class MetamodelCoreTest(unittest.TestCase):
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
        with self.assertRaises(ValueError):
            x = Bool(17)
        with self.assertRaises(ValueError):
            x = Bool("a")


if __name__ == '__main__':
    unittest.main()

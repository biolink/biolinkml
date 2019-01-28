import os
import unittest
from contextlib import redirect_stderr
from io import StringIO

from biolinkml.utils.schemaloader import SchemaLoader
from tests import skip_biolink_model
from tests.test_utils import datadir
from tests.test_utils.support.base import Base


class SchemaLoaderTestCase(Base):
    def test_basic_merge(self):
        """ Test the basic merge paths """
        errfile = StringIO()
        with redirect_stderr(errfile):
            self.eval_loader("merge1")
        self.assertEqual("Warning: Shared slot and subset names: s1", errfile.getvalue().strip())

    def test_mergeerror1(self):
        """ Test conflicting definitions path """
        fn = os.path.join(datadir, 'mergeerror1.yaml')
        with self.assertRaises(ValueError):
            SchemaLoader(fn)

    def test_meta(self):
        """ Load up a static image of the metamodel and emit it

        Note: you may want to periodically refresh the metamodel in the data section """
        self.maxDiff = None
        self.eval_loader('meta')

    def test_types(self):
        self.eval_loader('includes/types')

    def test_imports(self):
        self.eval_loader('base')

    def test_error_paths(self):
        """ Test various loader error situations"""

        fn = os.path.join(datadir, 'loadererror1.yaml')
        with self.assertRaises(ValueError, msg="Unknown slot domain should fail"):
            SchemaLoader(fn).resolve()

        fn = os.path.join(datadir, 'loadererror2.yaml')
        with self.assertRaises(ValueError, msg="Optional key slot should fail"):
            SchemaLoader(fn).resolve()

        fn = os.path.join(datadir, 'loadertest1.yaml')
        schema = SchemaLoader(fn).resolve()
        self.assertEqual('string', schema.slots['s1'].range)

        fn = os.path.join(datadir, 'loadererror4.yaml')
        with self.assertRaises(ValueError, msg="Default prefix is not defined"):
            SchemaLoader(fn).resolve()

    def test_empty_range(self):
        """ A type must have either a base or a parent """
        fn = os.path.join(datadir, 'loadererror5.yaml')
        with self.assertRaises(ValueError, msg="Range error should be raised"):
            _ = SchemaLoader(fn).resolve()

    def test_multi_key(self):
        """ Multiple keys are not supported """
        fn = os.path.join(datadir, 'loadererror6.yaml')
        with self.assertRaises(ValueError, msg="Two or more keys are not allowed"):
            _ = SchemaLoader(fn).resolve()

        fn = os.path.join(datadir, 'loadererror7.yaml')
        with self.assertRaises(ValueError, msg="Two or more keys are not allowed"):
            _ = SchemaLoader(fn).resolve()

    def test_key_and_id(self):
        """ A slot cannot be both a key and an identifier """
        fn = os.path.join(datadir, 'loadererror8.yaml')
        with self.assertRaises(ValueError, msg="A slot cannot be both a key and identifier"):
            _ = SchemaLoader(fn).resolve()

        fn = os.path.join(datadir, 'loadererror9.yaml')
        with self.assertRaises(ValueError, msg="A slot cannot be both a key and identifier"):
            _ = SchemaLoader(fn).resolve()

    def test_missing_type_uri(self):
        """ A type with neither a typeof or uri is an error """
        fn = os.path.join(datadir, 'loadererror10.yaml')
        with self.assertRaises(ValueError, msg="A non-typeof type has to have a URI"):
            _ = SchemaLoader(fn).resolve()
        fn = os.path.join(datadir, 'loaderpass11.yaml')
        _ = SchemaLoader(fn).resolve()

    @unittest.skipIf(True, "Needs to be implemente3d")
    def test_undefined_subset(self):
        """ Throw an error on an undefined subset reference """
        self.assertTrue(False, "Implemement me")

if __name__ == '__main__':
    unittest.main()

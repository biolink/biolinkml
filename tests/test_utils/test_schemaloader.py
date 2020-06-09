import os
import unittest
from contextlib import redirect_stderr
from io import StringIO

import jsonasobj
from jsonasobj import as_json, load

from biolinkml import LOCAL_METAMODEL_YAML_FILE, LOCAL_TYPES_YAML_FILE
from biolinkml.utils.schemaloader import SchemaLoader
from tests.test_utils import inputdir, outputdir
from tests.test_utils.support.base import Base
from tests.utils.metadata_filters import json_metadata_filter


class SchemaLoaderTestCase(Base):
    def test_basic_merge(self):
        """ Test the basic merge paths """
        errfile = StringIO()
        with redirect_stderr(errfile):
            self.eval_loader("merge1")
        # Note: There is something about the PyCharm / UnitTest package that, if you are running a lot of tests, the
        # output ends up getting redirected to the test runner rather than stderr.  If there is nothing at all, we
        # will assume that this is the case.
        if errfile.getvalue().strip():
            self.assertIn("Shared slot and subset names: s1, s2", errfile.getvalue().strip())
        else:
            print("*** Warning not tested -- stderr redirect isn't working")

    def test_mergeerror1(self):
        """ Test conflicting definitions path """
        fn = os.path.join(inputdir, 'mergeerror1.yaml')
        with self.assertRaises(ValueError):
            SchemaLoader(fn)

    def test_meta(self):
        """ Load up a static image of the metamodel and emit it

        Note: you may want to periodically refresh the metamodel in the data section """
        self.maxDiff = None
        self.eval_loader('meta', source=LOCAL_METAMODEL_YAML_FILE)

    def test_types(self):
        self.eval_loader('includes/types', source=LOCAL_TYPES_YAML_FILE)

    def test_imports(self):
        self.eval_loader('base')

    def test_error_paths(self):
        """ Test various loader error situations"""

        fn = os.path.join(inputdir, 'loadererror1.yaml')
        with self.assertRaises(ValueError, msg="Unknown slot domain should fail") as e:
            SchemaLoader(fn).resolve()
        self.assertIn('loadererror1.yaml: line 11 col 13', str(e.exception))

        fn = os.path.join(inputdir, 'loadererror2.yaml')
        with self.assertRaises(ValueError, msg="Optional key slot should fail") as e:
            SchemaLoader(fn).resolve()
        self.assertIn('loadererror2.yaml: line 10 col 3', str(e.exception))

        fn = os.path.join(inputdir, 'loadertest1.yaml')
        schema = SchemaLoader(fn).resolve()
        self.assertEqual('string', schema.slots['s1'].range)

        fn = os.path.join(inputdir, 'loadererror4.yaml')
        with self.assertRaises(ValueError, msg="Default prefix is not defined") as e:
            SchemaLoader(fn).resolve()
        self.assertIn('loadererror4.yaml: line 6 col 17', str(e.exception))

    def test_empty_range(self):
        """ A type must have either a base or a parent """
        fn = os.path.join(inputdir, 'loadererror5.yaml')
        with self.assertRaises(ValueError, msg="Range error should be raised") as e:
            _ = SchemaLoader(fn).resolve()
        self.assertIn('loadererror5.yaml: line 9 col 3', str(e.exception))

    def test_multi_key(self):
        """ Multiple keys are not supported """
        fn = os.path.join(inputdir, 'loadererror6.yaml')
        with self.assertRaises(ValueError, msg="Two or more keys are not allowed") as e:
            _ = SchemaLoader(fn).resolve()
        self.assertIn('loadererror6.yaml: line 16 col 3', str(e.exception))

        fn = os.path.join(inputdir, 'loadererror7.yaml')
        with self.assertRaises(ValueError, msg="Two or more keys are not allowed") as e:
            _ = SchemaLoader(fn).resolve()
        self.assertIn('loadererror7.yaml: line 17 col 3', str(e.exception))

    @unittest.skipIf(True, "Never impelemented checking key and identifier")
    def test_key_and_id(self):
        """ A slot cannot be both a key and an identifier """
        fn = os.path.join(inputdir, 'loadererror8.yaml')
        _ = SchemaLoader(fn).resolve()
        with self.assertRaises(ValueError, msg="A slot cannot be both a key and identifier") as e:
            _ = SchemaLoader(fn).resolve()
        self.assertIn('loadererror8.yaml', str(e.exception))

        fn = os.path.join(inputdir, 'loadererror9.yaml')
        with self.assertRaises(ValueError, msg="A slot cannot be both a key and identifier") as e:
            _ = SchemaLoader(fn).resolve()
        self.assertIn('loadererror9.yaml', str(e.exception))

    def test_missing_type_uri(self):
        """ A type with neither a typeof or uri is an error """
        fn = os.path.join(inputdir, 'loadererror10.yaml')
        with self.assertRaises(ValueError, msg="A non-typeof type has to have a URI") as e:
            _ = SchemaLoader(fn).resolve()
        self.assertIn('loadererror10.yaml: line 12 col 3', str(e.exception))
        fn = os.path.join(inputdir, 'loaderpass11.yaml')
        _ = SchemaLoader(fn).resolve()

    def test_undefined_subset(self):
        """ Throw an error on an undefined subset reference """
        fn = os.path.join(inputdir, 'loadererror11.yaml')
        with self.assertRaises(ValueError, msg="Subset references must be valid") as e:
            _ = SchemaLoader(fn).resolve()
        self.assertIn('loadererror11.yaml: line 22 col 16', str(e.exception))

    def test_importmap(self):
        """ Test the importmap parameter """
        fn = os.path.join(inputdir, 'import_test_1.yaml')
        importmap = {"http://example.org/import_test_2" : "import_test_2",
                      "loc/imp3": "import_test_3",
                      "base:import_test_4": "http://example.org/import_test_4",
                      "http://example.org/import_test_4": "import_test_4",
                      "types": "http://w3id.org/biolink/biolinkml/types"}
        schema = SchemaLoader(fn, importmap=importmap).resolve()
        schema_image = as_json(schema)
        outfile = os.path.join(outputdir, 'import_test_1.json')
        if not os.path.exists(outfile):
            with open(outfile, 'w') as f:
                f.write(schema_image)
                self.fail("File {outfile} written - rerun test")
        expected = load(outfile)
        self.maxDiff = None
        self.assertEqual(json_metadata_filter(jsonasobj.as_json(expected)), json_metadata_filter(schema_image))



if __name__ == '__main__':
    unittest.main()

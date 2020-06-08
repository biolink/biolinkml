import os
import unittest

import yaml
from jsonasobj import as_json, loads, load

from biolinkml.utils.rawloader import load_raw_schema
from biolinkml.utils.yamlutils import DupCheckYamlLoader, as_yaml
from tests.test_utils import inputdir, outputdir
from tests.test_utils.support.base import Base


class YamlUtilTestCase(Base):

    def test_dupcheck_loader(self):
        """ Make sure the duplicate checker finds duplicates """
        with open(os.path.join(inputdir, 'yaml1.yaml')) as f:
            y1 = yaml.safe_load(f)
            self.assertEqual(17, y1['f1'])
        with open(os.path.join(inputdir, 'yaml1.yaml')) as f:
            with self.assertRaises(ValueError):
                yaml.load(f, DupCheckYamlLoader)
        with open(os.path.join(inputdir, 'yaml2.yaml')) as f:
            with self.assertRaises(ValueError):
                yaml.load(f, DupCheckYamlLoader)
        with open(os.path.join(inputdir, 'schema1.yaml')) as f:
            s1 = yaml.load(f, DupCheckYamlLoader)
            self.assertEqual('schema1', s1['name'])

    def test_as_json(self):
        schema = self.fix_schema_metadata(load_raw_schema(os.path.join(inputdir, 'schema6.yaml')))
        outfile = os.path.join(outputdir, 'schema6.json')
        if not os.path.exists(outfile):
            with open(outfile, 'w') as f:
                f.write(as_json(schema))
                self.fail(f"Generated {outfile} - run test again")
        else:
            self.assertEqual(load(outfile), loads(as_json(schema)))

    @unittest.skipIf(True, "Need to make yaml dump work again")
    def test_as_yaml(self):
        """ Test the YAML output representation """
        schema = self.fix_schema_metadata(load_raw_schema(os.path.join(inputdir, 'schema4.yaml')))
        outfile = os.path.join(outputdir, 'schema4.yaml')
        if not os.path.exists(outfile):
            with open(outfile, 'w') as f:
                f.write(as_yaml(schema))
            self.fail(f"Output file: {outfile} created - run test again")

        with open(outfile) as f:
            self.assertEqual(f.read(), as_yaml(schema))


if __name__ == '__main__':
    unittest.main()

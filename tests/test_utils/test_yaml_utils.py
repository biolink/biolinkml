import os
import unittest

import yaml
from jsonasobj import as_json, loads

from biolinkml.utils.rawloader import load_raw_schema
from biolinkml.utils.yamlutils import DupCheckYamlLoader, as_yaml
from tests.test_utils import inputdir
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
        self.assertEqual(loads("""{
   "name": "schema6",
   "id": "http://example.org/schema6.fuzz",
   "title": "Load Raw Schema Test",
   "types": [
      {
         "name": "foo",
         "from_schema": "http://example.org/schema6.fuzz",
         "base": "str",
         "uri": "http://example.org/types/String"
      }
   ],
   "slots": [
      {
         "name": "s1",
         "from_schema": "http://example.org/schema6.fuzz",
         "domain": "c1",
         "range": "foo"
      }
   ],
   "classes": [
      {
         "name": "c1",
         "from_schema": "http://example.org/schema6.fuzz"
      }
   ],
   "metamodel_version": "0.5.0",
   "source_file": "schema6.yaml",
   "source_file_date": "2018-12-31 17:23",
   "source_file_size": 259,
   "default_prefix": "http://example.org/schema6.fuzz/",
   "generation_date": "2018-12-31 17:23"
}"""), loads(as_json(schema)))

    def test_as_yaml(self):
        """ Test the YAML output representation """
        schema = self.fix_schema_metadata(load_raw_schema(os.path.join(inputdir, 'schema4.yaml')))

        self.assertEqual("""default_prefix: http://example.org/schema4/
generation_date: 2018-12-31 17:23
id: !!python/object/new:biolinkml.utils.metamodelcore.URI
- http://example.org/schema4
metamodel_version: 0.5.0
name: !!python/object/new:biolinkml.meta.SchemaDefinitionName
- schema4
source_file: schema4.yaml
source_file_date: 2018-12-31 17:23
source_file_size: 259
title: Load Raw Schema Test
types:
  integer:
    base: int
    from_schema: !!python/object/new:biolinkml.utils.metamodelcore.URI
    - http://example.org/schema5
    name: !!python/object/new:biolinkml.meta.TypeDefinitionName
    - integer
  string:
    base: str
    from_schema: !!python/object/new:biolinkml.utils.metamodelcore.URI
    - http://example.org/schema4
    name: !!python/object/new:biolinkml.meta.TypeDefinitionName
    - string
""", as_yaml(schema))


if __name__ == '__main__':
    unittest.main()

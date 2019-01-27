import datetime
import os
import unittest
from json import loads
from typing import Optional, Callable, Any

from jsonasobj import as_json

from biolinkml.meta import SchemaDefinition
from biolinkml.utils.schemaloader import SchemaLoader
from tests import sourcedir
from tests.test_utils import datadir

update_all_files: bool = False


class Base(unittest.TestCase):
    def fix_schema_metadata(self, schema: SchemaDefinition) -> SchemaDefinition:
        self.assertIsNotNone(schema.generation_date)
        schema.source_file = os.path.basename(schema.source_file)
        schema.generation_date = "2018-12-31 17:23"
        self.assertIsNotNone(schema.metamodel_version)
        schema.metamodel_version = "0.5.0"
        self.assertIsNotNone(schema.source_file_size)
        schema.source_file_size = 259
        self.assertIsNotNone(schema.source_file_date)
        schema.source_file_date = "2018-12-31 17:23"
        return schema

    def eval_output(self, actual: str, filename: str, conv_f: Optional[Callable[[str], Any]]=None) -> None:
        file_path = os.path.join(datadir, filename)
        file_created = False
        if not os.path.exists(file_path) or update_all_files:
            print(f"Creating {file_path}")
            with open(file_path, 'w') as f:
                f.write(actual)
            file_created = True
        with open(file_path) as f:
            expected = f.read()
        if conv_f:
            self.assertEqual(conv_f(expected), conv_f(actual))
        else:
            self.assertEqual(expected, actual)
        self.assertFalse(file_created, f"{file_path}: Created new file image -- rerun")

    def eval_loader(self, base_name: str, is_sourcedir: bool=False) -> None:
        fn = os.path.join(sourcedir if is_sourcedir else datadir, base_name + '.yaml')
        loader = SchemaLoader(fn)
        schema = as_json(self.fix_schema_metadata(loader.resolve()))
        self.eval_output(schema, base_name + '.json', loads)
        errors = '\n'.join(loader.synopsis.errors())
        self.eval_output(errors, base_name + '.errs')
        self.assertFalse(update_all_files, "Updating base files -- rerun")

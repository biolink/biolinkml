import logging
import os
import unittest
from json import loads
from typing import Optional, Callable, Any

from jsonasobj import as_json

from biolinkml.meta import SchemaDefinition
from biolinkml.utils.schemaloader import SchemaLoader
from tests.utils.test_environment import TestEnvironment


class Base(unittest.TestCase):
    env: TestEnvironment = None

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

    def eval_output(self, actual: str, filename: str, conv_f: Optional[Callable[[str], Any]] = None,
                    comp_f: Optional[Callable[[str, str], None]] = None) -> None:

        def _default_comparator(expected: str, actual: str) -> None:
            if expected != actual:
                print(f"\n***** Testing file: {file_path}. Remove to update test. *****\n")
                self.assertEqual(expected, actual)

        if comp_f is None:
            comp_f = _default_comparator

        file_path = self.env.expected_path(filename)
        file_created = False
        if not os.path.exists(file_path):
            print(f"Creating {file_path}")
            with open(file_path, 'w') as f:
                f.write(actual)
            file_created = True
        with open(file_path) as f:
            expected = f.read()

        if conv_f:
            self.maxDiff = None
            comp_f(conv_f(expected), conv_f(actual))
        else:
            comp_f(expected, actual)
        self.assertFalse(file_created, f"{file_path}: Created new file image -- rerun")

    def eval_loader(self, base_name: str, source: Optional[str]  =None,
                    logger: Optional[logging.Logger] = None) -> None:
        fn = source if source else self.env.input_path(base_name + '.yaml')
        loader = SchemaLoader(fn, logger=logger) if logger else SchemaLoader(fn)
        schema = as_json(self.fix_schema_metadata(loader.resolve()))
        self.eval_output(schema, base_name + '.json', loads)
        errors = '\n'.join(loader.synopsis.errors())
        self.eval_output(errors, base_name + '.errs')

import os
import unittest
from typing import Union, List

from biolinkml.utils.schemaloader import SchemaLoader
from tests import sourcedir, skip_biolink_model
from tests.test_utils import datadir
from tests.test_utils.support.base import Base, update_all_files


class SchemaSynopsisTestCase(Base):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.loader: SchemaLoader = None

    def loadit(self, source: str) -> None:
        self.loader = SchemaLoader(source)
        self.loader.resolve()

    """ Tests for various parts of the schema synopsis file """
    def eval_synopsis(self, base_name: str, *,  is_sourcedir: bool=False) -> None:
        fn = os.path.join(sourcedir if is_sourcedir else datadir, base_name + '.yaml')
        self.loadit(fn)
        errors = '\n'.join(self.loader.synopsis.errors())
        self.eval_output(errors, base_name + '.errs')

        synopsis = self.loader.synopsis.summary()
        self.eval_output(synopsis, base_name + '.synopsis')
        self.assertFalse(update_all_files, "Updating base files -- rerun")

    def assert_warning(self, text: str) -> bool:
        return f'* {text}' in self.loader.synopsis.summary()

    def assert_error(self, text: Union[str, List[str]]) -> None:
        if isinstance(text, str):
            text = [text]
        self.assertEqual(text, [e.strip() for e in self.loader.synopsis.errors()])

    def test_meta_synopsis(self):
        """ Summarize a static image of the meta model """
        self.eval_synopsis('meta')

    def test_unitialized_domain(self):
        self.loadit(os.path.join(datadir, 'synopsis1.yaml'))
        self.assert_error('Slot s1 has no owners')
        self.assert_warning('Unspecified domain: s1')

    def test_applyto(self):
        self.eval_synopsis('synopsis2')


if __name__ == '__main__':
    unittest.main()

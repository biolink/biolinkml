import os
import unittest
from typing import Union, List, Optional

from biolinkml import LOCAL_METAMODEL_YAML_FILE
from biolinkml.utils.schemaloader import SchemaLoader
from tests import sourcedir
from tests.test_utils import inputdir
from tests.test_utils.support.base import Base, update_all_files


class SchemaSynopsisTestCase(Base):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.loader: SchemaLoader = None

    def loadit(self, source: str) -> None:
        self.loader = SchemaLoader(source)
        self.loader.resolve()

    """ Tests for various parts of the schema synopsis file """
    def eval_synopsis(self, base_name: str, *,  is_sourcedir: bool=False, source: Optional[str]=None) -> None:
        fn = os.path.join(sourcedir if is_sourcedir else inputdir, base_name + '.yaml') if not source else source
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
        """ Raise a flag if the number of classes, slots, types or other elements change in the model  """
        self.eval_synopsis('meta', source=LOCAL_METAMODEL_YAML_FILE)

    def test_unitialized_domain(self):
        self.loadit(os.path.join(inputdir, 'synopsis1.yaml'))
        # Owners check no longer occurs
        # self.assert_error('Slot s1 has no owners')
        self.assert_warning('Unspecified domain: s1')

    def test_applyto(self):
        self.eval_synopsis('synopsis2')


if __name__ == '__main__':
    unittest.main()

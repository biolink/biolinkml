import unittest
from typing import Union, List, Optional

from biolinkml.utils.schemaloader import SchemaLoader
from tests.test_utils.environment import env
from tests.utils.base import Base


class SchemaSynopsisTestCase(Base):
    env = env

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.loader: SchemaLoader = None

    def loadit(self, source: str) -> None:
        self.loader = SchemaLoader(source)
        self.loader.resolve()

    """ Tests for various parts of the schema synopsis file """
    def eval_synopsis(self, base_name: str, source: Optional[str]=None) -> None:
        self.loadit(source if source else env.input_path(base_name + '.yaml'))
        errors = '\n'.join(self.loader.synopsis.errors())
        self.eval_output(errors, base_name + '.errs')

        synopsis = self.loader.synopsis.summary()
        self.eval_output(synopsis, base_name + '.synopsis')

    def assert_warning(self, text: str) -> bool:
        return f'* {text}' in self.loader.synopsis.summary()

    def assert_error(self, text: Union[str, List[str]]) -> None:
        if isinstance(text, str):
            text = [text]
        self.assertEqual(text, [e.strip() for e in self.loader.synopsis.errors()])

    def test_meta_synopsis(self):
        """ Raise a flag if the number of classes, slots, types or other elements change in the model  """
        self.eval_synopsis('meta', source=env.meta_yaml)

    def test_unitialized_domain(self):
        self.loadit(env.input_path('synopsis1.yaml'))
        # Owners check no longer occurs
        # self.assert_error('Slot s1 has no owners')
        self.assert_warning('Unspecified domain: s1')

    def test_applyto(self):
        self.eval_synopsis('synopsis2')


if __name__ == '__main__':
    unittest.main()

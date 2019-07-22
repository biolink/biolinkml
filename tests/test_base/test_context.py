import os
import re
import unittest

from biolinkml import LOCAL_YAML_PATH, LOCAL_CONTEXT_PATH, META_BASE_URI, METAMODEL_LDCONTEXT_NAME
from biolinkml.generators.jsonldcontextgen import ContextGenerator
from tests import targetdir


class LDContextTestCase(unittest.TestCase):
    @staticmethod
    def _strip_meta(txt: str) -> str:
        return re.sub(r'"_comments": ".*"', '"_comments": "(REMOVED)"', txt).strip()

    def test_context(self):
        """ Verify that the root context.jsonld is current """
        new_context = ContextGenerator(LOCAL_YAML_PATH).serialize(base=META_BASE_URI)
        target = os.path.join(targetdir, METAMODEL_LDCONTEXT_NAME)
        with open(target, 'w') as f:
            f.write(new_context)

        with open(LOCAL_CONTEXT_PATH) as f:
            old_context = f.read()
        self.assertEqual(self._strip_meta(old_context), self._strip_meta(new_context),
                         f'\n{LOCAL_CONTEXT_PATH} does not match output -- new file is in test/target')


if __name__ == '__main__':
    unittest.main()

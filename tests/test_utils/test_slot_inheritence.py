import os
import unittest

from biolinkml.utils.schemaloader import SchemaLoader
from tests.test_utils import inputdir


class InheritedSlotTestCase(unittest.TestCase):

    def test_inherited_slot(self):
        """ Validate default slot range settings """
        schema = SchemaLoader(os.path.join(inputdir, 'inherited_slots.yaml')).resolve()
        self.assertTrue('same as' in schema.classes['named thing'].slots)


if __name__ == '__main__':
    unittest.main()

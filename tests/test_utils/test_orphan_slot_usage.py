import os
import unittest

from biolinkml.generators.golrgen import GolrSchemaGenerator
from tests import targetdir
from tests.test_utils import inputdir
from tests.utils.dirutils import make_and_clear_directory


class OrphanSlotUsageTestCase(unittest.TestCase):

    def test_orphan_slot_usage(self):
        """ Make sure an orphan slot_usage works """
        # The bug is that this goes into an endless loop
        output_dir = os.path.join(targetdir, 'slottest')
        make_and_clear_directory(output_dir)
        GolrSchemaGenerator(os.path.join(inputdir, 'orphan_slot_usage.yaml')).serialize(directory=output_dir)
        make_and_clear_directory(output_dir)
        self.assertTrue(True)


if __name__ == '__main__':
    unittest.main()

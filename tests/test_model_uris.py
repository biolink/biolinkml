import os
import unittest

from biolinkml import LOCAL_YAML_PATH, METAMODEL_URI, METAMODEL_LOCAL_NAME, LOCAL_CONTEXT_PATH, METAMODEL_NAMESPACE, \
    METATYPE_NAMESPACE, METATYPE_LOCAL_NAME, METATYPE_URI, LOCAL_TYPES_PATH
from biolinkml.utils.rawloader import load_raw_schema


class ModelURITestCase(unittest.TestCase):

    def validate_yaml_content(self, meta_yaml, access_by_uri: bool) -> None:
        self.assertEqual(METAMODEL_URI, meta_yaml.id)
        self.assertEqual(METAMODEL_LOCAL_NAME, meta_yaml.default_prefix)
        self.assertEqual(METAMODEL_NAMESPACE, meta_yaml.prefixes[meta_yaml.default_prefix].prefix_reference)
        self.assertEqual(METAMODEL_URI if access_by_uri else LOCAL_YAML_PATH, meta_yaml.source_file)

    def test_model_uris(self):
        """ Test that the variables in meta.yaml match the contents of biolinkml/__init__.py """
        self.assertTrue(os.path.exists(LOCAL_YAML_PATH))
        self.assertTrue(os.path.exists(LOCAL_CONTEXT_PATH))
        meta_yaml = load_raw_schema(LOCAL_YAML_PATH)
        self.validate_yaml_content(meta_yaml, False)

        types_yaml = load_raw_schema(LOCAL_TYPES_PATH)
        self.assertEqual(METATYPE_LOCAL_NAME, types_yaml.default_prefix)
        self.assertEqual(METATYPE_URI, types_yaml.id)
        self.assertEqual(METATYPE_LOCAL_NAME, types_yaml.default_prefix)
        self.assertEqual(METATYPE_NAMESPACE, types_yaml.prefixes[types_yaml.default_prefix].prefix_reference)

    def test_model_access(self):
        """ Make sure that the law loader can dereference a URL and that the data matches """
        online_meta_yaml = load_raw_schema(METAMODEL_URI)
        self.validate_yaml_content(online_meta_yaml, True)


if __name__ == '__main__':
    unittest.main()

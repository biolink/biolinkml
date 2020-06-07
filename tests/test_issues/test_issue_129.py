import os
import unittest
import json

from biolinkml.generators.jsonschemagen import JsonSchemaGenerator
from biolinkml.generators.owlgen import OwlSchemaGenerator
from tests.test_issues import sourcedir


class IssueJSONSchemaTypesTestCase(unittest.TestCase):

    def header(self, txt: str) -> str:
        return '\n' + ("=" * 20) + f" {txt} " + ("=" * 20)

    def test_issue_types(self):
        """ Make sure that types are generated as part of the output """
        yaml_fname = os.path.join(sourcedir, 'issue_129.yaml')
        gen = JsonSchemaGenerator(yaml_fname)
        gen.topCls = 'c'
        jsonschema = gen.serialize()
        print(self.header("JSONSchema"))
        print(jsonschema)
        sobj = json.loads(jsonschema)
        defs = sobj['definitions']
        C = defs['C']
        props = C['properties']
        assert props['age_in_years']['type'] == 'integer'
        assert props['has_prop']['type'] == 'boolean'
        # multivalued primitive type, inlined
        assert props['scores']['type'] == 'array'
        assert props['scores']['items']['type'] == 'number'
        # single-valued complex type, inlined
        assert props['has_d']['$ref'] == "#/definitions/D"

        # multi-valued, inlined
        assert props['has_ds']['type'] == 'array'
        assert props['has_ds']['items']['$ref'] == "#/definitions/D"

        # single-valued, non-inlined (foreign key)
        assert props['parent']['type'] == "string"

        # multi-valued, non-inlined (foreign key)
        assert props['children']['type'] == 'array'
        assert props['children']['items']['type'] == "string"

if __name__ == '__main__':
    unittest.main()

import os
import unittest

from biolinkml.utils.schemaloader import SchemaLoader
from jsonasobj import as_dict
from tests.test_utils import inputdir


class ResolverTestCase(unittest.TestCase):

    def test_default_range(self):
        """ Validate default slot range settings """
        schema = SchemaLoader(os.path.join(inputdir, 'resolver1.yaml')).resolve()
        self.assertEqual({'s1':'t1', 's2':'t2'}, {slot.name: slot.range for slot in schema.slots.values()})
        schema = SchemaLoader(os.path.join(inputdir, 'resolver2.yaml')).resolve()
        self.assertEqual({'s1': 'string', 's2': 't2'}, {slot.name: slot.range for slot in schema.slots.values()})

    def test_type_uri(self):
        """ Validate type URI's and the fact that they aren't inherited """
        schema = SchemaLoader(os.path.join(inputdir, 'resolver2.yaml')).resolve()
        self.assertEqual({'string': 'xsd:string', 't1': 'xsd:string', 't2': 'xsd:int', 't3': 'xsd:string'},
                         {t.name: t.uri for t in schema.types.values()})

    def test_element_slots(self):
        """ Test all element slots and their inheritence """
        schema = SchemaLoader(os.path.join(inputdir, 'resolver3.yaml')).resolve()
        x = {k:v for k, v in as_dict(schema.slots['s1']).items() if v is not None and v != []}
        self.assertEqual(
            {'alt_descriptions': {},
             'comments': ["I'm a little comment"],
             'description': 'this is s1 it is good',
             'domain': 'c1',
             'examples': [{'description': 'an example', 'value': 'test: foo'},
                          {'description': None, 'value': 17}],
             'from_schema': 'http://example.org/yaml4',
             'in_subset': ['subset1', 'subset 2'],
             'local_names': {},
             'inlined': True,
             'name': 's1',
             'notes': ['Pay attention here', 'Something might be happening'],
             'owner': 's1',
             'range': 'c2',
             'required': False,
             'see_also': ['http://example.org/e1', 'ex:e2'],
             'slot_uri': 'http://example.org/yaml4/s1'}, x)




if __name__ == '__main__':
    unittest.main()

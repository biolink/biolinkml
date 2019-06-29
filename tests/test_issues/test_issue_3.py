import os
import unittest

from rdflib import Namespace, Graph, XSD

from biolinkml import LOCAL_TYPES_PATH
from biolinkml.generators.rdfgen import RDFGenerator

sourcedir = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'source')

META = Namespace("https://w3id.org/biolink/biolinkml/meta/")
METATYPE = Namespace("https://w3id.org/biolink/biolinkml/type/")


class DateTestCase(unittest.TestCase):
    def test_date_time(self):
        """ date datatype should be rdf:date and datetime rdf:datetime """
        rdf = RDFGenerator(LOCAL_TYPES_PATH).serialize()
        g = Graph()
        g.parse(data=rdf, format="turtle")
        self.assertEqual(XSD.date, g.value(METATYPE.date, META.uri))
        self.assertEqual(XSD.dateTime, g.value(METATYPE.datetime, META.uri))


if __name__ == '__main__':
    unittest.main()
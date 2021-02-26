import unittest

from rdflib import Graph, Namespace

from biolinkml.generators.jsonldgen import JSONLDGenerator
from biolinkml.generators.rdfgen import RDFGenerator
from biolinkml.meta import META
from tests.utils.test_environment import TestEnvironmentTestCase
from tests.test_issues.environment import env

NS = Namespace('https://example.org/test/')

schema = f'''id: {NS}
enums:
  test_enum:
    permissible_values:
      a b:
'''


class Issue381TestCase(TestEnvironmentTestCase):
    """ Test URL generation w/ non-mangled values """
    env = env

    def test_non_url_pv(self):
        g = Graph()
        g.parse(data=RDFGenerator(schema).serialize(), format="ttl")
        self.assertEqual('https://example.org/test/a%20b', str(g.value(NS.test_enum, META.permissible_values)))


if __name__ == '__main__':
    unittest.main()

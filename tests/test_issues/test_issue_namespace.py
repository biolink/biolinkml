import os
import unittest

from biolinkml import LOCAL_METAMODEL_LDCONTEXT_FILE
from biolinkml.generators.rdfgen import RDFGenerator
from tests.test_issues import sourcedir

@unittest.skipIf(True, "Test is not complete -- keep until fully resolved")
class NamespaceIssueTestCase(unittest.TestCase):
    def test_namespace(self):
        yaml_fname = os.path.join(sourcedir, 'issue_namespace.yaml')
        context = "https://biolink.github.io/biolink-model/context.jsonld"
        print(RDFGenerator(yaml_fname).serialize(context=context))

if __name__ == '__main__':
    unittest.main()

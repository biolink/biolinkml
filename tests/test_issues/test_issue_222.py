import unittest
from contextlib import redirect_stdout
from io import StringIO

from biolinkml.generators.rdfgen import cli
from tests import CLIExitException
from tests.test_issues.environment import env
from tests.utils.test_environment import TestEnvironmentTestCase


class RDFGenDefaultTest(TestEnvironmentTestCase):
    env = env

    def test_issue_222(self):
        """ Test that the RDF Generator default is correct """
        output = StringIO()
        try:
            with redirect_stdout(output):
                cli([env.root_input_path('meta.yaml')])
        except CLIExitException as e:
            self.assertEqual(0, e.code)


if __name__ == '__main__':
    unittest.main()

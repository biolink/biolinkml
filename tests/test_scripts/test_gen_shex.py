import os
import unittest
import click
from CFGraph import CFGraph
from pyshex import ShExEvaluator

from biolinkml import METAMODEL_NAMESPACE, METAMODEL_URI
from biolinkml.generators.jsonldcontextgen import ContextGenerator
from biolinkml.generators.rdfgen import RDFGenerator
from biolinkml.generators.shexgen import cli, ShExGenerator
from tests import source_yaml_path
from tests.test_scripts.clicktestcase import ClickTestCase
from tests.utils.dirutils import make_and_clear_directory


class GenShExTestCase(ClickTestCase):
    testdir = "genshex"
    click_ep = cli
    prog_name = "gen-shex"

    def test_help(self):
        self.do_test("--help", 'help')

    def test_meta(self):
        """ Generate various forms of the metamodel in ShEx """
        self.maxDiff = None
        self.do_test(source_yaml_path + ' -f json -C', 'metashex.json')
        self.do_test(source_yaml_path + ' -f rdf', 'metashex.ttl')
        self.do_test(source_yaml_path, 'metashex.shex')
        self.do_test(source_yaml_path + ' -f shex', 'metashex.shex')
        self.do_test(source_yaml_path + f' -f xsv', 'meta_error', error=click.exceptions.BadParameter)
        self.do_test(source_yaml_path + ' -f json -c', 'metashexnc.json')
        self.do_test(source_yaml_path + ' -f rdf -c', 'metashexnc.ttl')
        self.do_test(source_yaml_path + ' -c', 'metashexnc.shex')

    def test_meta_rdf(self):
        """ Generate ShEx and RDF for the model and verify that the RDF represents a valid instance """
        make_and_clear_directory(self.tmpdir_path)
        test_dir = os.path.join(self.tmpdir_path, 'meta_conformance_test')
        make_and_clear_directory(test_dir)
        context_file = os.path.join(test_dir, 'meta.jsonld')
        ContextGenerator(source_yaml_path).serialize(output=context_file)

        rdf_file = os.path.join(test_dir, 'meta.ttl')
        RDFGenerator(source_yaml_path).serialize(output=rdf_file, context=context_file)
        self.assertTrue(os.path.exists(rdf_file))

        shex_file = os.path.join(test_dir, 'meta.shex')
        ShExGenerator(source_yaml_path).serialize(output=shex_file, collections=False)
        self.assertTrue(os.path.exists(shex_file))

        g = CFGraph()
        g.load(rdf_file, format='ttl')
        focus = METAMODEL_URI
        start = METAMODEL_NAMESPACE.SchemaDefinition
        results = ShExEvaluator(g, shex_file, focus, start).evaluate()
        success = all(r.result for r in results)
        if not success:
            for r in results:
                if not r.result:
                    print(r.reason)
        else:
            make_and_clear_directory(test_dir)
        self.assertTrue(success)



if __name__ == '__main__':
    unittest.main()

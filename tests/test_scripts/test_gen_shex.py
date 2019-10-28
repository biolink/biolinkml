import os
import unittest

import click
from biolinkml import METAMODEL_NAMESPACE
from biolinkml.generators.jsonldcontextgen import ContextGenerator
from biolinkml.generators.jsonldgen import JSONLDGenerator
from biolinkml.generators.rdfgen import RDFGenerator
from biolinkml.generators.shexgen import cli, ShExGenerator
from pyshex import ShExEvaluator
from rdflib import Graph
from tests import source_yaml_path, DO_SHEX_VALIDATION
from tests.test_scripts.clicktestcase import ClickTestCase
from tests.utils.dirutils import make_and_clear_directory
from tests.utils.generator_utils import BIOLINK_IMPORT_MAP


class GenShExTestCase(ClickTestCase):
    testdir = "genshex"
    click_ep = cli
    prog_name = "gen-shex"

    def test_help(self):
        self.do_test("--help", 'help')

    def test_meta(self):
        """ Generate various forms of the metamodel in ShEx """
        self.maxDiff = None
        self.do_test(source_yaml_path, 'metashex.shex')
        self.do_test(source_yaml_path + ' -f json', 'metashex.json')
        self.do_test(source_yaml_path + ' -f rdf', 'metashex.ttl')
        self.do_test(source_yaml_path + ' -f shex', 'metashex.shex')
        self.do_test(source_yaml_path + ' --metauris', 'metashexn.shex')
        self.do_test(source_yaml_path + ' -f json', 'metashex.json')
        self.do_test(source_yaml_path + ' -f rdf', 'metashex.ttl')
        self.do_test(source_yaml_path + ' -f shex', 'metashex.shex')
        self.do_test(source_yaml_path + f' -f xsv', 'meta_error', error=click.exceptions.BadParameter)

    def test_rdf_shex(self):
        """ Generate ShEx and RDF for the model and verify that the RDF represents a valid instance """
        test_dir = os.path.join(self.tmpdir_path, 'meta_conformance_test')
        make_and_clear_directory(self.tmpdir_path)
        make_and_clear_directory(test_dir)

        json_file = os.path.join(test_dir, 'meta.jsonld')
        json_str = JSONLDGenerator(source_yaml_path, importmap=BIOLINK_IMPORT_MAP).serialize()
        with open(json_file, 'w') as f:
            f.write(json_str)

        context_file = os.path.join(test_dir, 'metacontext.jsonld')
        ContextGenerator(source_yaml_path, importmap=BIOLINK_IMPORT_MAP).serialize(output=context_file)
        self.assertTrue(os.path.exists(context_file))

        rdf_file = os.path.join(test_dir, 'meta.ttl')
        RDFGenerator(source_yaml_path, importmap=BIOLINK_IMPORT_MAP).serialize(output=rdf_file, context=context_file)
        self.assertTrue(os.path.exists(rdf_file))

        shex_file = os.path.join(test_dir, 'meta.shex')
        ShExGenerator(source_yaml_path, importmap=BIOLINK_IMPORT_MAP).serialize(output=shex_file, collections=False)
        self.assertTrue(os.path.exists(shex_file))

        if DO_SHEX_VALIDATION:
            g = Graph()
            g.load(rdf_file, format='ttl')
            focus = METAMODEL_NAMESPACE.metamodel
            start = METAMODEL_NAMESPACE.SchemaDefinition
            results = ShExEvaluator(g, shex_file, focus, start).evaluate(debug=False)
            success = all(r.result for r in results)
            if not success:
                for r in results:
                    if not r.result:
                        print(r.reason)
            else:
                make_and_clear_directory(test_dir)
            self.assertTrue(success)
        else:
            print("*** ShEX validation step was skipped. Set: tests.__init__.DO_SHEX_VALIDATION to run it")

if __name__ == '__main__':
    unittest.main()

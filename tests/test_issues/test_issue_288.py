import os
import unittest

from rdflib import URIRef, Graph
from rdflib.namespace import OWL, RDFS, RDF

from biolinkml.generators.sqlddlgen import SQLDDLGenerator
from biolinkml.generators.yamlgen import YAMLGenerator
from biolinkml.generators.jsonschemagen import JsonSchemaGenerator
from biolinkml.utils.sqlutils import SqlTransformer
from tests.utils.compare_rdf import compare_rdf
from tests.utils.test_environment import TestEnvironmentTestCase
from biolinkml.utils.yamlutils import as_yaml
from tests.test_issues.environment import env


class IssueSQLGenTestCase(TestEnvironmentTestCase):
    env = env

    def test_transform(self):
        """
        tests a schema->schema transform

        this does not output SQL - instead it outputs a 'sql-ready' transformed
        version of the schema, with multivalued keys transformed and inheritance
        flattened

        :return:
        """
        yaml_fname = env.input_path('issue_288.yaml')
        gen = YAMLGenerator(yaml_fname, mergeimports=False)
        tr = SqlTransformer()
        tr.transform_schema(gen.schema)
        gen2 = YAMLGenerator(tr.target_schema)
        s = gen2.serialize()
        print(s)

    def test_transform_and_generate(self):
        """
        tests full cycle of transformation and sql ddl gen
        :return:
        """
        yaml_fname = env.input_path('issue_288.yaml')
        gen = YAMLGenerator(yaml_fname, mergeimports=False)
        #print(jsgen.serialize())
        tr = SqlTransformer()
        tr.transform_schema(gen.schema)
        ddlgen = SQLDDLGenerator(tr.target_schema)
        #gen2 = YAMLGenerator(tr.target_schema)
        s = ddlgen.serialize()
        print(s)


if __name__ == '__main__':
    unittest.main()

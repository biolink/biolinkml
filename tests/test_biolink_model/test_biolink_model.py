import os
import re
import unittest
from typing import Optional, Callable

from biolinkml.generators.csvgen import CsvGenerator
from biolinkml.generators.dotgen import DotGenerator
from biolinkml.generators.golrgen import GolrSchemaGenerator
from biolinkml.generators.graphqlgen import GraphqlGenerator
from biolinkml.generators.jsonldcontextgen import ContextGenerator
from biolinkml.generators.jsonldgen import JSONLDGenerator
from biolinkml.generators.jsonschemagen import JsonSchemaGenerator
from biolinkml.generators.markdowngen import MarkdownGenerator
from biolinkml.generators.owlgen import OwlSchemaGenerator
from biolinkml.generators.protogen import ProtoGenerator
from biolinkml.generators.pythongen import PythonGenerator
from biolinkml.generators.rdfgen import RDFGenerator
from biolinkml.generators.shexgen import ShExGenerator
from biolinkml.utils.generator import Generator
from tests.test_scripts.clicktestcase import ClickTestCase, metadata_filter
from tests.utils.compare_directories import are_dir_trees_equal
from tests.utils.dirutils import make_and_clear_directory


class CurrentBiolinkModelTestCase(unittest.TestCase):
    cwd = os.path.abspath(os.path.dirname(__file__))

    source_path = os.path.join(cwd, 'source')
    target_path = os.path.join(cwd, 'target')
    biolink_model_path = os.path.join(cwd, 'yaml', 'biolink-model.yaml')

    def single_file_generator(self, suffix: str, gen: type(Generator), gen_args: Optional[dict] = None,
                              serialize_args: Optional[dict] = None,
                              filtr: Optional[Callable[[str], str]] = None) -> None:
        """

        :param suffix: File suffix (without '.')
        :param gen: Generator to use
        :param gen_args: Arguments to generator
        :param serialize_args: Arguments to serializer
        :param filtr: Filter to remove metadata specific info from the file
        :return:
        """
        if gen_args is None:
            gen_args = {}
        if serialize_args is None:
            serialize_args = {}
        if filtr is None:
            def filtr(s): return s
        old_file = os.path.join(self.source_path, 'biolink_model.' + suffix)
        new_file = os.path.join(self.target_path, 'biolink_model.' + suffix)
        if os.path.exists(new_file):
            os.remove(new_file)
        new_data = filtr(str(gen(self.biolink_model_path, **gen_args).serialize(**serialize_args)))

        if not os.path.exists(old_file):
            with open(old_file, 'w') as oldf:
                oldf.write(new_data)
            self.assertTrue(False, f"Created {old_file} - run again")

        # Note: we assume old file (source) is pre-filtered.  This prevents unnecessary git updates
        with open(old_file) as oldf:
            old_data = oldf.read()
        self.maxDiff = None
        if old_data != new_data:
            with open(new_file, 'w') as newf:
                newf.write(new_data)
            print(ClickTestCase.closein_comparison(old_data, new_data))
            self.assertEqual(old_data, new_data)

    def directory_generator(self, dirname: str, gen: type(Generator), gen_args: Optional[dict] = None,
                            serialize_args: Optional[dict] = None):
        if gen_args is None:
            gen_args = {}
        if serialize_args is None:
            serialize_args = {}

        source_dir = os.path.join(self.source_path, dirname)
        if not os.path.exists(source_dir):
            make_and_clear_directory(source_dir)
            target_dir = source_dir
        else:
            target_dir = os.path.join(self.target_path, dirname)
            make_and_clear_directory(target_dir)
        gen(self.biolink_model_path, **gen_args).serialize(directory=target_dir, **serialize_args)
        if source_dir == target_dir:
            self.assertTrue(False, f"{dirname} created - rerun test")

        diffs = are_dir_trees_equal(target_dir, source_dir)
        if diffs:
            print(diffs)
            self.assertTrue(False, f"{dirname} mismatch")
        make_and_clear_directory(target_dir)

    def test_biolink_python(self):
        """ Test the python generator for the biolink model """
        self.single_file_generator('py', PythonGenerator, {'emit_metadata': True}, filtr=metadata_filter)

    def test_biolink_markdown(self):
        """ Test the markdown generator for the biolink model """
        self.directory_generator('markdown', MarkdownGenerator)

    def test_biolink_tsv(self):
        """ Test the tsv generator for the biolink model """
        def filtr(s: str) -> str:
            return s.replace('\r\n', '\n')
        self.single_file_generator('tsv', CsvGenerator, {'fmt':'tsv'}, filtr=filtr)

    def test_biolink_graphviz(self):
        """ Test the dotty generator for the biolink model """
        self.directory_generator('graphviz', DotGenerator)

    def test_biolink_golr(self):
        """ Test the golr schema generator for the biolink model """
        self.directory_generator('golr', GolrSchemaGenerator)

    def test_biolink_graphql(self):
        """ Test the graphql schema generator for the biolink model """
        self.single_file_generator('graphql', GraphqlGenerator)

    def test_biolink_jsonld(self):
        """ Test the jsonld schema generator for the biolink model """
        def filtr(s: str) -> str:
            return re.sub(r'"generation_date": ".*?",', '"generation_date": "2019-01-01 12:00",', s)
        self.single_file_generator('jsonld', JSONLDGenerator, filtr=filtr)

    def test_biolink_context(self):
        """ Test the jsonld context generator for the biolink model """
        def filtr(s: str) -> str:
            return re.sub(r'Generation date: .*?\\n', r'Generation date: \\n',
                          re.sub(r' version: .*?\\n', r' version: \\n', s))
        self.single_file_generator('context.jsonld', ContextGenerator, filtr=filtr)

    def test_biolink_json_schema(self):
        """ Test the jsonld context generator for the biolink model """
        self.single_file_generator('json.schema', JsonSchemaGenerator)

    def test_biolink_owl_schema(self):
        """ Test the owl schema generator for the biolink model """
        self.single_file_generator('owl', OwlSchemaGenerator)

    def test_biolink_proto(self):
        """ Test the proto schema generator for the biolink model """
        self.single_file_generator('proto', ProtoGenerator)

    def test_biolink_rdf(self):
        """ Test the rdf generator for the biolink model """
        # Generate a local context because we may be changing
        context_file = os.path.join(self.target_path, 'biolink_model.rdf.context.jsonld')
        ContextGenerator(self.biolink_model_path).serialize(output=context_file)
        self.assertTrue(os.path.exists(context_file))
        self.single_file_generator('ttl', RDFGenerator, serialize_args={"context": context_file})
        os.remove(context_file)

    def test_biolink_shex(self):
        """ Test the shex generator for the biolink model """
        self.single_file_generator('shex', ShExGenerator)

    # def test_rdf_shex(self):
    #     """ Generate ShEx and RDF for the model and verify that the RDF represents a valid instance """
    #     test_dir = os.path.join(self.target_path, 'rdf_shex')
    #     make_and_clear_directory(test_dir)
    #
    #     json_file = os.path.join(test_dir, 'meta.jsonld')
    #     json_str = JSONLDGenerator(self.biolink_model_path).serialize()
    #     with open(json_file, 'w') as f:
    #         f.write(json_str)
    #
    #     context_file = os.path.join(test_dir, 'metacontext.jsonld')
    #     ContextGenerator(self.biolink_model_path).serialize(output=context_file)
    #     self.assertTrue(os.path.exists(context_file))
    #
    #     rdf_file = os.path.join(test_dir, 'meta.ttl')
    #     RDFGenerator(self.biolink_model_path).serialize(output=rdf_file, context=context_file)
    #     self.assertTrue(os.path.exists(rdf_file))
    #
    #     shex_file = os.path.join(test_dir, 'meta.shex')
    #     ShExGenerator(self.biolink_model_path).serialize(output=shex_file, collections=False)
    #     self.assertTrue(os.path.exists(shex_file))
    #
    #     g = Graph()
    #     g.load(rdf_file, format='ttl')
    #     focus = METAMODEL_NAMESPACE.metamodel
    #     start = METAMODEL_NAMESPACE.SchemaDefinition
    #     results = ShExEvaluator(g, shex_file, focus, start).evaluate(debug=False)
    #     success = all(r.result for r in results)
    #     if not success:
    #         for r in results:
    #             if not r.result:
    #                 print(r.reason)
    #     else:
    #         make_and_clear_directory(test_dir)
    #     self.assertTrue(success)


if __name__ == '__main__':
    unittest.main()

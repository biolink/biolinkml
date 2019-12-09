import os
import unittest
from types import ModuleType

from jsonasobj import as_json

from biolinkml.generators.jsonldcontextgen import ContextGenerator
from biolinkml.generators.markdowngen import MarkdownGenerator
from biolinkml.generators.pythongen import PythonGenerator
from biolinkml.utils.yamlutils import as_rdf
from tests.test_issues import sourcedir, outputdir
from tests.utils.dirutils import make_and_clear_directory


class Issue80TestCase(unittest.TestCase):

    def test_issue_80(self):
        """ Make sure that types are generated as part of the output """
        yaml_fname = os.path.join(sourcedir, 'issue_80.yaml')
        python = PythonGenerator(yaml_fname).serialize()
        spec = compile(python, 'test', 'exec')
        module = ModuleType('test')
        exec(spec, module.__dict__)
        example = module.Person("http://example.org/person/17", "Fred Jones", 43)

        # JSON Representation
        print(as_json(example))

        # Generate a context for this particular model
        context = ContextGenerator(yaml_fname).serialize()
        print(context)

        # RDF Representation
        print(as_rdf(example, contexts=context).serialize(format="turtle").decode())


if __name__ == '__main__':
    unittest.main()

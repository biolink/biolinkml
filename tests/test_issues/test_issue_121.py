import os
import unittest
from types import ModuleType

from jsonasobj import as_json

from biolinkml.generators.jsonldcontextgen import ContextGenerator
from biolinkml.generators.pythongen import PythonGenerator
from biolinkml.utils.yamlutils import as_rdf
from tests.test_issues import sourcedir


class Issue121TestCase(unittest.TestCase):

    def header(self, txt: str) -> str:
        return '\n' + ("=" * 20) + f" {txt} " + ("=" * 20)

    def test_issue_121(self):
        """ Make sure that types are generated as part of the output """
        yaml_fname = os.path.join(sourcedir, 'issue_113.yaml')
        python = PythonGenerator(yaml_fname).serialize()
        print(self.header("Python"))
        print(python)

        has_includes = False
        for line in python.split("\n"):
            if line.startswith("from includes.types"):
                assert line == "from includes.types import String"
                has_includes = True
        assert has_includes

        spec = compile(python, 'test', 'exec')
        module = ModuleType('test')
        exec(spec, module.__dict__)
        example = module.TestClass(test_attribute_2="foo")
        assert hasattr(example, "test_attribute_2")
        assert hasattr(example, "test_attribute_1")
        example.wiible = "foo";
        example.test_attribute_1 = "foo";
        example.test_attribute_2 = "foo";

        # JSON Representation
        print(self.header("JSON"))
        print(as_json(example))


if __name__ == '__main__':
    unittest.main()

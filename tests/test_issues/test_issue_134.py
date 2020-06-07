import os
import unittest
import json
from types import ModuleType

from biolinkml.generators.pythongen import PythonGenerator
from tests.test_issues import sourcedir


class IssuePythonOrderingTestCase(unittest.TestCase):

    def header(self, txt: str) -> str:
        return '\n' + ("=" * 20) + f" {txt} " + ("=" * 20)

    def test_issue_python_ordering(self):
        """ Make sure that types are generated as part of the output """
        yaml_fname = os.path.join(sourcedir, 'issue_134.yaml')
        gen = PythonGenerator(yaml_fname)
        py = gen.serialize()
        print(self.header("Py"))
        print(py)
        spec = compile(py, 'test', 'exec')
        module = ModuleType('test')
        exec(spec, module.__dict__)
        e = module.E('id:1')
        b = module.B('id:2')
        e.has_b = b


if __name__ == '__main__':
    unittest.main()

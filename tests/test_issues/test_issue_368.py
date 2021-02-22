import os
import unittest

from jsonasobj import as_json

from biolinkml.generators.pythongen import PythonGenerator
from tests.test_issues.environment import env
from tests.utils.python_comparator import compare_python, compile_python
from tests.utils.test_environment import TestEnvironmentTestCase


class Issue368TestCase(TestEnvironmentTestCase):
    env = env

    def header(self, txt: str) -> str:
        return '\n' + ("=" * 20) + f" {txt} " + ("=" * 20)

    def test_issue_368(self):
        """ Make sure that types are generated as part of the output """
        env.generate_single_file('issues_368_imports.py',
                                lambda: PythonGenerator(env.input_path('issues_368_imports.yaml'),
                                                     mergeimports=False).serialize(),
                                comparator=lambda exp, act: compare_python(exp, act, self.env.expected_path('issues_368_imports.py')),
                                value_is_returned=True)
        env.generate_single_file('issue_368.py',
                                 lambda: PythonGenerator(env.input_path('issue_368.yaml'),
                                                         mergeimports=False).serialize(),
                                 comparator=lambda exp, act: compare_python(exp, act, self.env.expected_path('issue_368.py')),
                                 value_is_returned=True)
        with open(env.expected_path('issue_368.py')) as f:
            python= f.read()

        has_imports = False
        for line in python.split("\n"):
            if line.startswith("from . issues_368_imports"):
                imps = line.replace("from . issues_368_imports import ","").split(", ")
                assert 'E' in imps
                assert 'ParentClass' in imps
                has_imports = True
        assert has_imports
        module = compile_python(env.expected_path('issue_368.py'))

        enum_inst = module.E("a") # EnumInstanceImpl
        example = module.C(s="a")
        assert hasattr(example, "s")
        assert example.s.code.text == enum_inst.code.text
        assert str(example.s) == "a: A"
        def output_generator(dirname) -> None:
            with open(os.path.join(dirname, 'issue_368_1.json'), 'w') as f:
                f.write(as_json(example))

        # TODO: fix this
        # env.generate_directory('issue_368', lambda dirname: output_generator(dirname))


if __name__ == '__main__':
    unittest.main()

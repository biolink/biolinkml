import unittest
from types import ModuleType

import click


from biolinkml.generators import pythongen
from tests.test_scripts.environment import env
from tests.utils.clicktestcase import ClickTestCase
from tests.utils.filters import metadata_filter


class GenPythonTestCase(ClickTestCase):
    testdir = "genpython"
    click_ep = pythongen.cli
    prog_name = "gen-python"
    env = env

    def gen_and_comp_python(self, base: str) -> None:
        """ Generate yaml_file into python_file and compare it against master_file  """
        yaml_file = base + '.yaml'
        python_file = base + '.py'
        yaml_path = self.source_file_path(yaml_file)
        target_path = self.expected_file_path(python_file)

        self.do_test([yaml_path, '--no-head'], python_file, add_yaml=False)

        # Make sure the python is valid
        with open(target_path) as pyf:
            pydata = pyf.read()
            spec = compile(pydata, 'test', 'exec')
            module = ModuleType('test')
            exec(spec, module.__dict__)

    def test_help(self):
        self.do_test("--help", 'help')

    def test_meta(self):
        self.maxDiff = None
        self.do_test([], 'meta.py', filtr=metadata_filter)
        self.do_test('-f py', 'meta.py', filtr=metadata_filter)
        self.do_test('-f xsv', 'meta_error', expected_error=click.exceptions.BadParameter)

    def test_head(self):
        """ Validate the head/nohead parameter """
        yaml = '''id: "https://w3id.org/biolink/metamodel"
description: Metamodel for biolink schema
license: https://creativecommons.org/publicdomain/zero/1.0/
version: 0.4.0
default_range: string
prefixes:
    xsd: http://www.w3.org/2001/XMLSchema#
types:
   string:
      base: str
      uri: xsd:string'''
        output = pythongen.PythonGenerator(yaml, "py", emit_metadata=True).serialize()
        self.assertTrue(output.startswith(f'# Auto generated from None by pythongen.py version: '
                                          f'{pythongen.PythonGenerator.generatorversion}'))
        output = pythongen.PythonGenerator(yaml, "py", emit_metadata=False).serialize()
        self.assertTrue(output.startswith('\n# id: https://w3id.org/biolink/metamodel'))

    def test_multi_id(self):
        """ Test the multi-identifier error """
        self.gen_and_comp_python('multi_id')

    @unittest.skipIf(True, "See https://github.com/biolink/biolinkml/issues/141")
    def test_timepoint(self):
        """ Test an issue with the biolink-model timepoint rendering """
        self.gen_and_comp_python('timepoint')

    def test_type_inheritence(self):
        """ Make sure that typeof's get represented correctly """
        self.gen_and_comp_python('testtypes')

    def test_inherited_identifiers(self):
        self.gen_and_comp_python('inheritedid')

    # This still needs to be fixed
    @unittest.skipIf(False, "This used to fail consistently - may want to find out what happened")
    def test_ordering(self):
        self.gen_and_comp_python('ordering')

    def test_default_namespace(self):
        """ Test that curie_for replaces '@default' with a blank """
        self.gen_and_comp_python('default_namespace')


if __name__ == '__main__':
    unittest.main()

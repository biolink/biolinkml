import os
import unittest

# This has to occur post ClickTestCase
from types import ModuleType

import click


from biolinkml.generators.pythongen import cli, PythonGenerator
from tests import sourcedir, targetdir, source_yaml_path
from tests.test_scripts.clicktestcase import ClickTestCase
from tests.utils.metadata_filters import metadata_filter


class GenPythonTestCase(ClickTestCase):
    testdir = "genpython"
    click_ep = cli
    prog_name = "gen-py-classes"

    def gen_and_comp_python(self, base: str) -> None:
        """ Generate yaml_file into python_file and compare it against master_file  """
        yaml_path = os.path.abspath(os.path.join(sourcedir, f"{base}.yaml"))
        target_path = os.path.join(targetdir, f'{base}.py')
        master_path = os.path.join(sourcedir, f'{base}.py')

        pydata = str(PythonGenerator(yaml_path, "py", emit_metadata=False).serialize())
        newdat = metadata_filter(pydata)

        # If the master for comparison doesn't exist, create it
        if not os.path.exists(master_path):
            with open(master_path, 'w') as mf:
                mf.write(newdat)
            self.assertFalse(True, f"Regenerated {os.path.basename(master_path)} - rerun to complete test")

        # Compare the current master with what we've generated
        with open(master_path) as oldf:
            olddat = oldf.read()
        if olddat != newdat:
            # Save the old if we're different
            with open(target_path, 'w') as newf:
                newf.write(pydata)
            self.maxDiff = None
            if olddat != newdat:
                print(f"Data file: {master_path}")
            self.assertEqual(olddat, newdat)

        # Make sure the python is valid
        spec = compile(pydata, 'test', 'exec')
        module = ModuleType('test')
        exec(spec, module.__dict__)

        if os.path.exists(target_path):
            os.remove(target_path)

    def test_help(self):
        self.do_test("--help", 'help')

    def test_meta(self):
        self.maxDiff = None
        self.do_test(source_yaml_path, 'meta.py', filtr=metadata_filter)
        self.do_test(source_yaml_path + ' -f py', 'meta.py', filtr=metadata_filter)
        self.do_test(source_yaml_path + ' -f xsv', 'meta_error', error=click.exceptions.BadParameter)

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
        output = PythonGenerator(yaml, "py", emit_metadata=True).serialize()
        self.assertTrue(output.startswith(f'# Auto generated from None by pythongen.py version: '
                                          f'{PythonGenerator.generatorversion}'))
        output = PythonGenerator(yaml, "py", emit_metadata=False).serialize()
        self.assertTrue(output.startswith('\n# id: https://w3id.org/biolink/metamodel'))

    def test_multi_id(self):
        """ Test the multi-identifier error """
        self.gen_and_comp_python('multi_id')

    def test_timepoint(self):
        """ Test an issue with the biolink-model timepoint rendering """
        self.gen_and_comp_python('timepoint')

    def test_type_inheritence(self):
        """ Make sure that typeof's get represented correctly """
        self.gen_and_comp_python('testtypes')

    def test_inherited_identifiers(self):
        self.gen_and_comp_python('inheritedid')

    # This still needs to be fixed
    @unittest.expectedFailure
    def test_ordering(self):
        self.gen_and_comp_python('ordering')

    def test_default_namespace(self):
        """ Test that curie_for replaces '@default' with a blank """
        self.gen_and_comp_python('default_namespace')


if __name__ == '__main__':
    unittest.main()

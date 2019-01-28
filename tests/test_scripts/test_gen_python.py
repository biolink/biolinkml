import os
import unittest

# This has to occur post ClickTestCase
import click


from biolinkml.generators.pythongen import cli, PythonGenerator
from tests import sourcedir, targetdir, source_yaml_path
from tests.test_scripts.clicktestcase import ClickTestCase, metadata_filter


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
        with open(target_path, 'w') as pyfile:
            pyfile.write(pydata)

        if not os.path.exists(master_path):
            with open(master_path, 'w') as mf:
                mf.write(pydata)
            self.assertFalse(True, f"Regenerated {os.path.basename(master_path)} - rerun to complete test")

        with open(target_path) as newf:
            newdat = metadata_filter(newf.read())
            with open(master_path) as oldf:
                olddat = metadata_filter(oldf.read())
                self.maxDiff = None
        self.assertEqual(olddat, newdat)

    def test_help(self):
        self.do_test("--help", 'help')

    def test_meta(self):
        self.maxDiff = None
        self.do_test(source_yaml_path, 'meta.py', filtr=metadata_filter)
        self.do_test(source_yaml_path + ' -f py', 'meta.py', filtr=metadata_filter)
        self.do_test(source_yaml_path + ' -f xsv', 'meta_error', error=click.exceptions.BadParameter)

    def test_head(self):
        """ Validate the head/nohead parameter """
        yaml = '''id: "http://w3id.org/biolink/metamodel"
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
        self.assertTrue(output.startswith('\n# id: http://w3id.org/biolink/metamodel'))

    def test_multi_id(self):
        """ Test the multi-identifier error """
        self.gen_and_comp_python('multi_id')

    def test_timepoint(self):
        """ Test an issue with the biolink-model timepoint rendering """
        self.gen_and_comp_python('timepoint')

    def test_type_inheritence(self):
        """ Make sure that typeof's get represented correctly """
        self.gen_and_comp_python('testtypes')


if __name__ == '__main__':
    unittest.main()

import os
import unittest

from biolinkml.generators.pythongen import PythonGenerator
from biolinkml.generators.shexgen import ShExGenerator
from tests.test_issues import sourcedir, outputdir

expected_shex = """BASE <http://example.com/>
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX xsd: <http://www.w3.org/2001/XMLSchema#>


<String> xsd:string

<TestClass1> CLOSED {
    (  $<TestClass1_tes> (  <optional_mixin_slot> @<String> ? ;
          <required_mixin_slot> @<String>
       ) ;
       rdf:type [ <TestClass1> ]
    )
}

<TestClass2> CLOSED {
    (  $<TestClass2_tes> (  <optional_mixin_slot> @<String> ? ;
          <required_mixin_slot> @<String>
       ) ;
       rdf:type [ <TestClass2> ]
    )
}

<TestClass3> CLOSED {
    (  $<TestClass3_tes> (  <optional_domain_slot> @<String> ? ;
          <required_domain_slot> @<String>
       ) ;
       rdf:type [ <TestClass3> ]
    )
}
"""


class MultipleDomainTestCase(unittest.TestCase):
    def test_multiple_domains(self):
        """ Test multiple domains for the same slot """

        yaml_fname = os.path.join(sourcedir, 'issue_50.yaml')
        shex = ShExGenerator(yaml_fname, format='shex').serialize()
        self.assertEqual(expected_shex.strip(), shex.strip())
        python = PythonGenerator(yaml_fname).serialize()

        outfile = os.path.join(outputdir, 'issue_50.py')
        if not os.path.exists(outfile):
            with open(outfile, 'w') as f:
                f.write(python)
            self.fail(f"Writing {outfile} - rerun test")
        else:
            with open(outfile) as f:
                old_python = f.read()
        self.assertEqual(old_python, python, "Remove {outfile} to update target")


if __name__ == '__main__':
    unittest.main()

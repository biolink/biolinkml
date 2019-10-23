import os
import unittest

from biolinkml.generators.pythongen import PythonGenerator
from tests.test_issues import sourcedir, outputdir


class Issue44UnitTest(unittest.TestCase):
    def test_multiple_postinit(self):
        """ Generate postinit code for a multi-occurring element """
        python = PythonGenerator(os.path.join(sourcedir, 'issue_44.yaml'), emit_metadata=False).serialize()
        os.makedirs(outputdir, exist_ok=True)
        outfile = os.path.join(outputdir, 'issue_44.py')
        if not os.path.exists(outfile):
            with open(outfile, 'w') as f:
                f.write(python)
            self.fail(f"Writing {outfile} - rerun test")
        else:
            with open(outfile) as f:
                old_python = f.read()
        self.assertEqual(old_python, python, f"Remove {outfile} to update target")


if __name__ == '__main__':
    unittest.main()

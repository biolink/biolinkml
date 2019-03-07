import os
import unittest
from contextlib import redirect_stdout
from io import StringIO

from tests.test_notebooks import output_directory


class ExamplesTestCase(unittest.TestCase):
    def test_notebook(self):
        output = StringIO()
        output_file = os.path.join(output_directory, 'examples.txt')
        with redirect_stdout(output):
            import tests.test_notebooks.examples
        with open(output_file, 'w') as f:
            f.write(output.getvalue())
        print(f"Output written to {output_file}")



if __name__ == '__main__':
    unittest.main()

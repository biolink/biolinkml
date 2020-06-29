import unittest


class MyTestCase(unittest.TestCase):
    def test_something(self):
        print('File "/Users/solbrig/git/biolink/biolinkml/tests/test_b.py", line 6, in test_something')
        self.assertEqual(True, False)


if __name__ == '__main__':
    unittest.main()

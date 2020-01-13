import unittest
from dataclasses import dataclass, InitVar, field, fields
from typing import Optional, ClassVar, Dict, Any


class Issue83TestCase(unittest.TestCase):
    # The goal is to provide line numbers on error messages.   We've tweaked the parser so that it returns augmented
    # str's and int's with the line numbers on them.  The problem we are trying to address now is that the dataclass
    # constructor doesn't support **argv out of the box.  We can certainly tweak the generator to emit the __init__
    # method to do this, but it would be really handy


    @dataclass
    class FesterBesterTester:
        cv: ClassVar[int] = 42

        a: Optional[int] = 0
        b: Optional[str] = None

        def __init__(self, a: Optional[int] = 0, b: Optional[str] = None, **kwargs):
            self.a = a
            self.b = b
            if kwargs:
                argnames = ', '.join(list(kwargs.keys()))
                print(f"Unexpected arguments: {argnames}")

    def test_initvar(self):
        t = Issue83TestCase.FesterBesterTester(a=12, b="Sell", c="buy")
        t = Issue83TestCase.FesterBesterTester()
        print(t)
        self.assertEqual(True, False)


if __name__ == '__main__':
    unittest.main()

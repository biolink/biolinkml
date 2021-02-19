from typing import Callable

from tests.utils.test_environment import TestEnvironment, TestEnvironmentTestCase


class LDTestCase(TestEnvironmentTestCase):
    env = TestEnvironment(__file__)

    def dump_test(self, filename: str,  dumper: Callable[[str], None], comparator: Callable[[str], str] = None)\
            -> bool:
        """
        Invoke the dumper passing it the output file name and then compare the result to an expected output
        :param filename: non-pathed file name to dump to and test
        :param dumper: when called with pathed file name, creates the output
        :param comparator: content comparator
        :returns: Success indicator
        """
        actual_file = self.env.actual_path(filename)
        expected_file = self.env.expected_path(filename.replace('.', '_d.'))

        dumper(actual_file)

        with open(actual_file) as actual_f:
            actual = actual_f.read()
        return self.env.eval_single_file(expected_file, actual, comparator=comparator)

    def dumps_test(self, filename: str, dumper: Callable[[], str], comparator: Callable[[], str] = None)\
            -> bool:
        """
        Invoke the string dumper and evaluate the results
        :param filename: filename to test
        :param dumper: function that produces
        :param comparator: content comparator
        """
        actual = dumper()
        expected_file = self.env.expected_path(filename.replace('.', '_ds.'))

        return self.env.eval_single_file(expected_file, actual, comparator=comparator)

import contextlib
import os
import shutil
from enum import Enum
from io import StringIO
from typing import Optional, Callable

import click

from tests.utils.compare_directories import are_dir_trees_equal
from tests.utils.mismatchlog import MismatchLog


class CLIExitException(Exception):
    ...


def no_click_exit(_self, _code=0):
    raise CLIExitException()


click.core.Context.exit = no_click_exit


class MismatchAction(Enum):
    Ignore = 0
    Report = 1
    Fail = 2


class TestEnvironment:
    """ Output testing environment """
    def __init__(self, filedir: str) -> None:
        self.cwd = os.path.dirname(filedir)
        self.indir = os.path.join(self.cwd, 'input')
        self.outdir = os.path.join(self.cwd, 'output')
        self.tempdir = os.path.join(self.cwd, 'temp')
        self._log = MismatchLog()
        self.mismatch_action = MismatchAction.Report

    def clear(self) -> None:
        self._log = MismatchLog()

    def input_path(self, *path: str) -> str:
        return os.path.join(self.indir, *path)

    def expected_path(self, *path: str) -> str:
        return os.path.join(self.outdir, *path)

    def actual_path(self, *path: str) -> str:
        return os.path.join(self.tempdir, *path)

    def temp_file_path(self, *path: str) -> str:
        return self.actual_path(*path)

    def __str__(self):
        return '\n\n'.join([str(e) for e in self._log.entries])

    def make_temp_dir(self, *paths: str) -> str:
        full_path = self.tempdir
        TestEnvironment.make_testing_directory(full_path)
        for p in paths:
            full_path = os.path.join(full_path, p)
            TestEnvironment.make_testing_directory(full_path, clear=True)
        return full_path

    def string_comparator(self, expected: str, actual: str) -> Optional[str]:
        """
        Compare two strings w/ embedded line feeds
        :param expected:
        :param actual:
        :return: Error message if mismatch else None
        """
        if expected.replace('\r\n', '\n').strip() == actual.replace('\r\n', '\n').strip():
            return None
        else:
            verb = "will be" if self.mismatch_action == MismatchAction.Fail else "was"
            return f"Output {verb} changed."

    @staticmethod
    def remove_testing_directory(directory: str) -> None:
        shutil.rmtree(directory, ignore_errors=True)


    @staticmethod
    def make_testing_directory(directory: str, clear: bool = False) -> None:
        """
        Create directory if necessary and clear it if requested
        :param directory: Directory to create
        :param clear: True means remove everything there
        """
        if clear or not os.path.exists(directory):
            safety_file = os.path.join(directory, "generated")
            if os.path.exists(directory):
                if not os.path.exists(safety_file):
                    raise FileNotFoundError(f"'generated' guard file not found in {directory}")
                shutil.rmtree(directory)
            os.makedirs(directory, exist_ok=True)
            with open(safety_file, "w") as f:
                f.write("Generated for safety.  Directory will not be cleared if this file is not present")

    def generate_directory(self, dirname: str, generator: Callable[[str], None]) -> None:
        """
        Invoke the generator and compare the output in a temp directory to the output directory.  Report the results
        and then update the output directory
        :param dirname: relative directory name (e.g. gengolr/meta)
        :param generator: function to create the output. First argument is the target directory
        """
        temp_output_directory = self.make_temp_dir(dirname)
        expected_output_directory = self.expected_path(dirname)
        self.make_testing_directory(expected_output_directory)

        generator(temp_output_directory)

        diffs = are_dir_trees_equal(expected_output_directory, temp_output_directory)
        if diffs:
            self._log.log(expected_output_directory, diffs)
            shutil.rmtree(expected_output_directory)
            os.rename(temp_output_directory, expected_output_directory)
        else:
            shutil.rmtree(temp_output_directory)

    def generate_single_file(self, filename: str, generator: Callable[[Optional[str]], Optional[str]],
                             direct_to_file: bool = False, filtr: Callable[[str], str] = None,
                             comparator: Callable[[str, str], str] = None) -> None:
        """
        Invoke the generator and compare the actual results to the expected.
        :param filename: relative file name (no path)
        :param generator: output generator. Either produces a string or creates a file
        :param direct_to_file: True means generator creates a file
        :param filtr: Optional filter to remove non-compare information (e.g. dates, specific paths, etc.)
        :param comparator: Optional output comparison function.
        """
        # If no filter, default to identity function
        if not filtr:
            filtr = lambda s: s

        actual_file = self.actual_path(filename)
        expected_file = self.expected_path(filename)
        verb = 'will be' if self.mismatch_action == MismatchAction.Fail else 'was'

        if direct_to_file:
            # If the output writes directly to a file, create a scratch file to writ it into
            os.makedirs(self.tempdir, exist_ok=True)
            with contextlib.suppress(FileNotFoundError):
                os.remove(actual_file)

            generator(actual_file)

            if os.path.exists(actual_file):
                with open(actual_file) as tmpf:
                    actual = filtr(tmpf.read())
                os.remove(actual_file)
            else:
                self._log.log(expected_file, f"No output {verb} generated")
                if self.mismatch_action != MismatchAction.Fail:
                    with contextlib.suppress(FileNotFoundError):
                        os.remove(expected_file)
        else:
            outf = StringIO()
            with contextlib.redirect_stdout(outf):
                try:
                    generator()
                except CLIExitException:
                    pass
            actual = filtr(outf.getvalue())

        # Determine whether there is any change
        if os.path.exists(expected_file):
            with open(expected_file) as expf:
                expected = filtr(expf.read())
            msg = comparator(expected, actual) if comparator else self.string_comparator(expected, actual)
        else:
            msg = f"New file {verb} created"
        if msg:
            self._log.log(expected_file, msg)
            if not self.mismatch_action == MismatchAction.Fail:
                with open(expected_file, 'w') as outf:
                    outf.write(actual)

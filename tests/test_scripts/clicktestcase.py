import os
import re
import shutil
import sys
import textwrap
import unittest
from contextlib import redirect_stdout
from io import StringIO
from typing import Union, List, Optional, Callable

# Make sure you import click from here rather than the root
import click
# Stop click from doing a sys.exit
from rdflib import Graph, Namespace
from rdflib.compare import to_isomorphic, graph_diff

from tests.utils.compare_directories import are_dir_trees_equal
from tests.utils.dirutils import make_and_clear_directory
from biolinkml import MODULE_DIR, METAMODEL_NAMESPACE


class CLIExitException(Exception):
    ...


def no_click_exit(_self, _code=0):
    raise CLIExitException()


click.core.Context.exit = no_click_exit


def metadata_filter(s: str) -> str:
    return re.sub(r'(# Auto generated from ).*(\.yaml by pythongen\.py version:) .*', r'\1\2',
                  re.sub(r'(# Generation date:) .*', r'\1', re.sub(r'\r\n', '\n', s)))


class ClickTestCase(unittest.TestCase):
    # The four variables below must be set by the inheriting class
    testdir: str = None
    click_ep = None
    prog_name: str = None

    soft_compare: Optional[str] = None
    test_base_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), 'output'))
    temp_base_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), 'temp'))

    @classmethod
    def setUpClass(cls):
        assert cls.testdir is not None, "Test directory must be defined"

        cls.testdir_path = os.path.join(cls.test_base_dir, cls.testdir)
        cls.tmpdir_path = os.path.join(cls.temp_base_dir, cls.testdir)
        if not os.path.exists(cls.testdir_path):
            print(f"Creating {cls.testdir_path}\n")
            make_and_clear_directory(cls.testdir_path)
        cls.creation_messages = []
        cls.keep_temp_directory = False

    @classmethod
    def tearDownClass(cls):
        if not cls.keep_temp_directory and os.path.exists(cls.tmpdir_path):
            make_and_clear_directory(cls.tmpdir_path)
            cls.keep_temp_directory = False
        if cls.creation_messages:
            for msg in cls.creation_messages:
                print(msg, file=sys.stderr)
            cls.creation_messages = []
            assert False, "Tests failed because baseline files were being created"

    @staticmethod
    def _print_triples(g: Graph):
        g.bind('meta', METAMODEL_NAMESPACE)
        g_text = re.sub(r'@prefix.*\n', '', g.serialize(format="turtle").decode())
        print(g_text)

    def n3_comparator(self, old_data: str, new_data: str) -> str:
        return self.compare_rdf(old_data, new_data, "n3")

    def rdf_comparator(self, old_data: str, new_data: str) -> str:
        return self.compare_rdf(old_data, new_data, "turtle")

    def compare_rdf(self, old_data: str, new_data: str, fmt: str) -> Optional[str]:
        old_graph = Graph()
        new_graph = Graph()
        old_graph.parse(data=old_data, format=fmt)
        new_graph.parse(data=new_data, format=fmt)
        old_iso = to_isomorphic(old_graph)
        # Remove the metadata specific triples
        for t in list(old_iso.triples((None, METAMODEL_NAMESPACE.generation_date, None))):
            old_iso.remove(t)
        new_iso = to_isomorphic(new_graph)
        for t in list(new_iso.triples((None, METAMODEL_NAMESPACE.generation_date, None))):
            new_iso.remove(t)
        # Graph compare takes a Looong time
        in_both, in_old, in_new = graph_diff(old_iso, new_iso)
        # if old_iso != new_iso:
        #     in_both, in_old, in_new = graph_diff(old_iso, new_iso)
        old_len = len(list(in_old))
        new_len = len(list(in_new))
        if old_len or new_len:
            txt = StringIO()
            with redirect_stdout(txt):
                if old_len:
                    print("----- Old graph only -----")
                    self._print_triples(in_old)
                if new_len:
                    print("----- New Grapn Only -----")
                    self._print_triples(in_new)
            return txt.getvalue()
        return None

    @staticmethod
    def closein_comparison(old_txt: str, new_txt: str) -> None:
        """ Assist with testing comparison -- zero in on the first difference in a big string

        @param old_txt:
        @param new_txt:
        """
        window = 30
        view = 120

        nw = nt = new_txt.strip()
        ow = ot = old_txt.strip()
        if ot != nt:
            offset = 0
            while nt and ot and nt[:window] == ot[:window]:
                offset += window
                nt = nt[window:]
                ot = ot[window:]
            offset = max(offset-view, 0)
            print("   - - EXPECTED - -")
            print(ow[offset:offset+view+view])
            print("\n   - - ACTUAL - -")
            print(nw[offset:offset+view+view])

    def do_test(self, args: Union[str, List[str]], testfile: Optional[str] = "", *, error: type(Exception) = None,
                filtr: Optional[Callable[[str], str]] = None, tox_wrap_fix: bool = False,
                bypass_soft_compare: bool = False, dirbase: Optional[str] = None,
                comparator: Callable[[type(unittest.TestCase), str, str, str], str] = None) -> None:
        """ Execute a command test

        @param args: Argument string or list to command
        @param testfile: name of file to record output in.  If absent, using directory mode
        @param error: If present, we expect this error
        @param filtr: Filter to remove date and app specific information from text
        @param tox_wrap_fix: tox seems to wrap redirected output at 60 columns.  If true, try wrapping the test
        file before failing
        @param bypass_soft_compare: True means not to use the class level soft compare
        @param dirbase: If present, compare tmpdir_path (new) to testdir_path(old)
        @param comparator: If present, use this method for comparison
        """
        new_directory = os.path.join(self.tmpdir_path, dirbase) if dirbase else None

        outf = StringIO()
        arg_list = args.split() if isinstance(args, str) else args
        if error:
            with self.assertRaises(error):
                self.click_ep(arg_list, standalone_mode=False)
            return

        with redirect_stdout(outf):
            try:
                self.click_ep(arg_list, prog_name=self.prog_name, standalone_mode=False)
            except CLIExitException:
                pass

        if not testfile:
            if dirbase:
                old_directory = os.path.join(self.testdir_path, dirbase)
                if os.path.exists(old_directory):
                    diffs = are_dir_trees_equal(old_directory, new_directory)
                    if diffs:
                        self.__class__.keep_temp_directory = True
                        print(diffs)
                        self.assertTrue(False)
                else:
                    shutil.copytree(new_directory, old_directory)
                    self.__class__.creation_messages.append(f"Directory: {old_directory} created")
            else:
                print("Directory comparison needs to be added", file=sys.stderr)
        else:
            testfile_path = os.path.join(self.testdir_path, testfile)
            new_txt = outf.getvalue().replace('\r\n', '\n').strip()
            if filtr:
                new_txt = filtr(new_txt)
            if not os.path.exists(testfile_path):
                with open(testfile_path, 'w') as f:
                    f.write(outf.getvalue())
                self.__class__.creation_messages.append(f"File: {testfile_path} created")
            else:
                with open(testfile_path) as f:
                    old_txt = f.read().replace('\r\n', '\n').strip()
                if filtr:
                    old_txt = filtr(old_txt)

                if old_txt != new_txt and not comparator and tox_wrap_fix:
                    old_txt = textwrap.fill(old_txt, 60)
                    new_txt = textwrap.fill(new_txt, 60)
                if comparator:
                    compare_text = comparator(self, old_txt, new_txt)
                else:
                    compare_text = None if old_txt == new_txt else ''

                # If necessary, update the test file
                if compare_text is not None:
                    print(f"\n***** Mismatch on: {os.path.relpath(testfile_path, MODULE_DIR)}. "
                          f"Remove file to refresh *****\n")
                    if self.soft_compare and not bypass_soft_compare:
                        print(f"{self.id()}: {self.soft_compare}")
                    elif not comparator:
                        if len(old_txt) > 10000:
                            print(self.closein_comparison(old_txt, new_txt))
                        self.maxDiff = None
                        self.assertEqual(old_txt, new_txt)
                    else:
                        print(compare_text)
                        self.assertFalse(True, "Mismatch")

    def temp_directory(self, base: str) -> str:
        """
        Create a temporary directory and return the path

        :param base:
        :return: directory
        """
        if not os.path.exists(self.tmpdir_path):
            make_and_clear_directory(self.tmpdir_path)
        new_directory = os.path.join(self.tmpdir_path, base)
        make_and_clear_directory(new_directory)
        return new_directory


if __name__ == '__main__':
    unittest.main()

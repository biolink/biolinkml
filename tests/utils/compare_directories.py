import filecmp
import os.path
from contextlib import redirect_stdout
from io import StringIO
from typing import Optional


def are_dir_trees_equal(dir1: str, dir2: str) -> Optional[str]:
    """
    Compare two directories recursively. Files in each directory are
    assumed to be equal if their names and contents are equal.

    @param dir1: First directory path
    @param dir2: Second directory path

    @return: None if directories match, else summary of differences
   """

    dirs_cmp = filecmp.dircmp(dir1, dir2)
    output = StringIO()
    if dirs_cmp.diff_files or dirs_cmp.funny_files or dirs_cmp.left_only or dirs_cmp.right_only or dirs_cmp.funny_files:
        with redirect_stdout(output):
            dirs_cmp.report_full_closure()
        return output.getvalue()
    return None

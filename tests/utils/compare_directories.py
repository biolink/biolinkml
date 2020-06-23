import filecmp
from contextlib import redirect_stdout
from io import StringIO
from typing import Optional, Callable


class dircmp(filecmp.dircmp):
    """
    Compare the content of dir1 and dir2. In contrast with filecmp.dircmp, this
    subclass compares the content of files with the same path.
    """
    def phase3(self):
        """
        Find out differences between common files.
        Ensure we are using content comparison with shallow=False.
        """
        fcomp = filecmp.cmpfiles(self.left, self.right, self.common_files,
                                 shallow=False)
        self.same_files, self.diff_files, self.funny_files = fcomp

    filecmp.dircmp.methodmap['same_files'] = phase3
    filecmp.dircmp.methodmap['diff_files'] = phase3
    filecmp.dircmp.methodmap['funny_files'] = phase3



def are_dir_trees_equal(dir1: str, dir2: str) -> Optional[str]:
    """
    Compare two directories recursively. Files in each directory are
    assumed to be equal if their names and contents are equal.

    @param dir1: First directory path
    @param dir2: Second directory path

    @return: None if directories match, else summary of differences
   """

    dirs_cmp = dircmp(dir1, dir2)
    output = StringIO()
    if dirs_cmp.diff_files or dirs_cmp.funny_files or dirs_cmp.left_only or dirs_cmp.right_only or dirs_cmp.funny_files:
        with redirect_stdout(output):
            dirs_cmp.report_full_closure()
        return output.getvalue()
    return None

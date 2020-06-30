import logging
# Global testing control variables


from tests.utils.test_environment import MismatchAction

# Parts of the ShEx validation still need some performance optimization
DO_SHEX_VALIDATION = False

# There are lots of warnings emitted by the generators. Default logging level
DEFAULT_LOG_LEVEL = logging.ERROR
DEFAULT_LOG_LEVEL_TEXT = 'ERROR'

# Sometimes it is convenient to bypass graphviz testing output
SKIP_GRAPHVIZ_VALIDATION = True

# Same for markdown
SKIP_MARKDOWN_VALIDATION = False

# Action on mismatch.  One of 'Ignore', 'Report' or 'Fail'
#  If 'Fail', the expected file will be saved in the appropriate temp directory
DEFAULT_MISMATCH_ACTION = MismatchAction.Report


# Exception for use in script testing.  Global to prevent redefinition
class CLIExitException(Exception):
    ...

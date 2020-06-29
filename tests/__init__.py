import logging
# Global testing control variables

# Parts of the ShEx validation still need some performance optimization
from tests.utils.test_environment import MismatchAction

DO_SHEX_VALIDATION = False

# Set this to True if you are making changes to the model itself.  Note, however, that it needs to be reset to False
# once the new types and/or meta elements have been submitted to the main repository
USE_LOCAL_IMPORT_MAP = False

# There are lots of warnings emitted by the generators. Default logging level
DEFAULT_LOG_LEVEL = logging.ERROR
DEFAULT_LOG_LEVEL_TEXT = 'ERROR'

# Sometimes it is convenient to bypass graphviz testing output
SKIP_GRAPHVIZ_VALIDATION = False

# Same for markedown
SKIP_MARKDOWN_VALIDATION = False

# Action on mismatch
DEFAULT_MISMATCH_ACTION = MismatchAction.Report


# Exception for use in script testing.  Global to prevent redefinition
class CLIExitException(Exception):
    ...



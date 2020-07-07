import logging
# Global testing control variables


from tests.utils.test_environment import MismatchAction

# There are lots of warnings emitted by the generators. Default logging level
DEFAULT_LOG_LEVEL = logging.ERROR
DEFAULT_LOG_LEVEL_TEXT = 'ERROR'

# Parts of the ShEx validation still need some performance optimization
SKIP_SHEX_VALIDATION = True
SKIP_SHEX_VALIDATION_REASON = "tests/__init__.py ShEx validation skipped: SKIP_SHEX_VALIDATION is True"

# Sometimes it is convenient to bypass graphviz testing output
# NOTE: This will remain disabled until it is determined whether GraphViz output is still needed
SKIP_GRAPHVIZ_VALIDATION = True
SKIP_GRAPHVIZ_VALIDATION_REASON = "tests/__init__.py GraphViz generation skipped SKIP_GRAPHVIZ_VALIDATION is True"

# Same for markdown
SKIP_MARKDOWN_VALIDATION = False
SKIP_MARKDOWN_VALIDATION_REASON = "tests/__init__.py Markdown generation SKIP_MARKDOWN_VALIDATION is True"

# Skip RDF comparison, as it takes a lot of time
SKIP_RDF_COMPARE = True
SKIP_RDF_COMPARE_REASON = "tests/__init__.py RDF output not checked SKIP_RDF_COMPARE is True"

# Skip Rewrite rules tests -- these only get re-tested when we change the w3id.org server
SKIP_REWRITE_RULES = True
SKIP_REWRITE_RULES_REASON = "tests/__init__.py SKIP_REWRITE_RULES is True"

# Action on mismatch.  One of 'Ignore', 'Report' or 'Fail'
#  If 'Fail', the expected file will be saved in the appropriate temp directory
#  NOTE: Before setting this back to Report or Ignore, you need to run cleartemp.sh in this directory
DEFAULT_MISMATCH_ACTION = MismatchAction.Report


# Exception for use in script testing.  Global to prevent redefinition
class CLIExitException(Exception):
    ...

import os

from biolinkml import LOCAL_METAMODEL_YAML_FILE, LOCAL_METAMODEL_LDCONTEXT_FILE, METAMODEL_FILE_NAME

refresh_files = False               # True means update target files
skip_biolink_model = True          # True means run unit tests against biolink models


testdir = os.path.abspath(os.path.dirname(__file__))
sourcedir = os.path.join(testdir, 'source')
targetdir = os.path.join(testdir, 'target')
source_yaml_path = LOCAL_METAMODEL_YAML_FILE
target_yaml_path = os.path.join(targetdir, METAMODEL_FILE_NAME)
source_context_path = LOCAL_METAMODEL_LDCONTEXT_FILE

DO_SHEX_VALIDATION = False

# Set this to True if you are making changes to the model itself.  Note, however, that it needs to be reset to False
# once the new types and/or meta elements have been submitted to the main repository
USE_LOCAL_IMPORT_MAP = False
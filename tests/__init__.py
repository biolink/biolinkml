import os

from biolinkml import LOCAL_YAML_PATH, LOCAL_CONTEXT_PATH, METAMODEL_FILE_NAME

refresh_files = False               # True means update target files
skip_biolink_model = True          # True means run unit tests against biolink models


testdir = os.path.abspath(os.path.dirname(__file__))
sourcedir = os.path.join(testdir, 'source')
targetdir = os.path.join(testdir, 'target')
source_yaml_path = LOCAL_YAML_PATH
target_yaml_path = os.path.join(targetdir, METAMODEL_FILE_NAME)
source_context_path = LOCAL_CONTEXT_PATH

DO_SHEX_VALIDATION = False

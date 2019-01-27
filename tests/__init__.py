import os


refresh_files = False               # True means update target files
skip_biolink_model = True          # True means run unit tests against biolink models


testdir = os.path.abspath(os.path.dirname(__file__))
sourcedir = os.path.join(testdir, 'source')
targetdir = os.path.join(testdir, 'target')
source_yaml_path = os.path.join(sourcedir, 'meta.yaml')
target_yaml_path = os.path.join(targetdir, 'meta.yaml')
source_context_path = os.path.join(sourcedir, 'context.jsonld')

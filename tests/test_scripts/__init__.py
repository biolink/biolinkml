import filecmp
from warnings import warn

from tests.utils.testingenvironment import TestEnvironment, MismatchAction
from tests import source_yaml_path

env = TestEnvironment(__file__)

# Can be set to Ignore, Report or Fail.  Default is report
env.mismatch_action = MismatchAction.Fail

# Warn if the dependent test data is out of date
meta_yaml = env.input_path('meta.yaml')
if not filecmp.cmp(meta_yaml, source_yaml_path):
    print(f"WARNING: Test file {meta_yaml} does not match {source_yaml_path}.  You may want to update the test version and rerun")
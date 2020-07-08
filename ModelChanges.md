# Making changes to the underlying model

## Steps
1) Edit [tests/input/meta.yaml](), [tests/input/includes/types.yaml]() and/or [tests/input/includes/mappings.yaml]().
  Be sure to update the version # if the changes are significant using SemVer rules.
    1) Run [tests/test-base/test_python.py]().  Verify that the generated python in [tests/output/meta.py](),
     [tests/output/includes/types.py]() and/or [tests/output/includes/mappings.py]()reflects the changes.
    2) Run *all* unit tests in `tests/test_base`. Make sure that all output file changes are what is expected.
2) Copy [tests/input/meta.py]() to the [biolinkml]() directory. Copy any other changes to the root directory, including
   changes in [includes](). 
   ```shell script
    > cd tests
    > ./newmodel.sh
   ```
   NOTE: Double check that [tests/__init__.py]()  `SKIP_MARKDOWN_VALIDATION` is `False`
   2) Edit [biolinkml/meta.py]() and set the version number to the same as in the yaml file
3) Run ALL unit tests.  
   Note that an unexpected source of testing errors is [tests/test_scripts/test_gen_jsonld/GenGSONLDTestCase.#67]()

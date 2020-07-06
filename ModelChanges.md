# Making changes to the underlying model

## Steps
1) Edit [tests/input/meta.yaml](), [tests/input/includes/types.yaml]() and/or tests/input/includes/types.yaml]().
  Be sure to update the version # if the changes are significant using SemVer rules.
    1) Run [tests/test-base/test_python.py]().  Verify that the generated python in [tests/output/meta.py](),
     [tests/output/includes/types.py]() and/or [tests/output/includes/mappings.py]()reflects the changes.
    2) Run *all* unit tests in `tests/test_base`. Make sure that all output file changes are what is expected.
2) Copy [tests/input/meta.py]() to the [biolinkml]() directory. Copy any other changes to the root directory, including
   changes in [includes](). Don't forget to update [meta.yaml]()
   1) Replace the root [docs]() directory with [tests/output/docs]().  NOTE: Double check that [tests/__init__.py]() 
   `SKIP_MARKDOWN_VALIDATION` is `False`
   2) Edit [biolinkml/meta.py]() and set the version number to the same as in the yaml file
3) Run ALL unit tests.  Note that an unexpected source of testing errors is [tests/test_scripts/test_gen_jsonld/GenGSONLDTestCase.#67]()






## <span color="F0F0F0">WARNING:</span> This document is not current. The new testing environment has simplified what needs to happen below.  It will
be revised shortly.
This document describes how one goes about making a change to the underlying meta.yaml, types.yaml or other 
building block.  The general problem is that, when these changes are made, almost every unit test in the package
will break.   

# Steps
1) Make the edits to meta.yaml and other source files.  Be sure to update the version # if the changes are significant, using SemVer
1) Change the model itself.  Do _NOT_ add code to the generators, etc. that reference the model change(s) until the
model python has been regenerated.
    * Run `tests/test_base/test_meta_python.py`
    * Look at `tests/target/meta.py` and make sure it does what you want it to do (and, importantly, it compiles)
        * NOTE: Some IDE's will emit errors on the `__post_init__` methods.  These are actually OK, as they are the way 
        we report line numbers on misspelled or unexpected arguments. Example:
           ![__post_init__ example](images/post_init.png "Post Init warning")
    * Copy `tests/tartget/meta.py` to `biolinkml/meta.py`
    * Update the `metamodel_version` in `biolinkml/meta.py`, `includes/types.py`, `includes/types.jsonld`, `includes/mappings.py`, and `includes/mappings.jsonld`
    * Run the test again amd make sure it passes
2) Now that you have the python for the new model, make any additional changes in the utils or generators
3) Run all tests in tests/test_base and double check that the resulting changes to the various outputs are what is
needed.  The following items should be updated by a model change:
    * `context.jsonld` - json-ld context for models
    * `meta.json` - json representation of the model
    * `meta.owl` - OWL representation of the model
    * `meta.shex` - ShExC representation of the model
    * `meta.shexj` - ShExJ (json) representation of the model
    * `meta.ttl` - RDF representation of the model
    * `biolinkml/meta.py` - Python representation of the model
    * `includes/types.py` - Python representation of the types package
    * `includes/mappings.py` - Python representation of the mappings package
    
    The file `tests/test_base/new_model.sh` has the instructions to update all of the files. To run it:
      ```bash
        > cd tests/test_base
        > ./new_model.sh
      ```
    Note that the tests have to be run at least twice to update the removed files.
4) Replace ALL instances of `metamodel_version = "<old version>"` with `metamodel_version = "<old version>"`.  Example: `metamodel_version = "1.4.3"` --> `metamodel_version = "1.4.4"`
5) Change the version number in meta.yaml
6) Run tests/test_utils.  `tests/test_utils/new_model.sh` can be used to reset output -- execute it in the `test_utils` directory.
5) Run tests/test_scripts.  `tests/test_scripts/new_model.sh` can be used to reset output.  You also may need to edit
line 85 in `test_gen_jsonld.py`
6) Run tests/test_issues. `tests/test_scripts/new_model.sh` can be used to reset output.
7) Run tests/test_biolinkml. `tests/test_scripts/new_model.sh` can be used to reset output.
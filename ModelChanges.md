# Making changes to the underlying model
This document describes how one goes about making a change to the underlying meta.yaml, types.yaml or other 
building block.  The general problem is that, when these changes are made, almost every unit test in the package
will break.   

# Steps
1) Make the edits to meta.yaml and other source files.  Be sure to update the version # if the changes are significant, using SemVer
1) Change the model itself.  Do _NOT_ add code to the generators, etc. that reference the model change(s) until the
model python has been regenerated.
    * Run `tests/test_base/test_meta_python.py`
    * Look at `tests/target/meta.py` and make sure it does what you want it to do (and, importantly, it compiles)
    * Update the `metamodel_version` in `tests/target/meta.py`
    * Copy `tests/tartget/meta.py` to `biolinkml/meta.py`
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
    
    The file `tests/test_base/new_model.sh` has the instructions to update all of the files.  Note that the tests have
    to be run at least twice to update the removed files.
4) Run tests/test_utils.  `tests/test_utils/new_model.sh` can be used to reset output
5) Run tests/test_scripts.  `tests/test_scripts/new_model.sh` can be used to reset output.  You also may need to edit
line 85 in `test_gen_jsonld.py`
6) Run tests/test_issues. `tests/test_scripts/new_model.sh` can be used to reset output.
7) Run tests/test_biolinkml. `tests/test_scripts/new_model.sh` can be used to reset output.
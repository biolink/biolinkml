
# It can be fairly expensive to regenerate the various png's in the markdown.
# There are three alternatives:
#   1) make imgflags="-i"             -- generate uml images in images subdirectory (default)
#   2) make imgflags="-i --noimages"  -- assume uml images already exist and generate links to them
#   3) make imgflags=""               -- genrate uml images as inline url's
imgflags?=

SPECIFICATION.pdf: SPECIFICATION.md
	pandoc $< -o $@

meta.shex: meta.yaml
	pipenv run gen-shex $< > $@
meta.owl: meta.yaml
	pipenv run gen-owl $< > $@

# ~~~~~~~~~~~~~~~~~~~~
# DOCS
# ~~~~~~~~~~~~~~~~~~~~
docs/index.md: meta.yaml
	pipenv run gen-markdown --dir docs $(imgflags) $<

# ~~~~~~~~~~~~~~~~~~~~
# EXAMPLES
# ~~~~~~~~~~~~~~~~~~~~

all-examples: all-examples-organization

all-examples-%: examples/%.py examples/%.schema.json  examples/%.shex  examples/%.graphql  examples/%.graphql  examples/%.shex examples/%.proto  examples/%.shex

examples/%.py: examples/%.yaml
	pipenv run gen-py-classes $< > $@ && pipenv run python -m examples.$*
examples/%.shex: examples/%.yaml
	pipenv run gen-shex $< > $@
examples/%.schema.json: examples/%.yaml
	pipenv run gen-json-schema -t $* $< > $@
examples/%.context.jsonld: examples/%.yaml
	pipenv run gen-jsonld-context -t $* $< > $@
examples/%.graphql: examples/%.yaml
	pipenv run gen-graphql $< > $@
examples/%.context.jsonld: examples/%.yaml
	pipenv run gen-jsonld-context $< > $@
examples/%.jsonld: examples/%.yaml
	pipenv run gen-jsonld $< > $@
examples/%.shex: examples/%.yaml
	pipenv run gen-shex $< > $@
examples/%.proto: examples/%.yaml
	pipenv run gen-proto $< > $@
examples/%.owl: examples/%.yaml
	pipenv run gen-owl $< > $@
examples/%-docs: examples/%.yaml
	pipenv run gen-markdown $< -d $@
examples/%.valid: examples/%-data.json examples/%.schema.json
	jsonschema -i $^

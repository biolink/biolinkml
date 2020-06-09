
SPECIFICATION.pdf: SPECIFICATION.md
	pandoc $< -o $@

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

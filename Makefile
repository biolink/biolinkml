# Make sure we've got the needed executables
ifeq (, $(shell which pipenv))
 $(error "No pipenv - consider 'pip install pipenv'")
endif

# It can be fairly expensive to regenerate the various png's in the markdown.
# There are three alternatives:
#   1) make IMGFLAGS="-i"			 -- generate uml images in images subdirectory (default)
#   2) make IMGFLAGS="-i --noimages"  -- assume uml images already exist and generate links to them
#   3) make IMGFLAGS=""			   -- genrate uml images as inline url's
IMGFLAGS?=-i 


# ----------------------------------------
# TOP LEVEL TARGETS
# ----------------------------------------

all: pipenv ldcontext shex rdf owl docs

ldcontext:  context.jsonld
shex:  meta.shex metanc.shex
rdf: meta.ttl
owl:  meta.owl
docs:  docs/index.md

pipenv: env.lock
regen-mm:  biolinkml/meta.py

# ----------------------------------------
# Install package into build environment
# ----------------------------------------
env.lock:
	pipenv install -d -e .
	cp /dev/null env.lock


# ----------------------------------------
# Update requirements.txt
# ----------------------------------------
requirements.txt: env.lock
	pipenv lock -r > $@

# ----------------------------------------
# Regenerate meta.py - the master source file
# ----------------------------------------
biolinkml/meta.py:  meta.yaml env.lock
	pipenv run gen-py-classes $< > tmp.py && pipenv run python tmp.py && touch $@ && (pipenv run comparefiles tmp.py $@ && cp $@ $@-PREV && cp tmp.py $@ && echo $@  updated); touch $@; rm tmp.py

# ----------------------------------------
# Generate context.jsonld
# ----------------------------------------
context.jsonld: meta.yaml env.lock
	pipenv run gen-jsonld-context --base http://w3id.org/biolink/biolinkml $< > tmp.jsonld && touch $@ &&  (pipenv run comparefiles tmp.jsonld $@ -c "^\s*\"comments\":.*\n" && cp tmp.jsonld $@ && echo $@ updated);  rm tmp.jsonld

# ----------------------------------------
# Generate meta.ttl
# ----------------------------------------
meta.ttl: meta.yaml context.jsonld env.lock
	pipenv run gen-rdf $< -f ttl --context context.jsonld > $@

# ----------------------------------------
# Generate meta.owl
# ----------------------------------------
meta.owl: meta.yaml env.lock
	pipenv run gen-owl $< > tmp.owl && (pipenv run comparefiles tmp.owl $@ -c "\s*(meta:generation_date|meta:source_file_date).*;" && cp tmp.owl $@ && echo $@ updated); rm tmp.owl

# ----------------------------------------
# Generate meta.shex
# ----------------------------------------
metanc.shex: meta.yaml env.lock
	pipenv run gen-shex $< -c -f shex > $@

meta.shex: meta.yaml
	pipenv run gen-shex $< -f shex > $@

# ----------------------------------------
# Documentation
# ----------------------------------------
docs/index.md: meta.yaml env.lock
	rm -rf docs/*
	pipenv run gen-markdown --dir docs $(IMGFLAGS) $<

# ------------------
# Test
# ------------------
test: env.lock
	pipenv run python -m unittest discover -p 'test_*.py'
	pipenv run gen-jsonld-context --help > /dev/null
	pipenv run gen-csv --help > /dev/null
	pipenv run gen-graphviz --help > /dev/null
	pipenv run gen-golr-views --help > /dev/null
	pipenv run gen-graphql --help > /dev/null
	pipenv run gen-jsonld --help > /dev/null
	pipenv run gen-json-schema --help > /dev/null
	pipenv run gen-markdown --help > /dev/null
	pipenv run gen-owl --help > /dev/null
	pipenv run gen-proto --help > /dev/null
	pipenv run gen-py-classes --help > /dev/null
	pipenv run gen-rdf --help > /dev/null
	pipenv run gen-shex --help > /dev/null
	pipenv run gen-yuml --help > /dev/null
	pipenv run comparefiles --help > /dev/null

# ----------------------------------------
# Installation - from https://pypi.org/project/pipenv-to-requirements/
# ----------------------------------------
dev:
	pipenv install --dev
	pipenv run pip install -e .

dists: requirements sdist bdist wheels

requirements:
	pipenv run pipenv_to_requirements -f

sdist: requirements
	pipenv run python setup.py sdist

bdist: requirements
	pipenv run python setup.py bdist

wheels: requirements
	pipenv run python setup.py bdist_wheel

clean:
	pipenv --rm
	rm env.lock

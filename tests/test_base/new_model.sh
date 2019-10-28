#!/bin/bash
pushd ../..
# test_base
cp tests/target/meta.py biolinkml/meta.py
cp tests/target/meta.jsonld meta.jsonld
cp tests/target/context.jsonld context.jsonld
cp tests/target/meta.owl meta.owl
cp tests/target/meta.shex meta.shex
cp tests/target/meta.shexj meta.shexj
cp tests/target/meta.ttl meta.ttl
rm -rf docs

cp tests/target/mappings.context.jsonld includes/mappings.context.jsonld
cp tests/target/mappings.jsonld includes/mappings.jsonld
cp tests/target/mappings.py includes/mappings.py
cp tests/target/types.context.jsonld includes/types.context.jsonld
cp tests/target/types.jsonld includes/types.jsonld
cp tests/target/types.py includes/types.py

rm tests/source/meta_mappings.py
rm tests/source/meta_mappings.json
rm tests/source/meta_mappings.ttl

popd
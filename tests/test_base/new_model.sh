#!/bin/bash
pushd ../..
# test_base
cp tests/target/meta.json meta.json
cp tests/target/types.py includes/types.py
cp tests/target/meta.owl meta.owl
cp tests/target/meta.shex meta.shex
cp tests/target/meta.shexj meta.shexj
rm meta.ttl
rm -rf docs

rm tests/source/meta_mappings.py
rm tests/source/meta_mappings.json
rm tests/source/meta_mappings.ttl

popd
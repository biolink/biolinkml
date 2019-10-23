#!/bin/bash
pushd output
rm *.json *.py *.owl includes/types.json
rm meta.synopsis
rm schema4.yaml
popd
pushd input
rm *.py
rm *.json
popd
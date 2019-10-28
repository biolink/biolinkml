#!/bin/bash
pushd output
rm gencontext/meta_*.jsonld
rm -rf gengolr/meta
rm gengraphql/meta.graphql
rm genjsonschema/meta*.json
rm genjsonld/meta.jsonld
rm -rf genmarkdown/issue2
rm -rf genmarkdown/meta
rm genowl/meta_owl.*
rm genproto/meta.proto
rm genpython/meta.py
rm genrdf/make_output.ttl
rm genrdf/meta*.*
rm genshex/metashex*.*
rm -rf gengraphviz/meta*
rm -rf genyuml/meta*
rm genyuml/*.yuml
popd
pushd ../source
rm default_namespace.py
rm inheritedid.py
rm multi_id.py
rm ordering.py
rm timepoint.py
rm testtypes.py
popd
# biolinkml specification (DRAFT)


## Introduction (Informative)

This document defines the biolinkml syntax and language.

A Biolinkml (blml) schema is a formal computable description of how
entities within a data model are inter-related. While blml arose in
response to a need in life-sciences domain modeling to define the
Biolink Model, it is completely domain-neutral, and can be used to
model pet stores, etc.

The primary representation of a schema is via a YAML document. This
document can be translated to other representations.

The 3 core modeling elements in blml are *types*, *classes*, and *slots*:

 - **types** correspond to primitive datatypes, such as integers, strings, URIs
 - **classes** are categories for data instances
 - **slots** categorize the linkages instances can have to other instances, or to type instances
 
blml is intended to be used in a variety of modeling contexts: JSON
documents, RDF graphs, RDF* graphs and property graphs, as well as
tabular data. Converters exist for these different representations.

blml also provides rich meta-modeling constructs. For examples,
modeling have description fields, comments, mappings to other systems...

This document contains a mixture of normative and informative
sections. Normative sections may have informative examples
within. Normative elements are those that are prescriptive, that is
they are to be followed in order to comply with scheme
requirements. Informative elements are those that are descriptive,
that is they are designed to help the reader understand the concepts
presented in the normative elements.

blml is also described by its [own schema](meta.yaml), which is also
Normative. The documentation in this specification _must_ be
consistent with the yaml representation.

The italicized keywords _must_, _must not_, _should_, _should not_,
and _may_ are used to specify normative features of OWL 2 documents
and tools, and are interpreted as specified in RFC 211.

## Domain (Normative)

RDF* graphs

Representations and JSON representation

YAML: JSON subset

## Schema Representation (Informative)

The normative representation of a blml schema is as a YAML document.

The document includes dictionaries of schema **elements**. Each
dictionary is indexed by the element **name**. Dictionaries _may_ be
empty, and they _may_ be listed in any order.

The structure of the document

 * dictionary of prefixes
 * dictionary of subsets
 * dictionary of types
 * dictionary of classes
 * dictionary of slots
 * additional schema-level declarations
    * the schema _must_ have an [id](https://w3id.org/biolink/biolinkml/meta/id)
    * the schema _may_ have other declarations as allowed by [SchemaDefinition](https://w3id.org/biolink/biolinkml/meta/SchemaDefinition)

Example (Informative):

This example illustrates broadly structure of a blml schema. Ellipses indicate information omitted for brevity

```yaml
id: https://example.org/example-schema
name: example schema
description: This is...
license: https://creativecommons.org/publicdomain/zero/1.0/

prefixes:
  biolinkml: https://w3id.org/biolink/biolinkml/
  ex: https://example.org/example-schema#
  wgs: http://www.w3.org/2003/01/geo/wgs84_pos
  qud: http://qudt.org/1.1/schema/qudt#
  
default_prefix: ex

default_curi_maps:
  - semweb_context

emit_prefixes:
  - rdf
  - rdfs
  - xsd
  - skos

imports:
  - biolinkml:types

subsets: ...

# Main schema follows
types: ...
classes: ...
slots: ...

```

## Names and Namespaces (Normative)

All schema elements _must_ have a unique name and a unique IRI. Names _must_ be declared as keys in dictionaries, and IRIs are constructed automatically for these by concatenating the [default_prefix](https://w3id.org/biolink/biolinkml/meta/default_prefix) with the IRI construction rule for that element type:

 * class elements use a CamelCase construction rule
 * slot, types, subset elements use a snake_case construction rule

TODO: define these rules.

Values for schema element slots _may_ be IRIs, and these _may_ be specified as CURIEs. CURIEs are shortform representations of URIs, and _must_ be specified as `PREFIX:LocalID`, where the prefix has an associated URI base. The prefix _must_ be declared in either:

 * a [prefixes](https://w3id.org/biolink/biolinkml/meta/prefixes) dictionary, where the keys are prefixes and the values are URI bases.
 * an external CURIE map specified via a [default_curi_maps](https://w3id.org/biolink/biolinkml/meta/default_curi_maps) section

Example (Informative):

```yaml
prefixes:
  biolink: https://w3id.org/biolink/vocab/
  biolinkml: https://w3id.org/biolink/biolinkml/
  OBAN: http://purl.org/oban/
  SIO: http://semanticscience.org/resource/SIO_
  wgs: http://www.w3.org/2003/01/geo/wgs84_pos
  qud: http://qudt.org/1.1/schema/qudt#
  UMLSSG: https://uts-ws.nlm.nih.gov/rest/semantic-network/semantic-network/current/GROUP/
  UMLSST: https://uts-ws.nlm.nih.gov/rest/semantic-network/semantic-network/current/STY/
  UMLSSC: https://uts-ws.nlm.nih.gov/rest/semantic-network/semantic-network/current/TUI/
```

## Schema Metadata (Normative)

 * [biolinkml:ClassDefinition](https://w3id.org/biolink/biolinkml/meta/ClassDefinition)

## Imports (Normative)


## Metadata elements (Normative)



## Core elements: Classes, Slots, and Types (Normative)

## Class Hierarchies (Normative)

## Glossary of terms (Information)


# biolinkml specification (DRAFT)

<!--

Editors note: add comments using HTML syntax, such as this one

-->

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
  biolinkml: https://w3id.org/biolink/biolinkml/
  wgs: http://www.w3.org/2003/01/geo/wgs84_pos
  qud: http://qudt.org/1.1/schema/qudt#
```

## Schema Metadata (Normative)

 * [ClassDefinition](https://w3id.org/biolink/biolinkml/meta/ClassDefinition)

### Imports (Normative)

Imports are specified as an import list in the main schema object.

```yaml
imports:
  - <IMPORT_1>
  - <IMPORT_2>
  - ...
  - <IMPORT_n>  
```

TODO:

 * https://github.com/biolink/biolinkml/projects/1

### Metadata elements (Normative)



## Core elements: Classes, Slots, and Types (Normative)

### Slots (Normative)

Slots are properties that can be assigned to individuals.

The set of slots available in a model is defined in a slot dictionary, declared at the schema level

```yaml
slots:
  SLOT_NAME_1: DEFINITION_1
  SLOT_NAME_2: DEFINITION_2
  ...
  SLOT_NAME_m: DEFINITION_n
```

Each key in the dictionary is the slot [name](https://w3id.org/biolink/biolinkml/meta/name). The slot name must be unique.


The [SlotDefinition](https://w3id.org/biolink/biolinkml/meta/SlotDefinition) is described in the metamodel.

### Class Slots (Normative)

A class _may_ have any number of slots declared

```yaml
  CLASS:
    slots:
      - SLOT_1
      - SLOT_2
      - ...
      - SLOT_n
```

Each declared slot _must_ be defined in the slot dictionary.

### Class Hierarchies (Normative)

Each class _must_ have zero or one **is_a** parents, as defined by [biolinkml:is_a](https://w3id.org/biolink/biolinkml/meta/is_a)

In addition a class _may_ have multiple **mixin** parents, as defined by [biolinkml:mixins](https://w3id.org/biolink/biolinkml/meta/mixin)

We define function `ancestors*(c)` which is the transitive close of the union of *c*, the parents of *c* and defined by the union of is_a and mixins.

### Slot Usages

Each class _may_ declare a dictionary of [slot_usage](https://w3id.org/biolink/biolinkml/meta/slot_usage)s.

```yaml
  CLASS:
    slot_usage:
      SLOT_1: USAGE_1
      SLOT_2: USAGE_2
      ...
      SLOT_n: USAGE_n
```

These refine a slot definition in the context of a particular class


```python
def effective_slot_property(s, p, c):
   if c declares slot_usage for p:
      use the value for p
   elif any m in mixins(c) declares a slot_usage for p:
      use the value for p from this mixin
   else:
      if effective_slot_property(s, p, c.is_a):
         use this
      elif: effective_slot_property(s, p, m) for any mixin m:
         use this
      else:
         use the default value of p for s
```


### Slot Validation

This section describes which slots can be used to describe which instances.

Consider instance *i* of type *t*, with an association of type *s* connecting to object or instance *j*.

```json
{
  ## instance i of type t
  "s": <j>
}
```

For this to be valid, it *must* be the case that:

 * for all *r* 

## Domain Declarations

<!--

test_issue_3 

-->

## Built-in Types (Informative)

You can import standard types:

```yaml
imports:
  - biolinkml:types
```

includes in its type dictionary entries such as:

```yaml
  date:
    uri: xsd:date
    base: XSDDate
    repr: str
```

[types.yaml](./includes/types.yaml)

<!--

test_issue_3 

-->

## Glossary of terms (Information)


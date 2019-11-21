[![Build Status](https://travis-ci.org/biolink/biolinkml.svg?branch=master)](https://travis-ci.org/biolink/biolinkml)

[Binder Link](https://mybinder.org/v2/gh/biolink/biolinkml/master?filepath=notebooks)

# biolinkml - biolink modeling language

biolinkml is a general purpose modeling language following object-oriented and ontological principles. Models are authored in YAML. A variety of artefacts can be generated from the model, including ShEx, JSON-Schema, OWL, Python dataclasses, UML diagrams, Markdown pages for deployment in a GitHub pages site, and more.

biolinkml is used for development of the [BioLink Model](https://biolink.github.io/biolink-model), but the framework is general purpose and can be used for any kind of modeling.

Quickstart docs:

 * Browse the model (biolinkml is self-describing): [https://biolink.github.io/biolinkml/docs](https://biolink.github.io/biolinkml/docs)
    * [class definition](https://biolink.github.io/biolinkml/docs/ClassDefinition) Class definitions
    * [slot definition](https://biolink.github.io/biolinkml/docs/SlotDefinition) Class properties
    * [type definition](https://biolink.github.io/biolinkml/docs/TypeDefinition) Data types
    * [schema ddefinition](https://biolink.github.io/biolinkml/docs/SchemaDefinition) Schema definition

For an example, see the [Jupyter notebook example](https://nbviewer.jupyter.org/github/biolink/biolinkml/blob/master/notebooks/examples.ipynb)

## Installation
```bash
> pipenv install biolinkml
```

## Examples

This basic example shows a schema with a single class together with slots that can be used for instances of that class:

```yaml
id: http://example.org/sample/example1
name: synopsis2

types:
  yearCount:
    base: int
    uri: xsd:int
  string:
    base: str
    uri: xsd:string
    
classes:
  person:
    description: A person, living or dead
    slots:
      - id
      - first name
      - last name
      - age

slots:
  id:
    description: Unique identifier of a person
    identifier: true

  first name:
    description: The first name of a person
    range: string
    
  last name:
    description: The last name of a person
    range: string
    required: true

  age:
    description: The age of a person if living or age of death if not
    range: yearCount
```        

## Generated Aretfacts

* Python 3 dataclasses
* [ShEx](http://shex.io/shex-semantics/index.html) - Shape Expressions Langauge
* [YUML](https://yuml.me/) - UML diagram drawing tool
* Class and interface definitions for [GraphQL](https://graphql.org/)
* Graphviz -- fairly basic representation of hierarchies
* [JSON](https://json.org/) and [JSON-LD](https://json-ld.org/)
* [JSON Schema](https://json-schema.org/)
* [Markdown](https://daringfireball.net/projects/markdown/) - markup language used by github and others
* [OWL](https://www.w3.org/TR/2012/REC-owl2-overview-20121211/) - Web Ontology Language
* [RDF](https://www.w3.org/2001/sw/wiki/RDF) - Resource Description Format

## Language Features

In future we will have examples for each of these.

 * polymorphism/inheritance, see [is_a](https://biolink.github.io/biolinkml/docs/is_a)
 * [abstract](https://biolink.github.io/biolinkml/docs/abstract) and [mixin](https://biolink.github.io/biolinkml/docs/mixin) classes
 * control JSON-LD mappings to URIs via [prefixes](https://biolink.github.io/biolinkml/docs/prefixes) declarations
 * ability to refine meaning of a slot in the context of a particular class via [slot usage](https://biolink.github.io/biolinkml/docs/slot_usage)

## Formal Semantics

These are specified using First Order Logic (FOL) axioms. See the [semantics](semantics) folder

## FAQ

### Why not use X as the modeling framework?

Why invent our own yaml and not use JSON-Schema, SQL, UML, ProtoBuf,
OWL, ...

each of these is tied to a particular formalisms. E.g. JSON-Schema to
trees. OWL to open world logic. There are various impedance mismatches
in converting between these. The goal was to develop something simple
and more general that is not tied to any one serialization format or
set of assumptions.

There are other projects with similar goals, e.g
https://github.com/common-workflow-language/schema_salad

It may be possible to align with these.

### Why not use X as the datamodel

Here X may be bioschemas, some upper ontology (BioTop), UMLS
metathesaurus, bio*, various other attempts to model all of biology in
an object model.

Currently as far as we know there is no existing reference datamodel
that is flexible enough to be used here.


## Biolink Modeling Language

### Type Definitions

```
typeof:
    domain: type definition
    range: type definition
    description: supertype

  base:
    domain: type definition
    description: python base type that implements this type definition
    inherited: true

  type uri:
    domain: type definition
    range: uri
    alias: uri
    description: the URI to be used for the type in semantic web mappings

  repr:
    domain: type definition
    range: string
    description: the python representation of this type if different than the base type
    inherited: true
```


### Slot Definitions





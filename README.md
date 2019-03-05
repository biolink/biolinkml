[![Build Status](https://travis-ci.org/biolink/biolinkml.svg?branch=master)](https://travis-ci.org/biolink/biolinkml)

[Binder Link](https://mybinder.org/v2/gh/biolink/biolinkml/master?filepath=notebooks)
# biolinkml - biolink modeling language

Quickstart docs:

 * Browse the model: [https://biolink.github.io/biolinkml](https://biolink.github.io/biolikml)
    * [class definition](docs/ClassDefinition.html) Class definitions
    * [slot definition](docs/SlotDefinition.html) Class properties
    * [type definition](docs/TypeDefinition.html) Data types
    * [schema ddefinition](docs/SchemaDefinition.html) Schema definition



## Installation
```bash
> pipenv install biolinkml
```

## Examples


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



### Slot Definitions





[![Build Status](https://travis-ci.org/biolink/biolinkml.svg?branch=master)](https://travis-ci.org/biolink/biolinkml)

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




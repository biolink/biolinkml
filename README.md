[![Pyversions](https://img.shields.io/pypi/pyversions/biolinkml.svg)](https://pypi.python.org/pypi/biolinkml)
![](https://github.com/biolink/biolinkml/workflows/Build/badge.svg)
[![PyPi](https://img.shields.io/pypi/v/biolinkml.svg)](https://pypi.python.org/pypi/biolinkml)


[Binder Link](https://mybinder.org/v2/gh/biolink/biolinkml/master?filepath=notebooks)

# biolinkml - biolink modeling language

biolinkml is a general purpose modeling language following object-oriented and ontological principles. Models are authored in YAML. A variety of artefacts can be generated from the model, including ShEx, JSON-Schema, OWL, Python dataclasses, UML diagrams, Markdown pages for deployment in a GitHub pages site, and more.

biolinkml is used for development of the [BioLink Model](https://biolink.github.io/biolink-model), but the framework is general purpose and can be used for any kind of modeling.


Quickstart docs:

 * Browse the model (biolinkml is self-describing): [https://biolink.github.io/biolinkml/docs](https://biolink.github.io/biolinkml/docs)
    * [class definition](https://biolink.github.io/biolinkml/docs/ClassDefinition) Class definitions
    * [slot definition](https://biolink.github.io/biolinkml/docs/SlotDefinition) Class properties
    * [type definition](https://biolink.github.io/biolinkml/docs/TypeDefinition) Data types
    * [schema definition](https://biolink.github.io/biolinkml/docs/SchemaDefinition) Schema definition

For an example, see the [Jupyter notebook example](https://nbviewer.jupyter.org/github/biolink/biolinkml/blob/master/notebooks/examples.ipynb)

## Installation
```bash
> pipenv install biolinkml
```

## Language Features

 * polymorphism/inheritance, see [is_a](https://biolink.github.io/biolinkml/docs/is_a)
 * [abstract](https://biolink.github.io/biolinkml/docs/abstract) and [mixin](https://biolink.github.io/biolinkml/docs/mixin) classes
 * control JSON-LD mappings to URIs via [prefixes](https://biolink.github.io/biolinkml/docs/prefixes) declarations
 * ability to refine meaning of a slot in the context of a particular class via [slot usage](https://biolink.github.io/biolinkml/docs/slot_usage)


## Examples

biolinkml can be used as a modeling language in its own right, or it can be
compiled to other schema/modeling languages

We use a basic schema for illustrative purposes:

```yaml
id: http://example.org/sample/organization
name: organization

types:
  yearCount:
    base: int
    uri: xsd:int
  string:
    base: str
    uri: xsd:string

classes:

  organization:
    slots:
      - id
      - name
      - has boss

  employee:
    description: A person
    slots:
      - id
      - first name
      - last name
      - aliases
      - age in years
    slot_usage:
      last name :
        required: true

  manager:
    description: An employee who manages others
    is_a: employee
    slots:
      - has employees

slots:
  id:
    description: Unique identifier of a person
    identifier: true

  name:
    description: human readable name
    range: string

  aliases:
    is_a: name
    description: An alternative name
    multivalued: true

  first name:
    is_a: name
    description: The first name of a person

  last name:
    is_a: name
    description: The last name of a person

  age in years:
    description: The age of a person if living or age of death if not
    range: yearCount

  has employees:
    range: employee
    multivalued: true
    inlined: true

  has boss:
    range: manager
    inlined: true
```

Note this schema does not illustrate the more advanced features of blml

### JSON Schema

[JSON Schema](https://json-schema.org/) is a schema language for JSON documents

`pipenv run gen-json-schema examples/organization.yaml`

See [examples/organization.schema.json](examples/organization.schema.json)


### Python DataClasses

`pipenv run gen-py-classes examples/organization.yaml > examples/organization.py`

See [examples/organization.py](examples/organization.py)

For example:

```python
@dataclass
class Organization(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = URIRef("http://example.org/sample/organization/Organization")
    class_class_curie: ClassVar[str] = None
    class_name: ClassVar[str] = "organization"
    class_model_uri: ClassVar[URIRef] = URIRef("http://example.org/sample/organization/Organization")

    id: Union[str, OrganizationId]
    name: Optional[str] = None
    has_boss: Optional[Union[dict, "Manager"]] = None

    def __post_init__(self, **kwargs: Dict[str, Any]):
        if self.id is None:
            raise ValueError(f"id must be supplied")
        if not isinstance(self.id, OrganizationId):
            self.id = OrganizationId(self.id)
        if self.has_boss is not None and not isinstance(self.has_boss, Manager):
            self.has_boss = Manager(self.has_boss)
        super().__post_init__(**kwargs)

```

### ShEx

 [ShEx](http://shex.io/shex-semantics/index.html) - Shape Expressions Langauge

`pipenv run gen-shex examples/organization.yaml > examples/organization.shex`

See [examples/organization.shex](examples/organization.shex)


## Generating Markdown documentation

`pipenv run gen-markdown examples/organization.yaml -d examples/organization-docs/`

This will generate a markdown document for every class and slot in the model

### Others

* [YUML](https://yuml.me/) - UML diagram drawing tool
* Class and interface definitions for [GraphQL](https://graphql.org/)
* Graphviz -- fairly basic representation of hierarchies
* Protobuf
* [JSON](https://json.org/) and [JSON-LD](https://json-ld.org/)
* [Markdown](https://daringfireball.net/projects/markdown/) - markup language used by github and others
* [OWL](https://www.w3.org/TR/2012/REC-owl2-overview-20121211/) - Web Ontology Language
* [RDF](https://www.w3.org/2001/sw/wiki/RDF) - Resource Description Format


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


## Developers Notes

### Release to Pypi

[A Github action] is set up to automatically release the Pypi package. When it is ready
for a new release, create a [Github release](https://github.com/biolink/biolinkml/releases). The version
should be in the vX.X.X format following [the smantic versioning specification](https://semver.org/).

After the release is created, the GitHub action will be triggered to publish to Pypi. The release version will be used to create the Pypi package.

If the Pypi release failed, make fixes, [delete the GitHub release](https://help.github.com/en/enterprise/2.16/user/github/administering-a-repository/editing-and-deleting-releases#:~:text=Deleting%20a%20release,-Tip%3A%20You%20must&text=Under%20your%20repository%20name%2C%20click%20Releases.,of%20the%20page%2C%20click%20Delete.), and recreate a release with the same version again.

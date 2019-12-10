
# Type: physical entity


An entity that has physical properties such as mass, volume, or charge

URI: [biolink:PhysicalEntity](https://w3id.org/biolink/vocab/PhysicalEntity)


![img](http://yuml.me/diagram/nofunky;dir:TB/class/\[MolecularEntity]uses%20-.->\[PhysicalEntity&#124;id(i):identifier_type;name(i):label_type;category(i):iri_type%20%2B],%20\[MaterialSample]uses%20-.->\[PhysicalEntity],%20\[AnatomicalEntity]uses%20-.->\[PhysicalEntity],%20\[NamedThing]^-\[PhysicalEntity])

## Parents

 *  is_a: [named thing](named thing.md) - a databased entity or concept/class

## Mixin for

 * [anatomical entity](anatomical entity.md) (mixin)  - A subcellular location, cell type or gross anatomical part
 * [material sample](material sample.md) (mixin)  - A sample is a limited quantity of something (e.g. an individual or set of individuals from a population, or a portion of a substance) to be used for testing, analysis, inspection, investigation, demonstration, or trial use. [SIO]
 * [molecular entity](molecular entity.md) (mixin)  - A gene, gene product, small molecule or macromolecule (including protein complex)

## Referenced by class


## Attributes


### Inherited from named thing:

 * [id](id.md)  <sub>REQ</sub>
    * Description: A unique identifier for a thing. Must be either a CURIE shorthand for a URI or a complete URI
    * range: [IdentifierType](type/IdentifierType.md)
    * inherited from: [named thing](named thing.md)
    * in subsets: (translator_minimal)
 * [name](name.md)  <sub>REQ</sub>
    * Description: A human-readable name for a thing
    * range: [LabelType](type/LabelType.md)
    * inherited from: [named thing](named thing.md)
    * in subsets: (translator_minimal)
 * [category](category.md)  <sub>1..*</sub>
    * Description: Name of the high level ontology class in which this entity is categorized. Corresponds to the label for the biolink entity type class. In a neo4j database this MAY correspond to the neo4j label tag
    * range: [IriType](type/IriType.md)
    * inherited from: [named thing](named thing.md)
    * in subsets: (translator_minimal)

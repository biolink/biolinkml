
# Type: biological process or activity


Either an individual molecular activity, or a collection of causally connected molecular activities

URI: [biolink:BiologicalProcessOrActivity](https://w3id.org/biolink/vocab/BiologicalProcessOrActivity)


![img](http://yuml.me/diagram/nofunky;dir:TB/class/\[BiologicalProcessOrActivity&#124;id(i):identifier_type;name(i):label_type;category(i):iri_type%20%2B]uses%20-.->\[Occurrent],%20\[BiologicalProcessOrActivity]^-\[MolecularActivity],%20\[BiologicalProcessOrActivity]^-\[BiologicalProcess],%20\[BiologicalEntity]^-\[BiologicalProcessOrActivity])

## Parents

 *  is_a: [biological entity](biological entity.md)

## Uses Mixins

 *  mixin: [occurrent](occurrent.md) - A processual entity

## Children

 * [biological process](biological process.md) - One or more causally connected executions of molecular functions
 * [molecular activity](molecular activity.md) - An execution of a molecular function carried out by a gene product or macromolecular complex.

## Referenced by class

 *  **[occurrent](occurrent.md)** *[enabled by](enabled_by.md)*  <sub>0..*</sub>  **[biological process or activity](biological process or activity.md)**

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

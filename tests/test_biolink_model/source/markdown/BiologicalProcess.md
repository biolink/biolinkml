
# Type: biological process


One or more causally connected executions of molecular functions

URI: [biolink:BiologicalProcess](https://w3id.org/biolink/vocab/BiologicalProcess)


![img](http://yuml.me/diagram/nofunky;dir:TB/class/\[MacromolecularMachineToBiologicalProcessAssociation]-%20object%201..1>\[BiologicalProcess&#124;id(i):identifier_type;name(i):label_type;category(i):iri_type%20%2B],%20\[BiologicalProcess]uses%20-.->\[Occurrent],%20\[BiologicalProcess]^-\[PhysiologicalProcess],%20\[BiologicalProcess]^-\[Pathway],%20\[BiologicalProcessOrActivity]^-\[BiologicalProcess])

## Parents

 *  is_a: [biological process or activity](biological process or activity.md) - Either an individual molecular activity, or a collection of causally connected molecular activities

## Uses Mixins

 *  mixin: [occurrent](occurrent.md) - A processual entity

## Children

 * [pathway](pathway.md)
 * [physiological process](physiological process.md)

## Referenced by class

 *  **[macromolecular machine to biological process association](macromolecular machine to biological process association.md)** *[macromolecular machine to biological process association➞object](macromolecular_machine_to_biological_process_association_object.md)*  <sub>REQ</sub>  **[biological process](biological process.md)**

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

## Other properties

|  |  |  |
| --- | --- | --- |
| **Mappings:** | | GO:0008150 |
|  | | SIO:000006 |
|  | | WD:Q2996394 |


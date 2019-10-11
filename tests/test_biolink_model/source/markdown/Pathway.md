
# Type: pathway




URI: [biolink:Pathway](https://w3id.org/biolink/vocab/Pathway)


![img](http://yuml.me/diagram/nofunky;dir:TB/class/\[ChemicalToPathwayAssociation]-%20object%201..1>\[Pathway|id(i):identifier_type;name(i):label_type;category(i):iri_type%20%2B],%20\[BiologicalProcess]^-\[Pathway])

## Parents

 *  is_a: [biological process](biological process.md) - One or more causally connected executions of molecular functions

## Referenced by class

 *  **[chemical to pathway association](chemical to pathway association.md)** *[object](chemical_to_pathway_association_object.md)*  <sub>REQ</sub>  **[pathway](pathway.md)**

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
| **Mappings:** | | GO:0007165 |
|  | | SIO:010526 |
|  | | PW:0000001 |
|  | | WD:Q4915012 |


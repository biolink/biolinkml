
# Type: pathway




URI: [biolink:Pathway](https://w3id.org/biolink/vocab/Pathway)


![img](http://yuml.me/diagram/nofunky;dir:TB/class/\[BiologicalProcessOrActivity]<enabled%20by(i)%200..*-%20\[Pathway&#124;id(i):identifier_type;name(i):label_type;category(i):iri_type%20%2B],%20\[ChemicalToPathwayAssociation]-%20object%201..1>\[Pathway],%20\[BiologicalProcess]^-\[Pathway])

## Parents

 *  is_a: [BiologicalProcess](BiologicalProcess.md) - One or more causally connected executions of molecular functions

## Referenced by class

 *  **[ChemicalToPathwayAssociation](ChemicalToPathwayAssociation.md)** *[chemical to pathway association➞object](chemical_to_pathway_association_object.md)*  <sub>REQ</sub>  **[Pathway](Pathway.md)**

## Attributes


### Inherited from biological process or activity:

 * [enabled by](enabled_by.md)  <sub>0..*</sub>
    * Description: holds between a process and a physical entity, where the physical entity executes the process
    * range: [BiologicalProcessOrActivity](BiologicalProcessOrActivity.md)
    * inherited from: [Occurrent](Occurrent.md)
    * in subsets: (translator_minimal)

### Inherited from named thing:

 * [id](id.md)  <sub>REQ</sub>
    * Description: A unique identifier for a thing. Must be either a CURIE shorthand for a URI or a complete URI
    * range: [IdentifierType](types/IdentifierType.md)
    * inherited from: [NamedThing](NamedThing.md)
    * in subsets: (translator_minimal)
 * [name](name.md)  <sub>REQ</sub>
    * Description: A human-readable name for a thing
    * range: [LabelType](types/LabelType.md)
    * inherited from: [NamedThing](NamedThing.md)
    * in subsets: (translator_minimal)
 * [category](category.md)  <sub>1..*</sub>
    * Description: Name of the high level ontology class in which this entity is categorized. Corresponds to the label for the biolink entity type class. In a neo4j database this MAY correspond to the neo4j label tag
    * range: [IriType](types/IriType.md)
    * inherited from: [NamedThing](NamedThing.md)
    * in subsets: (translator_minimal)

## Other properties

|  |  |  |
| --- | --- | --- |
| **Mappings:** | | GO:0007165 |
|  | | SIO:010526 |
|  | | PW:0000001 |
|  | | WD:Q4915012 |


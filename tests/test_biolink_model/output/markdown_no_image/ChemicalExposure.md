
# Type: chemical exposure


A chemical exposure is an intake of a particular chemical substance

URI: [biolink:ChemicalExposure](https://w3id.org/biolink/vocab/ChemicalExposure)


![img](http://yuml.me/diagram/nofunky;dir:TB/class/[ExposureEvent],[DrugExposure],[ChemicalExposure&#124;id(i):string;name(i):label_type;category(i):iri_type%20%2B]^-[DrugExposure],[ExposureEvent]^-[ChemicalExposure])

## Parents

 *  is_a: [ExposureEvent](ExposureEvent.md) - A feature of the environment of an organism that influences one or more phenotypic features of that organism, potentially mediated by genes

## Children

 * [DrugExposure](DrugExposure.md) - A drug exposure is an intake of a particular chemical substance

## Referenced by class


## Attributes


### Inherited from exposure event:

 * [category](category.md)  <sub>1..*</sub>
    * Description: Name of the high level ontology class in which this entity is categorized. Corresponds to the label for the biolink entity type class. In a neo4j database this MAY correspond to the neo4j label tag
    * range: [IriType](types/IriType.md)
    * in subsets: (translator_minimal)
 * [id](id.md)  <sub>REQ</sub>
    * Description: A unique identifier for a thing. Must be either a CURIE shorthand for a URI or a complete URI
    * range: [String](types/String.md)
    * in subsets: (translator_minimal)
 * [name](name.md)  <sub>REQ</sub>
    * Description: A human-readable name for a thing
    * range: [LabelType](types/LabelType.md)
    * in subsets: (translator_minimal)

## Other properties

|  |  |  |
| --- | --- | --- |
| **Mappings:** | | ECTO:9000000 |


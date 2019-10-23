
# Type: treatment


A treatment is targeted at a disease or phenotype and may involve multiple drug 'exposures'

URI: [biolink:Treatment](https://w3id.org/biolink/vocab/Treatment)


![img](http://yuml.me/diagram/nofunky;dir:TB/class/\[SequenceVariantModulatesTreatmentAssociation]-%20object%201..1>\[Treatment|id(i):identifier_type;name(i):label_type;category(i):iri_type%20%2B],%20\[ExposureEvent]^-\[Treatment])

## Parents

 *  is_a: [exposure event](exposure event.md) - A feature of the environment of an organism that influences one or more phenotypic features of that organism, potentially mediated by genes

## Referenced by class

 *  **[sequence variant modulates treatment association](sequence variant modulates treatment association.md)** *[sequence variant modulates treatment association➞object](sequence_variant_modulates_treatment_association_object.md)*  <sub>REQ</sub>  **[treatment](treatment.md)**

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

### Domain for slot:

 * [treatment➞has part](treatment_has_part.md)  <sub>1..*</sub>
    * range: [drug exposure](drug exposure.md)
 * [treats](treats.md)  <sub>1..*</sub>
    * Description: holds between a therapeutic procedure or chemical substance and a disease or phenotypic feature that it is used to treat
    * range: [disease or phenotypic feature](disease or phenotypic feature.md)
    * in subsets: (translator_minimal)

## Other properties

|  |  |  |
| --- | --- | --- |
| **Aliases:** | | medical action |
| **Mappings:** | | OGMS:0000090 |
|  | | SIO:001398 |


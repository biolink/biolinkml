
# Type: organismal entity


A named entity that is either a part of an organism, a whole organism, population or clade of organisms, excluding molecular entities

URI: [biolink:OrganismalEntity](https://w3id.org/biolink/vocab/OrganismalEntity)


![img](http://yuml.me/diagram/nofunky;dir:TB/class/\[OrganismalEntity|id(i):identifier_type;name(i):label_type;category(i):iri_type%20%2B]^-\[PopulationOfIndividualOrganisms],%20\[OrganismalEntity]^-\[LifeStage],%20\[OrganismalEntity]^-\[IndividualOrganism],%20\[OrganismalEntity]^-\[CellLine],%20\[OrganismalEntity]^-\[AnatomicalEntity],%20\[BiologicalEntity]^-\[OrganismalEntity])

## Parents

 *  is_a: [biological entity](biological entity.md)

## Children

 * [anatomical entity](anatomical entity.md) - A subcellular location, cell type or gross anatomical part
 * [cell line](cell line.md)
 * [individual organism](individual organism.md)
 * [life stage](life stage.md) - A stage of development or growth of an organism, including post-natal adult stages
 * [population of individual organisms](population of individual organisms.md) - A collection of individuals from the same taxonomic class distinguished by one or more characteristics. Characteristics can include, but are not limited to, shared geographic location, genetics, phenotypes [Alliance for Genome Resources]

## Referenced by class

 *  **[exposure event](exposure event.md)** *[has receptor](has_receptor.md)*  <sub>OPT</sub>  **[organismal entity](organismal entity.md)**

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
| **Mappings:** | | WD:Q7239 |


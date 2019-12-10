
# Type: disease




URI: [biolink:Disease](https://w3id.org/biolink/vocab/Disease)


![img](http://yuml.me/diagram/nofunky;dir:TB/class/\[OrganismTaxon]<in%20taxon(i)%200..*-%20\[Disease&#124;id(i):identifier_type;name(i):label_type;category(i):iri_type%20%2B],%20\[DiseaseToExposureAssociation]-%20subject%201..1>\[Disease],%20\[DiseaseToThingAssociation]-%20subject%201..1>\[Disease],%20\[DiseaseOrPhenotypicFeature]^-\[Disease])

## Parents

 *  is_a: [disease or phenotypic feature](disease or phenotypic feature.md) - Either one of a disease or an individual phenotypic feature. Some knowledge resources such as Monarch treat these as distinct, others such as MESH conflate.

## Referenced by class

 *  **[disease to exposure association](disease to exposure association.md)** *[disease to exposure association➞subject](disease_to_exposure_association_subject.md)*  <sub>REQ</sub>  **[disease](disease.md)**
 *  **[disease to thing association](disease to thing association.md)** *[disease to thing association➞subject](disease_to_thing_association_subject.md)*  <sub>REQ</sub>  **[disease](disease.md)**
 *  **[entity to disease association](entity to disease association.md)** *[entity to disease association➞object](entity_to_disease_association_object.md)*  <sub>REQ</sub>  **[disease](disease.md)**
 *  **[named thing](named thing.md)** *[manifestation of](manifestation_of.md)*  <sub>0..*</sub>  **[disease](disease.md)**

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

### Inherited from thing with taxon:

 * [in taxon](in_taxon.md)  <sub>0..*</sub>
    * Description: connects a thing to a class representing a taxon
    * range: [organism taxon](organism taxon.md)
    * inherited from: [thing with taxon](thing with taxon.md)
    * in subsets: (translator_minimal)

## Other properties

|  |  |  |
| --- | --- | --- |
| **Aliases:** | | condition |
|  | | disorder |
|  | | medical condition |
| **Mappings:** | | MONDO:0000001 |
|  | | WD:Q12136 |
|  | | SIO:010299 |
|  | | UMLSSG:DISO |
|  | | UMLSSC:T019 |
|  | | UMLSST:cgab |
|  | | UMLSSC:T020 |
|  | | UMLSST:acab |
|  | | UMLSSC:T037 |
|  | | UMLSST:inpo |
|  | | UMLSSC:T046 |
|  | | UMLSST:patf |
|  | | UMLSSC:T047 |
|  | | UMLSST:dsyn |
|  | | UMLSSC:T048 |
|  | | UMLSST:mobd |
|  | | UMLSSC:T049 |
|  | | UMLSST:comd |
|  | | UMLSSC:T184 |
|  | | UMLSST:sosy |
|  | | UMLSSC:T190 |
|  | | UMLSST:anab |
|  | | UMLSSC:T191 |
|  | | UMLSST:neop |


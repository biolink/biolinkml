
# Type: disease or phenotypic feature association to location association


An association between either a disease or a phenotypic feature and an anatomical entity, where the disease/feature manifests in that site.

URI: [biolink:DiseaseOrPhenotypicFeatureAssociationToLocationAssociation](https://w3id.org/biolink/vocab/DiseaseOrPhenotypicFeatureAssociationToLocationAssociation)


![img](http://yuml.me/diagram/nofunky;dir:TB/class/[Publication],[Provider],[OntologyClass],[DiseaseOrPhenotypicFeatureAssociationToThingAssociation],[AnatomicalEntity]<object%201..1-%20[DiseaseOrPhenotypicFeatureAssociationToLocationAssociation&#124;relation(i):uriorcurie;id(i):string;negated(i):boolean%20%3F],[DiseaseOrPhenotypicFeatureAssociationToThingAssociation]^-[DiseaseOrPhenotypicFeatureAssociationToLocationAssociation],[DiseaseOrPhenotypicFeature],[AnatomicalEntity])

## Parents

 *  is_a: [DiseaseOrPhenotypicFeatureAssociationToThingAssociation](DiseaseOrPhenotypicFeatureAssociationToThingAssociation.md)

## Referenced by class


## Attributes


### Own

 * [disease or phenotypic feature association to location association➞object](disease_or_phenotypic_feature_association_to_location_association_object.md)  <sub>REQ</sub>
    * Description: anatomical entity in which the disease or feature is found
    * range: [AnatomicalEntity](AnatomicalEntity.md)

### Inherited from disease or phenotypic feature association to thing association:

 * [association type](association_type.md)  <sub>OPT</sub>
    * Description: connects an association to the type of association (e.g. gene to phenotype)
    * range: [OntologyClass](OntologyClass.md)
 * [association➞id](association_id.md)  <sub>REQ</sub>
    * Description: A unique identifier for an association
    * range: [String](types/String.md)
    * in subsets: (translator_minimal)
 * [disease or phenotypic feature association to thing association➞subject](disease_or_phenotypic_feature_association_to_thing_association_subject.md)  <sub>REQ</sub>
    * Description: disease or phenotype
    * range: [DiseaseOrPhenotypicFeature](DiseaseOrPhenotypicFeature.md)
 * [negated](negated.md)  <sub>OPT</sub>
    * Description: if set to true, then the association is negated i.e. is not true
    * range: [Boolean](types/Boolean.md)
 * [provided by](provided_by.md)  <sub>0..*</sub>
    * Description: connects an association to the agent (person, organization or group) that provided it
    * range: [Provider](Provider.md)
 * [publications](publications.md)  <sub>0..*</sub>
    * Description: connects an association to publications supporting the association
    * range: [Publication](Publication.md)
 * [qualifiers](qualifiers.md)  <sub>0..*</sub>
    * Description: connects an association to qualifiers that modify or qualify the meaning of that association
    * range: [OntologyClass](OntologyClass.md)
 * [relation](relation.md)  <sub>REQ</sub>
    * Description: the relationship type by which a subject is connected to an object in an association
    * range: [Uriorcurie](types/Uriorcurie.md)

## Other properties

|  |  |  |
| --- | --- | --- |
| **Mappings:** | | NCIT:R100 |


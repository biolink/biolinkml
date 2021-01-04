
# Type: disease to thing association




URI: [biolink:DiseaseToThingAssociation](https://w3id.org/biolink/vocab/DiseaseToThingAssociation)


![img](http://yuml.me/diagram/nofunky;dir:TB/class/[Publication],[Provider],[OntologyClass],[NamedThing],[Disease]<subject%201..1-%20[DiseaseToThingAssociation&#124;relation(i):uriorcurie;id(i):string;negated(i):boolean%20%3F],[DiseaseToPhenotypicFeatureAssociation]uses%20-.->[DiseaseToThingAssociation],[DiseaseToThingAssociation]^-[DiseaseToExposureAssociation],[Association]^-[DiseaseToThingAssociation],[DiseaseToPhenotypicFeatureAssociation],[DiseaseToExposureAssociation],[Disease],[Association])

## Parents

 *  is_a: [Association](Association.md) - A typed association between two entities, supported by evidence

## Children

 * [DiseaseToExposureAssociation](DiseaseToExposureAssociation.md) - An association between an exposure event and a disease

## Mixin for

 * [DiseaseToPhenotypicFeatureAssociation](DiseaseToPhenotypicFeatureAssociation.md) (mixin)  - An association between a disease and a phenotypic feature in which the phenotypic feature is associated with the disease in some way

## Referenced by class


## Attributes


### Own

 * [disease to thing association➞subject](disease_to_thing_association_subject.md)  <sub>REQ</sub>
    * Description: disease class
    * range: [Disease](Disease.md)
    * Example:    

### Inherited from association:

 * [association type](association_type.md)  <sub>OPT</sub>
    * Description: connects an association to the type of association (e.g. gene to phenotype)
    * range: [OntologyClass](OntologyClass.md)
 * [association➞id](association_id.md)  <sub>REQ</sub>
    * Description: A unique identifier for an association
    * range: [String](types/String.md)
    * in subsets: (translator_minimal)
 * [negated](negated.md)  <sub>OPT</sub>
    * Description: if set to true, then the association is negated i.e. is not true
    * range: [Boolean](types/Boolean.md)
 * [object](object.md)  <sub>REQ</sub>
    * Description: connects an association to the object of the association. For example, in a gene-to-phenotype association, the gene is subject and phenotype is object.
    * range: [NamedThing](NamedThing.md)
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
    * Description: The relation which describes an association between a subject and an object in a more granular manner. Usually this is a term from Relation Ontology, but it can be any edge CURIE.
    * range: [Uriorcurie](types/Uriorcurie.md)

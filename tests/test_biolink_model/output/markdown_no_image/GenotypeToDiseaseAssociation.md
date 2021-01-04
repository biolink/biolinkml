
# Type: genotype to disease association




URI: [biolink:GenotypeToDiseaseAssociation](https://w3id.org/biolink/vocab/GenotypeToDiseaseAssociation)


![img](http://yuml.me/diagram/nofunky;dir:TB/class/[SeverityValue],[Publication],[Provider],[OntologyClass],[Onset],[NamedThing],[GenotypeToThingAssociation],[NamedThing]<object%201..1-%20[GenotypeToDiseaseAssociation&#124;relation:uriorcurie;id(i):string;negated(i):boolean%20%3F],[NamedThing]<subject%201..1-%20[GenotypeToDiseaseAssociation],[GenotypeToDiseaseAssociation]uses%20-.->[GenotypeToThingAssociation],[GenotypeToDiseaseAssociation]uses%20-.->[EntityToDiseaseAssociation],[GenotypeToDiseaseAssociation]^-[GenotypeAsAModelOfDiseaseAssociation],[Association]^-[GenotypeToDiseaseAssociation],[GenotypeAsAModelOfDiseaseAssociation],[FrequencyValue],[EntityToDiseaseAssociation],[Association])

## Parents

 *  is_a: [Association](Association.md) - A typed association between two entities, supported by evidence

## Uses Mixins

 *  mixin: [GenotypeToThingAssociation](GenotypeToThingAssociation.md)
 *  mixin: [EntityToDiseaseAssociation](EntityToDiseaseAssociation.md) - mixin class for any association whose object (target node) is a disease

## Children

 * [GenotypeAsAModelOfDiseaseAssociation](GenotypeAsAModelOfDiseaseAssociation.md)

## Referenced by class


## Attributes


### Own

 * [genotype to disease association➞object](genotype_to_disease_association_object.md)  <sub>REQ</sub>
    * Description: a disease that is associated with that genotype
    * range: [NamedThing](NamedThing.md)
    * Example:    
 * [genotype to disease association➞relation](genotype_to_disease_association_relation.md)  <sub>REQ</sub>
    * Description: E.g. is pathogenic for
    * range: [Uriorcurie](types/Uriorcurie.md)
 * [genotype to disease association➞subject](genotype_to_disease_association_subject.md)  <sub>REQ</sub>
    * Description: a genotype that is associated in some way with a disease state
    * range: [NamedThing](NamedThing.md)

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
 * [provided by](provided_by.md)  <sub>0..*</sub>
    * Description: connects an association to the agent (person, organization or group) that provided it
    * range: [Provider](Provider.md)
 * [publications](publications.md)  <sub>0..*</sub>
    * Description: connects an association to publications supporting the association
    * range: [Publication](Publication.md)
 * [qualifiers](qualifiers.md)  <sub>0..*</sub>
    * Description: connects an association to qualifiers that modify or qualify the meaning of that association
    * range: [OntologyClass](OntologyClass.md)

### Mixed in from frequency qualifier mixin:

 * [frequency qualifier](frequency_qualifier.md)  <sub>OPT</sub>
    * Description: a qualifier used in a phenotypic association to state how frequent the phenotype is observed in the subject
    * range: [FrequencyValue](FrequencyValue.md)

### Mixed in from entity to feature or disease qualifiers:

 * [onset qualifier](onset_qualifier.md)  <sub>OPT</sub>
    * Description: a qualifier used in a phenotypic association to state when the phenotype appears is in the subject
    * range: [Onset](Onset.md)

### Mixed in from entity to feature or disease qualifiers:

 * [severity qualifier](severity_qualifier.md)  <sub>OPT</sub>
    * Description: a qualifier used in a phenotypic association to state how severe the phenotype is in the subject
    * range: [SeverityValue](SeverityValue.md)

## Other properties

|  |  |  |
| --- | --- | --- |
| **Comments:** | | TODO decide no how to model pathogenicity |



# Type: entity to disease association


mixin class for any association whose object (target node) is a disease

URI: [biolink:EntityToDiseaseAssociation](https://w3id.org/biolink/vocab/EntityToDiseaseAssociation)


![img](http://yuml.me/diagram/nofunky;dir:TB/class/[SeverityValue],[Onset],[FrequencyValue],[EntityToFeatureOrDiseaseQualifiers],[Disease]<object%201..1-%20[EntityToDiseaseAssociation],[VariantToDiseaseAssociation]uses%20-.->[EntityToDiseaseAssociation],[GeneToDiseaseAssociation]uses%20-.->[EntityToDiseaseAssociation],[GeneAsAModelOfDiseaseAssociation]uses%20-.->[EntityToDiseaseAssociation],[EntityToFeatureOrDiseaseQualifiers]^-[EntityToDiseaseAssociation],[VariantToDiseaseAssociation],[GeneToDiseaseAssociation],[GeneAsAModelOfDiseaseAssociation],[Disease])

## Parents

 *  is_a: [EntityToFeatureOrDiseaseQualifiers](EntityToFeatureOrDiseaseQualifiers.md) - Qualifiers for entity to disease or phenotype associations

## Mixin for

 * [GeneAsAModelOfDiseaseAssociation](GeneAsAModelOfDiseaseAssociation.md) (mixin) 
 * [GeneToDiseaseAssociation](GeneToDiseaseAssociation.md) (mixin) 
 * [VariantToDiseaseAssociation](VariantToDiseaseAssociation.md) (mixin) 

## Referenced by class


## Attributes


### Own

 * [entity to disease association➞object](entity_to_disease_association_object.md)  <sub>REQ</sub>
    * Description: disease
    * range: [Disease](Disease.md)

### Inherited from entity to feature or disease qualifiers:

 * [frequency qualifier](frequency_qualifier.md)  <sub>OPT</sub>
    * Description: a qualifier used in a phenotypic association to state how frequent the phenotype is observed in the subject
    * range: [FrequencyValue](FrequencyValue.md)
 * [onset qualifier](onset_qualifier.md)  <sub>OPT</sub>
    * Description: a qualifier used in a phenotypic association to state when the phenotype appears is in the subject
    * range: [Onset](Onset.md)
 * [severity qualifier](severity_qualifier.md)  <sub>OPT</sub>
    * Description: a qualifier used in a phenotypic association to state how severe the phenotype is in the subject
    * range: [SeverityValue](SeverityValue.md)

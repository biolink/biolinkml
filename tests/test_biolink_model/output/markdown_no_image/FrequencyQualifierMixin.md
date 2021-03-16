
# Class: FrequencyQualifierMixin


Qualifier for frequency type associations

URI: [biolink:FrequencyQualifierMixin](https://w3id.org/biolink/vocab/FrequencyQualifierMixin)


![img](http://yuml.me/diagram/nofunky;dir:TB/class/[VariantToPopulationAssociation]uses%20-.->[FrequencyQualifierMixin&#124;frequency_qualifier:frequency_value%20%3F],[FrequencyQualifierMixin]^-[EntityToFeatureOrDiseaseQualifiersMixin],[VariantToPopulationAssociation],[EntityToFeatureOrDiseaseQualifiersMixin])

## Children

 * [EntityToFeatureOrDiseaseQualifiersMixin](EntityToFeatureOrDiseaseQualifiersMixin.md) - Qualifiers for entity to disease or phenotype associations.

## Mixin for

 * [VariantToPopulationAssociation](VariantToPopulationAssociation.md) (mixin)  - An association between a variant and a population, where the variant has particular frequency in the population

## Referenced by class


## Attributes


### Own

 * [frequency qualifier](frequency_qualifier.md)  <sub>OPT</sub>
     * Description: a qualifier used in a phenotypic association to state how frequent the phenotype is observed in the subject
     * range: [FrequencyValue](types/FrequencyValue.md)

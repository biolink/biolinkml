
# Type: entity to disease association


mixin class for any association whose object (target node) is a disease

URI: [biolink:EntityToDiseaseAssociation](https://w3id.org/biolink/vocab/EntityToDiseaseAssociation)


![img](http://yuml.me/diagram/nofunky;dir:TB/class/\[VariantToDiseaseAssociation]uses%20-.->\[EntityToDiseaseAssociation],%20\[GeneToDiseaseAssociation]uses%20-.->\[EntityToDiseaseAssociation],%20\[GeneAsAModelOfDiseaseAssociation]uses%20-.->\[EntityToDiseaseAssociation],%20\[EntityToFeatureOrDiseaseQualifiers]^-\[EntityToDiseaseAssociation])

## Parents

 *  is_a: [entity to feature or disease qualifiers](entity to feature or disease qualifiers.md) - Qualifiers for entity to disease or phenotype associations

## Mixin for

 * [gene as a model of disease association](gene as a model of disease association.md) (mixin) 
 * [gene to disease association](gene to disease association.md) (mixin) 
 * [variant to disease association](variant to disease association.md) (mixin) 

## Referenced by class


## Attributes


### Domain for slot:

 * [object](entity_to_disease_association_object.md)  <sub>REQ</sub>
    * range: [disease](disease.md)

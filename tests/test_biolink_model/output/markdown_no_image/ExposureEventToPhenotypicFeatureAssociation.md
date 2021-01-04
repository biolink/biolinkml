
# Type: exposure event to phenotypic feature association


Any association between an environment and a phenotypic feature, where being in the environment influences the phenotype

URI: [biolink:ExposureEventToPhenotypicFeatureAssociation](https://w3id.org/biolink/vocab/ExposureEventToPhenotypicFeatureAssociation)


![img](http://yuml.me/diagram/nofunky;dir:TB/class/[SeverityValue],[Publication],[Provider],[OntologyClass],[Onset],[NamedThing],[FrequencyValue],[ExposureEvent]<subject%201..1-%20[ExposureEventToPhenotypicFeatureAssociation&#124;description:narrative_text%20%3F;relation(i):uriorcurie;id(i):string;negated(i):boolean%20%3F],[ExposureEventToPhenotypicFeatureAssociation]uses%20-.->[EntityToPhenotypicFeatureAssociation],[Association]^-[ExposureEventToPhenotypicFeatureAssociation],[ExposureEvent],[EntityToPhenotypicFeatureAssociation],[BiologicalSex],[Association])

## Parents

 *  is_a: [Association](Association.md) - A typed association between two entities, supported by evidence

## Uses Mixins

 *  mixin: [EntityToPhenotypicFeatureAssociation](EntityToPhenotypicFeatureAssociation.md)

## Referenced by class


## Attributes


### Own

 * [exposure event to phenotypic feature association➞subject](exposure_event_to_phenotypic_feature_association_subject.md)  <sub>REQ</sub>
    * range: [ExposureEvent](ExposureEvent.md)

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

### Mixed in from entity to phenotypic feature association:

 * [entity to phenotypic feature association➞description](entity_to_phenotypic_feature_association_description.md)  <sub>OPT</sub>
    * Description: A description of specific aspects of this phenotype, not otherwise covered by the phenotype ontology class
    * range: [NarrativeText](types/NarrativeText.md)

### Mixed in from entity to phenotypic feature association:

 * [sex qualifier](sex_qualifier.md)  <sub>OPT</sub>
    * Description: a qualifier used in a phenotypic association to state whether the association is specific to a particular sex.
    * range: [BiologicalSex](BiologicalSex.md)

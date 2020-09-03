
# Type: sequence feature relationship


For example, a particular exon is part of a particular transcript or gene

URI: [biolink:SequenceFeatureRelationship](https://w3id.org/biolink/vocab/SequenceFeatureRelationship)


![img](http://yuml.me/diagram/nofunky;dir:TB/class/[TranscriptToGeneRelationship],[GenomicEntity]<object%201..1-%20[SequenceFeatureRelationship&#124;relation(i):uriorcurie;id(i):string;negated(i):boolean%20%3F],[GenomicEntity]<subject%201..1-%20[SequenceFeatureRelationship],[SequenceFeatureRelationship]^-[TranscriptToGeneRelationship],[SequenceFeatureRelationship]^-[GeneToGeneProductRelationship],[SequenceFeatureRelationship]^-[ExonToTranscriptRelationship],[Association]^-[SequenceFeatureRelationship],[Publication],[Provider],[OntologyClass],[GenomicEntity],[GeneToGeneProductRelationship],[ExonToTranscriptRelationship],[Association])

## Parents

 *  is_a: [Association](Association.md) - A typed association between two entities, supported by evidence

## Children

 * [ExonToTranscriptRelationship](ExonToTranscriptRelationship.md) - A transcript is formed from multiple exons
 * [GeneToGeneProductRelationship](GeneToGeneProductRelationship.md) - A gene is transcribed and potentially translated to a gene product
 * [TranscriptToGeneRelationship](TranscriptToGeneRelationship.md) - A gene is a collection of transcripts

## Referenced by class


## Attributes


### Own

 * [sequence feature relationship➞object](sequence_feature_relationship_object.md)  <sub>REQ</sub>
    * range: [GenomicEntity](GenomicEntity.md)
 * [sequence feature relationship➞subject](sequence_feature_relationship_subject.md)  <sub>REQ</sub>
    * range: [GenomicEntity](GenomicEntity.md)

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
 * [relation](relation.md)  <sub>REQ</sub>
    * Description: The relation which describes an association between a subject and an object in a more granular manner. Usually this is a term from Relation Ontology, but it can be any edge CURIE.
    * range: [Uriorcurie](types/Uriorcurie.md)


# Type: exon to transcript relationship


A transcript is formed from multiple exons

URI: [biolink:ExonToTranscriptRelationship](https://w3id.org/biolink/vocab/ExonToTranscriptRelationship)


![img](http://yuml.me/diagram/nofunky;dir:TB/class/\[Provider]<provided%20by(i)%200..1-%20\[ExonToTranscriptRelationship|relation(i):uriorcurie;id(i):nodeidentifier;negated(i):boolean%20%3F],%20\[Publication]<publications(i)%200..*-%20\[ExonToTranscriptRelationship],%20\[OntologyClass]<qualifiers(i)%200..*-%20\[ExonToTranscriptRelationship],%20\[OntologyClass]<association%20type(i)%200..1-%20\[ExonToTranscriptRelationship],%20\[Transcript]<object%201..1-%20\[ExonToTranscriptRelationship],%20\[Exon]<subject%201..1-%20\[ExonToTranscriptRelationship],%20\[SequenceFeatureRelationship]^-\[ExonToTranscriptRelationship])

## Parents

 *  is_a: [sequence feature relationship](sequence feature relationship.md) - For example, a particular exon is part of a particular transcript or gene

## Referenced by class


## Attributes


### Own

 * [object](exon_to_transcript_relationship_object.md)  <sub>REQ</sub>
    * range: [transcript](transcript.md)
 * [subject](exon_to_transcript_relationship_subject.md)  <sub>REQ</sub>
    * range: [exon](exon.md)

### Inherited from association:

 * [subject](subject.md)  <sub>REQ</sub>
    * Description: connects an association to the subject of the association. For example, in a gene-to-phenotype association, the gene is subject and phenotype is object.
    * range: [named thing](named thing.md)
    * inherited from: [association](association.md)
 * [relation](relation.md)  <sub>REQ</sub>
    * Description: the relationship type by which a subject is connected to an object in an association
    * range: [Uriorcurie](type/Uriorcurie.md)
    * inherited from: [association](association.md)
 * [object](object.md)  <sub>REQ</sub>
    * Description: connects an association to the object of the association. For example, in a gene-to-phenotype association, the gene is subject and phenotype is object.
    * range: [named thing](named thing.md)
    * inherited from: [association](association.md)
 * [id](association_id.md)  <sub>REQ</sub>
    * Description: A unique identifier for an association
    * range: [Nodeidentifier](type/Nodeidentifier.md)
    * inherited from: [association](association.md)
    * in subsets: (translator_minimal)
 * [negated](negated.md)  <sub>OPT</sub>
    * Description: if set to true, then the association is negated i.e. is not true
    * range: [Boolean](type/Boolean.md)
    * inherited from: [association](association.md)
 * [association type](association_type.md)  <sub>OPT</sub>
    * Description: connects an association to the type of association (e.g. gene to phenotype)
    * range: [ontology class](ontology class.md)
    * inherited from: [association](association.md)
 * [qualifiers](qualifiers.md)  <sub>0..*</sub>
    * Description: connects an association to qualifiers that modify or qualify the meaning of that association
    * range: [ontology class](ontology class.md)
    * inherited from: [association](association.md)
 * [publications](publications.md)  <sub>0..*</sub>
    * Description: connects an association to publications supporting the association
    * range: [publication](publication.md)
    * inherited from: [association](association.md)
 * [provided by](provided_by.md)  <sub>OPT</sub>
    * Description: connects an association to the agent (person, organization or group) that provided it
    * range: [provider](provider.md)
    * inherited from: [association](association.md)

### Domain for slot:

 * [object](exon_to_transcript_relationship_object.md)  <sub>REQ</sub>
    * range: [transcript](transcript.md)
 * [subject](exon_to_transcript_relationship_subject.md)  <sub>REQ</sub>
    * range: [exon](exon.md)


# Type: transcript


An RNA synthesized on a DNA or RNA template by an RNA polymerase

URI: [biolink:Transcript](https://w3id.org/biolink/vocab/Transcript)


![img](http://yuml.me/diagram/nofunky;dir:TB/class/\[OrganismTaxon]<in%20taxon(i)%200..*-%20\[Transcript|id(i):identifier_type;name(i):label_type;category(i):iri_type%20%2B],%20\[ExonToTranscriptRelationship]-%20object%201..1>\[Transcript],%20\[TranscriptToGeneRelationship]-%20subject%201..1>\[Transcript],%20\[GenomicEntity]^-\[Transcript])

## Parents

 *  is_a: [genomic entity](genomic entity.md) - an entity that can either be directly located on a genome (gene, transcript, exon, regulatory region) or is encoded in a genome (protein)

## Referenced by class

 *  **[molecular entity](molecular entity.md)** *[affects splicing of](affects_splicing_of.md)*  <sub>0..*</sub>  **[transcript](transcript.md)**
 *  **[molecular entity](molecular entity.md)** *[decreases splicing of](decreases_splicing_of.md)*  <sub>0..*</sub>  **[transcript](transcript.md)**
 *  **[exon to transcript relationship](exon to transcript relationship.md)** *[object](exon_to_transcript_relationship_object.md)*  <sub>REQ</sub>  **[transcript](transcript.md)**
 *  **[molecular entity](molecular entity.md)** *[increases splicing of](increases_splicing_of.md)*  <sub>0..*</sub>  **[transcript](transcript.md)**
 *  **[transcript to gene relationship](transcript to gene relationship.md)** *[subject](transcript_to_gene_relationship_subject.md)*  <sub>REQ</sub>  **[transcript](transcript.md)**

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
| **Mappings:** | | SO:0000673 |
|  | | SIO:010450 |


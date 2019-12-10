
# Type: genomic entity


an entity that can either be directly located on a genome (gene, transcript, exon, regulatory region) or is encoded in a genome (protein)

URI: [biolink:GenomicEntity](https://w3id.org/biolink/vocab/GenomicEntity)


![img](http://yuml.me/diagram/nofunky;dir:TB/class/\[OrganismTaxon]<in%20taxon(i)%200..*-%20\[GenomicEntity&#124;id(i):identifier_type;name(i):label_type;category(i):iri_type%20%2B],%20\[GenomicSequenceLocalization]-%20object%201..1>\[GenomicEntity],%20\[GenomicSequenceLocalization]-%20subject%201..1>\[GenomicEntity],%20\[SequenceFeatureRelationship]-%20object%201..1>\[GenomicEntity],%20\[SequenceFeatureRelationship]-%20subject%201..1>\[GenomicEntity],%20\[GenomicEntity]^-\[Transcript],%20\[GenomicEntity]^-\[SequenceVariant],%20\[GenomicEntity]^-\[MacromolecularMachine],%20\[GenomicEntity]^-\[Haplotype],%20\[GenomicEntity]^-\[Genotype],%20\[GenomicEntity]^-\[Genome],%20\[GenomicEntity]^-\[Exon],%20\[GenomicEntity]^-\[CodingSequence],%20\[MolecularEntity]^-\[GenomicEntity])

## Parents

 *  is_a: [molecular entity](molecular entity.md) - A gene, gene product, small molecule or macromolecule (including protein complex)

## Children

 * [coding sequence](coding sequence.md)
 * [exon](exon.md) - A region of the transcript sequence within a gene which is not removed from the primary RNA transcript by RNA splicing
 * [genome](genome.md) - A genome is the sum of genetic material within a cell or virion.
 * [genotype](genotype.md) - An information content entity that describes a genome by specifying the total variation in genomic sequence and/or gene expression, relative to some extablished background
 * [haplotype](haplotype.md) - A set of zero or more Alleles on a single instance of a Sequence[VMC]
 * [macromolecular machine](macromolecular machine.md) - A union of gene, gene product, and macromolecular complex. These are the basic units of function in a cell. They either carry out individual biological activities, or they encode molecules which do this.
 * [sequence variant](sequence variant.md) - An allele that varies in its sequence from what is considered the reference allele at that locus.
 * [transcript](transcript.md) - An RNA synthesized on a DNA or RNA template by an RNA polymerase

## Referenced by class

 *  **[molecular entity](molecular entity.md)** *[affects expression of](affects_expression_of.md)*  <sub>0..*</sub>  **[genomic entity](genomic entity.md)**
 *  **[molecular entity](molecular entity.md)** *[affects mutation rate of](affects_mutation_rate_of.md)*  <sub>0..*</sub>  **[genomic entity](genomic entity.md)**
 *  **[molecular entity](molecular entity.md)** *[decreases expression of](decreases_expression_of.md)*  <sub>0..*</sub>  **[genomic entity](genomic entity.md)**
 *  **[molecular entity](molecular entity.md)** *[decreases mutation rate of](decreases_mutation_rate_of.md)*  <sub>0..*</sub>  **[genomic entity](genomic entity.md)**
 *  **[genomic sequence localization](genomic sequence localization.md)** *[genomic sequence localization➞object](genomic_sequence_localization_object.md)*  <sub>REQ</sub>  **[genomic entity](genomic entity.md)**
 *  **[genomic sequence localization](genomic sequence localization.md)** *[genomic sequence localization➞subject](genomic_sequence_localization_subject.md)*  <sub>REQ</sub>  **[genomic entity](genomic entity.md)**
 *  **[molecular entity](molecular entity.md)** *[increases expression of](increases_expression_of.md)*  <sub>0..*</sub>  **[genomic entity](genomic entity.md)**
 *  **[molecular entity](molecular entity.md)** *[increases mutation rate of](increases_mutation_rate_of.md)*  <sub>0..*</sub>  **[genomic entity](genomic entity.md)**
 *  **[sequence feature relationship](sequence feature relationship.md)** *[sequence feature relationship➞object](sequence_feature_relationship_object.md)*  <sub>REQ</sub>  **[genomic entity](genomic entity.md)**
 *  **[sequence feature relationship](sequence feature relationship.md)** *[sequence feature relationship➞subject](sequence_feature_relationship_subject.md)*  <sub>REQ</sub>  **[genomic entity](genomic entity.md)**

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
| **Aliases:** | | sequence feature |
| **Mappings:** | | SO:0000110 |
|  | | UMLSSC:T028 |
|  | | UMLSST:gngm |
|  | | UMLSSC:T086 |
|  | | UMLSST:nusq |



# Type: gene




URI: [biolink:Gene](https://w3id.org/biolink/vocab/Gene)


![img](http://yuml.me/diagram/nofunky;dir:TB/class/[TranscriptToGeneRelationship],[SequenceVariant],[OrganismTaxon],[NamedThing],[GenotypeToGeneAssociation],[GeneToGeneProductRelationship],[GeneOrGeneProduct],[GeneToGeneProductRelationship]-%20subject%201..1>[Gene&#124;name(i):symbol_type;has_biological_sequence(i):biological_sequence%20%3F;id(i):string;category(i):iri_type%20%2B],[GenotypeToGeneAssociation]-%20object%201..1>[Gene],[SequenceVariant]-%20has%20gene(i)%200..1>[Gene],[SequenceVariant]-%20has%20gene%200..*>[Gene],[TranscriptToGeneRelationship]-%20object%201..1>[Gene],[GeneOrGeneProduct]^-[Gene])

## Parents

 *  is_a: [GeneOrGeneProduct](GeneOrGeneProduct.md) - a union of genes or gene products. Frequently an identifier for one will be used as proxy for another

## Referenced by class

 *  **[GeneToGeneProductRelationship](GeneToGeneProductRelationship.md)** *[gene to gene product relationship➞subject](gene_to_gene_product_relationship_subject.md)*  <sub>REQ</sub>  **[Gene](Gene.md)**
 *  **[Gene](Gene.md)** *[genetically interacts with](genetically_interacts_with.md)*  <sub>0..*</sub>  **[Gene](Gene.md)**
 *  **[GenotypeToGeneAssociation](GenotypeToGeneAssociation.md)** *[genotype to gene association➞object](genotype_to_gene_association_object.md)*  <sub>REQ</sub>  **[Gene](Gene.md)**
 *  **[NamedThing](NamedThing.md)** *[has gene](has_gene.md)*  <sub>OPT</sub>  **[Gene](Gene.md)**
 *  **[SequenceVariant](SequenceVariant.md)** *[sequence variant➞has gene](sequence_variant_has_gene.md)*  <sub>0..*</sub>  **[Gene](Gene.md)**
 *  **[TranscriptToGeneRelationship](TranscriptToGeneRelationship.md)** *[transcript to gene relationship➞object](transcript_to_gene_relationship_object.md)*  <sub>REQ</sub>  **[Gene](Gene.md)**

## Attributes


### Inherited from gene or gene product:

 * [category](category.md)  <sub>1..*</sub>
    * Description: Name of the high level ontology class in which this entity is categorized. Corresponds to the label for the biolink entity type class. In a neo4j database this MAY correspond to the neo4j label tag
    * range: [IriType](types/IriType.md)
    * in subsets: (translator_minimal)
 * [has biological sequence](has_biological_sequence.md)  <sub>OPT</sub>
    * Description: connects a genomic feature to its sequence
    * range: [BiologicalSequence](types/BiologicalSequence.md)
 * [id](id.md)  <sub>REQ</sub>
    * Description: A unique identifier for a thing. Must be either a CURIE shorthand for a URI or a complete URI
    * range: [String](types/String.md)
    * in subsets: (translator_minimal)
 * [macromolecular machine➞name](macromolecular_machine_name.md)  <sub>REQ</sub>
    * range: [SymbolType](types/SymbolType.md)

## Other properties

|  |  |  |
| --- | --- | --- |
| **Aliases:** | | locus |
| **Mappings:** | | SO:0000704 |
|  | | SIO:010035 |
|  | | WD:Q7187 |


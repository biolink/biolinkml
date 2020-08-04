
# Type: sequence variant


An allele that varies in its sequence from what is considered the reference allele at that locus.

URI: [biolink:SequenceVariant](https://w3id.org/biolink/vocab/SequenceVariant)


![img](http://yuml.me/diagram/nofunky;dir:TB/class/[VariantToThingAssociation],[VariantToPopulationAssociation],[VariantToPhenotypicFeatureAssociation],[SequenceVariantModulatesTreatmentAssociation],[Gene]<has%20gene%200..*-%20[SequenceVariant&#124;has_biological_sequence:biological_sequence%20%3F;id:string;name(i):label_type;category(i):iri_type%20%2B],[GenotypeToVariantAssociation]-%20object%201..1>[SequenceVariant],[SequenceVariantModulatesTreatmentAssociation]-%20subject%201..1>[SequenceVariant],[GeneHasVariantThatContributesToDiseaseAssociation]-%20sequence%20variant%20qualifier%200..1>[SequenceVariant],[VariantToPhenotypicFeatureAssociation]-%20subject%201..1>[SequenceVariant],[VariantToPopulationAssociation]-%20subject%201..1>[SequenceVariant],[VariantToThingAssociation]-%20subject%201..1>[SequenceVariant],[GenomicEntity]^-[SequenceVariant],[OrganismTaxon],[GenotypeToVariantAssociation],[GenomicEntity],[GeneHasVariantThatContributesToDiseaseAssociation],[Gene],[Association])

## Parents

 *  is_a: [GenomicEntity](GenomicEntity.md) - an entity that can either be directly located on a genome (gene, transcript, exon, regulatory region) or is encoded in a genome (protein)

## Referenced by class

 *  **[GenotypeToVariantAssociation](GenotypeToVariantAssociation.md)** *[genotype to variant association➞object](genotype_to_variant_association_object.md)*  <sub>REQ</sub>  **[SequenceVariant](SequenceVariant.md)**
 *  **[SequenceVariantModulatesTreatmentAssociation](SequenceVariantModulatesTreatmentAssociation.md)** *[sequence variant modulates treatment association➞subject](sequence_variant_modulates_treatment_association_subject.md)*  <sub>REQ</sub>  **[SequenceVariant](SequenceVariant.md)**
 *  **[Association](Association.md)** *[sequence variant qualifier](sequence_variant_qualifier.md)*  <sub>OPT</sub>  **[SequenceVariant](SequenceVariant.md)**
 *  **[VariantToPhenotypicFeatureAssociation](VariantToPhenotypicFeatureAssociation.md)** *[variant to phenotypic feature association➞subject](variant_to_phenotypic_feature_association_subject.md)*  <sub>REQ</sub>  **[SequenceVariant](SequenceVariant.md)**
 *  **[VariantToPopulationAssociation](VariantToPopulationAssociation.md)** *[variant to population association➞subject](variant_to_population_association_subject.md)*  <sub>REQ</sub>  **[SequenceVariant](SequenceVariant.md)**
 *  **[VariantToThingAssociation](VariantToThingAssociation.md)** *[variant to thing association➞subject](variant_to_thing_association_subject.md)*  <sub>REQ</sub>  **[SequenceVariant](SequenceVariant.md)**

## Attributes


### Own

 * [sequence variant➞has biological sequence](sequence_variant_has_biological_sequence.md)  <sub>OPT</sub>
    * Description: The state of the sequence w.r.t a reference sequence
    * range: [BiologicalSequence](types/BiologicalSequence.md)
 * [sequence variant➞has gene](sequence_variant_has_gene.md)  <sub>0..*</sub>
    * Description: Each allele can be associated with any number of genes
    * range: [Gene](Gene.md)
 * [sequence variant➞id](sequence_variant_id.md)  <sub>REQ</sub>
    * range: [String](types/String.md)

### Inherited from genomic entity:

 * [category](category.md)  <sub>1..*</sub>
    * Description: Name of the high level ontology class in which this entity is categorized. Corresponds to the label for the biolink entity type class. In a neo4j database this MAY correspond to the neo4j label tag
    * range: [IriType](types/IriType.md)
    * in subsets: (translator_minimal)
 * [name](name.md)  <sub>REQ</sub>
    * Description: A human-readable name for a thing
    * range: [LabelType](types/LabelType.md)
    * in subsets: (translator_minimal)

## Other properties

|  |  |  |
| --- | --- | --- |
| **Aliases:** | | allele |
| **Local names:** | | allele (agr) |
| **Mappings:** | | GENO:0000002 |
|  | | WD:Q15304597 |
|  | | SIO:010277 |
|  | | VMC:Allele |
| **Alt Descriptions:** | | An enitity that describes a single affected, endogenous allele.  These can be of any type that matches that definition (AGR) |
|  | | A contiguous change at a Location (VMC) |
| **Comments:** | | This class is for modeling the specific state at a locus. A single dbSNP rs ID could correspond to more than one sequence variants (e.g CIViC:1252 and CIViC:1253, two distinct BRCA2 alleles for rs28897743) |


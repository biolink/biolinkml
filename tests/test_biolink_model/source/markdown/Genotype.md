
# Type: genotype


An information content entity that describes a genome by specifying the total variation in genomic sequence and/or gene expression, relative to some extablished background

URI: [biolink:Genotype](https://w3id.org/biolink/vocab/Genotype)


![img](http://yuml.me/diagram/nofunky;dir:TB/class/\[OrganismTaxon]<in%20taxon(i)%200..*-%20\[Genotype|id(i):identifier_type;name(i):label_type;category(i):iri_type%20%2B],%20\[GenotypeToGeneAssociation]-%20subject%201..1>\[Genotype],%20\[GenotypeToGenotypePartAssociation]-%20object%201..1>\[Genotype],%20\[GenotypeToGenotypePartAssociation]-%20subject%201..1>\[Genotype],%20\[GenotypeToPhenotypicFeatureAssociation]-%20subject%201..1>\[Genotype],%20\[GenotypeToThingAssociation]-%20subject%201..1>\[Genotype],%20\[GenotypeToVariantAssociation]-%20subject%201..1>\[Genotype],%20\[GenomicEntity]^-\[Genotype])

## Parents

 *  is_a: [genomic entity](genomic entity.md) - an entity that can either be directly located on a genome (gene, transcript, exon, regulatory region) or is encoded in a genome (protein)

## Referenced by class

 *  **[genotype to gene association](genotype to gene association.md)** *[subject](genotype_to_gene_association_subject.md)*  <sub>REQ</sub>  **[genotype](genotype.md)**
 *  **[genotype to genotype part association](genotype to genotype part association.md)** *[object](genotype_to_genotype_part_association_object.md)*  <sub>REQ</sub>  **[genotype](genotype.md)**
 *  **[genotype to genotype part association](genotype to genotype part association.md)** *[subject](genotype_to_genotype_part_association_subject.md)*  <sub>REQ</sub>  **[genotype](genotype.md)**
 *  **[genotype to phenotypic feature association](genotype to phenotypic feature association.md)** *[subject](genotype_to_phenotypic_feature_association_subject.md)*  <sub>REQ</sub>  **[genotype](genotype.md)**
 *  **[genotype to thing association](genotype to thing association.md)** *[subject](genotype_to_thing_association_subject.md)*  <sub>REQ</sub>  **[genotype](genotype.md)**
 *  **[genotype to variant association](genotype to variant association.md)** *[subject](genotype_to_variant_association_subject.md)*  <sub>REQ</sub>  **[genotype](genotype.md)**

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
| **Mappings:** | | GENO:0000536 |
|  | | SIO:001079 |
| **Comments:** | | Consider renaming as genotypic entity |


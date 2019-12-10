
# Type: molecular entity


A gene, gene product, small molecule or macromolecule (including protein complex)

URI: [biolink:MolecularEntity](https://w3id.org/biolink/vocab/MolecularEntity)


![img](http://yuml.me/diagram/nofunky;dir:TB/class/\[OrganismTaxon]<in%20taxon%200..*-%20\[MolecularEntity&#124;id(i):identifier_type;name(i):label_type;category(i):iri_type%20%2B],%20\[GeneToGoTermAssociation]-%20subject%201..1>\[MolecularEntity],%20\[PairwiseInteractionAssociation]-%20object%201..1>\[MolecularEntity],%20\[PairwiseInteractionAssociation]-%20subject%201..1>\[MolecularEntity],%20\[MolecularEntity]uses%20-.->\[ThingWithTaxon],%20\[MolecularEntity]uses%20-.->\[PhysicalEntity],%20\[MolecularEntity]^-\[GenomicEntity],%20\[MolecularEntity]^-\[GeneFamily],%20\[MolecularEntity]^-\[ChemicalSubstance],%20\[BiologicalEntity]^-\[MolecularEntity])

## Parents

 *  is_a: [biological entity](biological entity.md)

## Uses Mixins

 *  mixin: [thing with taxon](thing with taxon.md) - A mixin that can be used on any entity with a taxon
 *  mixin: [physical entity](physical entity.md) - An entity that has physical properties such as mass, volume, or charge

## Children

 * [chemical substance](chemical substance.md) - May be a chemical entity or a formulation with a chemical entity as active ingredient, or a complex material with multiple chemical entities as part
 * [gene family](gene family.md) - any grouping of multiple genes or gene products related by common descent
 * [genomic entity](genomic entity.md) - an entity that can either be directly located on a genome (gene, transcript, exon, regulatory region) or is encoded in a genome (protein)

## Referenced by class

 *  **[molecular entity](molecular entity.md)** *[affects abundance of](affects_abundance_of.md)*  <sub>0..*</sub>  **[molecular entity](molecular entity.md)**
 *  **[molecular entity](molecular entity.md)** *[affects activity of](affects_activity_of.md)*  <sub>0..*</sub>  **[molecular entity](molecular entity.md)**
 *  **[molecular entity](molecular entity.md)** *[affects degradation of](affects_degradation_of.md)*  <sub>0..*</sub>  **[molecular entity](molecular entity.md)**
 *  **[molecular entity](molecular entity.md)** *[affects folding of](affects_folding_of.md)*  <sub>0..*</sub>  **[molecular entity](molecular entity.md)**
 *  **[molecular entity](molecular entity.md)** *[affects localization of](affects_localization_of.md)*  <sub>0..*</sub>  **[molecular entity](molecular entity.md)**
 *  **[molecular entity](molecular entity.md)** *[affects metabolic processing of](affects_metabolic_processing_of.md)*  <sub>0..*</sub>  **[molecular entity](molecular entity.md)**
 *  **[molecular entity](molecular entity.md)** *[affects molecular modification of](affects_molecular_modification_of.md)*  <sub>0..*</sub>  **[molecular entity](molecular entity.md)**
 *  **[molecular entity](molecular entity.md)** *[affects response to](affects_response_to.md)*  <sub>0..*</sub>  **[molecular entity](molecular entity.md)**
 *  **[molecular entity](molecular entity.md)** *[affects secretion of](affects_secretion_of.md)*  <sub>0..*</sub>  **[molecular entity](molecular entity.md)**
 *  **[molecular entity](molecular entity.md)** *[affects stability of](affects_stability_of.md)*  <sub>0..*</sub>  **[molecular entity](molecular entity.md)**
 *  **[molecular entity](molecular entity.md)** *[affects synthesis of](affects_synthesis_of.md)*  <sub>0..*</sub>  **[molecular entity](molecular entity.md)**
 *  **[molecular entity](molecular entity.md)** *[affects transport of](affects_transport_of.md)*  <sub>0..*</sub>  **[molecular entity](molecular entity.md)**
 *  **[molecular entity](molecular entity.md)** *[affects uptake of](affects_uptake_of.md)*  <sub>0..*</sub>  **[molecular entity](molecular entity.md)**
 *  **[disease or phenotypic feature](disease or phenotypic feature.md)** *[correlated with](correlated_with.md)*  <sub>0..*</sub>  **[molecular entity](molecular entity.md)**
 *  **[molecular entity](molecular entity.md)** *[decreases abundance of](decreases_abundance_of.md)*  <sub>0..*</sub>  **[molecular entity](molecular entity.md)**
 *  **[molecular entity](molecular entity.md)** *[decreases activity of](decreases_activity_of.md)*  <sub>0..*</sub>  **[molecular entity](molecular entity.md)**
 *  **[molecular entity](molecular entity.md)** *[decreases degradation of](decreases_degradation_of.md)*  <sub>0..*</sub>  **[molecular entity](molecular entity.md)**
 *  **[molecular entity](molecular entity.md)** *[decreases folding of](decreases_folding_of.md)*  <sub>0..*</sub>  **[molecular entity](molecular entity.md)**
 *  **[molecular entity](molecular entity.md)** *[decreases localization of](decreases_localization_of.md)*  <sub>0..*</sub>  **[molecular entity](molecular entity.md)**
 *  **[molecular entity](molecular entity.md)** *[decreases metabolic processing of](decreases_metabolic_processing_of.md)*  <sub>0..*</sub>  **[molecular entity](molecular entity.md)**
 *  **[molecular entity](molecular entity.md)** *[decreases molecular modification of](decreases_molecular_modification_of.md)*  <sub>0..*</sub>  **[molecular entity](molecular entity.md)**
 *  **[molecular entity](molecular entity.md)** *[decreases response to](decreases_response_to.md)*  <sub>0..*</sub>  **[molecular entity](molecular entity.md)**
 *  **[molecular entity](molecular entity.md)** *[decreases secretion of](decreases_secretion_of.md)*  <sub>0..*</sub>  **[molecular entity](molecular entity.md)**
 *  **[molecular entity](molecular entity.md)** *[decreases stability of](decreases_stability_of.md)*  <sub>0..*</sub>  **[molecular entity](molecular entity.md)**
 *  **[molecular entity](molecular entity.md)** *[decreases synthesis of](decreases_synthesis_of.md)*  <sub>0..*</sub>  **[molecular entity](molecular entity.md)**
 *  **[molecular entity](molecular entity.md)** *[decreases transport of](decreases_transport_of.md)*  <sub>0..*</sub>  **[molecular entity](molecular entity.md)**
 *  **[molecular entity](molecular entity.md)** *[decreases uptake of](decreases_uptake_of.md)*  <sub>0..*</sub>  **[molecular entity](molecular entity.md)**
 *  **[gene to go term association](gene to go term association.md)** *[gene to go term association➞subject](gene_to_go_term_association_subject.md)*  <sub>REQ</sub>  **[molecular entity](molecular entity.md)**
 *  **[disease or phenotypic feature](disease or phenotypic feature.md)** *[has biomarker](has_biomarker.md)*  <sub>0..*</sub>  **[molecular entity](molecular entity.md)**
 *  **[molecular entity](molecular entity.md)** *[increases abundance of](increases_abundance_of.md)*  <sub>0..*</sub>  **[molecular entity](molecular entity.md)**
 *  **[molecular entity](molecular entity.md)** *[increases activity of](increases_activity_of.md)*  <sub>0..*</sub>  **[molecular entity](molecular entity.md)**
 *  **[molecular entity](molecular entity.md)** *[increases degradation of](increases_degradation_of.md)*  <sub>0..*</sub>  **[molecular entity](molecular entity.md)**
 *  **[molecular entity](molecular entity.md)** *[increases folding of](increases_folding_of.md)*  <sub>0..*</sub>  **[molecular entity](molecular entity.md)**
 *  **[molecular entity](molecular entity.md)** *[increases localization of](increases_localization_of.md)*  <sub>0..*</sub>  **[molecular entity](molecular entity.md)**
 *  **[molecular entity](molecular entity.md)** *[increases metabolic processing of](increases_metabolic_processing_of.md)*  <sub>0..*</sub>  **[molecular entity](molecular entity.md)**
 *  **[molecular entity](molecular entity.md)** *[increases molecular modification of](increases_molecular_modification_of.md)*  <sub>0..*</sub>  **[molecular entity](molecular entity.md)**
 *  **[molecular entity](molecular entity.md)** *[increases response to](increases_response_to.md)*  <sub>0..*</sub>  **[molecular entity](molecular entity.md)**
 *  **[molecular entity](molecular entity.md)** *[increases secretion of](increases_secretion_of.md)*  <sub>0..*</sub>  **[molecular entity](molecular entity.md)**
 *  **[molecular entity](molecular entity.md)** *[increases stability of](increases_stability_of.md)*  <sub>0..*</sub>  **[molecular entity](molecular entity.md)**
 *  **[molecular entity](molecular entity.md)** *[increases synthesis of](increases_synthesis_of.md)*  <sub>0..*</sub>  **[molecular entity](molecular entity.md)**
 *  **[molecular entity](molecular entity.md)** *[increases transport of](increases_transport_of.md)*  <sub>0..*</sub>  **[molecular entity](molecular entity.md)**
 *  **[molecular entity](molecular entity.md)** *[increases uptake of](increases_uptake_of.md)*  <sub>0..*</sub>  **[molecular entity](molecular entity.md)**
 *  **[molecular entity](molecular entity.md)** *[molecularly interacts with](molecularly_interacts_with.md)*  <sub>0..*</sub>  **[molecular entity](molecular entity.md)**
 *  **[molecular entity](molecular entity.md)** *[negatively regulates, entity to entity](negatively_regulates_entity_to_entity.md)*  <sub>0..*</sub>  **[molecular entity](molecular entity.md)**
 *  **[pairwise interaction association](pairwise interaction association.md)** *[pairwise interaction association➞object](pairwise_interaction_association_object.md)*  <sub>REQ</sub>  **[molecular entity](molecular entity.md)**
 *  **[pairwise interaction association](pairwise interaction association.md)** *[pairwise interaction association➞subject](pairwise_interaction_association_subject.md)*  <sub>REQ</sub>  **[molecular entity](molecular entity.md)**
 *  **[molecular entity](molecular entity.md)** *[positively regulates, entity to entity](positively_regulates_entity_to_entity.md)*  <sub>0..*</sub>  **[molecular entity](molecular entity.md)**
 *  **[molecular entity](molecular entity.md)** *[regulates, entity to entity](regulates_entity_to_entity.md)*  <sub>0..*</sub>  **[molecular entity](molecular entity.md)**

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
    * in subsets: (translator_minimal)

### Domain for slot:

 * [affects abundance of](affects_abundance_of.md)  <sub>0..*</sub>
    * Description: holds between two molecular entities where the action or effect of one changes the amount of the other within a system of interest
    * range: [molecular entity](molecular entity.md)
    * in subsets: (translator_minimal)
 * [affects activity of](affects_activity_of.md)  <sub>0..*</sub>
    * Description: holds between two molecular entities where the action or effect of one changes the activity of the other within a system of interest
    * range: [molecular entity](molecular entity.md)
    * in subsets: (translator_minimal)
 * [affects degradation of](affects_degradation_of.md)  <sub>0..*</sub>
    * Description: holds between two molecular entities where the action or effect of one impacts the rate of degradation of the other within a system of interest
    * range: [molecular entity](molecular entity.md)
    * in subsets: (translator_minimal)
 * [affects expression of](affects_expression_of.md)  <sub>0..*</sub>
    * Description: holds between two molecular entities where the action or effect of one changes the level of expression of the other within a system of interest
    * range: [genomic entity](genomic entity.md)
    * in subsets: (translator_minimal)
 * [affects folding of](affects_folding_of.md)  <sub>0..*</sub>
    * Description: holds between two molecular entities where the action or effect of one changes the rate or quality of folding of the other
    * range: [molecular entity](molecular entity.md)
    * in subsets: (translator_minimal)
 * [affects localization of](affects_localization_of.md)  <sub>0..*</sub>
    * Description: holds between two molecular entities where the action or effect of one changes the localization of the other within a system of interest
    * range: [molecular entity](molecular entity.md)
    * in subsets: (translator_minimal)
 * [affects metabolic processing of](affects_metabolic_processing_of.md)  <sub>0..*</sub>
    * Description: holds between two molecular entities where the action or effect of one impacts the metabolic processing of the other within a system of interest
    * range: [molecular entity](molecular entity.md)
    * in subsets: (translator_minimal)
 * [affects molecular modification of](affects_molecular_modification_of.md)  <sub>0..*</sub>
    * Description: holds between two molecular entities where the action or effect of one leads changes in the molecular modification(s) of the other (e.g. via post-translational modifications of proteins such as the addition of phosphoryl group, or via redox reaction that adds or subtracts electrons)
    * range: [molecular entity](molecular entity.md)
    * in subsets: (translator_minimal)
 * [affects mutation rate of](affects_mutation_rate_of.md)  <sub>0..*</sub>
    * Description: holds between a molecular entity and a genomic entity where the action or effect of the molecular entity impacts the rate of mutation of the genomic entity within a system of interest
    * range: [genomic entity](genomic entity.md)
    * in subsets: (translator_minimal)
 * [affects response to](affects_response_to.md)  <sub>0..*</sub>
    * Description: holds between two molecular entities where the action or effect of one impacts the susceptibility of a biological entity or system (e.g. an organism, cell, cellular component, macromolecular machine, biological or pathological process) to the other
    * range: [molecular entity](molecular entity.md)
    * in subsets: (translator_minimal)
 * [affects secretion of](affects_secretion_of.md)  <sub>0..*</sub>
    * Description: holds between two molecular entities where the action or effect of one impacts the rate of secretion of the other out of a cell, gland, or organ
    * range: [molecular entity](molecular entity.md)
    * in subsets: (translator_minimal)
 * [affects splicing of](affects_splicing_of.md)  <sub>0..*</sub>
    * Description: holds between a molecular entity and an mRNA where the action or effect of the molecular entity impacts the splicing of the mRNA
    * range: [transcript](transcript.md)
    * in subsets: (translator_minimal)
 * [affects stability of](affects_stability_of.md)  <sub>0..*</sub>
    * Description: holds between two molecular entities where the action or effect of one impacts the stability of the other within a system of interest
    * range: [molecular entity](molecular entity.md)
    * in subsets: (translator_minimal)
 * [affects synthesis of](affects_synthesis_of.md)  <sub>0..*</sub>
    * Description: holds between two molecular entities where the action or effect of one impacts the rate of chemical synthesis of the other
    * range: [molecular entity](molecular entity.md)
    * in subsets: (translator_minimal)
 * [affects transport of](affects_transport_of.md)  <sub>0..*</sub>
    * Description: holds between two molecular entities where the action or effect of one impacts the rate of transport of the other across some boundary in a system of interest
    * range: [molecular entity](molecular entity.md)
    * in subsets: (translator_minimal)
 * [affects uptake of](affects_uptake_of.md)  <sub>0..*</sub>
    * Description: holds between two molecular entities where the action or effect of one impacts the rate of uptake of the other into of a cell, gland, or organ
    * range: [molecular entity](molecular entity.md)
    * in subsets: (translator_minimal)
 * [biomarker for](biomarker_for.md)  <sub>0..*</sub>
    * Description: holds between a measurable molecular entity and a disease or phenotypic feature, where the entity is used as an indicator of the presence or state of the disease or feature.
    * range: [disease or phenotypic feature](disease or phenotypic feature.md)
    * in subsets: (translator_minimal)
 * [decreases abundance of](decreases_abundance_of.md)  <sub>0..*</sub>
    * Description: holds between two molecular entities where the action or effect of one decreases the amount of the other within a system of interest
    * range: [molecular entity](molecular entity.md)
    * in subsets: (translator_minimal)
 * [decreases activity of](decreases_activity_of.md)  <sub>0..*</sub>
    * Description: holds between two molecular entities where the action or effect of one decreases the activity of the other within a system of interest
    * range: [molecular entity](molecular entity.md)
    * in subsets: (translator_minimal)
 * [decreases degradation of](decreases_degradation_of.md)  <sub>0..*</sub>
    * Description: holds between two molecular entities where the action or effect of one decreases the rate of degradation of the other within a system of interest
    * range: [molecular entity](molecular entity.md)
    * in subsets: (translator_minimal)
 * [decreases expression of](decreases_expression_of.md)  <sub>0..*</sub>
    * Description: holds between two molecular entities where the action or effect of one decreases the level of expression of the other within a system of interest
    * range: [genomic entity](genomic entity.md)
    * in subsets: (translator_minimal)
 * [decreases folding of](decreases_folding_of.md)  <sub>0..*</sub>
    * Description: holds between two molecular entities where the action or effect of one decreases the rate or quality of folding of the other
    * range: [molecular entity](molecular entity.md)
    * in subsets: (translator_minimal)
 * [decreases localization of](decreases_localization_of.md)  <sub>0..*</sub>
    * Description: holds between two molecular entities where the action or effect of one decreases the proper localization of the other within a system of interest
    * range: [molecular entity](molecular entity.md)
    * in subsets: (translator_minimal)
 * [decreases metabolic processing of](decreases_metabolic_processing_of.md)  <sub>0..*</sub>
    * Description: holds between two molecular entities where the action or effect of one decreases the rate of metabolic processing of the other within a system of interest
    * range: [molecular entity](molecular entity.md)
    * in subsets: (translator_minimal)
 * [decreases molecular modification of](decreases_molecular_modification_of.md)  <sub>0..*</sub>
    * Description: holds between two molecular entities where the action or effect of one leads to decreased molecular modification(s) of the other (e.g. via post-translational modifications of proteins such as the addition of phosphoryl group, or via redox reaction that adds or subtracts electrons)
    * range: [molecular entity](molecular entity.md)
    * in subsets: (translator_minimal)
 * [decreases mutation rate of](decreases_mutation_rate_of.md)  <sub>0..*</sub>
    * Description: holds between a molecular entity and a genomic entity where the action or effect of the molecular entity decreases the rate of mutation of the genomic entity within a system of interest
    * range: [genomic entity](genomic entity.md)
    * in subsets: (translator_minimal)
 * [decreases response to](decreases_response_to.md)  <sub>0..*</sub>
    * Description: holds between two molecular entities where the action or effect of one decreases the susceptibility of a biological entity or system (e.g. an organism, cell, cellular component, macromolecular machine, biological or pathological process) to the other
    * range: [molecular entity](molecular entity.md)
    * in subsets: (translator_minimal)
 * [decreases secretion of](decreases_secretion_of.md)  <sub>0..*</sub>
    * Description: holds between two molecular entities where the action or effect of one decreases the rate of secretion of the other out of a cell, gland, or organ
    * range: [molecular entity](molecular entity.md)
    * in subsets: (translator_minimal)
 * [decreases splicing of](decreases_splicing_of.md)  <sub>0..*</sub>
    * Description: holds between a molecular entity and an mRNA where the action or effect of the molecular entity decreases the proper splicing of the mRNA
    * range: [transcript](transcript.md)
    * in subsets: (translator_minimal)
 * [decreases stability of](decreases_stability_of.md)  <sub>0..*</sub>
    * Description: holds between two molecular entities where the action or effect of one decreases the stability of the other within a system of interest
    * range: [molecular entity](molecular entity.md)
    * in subsets: (translator_minimal)
 * [decreases synthesis of](decreases_synthesis_of.md)  <sub>0..*</sub>
    * Description: holds between two molecular entities where the action or effect of one decreases the rate of chemical synthesis of the other
    * range: [molecular entity](molecular entity.md)
    * in subsets: (translator_minimal)
 * [decreases transport of](decreases_transport_of.md)  <sub>0..*</sub>
    * Description: holds between two molecular entities where the action or effect of one decreases the rate of transport of the other across some boundary in a system of interest
    * range: [molecular entity](molecular entity.md)
    * in subsets: (translator_minimal)
 * [decreases uptake of](decreases_uptake_of.md)  <sub>0..*</sub>
    * Description: holds between two molecular entities where the action or effect of one decreases the rate of uptake of the other into of a cell, gland, or organ
    * range: [molecular entity](molecular entity.md)
    * in subsets: (translator_minimal)
 * [increases abundance of](increases_abundance_of.md)  <sub>0..*</sub>
    * Description: holds between two molecular entities where the action or effect of one increases the amount of the other within a system of interest
    * range: [molecular entity](molecular entity.md)
    * in subsets: (translator_minimal)
 * [increases activity of](increases_activity_of.md)  <sub>0..*</sub>
    * Description: holds between two molecular entities where the action or effect of one increases the activity of the other within a system of interest
    * range: [molecular entity](molecular entity.md)
    * in subsets: (translator_minimal)
 * [increases degradation of](increases_degradation_of.md)  <sub>0..*</sub>
    * Description: holds between two molecular entities where the action or effect of one increases the rate of degradation of the other within a system of interest
    * range: [molecular entity](molecular entity.md)
    * in subsets: (translator_minimal)
 * [increases expression of](increases_expression_of.md)  <sub>0..*</sub>
    * Description: holds between two molecular entities where the action or effect of one increases the level of expression of the other within a system of interest
    * range: [genomic entity](genomic entity.md)
    * in subsets: (translator_minimal)
 * [increases folding of](increases_folding_of.md)  <sub>0..*</sub>
    * Description: holds between two molecular entities where the action or effect of one increases the rate or quality of folding of the other
    * range: [molecular entity](molecular entity.md)
    * in subsets: (translator_minimal)
 * [increases localization of](increases_localization_of.md)  <sub>0..*</sub>
    * Description: holds between two molecular entities where the action or effect of one increases the proper localization of the other within a system of interest
    * range: [molecular entity](molecular entity.md)
    * in subsets: (translator_minimal)
 * [increases metabolic processing of](increases_metabolic_processing_of.md)  <sub>0..*</sub>
    * Description: holds between two molecular entities where the action or effect of one increases the rate of metabolic processing of the other within a system of interest
    * range: [molecular entity](molecular entity.md)
    * in subsets: (translator_minimal)
 * [increases molecular modification of](increases_molecular_modification_of.md)  <sub>0..*</sub>
    * Description: holds between two molecular entities where the action or effect of one leads to increased molecular modification(s) of the other (e.g. via post-translational modifications of proteins such as the addition of phosphoryl group, or via redox reaction that adds or subtracts electrons)
    * range: [molecular entity](molecular entity.md)
    * in subsets: (translator_minimal)
 * [increases mutation rate of](increases_mutation_rate_of.md)  <sub>0..*</sub>
    * Description: holds between a molecular entity and a genomic entity where the action or effect of the molecular entity increases the rate of mutation of the genomic entity within a system of interest
    * range: [genomic entity](genomic entity.md)
    * in subsets: (translator_minimal)
 * [increases response to](increases_response_to.md)  <sub>0..*</sub>
    * Description: holds between two molecular entities where the action or effect of one increases the susceptibility of a biological entity or system (e.g. an organism, cell, cellular component, macromolecular machine, biological or pathological process) to the other
    * range: [molecular entity](molecular entity.md)
    * in subsets: (translator_minimal)
 * [increases secretion of](increases_secretion_of.md)  <sub>0..*</sub>
    * Description: holds between two molecular entities where the action or effect of one increases the rate of secretion of the other out of a cell, gland, or organ
    * range: [molecular entity](molecular entity.md)
    * in subsets: (translator_minimal)
 * [increases splicing of](increases_splicing_of.md)  <sub>0..*</sub>
    * Description: holds between a molecular entity and an mRNA where the action or effect of the molecular entity increases the proper splicing of the mRNA
    * range: [transcript](transcript.md)
    * in subsets: (translator_minimal)
 * [increases stability of](increases_stability_of.md)  <sub>0..*</sub>
    * Description: holds between two molecular entities where the action or effect of one increases the stability of the other within a system of interest
    * range: [molecular entity](molecular entity.md)
    * in subsets: (translator_minimal)
 * [increases synthesis of](increases_synthesis_of.md)  <sub>0..*</sub>
    * Description: holds between two molecular entities where the action or effect of one increases the rate of chemical synthesis of the other
    * range: [molecular entity](molecular entity.md)
    * in subsets: (translator_minimal)
 * [increases transport of](increases_transport_of.md)  <sub>0..*</sub>
    * Description: holds between two molecular entities where the action or effect of one increases the rate of transport of the other across some boundary in a system of interest
    * range: [molecular entity](molecular entity.md)
    * in subsets: (translator_minimal)
 * [increases uptake of](increases_uptake_of.md)  <sub>0..*</sub>
    * Description: holds between two molecular entities where the action or effect of one increases the rate of uptake of the other into of a cell, gland, or organ
    * range: [molecular entity](molecular entity.md)
    * in subsets: (translator_minimal)
 * [molecularly interacts with](molecularly_interacts_with.md)  <sub>0..*</sub>
    * range: [molecular entity](molecular entity.md)
    * in subsets: (translator_minimal)
 * [negatively regulates, entity to entity](negatively_regulates_entity_to_entity.md)  <sub>0..*</sub>
    * range: [molecular entity](molecular entity.md)
    * in subsets: (translator_minimal)
 * [positively regulates, entity to entity](positively_regulates_entity_to_entity.md)  <sub>0..*</sub>
    * range: [molecular entity](molecular entity.md)
    * in subsets: (translator_minimal)
 * [regulates, entity to entity](regulates_entity_to_entity.md)  <sub>0..*</sub>
    * range: [molecular entity](molecular entity.md)
    * in subsets: (translator_minimal)

## Other properties

|  |  |  |
| --- | --- | --- |
| **Aliases:** | | bioentity |
| **Mappings:** | | SIO:010341 |
|  | | WD:Q43460564 |
|  | | UMLSSG:GENE |
|  | | UMLSSC:T085 |
|  | | UMLSST:mosq |


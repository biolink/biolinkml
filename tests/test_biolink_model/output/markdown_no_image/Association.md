
# Class: Association


A typed association between two entities, supported by evidence

URI: [biolink:Association](https://w3id.org/biolink/vocab/Association)


![img](http://yuml.me/diagram/nofunky;dir:TB/class/[VariantToPopulationAssociation],[VariantToPhenotypicFeatureAssociation],[VariantToGeneAssociation],[VariantToDiseaseAssociation],[SequenceVariantModulatesTreatmentAssociation],[SequenceFeatureRelationship],[SequenceAssociation],[Publication],[PopulationToPopulationAssociation],[OrganismalEntityAsAModelOfDiseaseAssociation],[OrganismTaxonToOrganismTaxonAssociation],[OrganismTaxonToEnvironmentAssociation],[OntologyClass],[NamedThing],[MaterialSampleToDiseaseOrPhenotypicFeatureAssociation],[MaterialSampleDerivationAssociation],[GenotypeToVariantAssociation],[GenotypeToPhenotypicFeatureAssociation],[GenotypeToGenotypePartAssociation],[GenotypeToGeneAssociation],[GenotypeToDiseaseAssociation],[GeneToPhenotypicFeatureAssociation],[GeneToGeneAssociation],[GeneToExpressionSiteAssociation],[GeneToDiseaseAssociation],[GeneRegulatoryRelationship],[FunctionalAssociation],[ExposureEventToPhenotypicFeatureAssociation],[ExposureEventToOutcomeAssociation],[Entity],[DrugToGeneAssociation],[DiseaseToPhenotypicFeatureAssociation],[DiseaseToExposureEventAssociation],[DiseaseOrPhenotypicFeatureToLocationAssociation],[DiseaseOrPhenotypicFeatureAssociationToLocationAssociation],[ContributorAssociation],[ChemicalToPathwayAssociation],[ChemicalToGeneAssociation],[ChemicalToDiseaseOrPhenotypicFeatureAssociation],[ChemicalToChemicalAssociation],[CellLineToDiseaseOrPhenotypicFeatureAssociation],[CaseToPhenotypicFeatureAssociation],[BehaviorToBehavioralFeatureAssociation],[Attribute],[Publication]<publications%200..*-%20[Association&#124;predicate:predicate_type;relation:uriorcurie;negated:boolean%20%3F;type:string%20%3F;category:category_type%20*;id(i):string;iri(i):iri_type%20%3F;name(i):label_type%20%3F;description(i):narrative_text%20%3F;source(i):label_type%20%3F],[OntologyClass]<qualifiers%200..*-++[Association],[NamedThing]<object%201..1-%20[Association],[NamedThing]<subject%201..1-%20[Association],[Association]^-[VariantToPopulationAssociation],[Association]^-[VariantToPhenotypicFeatureAssociation],[Association]^-[VariantToGeneAssociation],[Association]^-[VariantToDiseaseAssociation],[Association]^-[SequenceVariantModulatesTreatmentAssociation],[Association]^-[SequenceFeatureRelationship],[Association]^-[SequenceAssociation],[Association]^-[PopulationToPopulationAssociation],[Association]^-[OrganismalEntityAsAModelOfDiseaseAssociation],[Association]^-[OrganismTaxonToOrganismTaxonAssociation],[Association]^-[OrganismTaxonToEnvironmentAssociation],[Association]^-[MaterialSampleToDiseaseOrPhenotypicFeatureAssociation],[Association]^-[MaterialSampleDerivationAssociation],[Association]^-[GenotypeToVariantAssociation],[Association]^-[GenotypeToPhenotypicFeatureAssociation],[Association]^-[GenotypeToGenotypePartAssociation],[Association]^-[GenotypeToGeneAssociation],[Association]^-[GenotypeToDiseaseAssociation],[Association]^-[GeneToPhenotypicFeatureAssociation],[Association]^-[GeneToGeneAssociation],[Association]^-[GeneToExpressionSiteAssociation],[Association]^-[GeneToDiseaseAssociation],[Association]^-[GeneRegulatoryRelationship],[Association]^-[FunctionalAssociation],[Association]^-[ExposureEventToPhenotypicFeatureAssociation],[Association]^-[ExposureEventToOutcomeAssociation],[Association]^-[DrugToGeneAssociation],[Association]^-[DiseaseToPhenotypicFeatureAssociation],[Association]^-[DiseaseToExposureEventAssociation],[Association]^-[DiseaseOrPhenotypicFeatureToLocationAssociation],[Association]^-[DiseaseOrPhenotypicFeatureAssociationToLocationAssociation],[Association]^-[ContributorAssociation],[Association]^-[ChemicalToPathwayAssociation],[Association]^-[ChemicalToGeneAssociation],[Association]^-[ChemicalToDiseaseOrPhenotypicFeatureAssociation],[Association]^-[ChemicalToChemicalAssociation],[Association]^-[CellLineToDiseaseOrPhenotypicFeatureAssociation],[Association]^-[CaseToPhenotypicFeatureAssociation],[Association]^-[BehaviorToBehavioralFeatureAssociation],[Association]^-[AnatomicalEntityToAnatomicalEntityAssociation],[Entity]^-[Association],[AnatomicalEntityToAnatomicalEntityAssociation],[Agent])

## Parents

 *  is_a: [Entity](Entity.md) - Root Biolink Model class for all things and informational relationships, real or imagined.

## Children

 * [AnatomicalEntityToAnatomicalEntityAssociation](AnatomicalEntityToAnatomicalEntityAssociation.md)
 * [BehaviorToBehavioralFeatureAssociation](BehaviorToBehavioralFeatureAssociation.md) - An association between an aggregate behavior and a behavioral feature manifested by the individual exhibited or has exhibited the behavior.
 * [CaseToPhenotypicFeatureAssociation](CaseToPhenotypicFeatureAssociation.md) - An association between a case (e.g. individual patient) and a phenotypic feature in which the individual has or has had the phenotype.
 * [CellLineToDiseaseOrPhenotypicFeatureAssociation](CellLineToDiseaseOrPhenotypicFeatureAssociation.md) - An relationship between a cell line and a disease or a phenotype, where the cell line is derived from an individual with that disease or phenotype.
 * [ChemicalToChemicalAssociation](ChemicalToChemicalAssociation.md) - A relationship between two chemical entities. This can encompass actual interactions as well as temporal causal edges, e.g. one chemical converted to another.
 * [ChemicalToDiseaseOrPhenotypicFeatureAssociation](ChemicalToDiseaseOrPhenotypicFeatureAssociation.md) - An interaction between a chemical entity and a phenotype or disease, where the presence of the chemical gives rise to or exacerbates the phenotype.
 * [ChemicalToGeneAssociation](ChemicalToGeneAssociation.md) - An interaction between a chemical entity and a gene or gene product.
 * [ChemicalToPathwayAssociation](ChemicalToPathwayAssociation.md) - An interaction between a chemical entity and a biological process or pathway.
 * [ContributorAssociation](ContributorAssociation.md) - Any association between an entity (such as a publication) and various agents that contribute to its realisation
 * [DiseaseOrPhenotypicFeatureAssociationToLocationAssociation](DiseaseOrPhenotypicFeatureAssociationToLocationAssociation.md)
 * [DiseaseOrPhenotypicFeatureToLocationAssociation](DiseaseOrPhenotypicFeatureToLocationAssociation.md) - An association between either a disease or a phenotypic feature and an anatomical entity, where the disease/feature manifests in that site.
 * [DiseaseToExposureEventAssociation](DiseaseToExposureEventAssociation.md) - An association between an exposure event and a disease.
 * [DiseaseToPhenotypicFeatureAssociation](DiseaseToPhenotypicFeatureAssociation.md) - An association between a disease and a phenotypic feature in which the phenotypic feature is associated with the disease in some way.
 * [DrugToGeneAssociation](DrugToGeneAssociation.md) - An interaction between a drug and a gene or gene product.
 * [ExposureEventToOutcomeAssociation](ExposureEventToOutcomeAssociation.md) - An association between an exposure event and an outcome.
 * [ExposureEventToPhenotypicFeatureAssociation](ExposureEventToPhenotypicFeatureAssociation.md) - Any association between an environment and a phenotypic feature, where being in the environment influences the phenotype.
 * [FunctionalAssociation](FunctionalAssociation.md) - An association between a macromolecular machine mixin (gene, gene product or complex of gene products) and either a molecular activity, a biological process or a cellular location in which a function is executed.
 * [GeneRegulatoryRelationship](GeneRegulatoryRelationship.md) - A regulatory relationship between two genes
 * [GeneToDiseaseAssociation](GeneToDiseaseAssociation.md)
 * [GeneToExpressionSiteAssociation](GeneToExpressionSiteAssociation.md) - An association between a gene and an expression site, possibly qualified by stage/timing info.
 * [GeneToGeneAssociation](GeneToGeneAssociation.md) - abstract parent class for different kinds of gene-gene or gene product to gene product relationships. Includes homology and interaction.
 * [GeneToPhenotypicFeatureAssociation](GeneToPhenotypicFeatureAssociation.md)
 * [GenotypeToDiseaseAssociation](GenotypeToDiseaseAssociation.md)
 * [GenotypeToGeneAssociation](GenotypeToGeneAssociation.md) - Any association between a genotype and a gene. The genotype have have multiple variants in that gene or a single one. There is no assumption of cardinality
 * [GenotypeToGenotypePartAssociation](GenotypeToGenotypePartAssociation.md) - Any association between one genotype and a genotypic entity that is a sub-component of it
 * [GenotypeToPhenotypicFeatureAssociation](GenotypeToPhenotypicFeatureAssociation.md) - Any association between one genotype and a phenotypic feature, where having the genotype confers the phenotype, either in isolation or through environment
 * [GenotypeToVariantAssociation](GenotypeToVariantAssociation.md) - Any association between a genotype and a sequence variant.
 * [MaterialSampleDerivationAssociation](MaterialSampleDerivationAssociation.md) - An association between a material sample and the material entity from which it is derived.
 * [MaterialSampleToDiseaseOrPhenotypicFeatureAssociation](MaterialSampleToDiseaseOrPhenotypicFeatureAssociation.md) - An association between a material sample and a disease or phenotype.
 * [OrganismTaxonToEnvironmentAssociation](OrganismTaxonToEnvironmentAssociation.md)
 * [OrganismTaxonToOrganismTaxonAssociation](OrganismTaxonToOrganismTaxonAssociation.md) - A relationship between two organism taxon nodes
 * [OrganismalEntityAsAModelOfDiseaseAssociation](OrganismalEntityAsAModelOfDiseaseAssociation.md)
 * [PopulationToPopulationAssociation](PopulationToPopulationAssociation.md) - An association between a two populations
 * [SequenceAssociation](SequenceAssociation.md) - An association between a sequence feature and a genomic entity it is localized to.
 * [SequenceFeatureRelationship](SequenceFeatureRelationship.md) - For example, a particular exon is part of a particular transcript or gene
 * [SequenceVariantModulatesTreatmentAssociation](SequenceVariantModulatesTreatmentAssociation.md) - An association between a sequence variant and a treatment or health intervention. The treatment object itself encompasses both the disease and the drug used.
 * [VariantToDiseaseAssociation](VariantToDiseaseAssociation.md)
 * [VariantToGeneAssociation](VariantToGeneAssociation.md) - An association between a variant and a gene, where the variant has a genetic association with the gene (i.e. is in linkage disequilibrium)
 * [VariantToPhenotypicFeatureAssociation](VariantToPhenotypicFeatureAssociation.md)
 * [VariantToPopulationAssociation](VariantToPopulationAssociation.md) - An association between a variant and a population, where the variant has particular frequency in the population

## Referenced by class


## Attributes


### Own

 * [association➞category](association_category.md)  <sub>0..*</sub>
     * range: [CategoryType](types/CategoryType.md)
 * [association➞type](association_type.md)  <sub>OPT</sub>
     * Description: rdf:type of biolink:Association should be fixed at rdf:Statement
     * range: [String](types/String.md)
 * [negated](negated.md)  <sub>OPT</sub>
     * Description: if set to true, then the association is negated i.e. is not true
     * range: [Boolean](types/Boolean.md)
 * [object](object.md)  <sub>REQ</sub>
     * Description: connects an association to the object of the association. For example, in a gene-to-phenotype association, the gene is subject and phenotype is object.
     * range: [NamedThing](NamedThing.md)
 * [predicate](predicate.md)  <sub>REQ</sub>
     * Description: A high-level grouping for the relationship type. AKA minimal predicate. This is analogous to category for nodes.
     * range: [PredicateType](types/PredicateType.md)
 * [publications](publications.md)  <sub>0..*</sub>
     * Description: connects an association to publications supporting the association
     * range: [Publication](Publication.md)
 * [qualifiers](qualifiers.md)  <sub>0..*</sub>
     * Description: connects an association to qualifiers that modify or qualify the meaning of that association
     * range: [OntologyClass](OntologyClass.md)
 * [relation](relation.md)  <sub>REQ</sub>
     * Description: The relation which describes an association between a subject and an object in a more granular manner. Usually this is a term from Relation Ontology, but it can be any edge CURIE.
     * range: [Uriorcurie](types/Uriorcurie.md)
 * [subject](subject.md)  <sub>REQ</sub>
     * Description: connects an association to the subject of the association. For example, in a gene-to-phenotype association, the gene is subject and phenotype is object.
     * range: [NamedThing](NamedThing.md)

### Inherited from entity:

 * [description](description.md)  <sub>OPT</sub>
     * Description: a human-readable description of an entity
     * range: [NarrativeText](types/NarrativeText.md)
     * in subsets: (translator_minimal)
 * [has attribute](has_attribute.md)  <sub>0..*</sub>
     * Description: connects any entity to an attribute
     * range: [Attribute](Attribute.md)
     * in subsets: (samples)
 * [id](id.md)  <sub>REQ</sub>
     * Description: A unique identifier for an entity. Must be either a CURIE shorthand for a URI or a complete URI
     * range: [String](types/String.md)
     * in subsets: (translator_minimal)
 * [iri](iri.md)  <sub>OPT</sub>
     * Description: An IRI for an entity. This is determined by the id using expansion rules.
     * range: [IriType](types/IriType.md)
     * in subsets: (translator_minimal,samples)
 * [name](name.md)  <sub>OPT</sub>
     * Description: A human-readable name for an attribute or entity.
     * range: [LabelType](types/LabelType.md)
     * in subsets: (translator_minimal,samples)
 * [provided by](provided_by.md)  <sub>0..*</sub>
     * Description: connects an association to the agent (person, organization or group) that provided it
     * range: [Agent](Agent.md)
 * [source](source.md)  <sub>OPT</sub>
     * Description: a lightweight analog to the association class 'has provider' slot, which is the string name, or the authoritative (i.e. database) namespace, designating the origin of the entity to which the slot belongs.
     * range: [LabelType](types/LabelType.md)
     * in subsets: (translator_minimal)

## Other properties

|  |  |  |
| --- | --- | --- |
| **Comments:** | | This is roughly the model used by biolink and ontobio at the moment |
| **Exact Mappings:** | | OBAN:association |
|  | | rdf:Statement |
|  | | owl:Axiom |


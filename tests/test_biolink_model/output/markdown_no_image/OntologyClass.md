
# Type: ontology class


a concept or class in an ontology, vocabulary or thesaurus

URI: [biolink:OntologyClass](https://w3id.org/biolink/vocab/OntologyClass)


![img](http://yuml.me/diagram/nofunky;dir:TB/class/[TaxonomicRank],[RelationshipType],[OrganismTaxon],[ClinicalMeasurement]-%20has%20attribute%20type%201..1>[OntologyClass&#124;id(i):string;iri(i):iri_type%20%3F;type(i):string%20%3F;name(i):label_type%20%3F;description(i):narrative_text%20%3F;source(i):label_type%20%3F],[ContributorAssociation]-%20qualifiers%200..*>[OntologyClass],[GeneExpressionMixin]-%20quantifier%20qualifier%200..1>[OntologyClass],[GeneToExpressionSiteAssociation]-%20quantifier%20qualifier%200..1>[OntologyClass],[Attribute]-%20has%20attribute%20type%201..1>[OntologyClass],[PairwiseMolecularInteraction]-%20interacting%20molecules%20category%200..1>[OntologyClass],[Association]-%20qualifiers%200..*>[OntologyClass],[GeneExpressionMixin]-%20quantifier%20qualifier(i)%200..1>[OntologyClass],[GeneToExpressionSiteAssociation]-%20quantifier%20qualifier(i)%200..1>[OntologyClass],[OntologyClass]^-[TaxonomicRank],[OntologyClass]^-[RelationshipType],[OntologyClass]^-[OrganismTaxon],[OntologyClass]^-[GeneOntologyClass],[NamedThing]^-[OntologyClass],[PairwiseMolecularInteraction],[NamedThing],[GeneToExpressionSiteAssociation],[GeneOntologyClass],[GeneExpressionMixin],[ContributorAssociation],[ClinicalMeasurement],[Attribute],[Association],[Agent])

## Parents

 *  is_a: [NamedThing](NamedThing.md) - a databased entity or concept/class

## Children

 * [GeneOntologyClass](GeneOntologyClass.md) - an ontology class that describes a functional aspect of a gene, gene prodoct or complex
 * [OrganismTaxon](OrganismTaxon.md) - A classification of a set of organisms. Example instances: NCBITaxon:9606 (Homo sapiens), NCBITaxon:2 (Bacteria). Can also be used to represent strains or subspecies.
 * [RelationshipType](RelationshipType.md) - An OWL property used as an edge label
 * [TaxonomicRank](TaxonomicRank.md) - A descriptor for the rank within a taxonomic classification. Example instance: TAXRANK:0000017 (kingdom)

## Referenced by class

 *  **[Association](Association.md)** *[association type](association_type.md)*  <sub>OPT</sub>  **[OntologyClass](OntologyClass.md)**
 *  **[ClinicalMeasurement](ClinicalMeasurement.md)** *[clinical measurement➞has attribute type](clinical_measurement_has_attribute_type.md)*  <sub>REQ</sub>  **[OntologyClass](OntologyClass.md)**
 *  **[ContributorAssociation](ContributorAssociation.md)** *[contributor association➞qualifiers](contributor_association_qualifiers.md)*  <sub>0..*</sub>  **[OntologyClass](OntologyClass.md)**
 *  **[GeneExpressionMixin](GeneExpressionMixin.md)** *[gene expression mixin➞quantifier qualifier](gene_expression_mixin_quantifier_qualifier.md)*  <sub>OPT</sub>  **[OntologyClass](OntologyClass.md)**
 *  **[GeneToExpressionSiteAssociation](GeneToExpressionSiteAssociation.md)** *[gene to expression site association➞quantifier qualifier](gene_to_expression_site_association_quantifier_qualifier.md)*  <sub>OPT</sub>  **[OntologyClass](OntologyClass.md)**
 *  **[Attribute](Attribute.md)** *[has attribute type](has_attribute_type.md)*  <sub>REQ</sub>  **[OntologyClass](OntologyClass.md)**
 *  **[NamedThing](NamedThing.md)** *[has molecular consequence](has_molecular_consequence.md)*  <sub>0..*</sub>  **[OntologyClass](OntologyClass.md)**
 *  **[NamedThing](NamedThing.md)** *[has topic](has_topic.md)*  <sub>OPT</sub>  **[OntologyClass](OntologyClass.md)**
 *  **[Association](Association.md)** *[interacting molecules category](interacting_molecules_category.md)*  <sub>OPT</sub>  **[OntologyClass](OntologyClass.md)**
 *  **[Association](Association.md)** *[qualifiers](qualifiers.md)*  <sub>0..*</sub>  **[OntologyClass](OntologyClass.md)**
 *  **[Association](Association.md)** *[quantifier qualifier](quantifier_qualifier.md)*  <sub>OPT</sub>  **[OntologyClass](OntologyClass.md)**
 *  **[OntologyClass](OntologyClass.md)** *[subclass of](subclass_of.md)*  <sub>0..*</sub>  **[OntologyClass](OntologyClass.md)**
 *  **[OntologyClass](OntologyClass.md)** *[superclass of](superclass_of.md)*  <sub>0..*</sub>  **[OntologyClass](OntologyClass.md)**

## Attributes


### Inherited from named thing:

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
 * [named thing➞category](named_thing_category.md)  <sub>1..*</sub>
    * range: [NamedThing](NamedThing.md)
 * [provided by](provided_by.md)  <sub>0..*</sub>
    * Description: connects an association to the agent (person, organization or group) that provided it
    * range: [Agent](Agent.md)
 * [source](source.md)  <sub>OPT</sub>
    * Description: a lightweight analog to the association class 'has provider' slot, which is the string name, or the authoritative (i.e. database) namespace, designating the origin of the entity to which the slot belongs.
    * range: [LabelType](types/LabelType.md)
    * in subsets: (translator_minimal)
 * [type](type.md)  <sub>OPT</sub>
    * range: [String](types/String.md)

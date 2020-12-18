
# Type: macromolecular machine


A union of gene, gene product, and macromolecular complex. These are the basic units of function in a cell. They either carry out individual biological activities, or they encode molecules which do this.

URI: [biolink:MacromolecularMachine](https://w3id.org/biolink/vocab/MacromolecularMachine)


![img](http://yuml.me/diagram/nofunky;dir:TB/class/[OrganismTaxon],[NamedThing],[MolecularActivity],[ChemicalToChemicalDerivationAssociation]-%20catalyst%20qualifier(i)%200..*>[MacromolecularMachine&#124;name:symbol_type%20%3F;has_biological_sequence(i):biological_sequence%20%3F;id(i):string;iri(i):iri_type%20%3F;type(i):string%20%3F;description(i):narrative_text%20%3F;source(i):label_type%20%3F],[ChemicalToChemicalDerivationAssociation]-%20catalyst%20qualifier%200..*>[MacromolecularMachine],[FunctionalAssociation]-%20subject%201..1>[MacromolecularMachine],[MolecularActivity]-%20enabled%20by%200..*>[MacromolecularMachine],[MacromolecularMachine]^-[MacromolecularComplex],[MacromolecularMachine]^-[GeneOrGeneProduct],[GenomicEntity]^-[MacromolecularMachine],[MacromolecularComplex],[GenomicEntity],[GeneOrGeneProduct],[FunctionalAssociation],[ChemicalToChemicalDerivationAssociation],[Attribute],[Association],[Agent])

## Parents

 *  is_a: [GenomicEntity](GenomicEntity.md) - an entity that can either be directly located on a genome (gene, transcript, exon, regulatory region) or is encoded in a genome (protein)

## Children

 * [GeneOrGeneProduct](GeneOrGeneProduct.md) - a union of genes or gene products. Frequently an identifier for one will be used as proxy for another
 * [MacromolecularComplex](MacromolecularComplex.md)

## Referenced by class

 *  **[Association](Association.md)** *[catalyst qualifier](catalyst_qualifier.md)*  <sub>0..*</sub>  **[MacromolecularMachine](MacromolecularMachine.md)**
 *  **[ChemicalToChemicalDerivationAssociation](ChemicalToChemicalDerivationAssociation.md)** *[chemical to chemical derivation association➞catalyst qualifier](chemical_to_chemical_derivation_association_catalyst_qualifier.md)*  <sub>0..*</sub>  **[MacromolecularMachine](MacromolecularMachine.md)**
 *  **[FunctionalAssociation](FunctionalAssociation.md)** *[functional association➞subject](functional_association_subject.md)*  <sub>REQ</sub>  **[MacromolecularMachine](MacromolecularMachine.md)**
 *  **[MolecularActivity](MolecularActivity.md)** *[molecular activity➞enabled by](molecular_activity_enabled_by.md)*  <sub>0..*</sub>  **[MacromolecularMachine](MacromolecularMachine.md)**

## Attributes


### Own

 * [macromolecular machine➞name](macromolecular_machine_name.md)  <sub>OPT</sub>
    * Description: genes are typically designated by a short symbol and a full name. We map the symbol to the default display name and use an additional slot for full name
    * range: [SymbolType](types/SymbolType.md)

### Inherited from genomic entity:

 * [description](description.md)  <sub>OPT</sub>
    * Description: a human-readable description of an entity
    * range: [NarrativeText](types/NarrativeText.md)
    * in subsets: (translator_minimal)
 * [has attribute](has_attribute.md)  <sub>0..*</sub>
    * Description: connects any entity to an attribute
    * range: [Attribute](Attribute.md)
    * in subsets: (samples)
 * [has biological sequence](has_biological_sequence.md)  <sub>OPT</sub>
    * Description: connects a genomic feature to its sequence
    * range: [BiologicalSequence](types/BiologicalSequence.md)
 * [id](id.md)  <sub>REQ</sub>
    * Description: A unique identifier for an entity. Must be either a CURIE shorthand for a URI or a complete URI
    * range: [String](types/String.md)
    * in subsets: (translator_minimal)
 * [iri](iri.md)  <sub>OPT</sub>
    * Description: An IRI for an entity. This is determined by the id using expansion rules.
    * range: [IriType](types/IriType.md)
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

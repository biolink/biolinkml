
# Type: chemical substance


May be a chemical entity or a formulation with a chemical entity as active ingredient, or a complex material with multiple chemical entities as part

URI: [biolink:ChemicalSubstance](https://w3id.org/biolink/vocab/ChemicalSubstance)


![img](http://yuml.me/diagram/nofunky;dir:TB/class/[ProcessedMaterial],[OrganismTaxon],[NamedThing],[MolecularEntity],[MolecularActivity],[Metabolite],[Food],[Drug],[ChemicalToEntityAssociationMixin],[ChemicalToChemicalDerivationAssociation],[ChemicalToChemicalAssociation],[ChemicalToChemicalAssociation]-%20object%201..1>[ChemicalSubstance&#124;id(i):string;iri(i):iri_type%20%3F;type(i):string%20%3F;name(i):label_type%20%3F;description(i):narrative_text%20%3F;source(i):label_type%20%3F],[ChemicalToChemicalDerivationAssociation]-%20object%201..1>[ChemicalSubstance],[ChemicalToChemicalDerivationAssociation]-%20subject%201..1>[ChemicalSubstance],[ChemicalToEntityAssociationMixin]-%20subject%201..1>[ChemicalSubstance],[Drug]-%20has%20active%20ingredient%200..*>[ChemicalSubstance],[Mixture]-%20has%20constituent%200..*>[ChemicalSubstance],[Drug]-%20has%20excipient%200..*>[ChemicalSubstance],[Food]-%20has%20nutrient%200..*>[ChemicalSubstance],[MolecularActivity]-%20has%20input%200..*>[ChemicalSubstance],[MolecularActivity]-%20has%20output%200..*>[ChemicalSubstance],[ChemicalSubstance]^-[ProcessedMaterial],[ChemicalSubstance]^-[Metabolite],[ChemicalSubstance]^-[ChemicalExposure],[ChemicalSubstance]^-[Carbohydrate],[MolecularEntity]^-[ChemicalSubstance],[Mixture],[ChemicalExposure],[Carbohydrate],[Attribute],[Agent])

## Parents

 *  is_a: [MolecularEntity](MolecularEntity.md) - A gene, gene product, small molecule or macromolecule (including protein complex)

## Children

 * [Carbohydrate](Carbohydrate.md)
 * [ChemicalExposure](ChemicalExposure.md) - A chemical exposure is an intake of a particular chemical substance, other than a drug.
 * [Metabolite](Metabolite.md) - Any intermediate or product resulting from metabolism. Includes primary and secondary metabolites.
 * [ProcessedMaterial](ProcessedMaterial.md) - A chemical substance (often a mixture) processed for consumption for nutritional, medical or technical use.

## Referenced by class

 *  **[ChemicalToChemicalAssociation](ChemicalToChemicalAssociation.md)** *[chemical to chemical association➞object](chemical_to_chemical_association_object.md)*  <sub>REQ</sub>  **[ChemicalSubstance](ChemicalSubstance.md)**
 *  **[ChemicalToChemicalDerivationAssociation](ChemicalToChemicalDerivationAssociation.md)** *[chemical to chemical derivation association➞object](chemical_to_chemical_derivation_association_object.md)*  <sub>REQ</sub>  **[ChemicalSubstance](ChemicalSubstance.md)**
 *  **[ChemicalToChemicalDerivationAssociation](ChemicalToChemicalDerivationAssociation.md)** *[chemical to chemical derivation association➞subject](chemical_to_chemical_derivation_association_subject.md)*  <sub>REQ</sub>  **[ChemicalSubstance](ChemicalSubstance.md)**
 *  **[ChemicalToEntityAssociationMixin](ChemicalToEntityAssociationMixin.md)** *[chemical to entity association mixin➞subject](chemical_to_entity_association_mixin_subject.md)*  <sub>REQ</sub>  **[ChemicalSubstance](ChemicalSubstance.md)**
 *  **[Drug](Drug.md)** *[has active ingredient](has_active_ingredient.md)*  <sub>0..*</sub>  **[ChemicalSubstance](ChemicalSubstance.md)**
 *  **[NamedThing](NamedThing.md)** *[has constituent](has_constituent.md)*  <sub>0..*</sub>  **[ChemicalSubstance](ChemicalSubstance.md)**
 *  **[Drug](Drug.md)** *[has excipient](has_excipient.md)*  <sub>0..*</sub>  **[ChemicalSubstance](ChemicalSubstance.md)**
 *  **[Food](Food.md)** *[has nutrient](has_nutrient.md)*  <sub>0..*</sub>  **[ChemicalSubstance](ChemicalSubstance.md)**
 *  **[MolecularActivity](MolecularActivity.md)** *[molecular activity➞has input](molecular_activity_has_input.md)*  <sub>0..*</sub>  **[ChemicalSubstance](ChemicalSubstance.md)**
 *  **[MolecularActivity](MolecularActivity.md)** *[molecular activity➞has output](molecular_activity_has_output.md)*  <sub>0..*</sub>  **[ChemicalSubstance](ChemicalSubstance.md)**

## Attributes


### Inherited from molecular entity:

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

## Other properties

|  |  |  |
| --- | --- | --- |
| **In Subsets:** | | model_organism_database |
| **Exact Mappings:** | | CHEBI:24431 |
|  | | SIO:010004 |
|  | | WIKIDATA:Q79529 |
|  | | UMLSSC:T103 |
|  | | UMLSST:chem |
| **Narrow Mappings:** | | UMLSSC:T104 |
|  | | UMLSST:chvs |
|  | | UMLSSC:T109 |
|  | | UMLSST:orch |
|  | | UMLSSC:T114 |
|  | | UMLSST:nnon |
|  | | UMLSSC:T120 |
|  | | UMLSST:chvf |
|  | | UMLSSC:T122 |
|  | | UMLSST:bodm |
|  | | UMLSSC:T130 |
|  | | UMLSST:irda |
|  | | UMLSSC:T131 |
|  | | UMLSST:hops |
|  | | UMLSSC:T196 |
|  | | UMLSST:elii |
|  | | UMLSSC:T197 |
|  | | UMLSST:inch |
| **Broad Mappings:** | | UMLSSC:T167 |
|  | | UMLSST:sbst |


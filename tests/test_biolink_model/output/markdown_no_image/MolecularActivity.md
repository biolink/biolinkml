
# Type: molecular activity


An execution of a molecular function carried out by a gene product or macromolecular complex.

URI: [biolink:MolecularActivity](https://w3id.org/biolink/vocab/MolecularActivity)


![img](http://yuml.me/diagram/nofunky;dir:TB/class/[Occurrent],[NamedThing],[MacromolecularMachine]<enabled%20by%200..*-%20[MolecularActivity&#124;id(i):string;iri(i):iri_type%20%3F;type(i):string%20%3F;name(i):label_type%20%3F;description(i):narrative_text%20%3F;source(i):label_type%20%3F],[ChemicalSubstance]<has%20output%200..*-%20[MolecularActivity],[ChemicalSubstance]<has%20input%200..*-%20[MolecularActivity],[MacromolecularMachineToMolecularActivityAssociation]-%20object%201..1>[MolecularActivity],[MolecularActivity]uses%20-.->[Occurrent],[BiologicalProcessOrActivity]^-[MolecularActivity],[MacromolecularMachineToMolecularActivityAssociation],[MacromolecularMachine],[ChemicalSubstance],[BiologicalProcessOrActivity],[Attribute],[Agent])

## Parents

 *  is_a: [BiologicalProcessOrActivity](BiologicalProcessOrActivity.md) - Either an individual molecular activity, or a collection of causally connected molecular activities

## Uses Mixins

 *  mixin: [Occurrent](Occurrent.md) - A processual entity

## Referenced by class

 *  **[MacromolecularMachineToMolecularActivityAssociation](MacromolecularMachineToMolecularActivityAssociation.md)** *[macromolecular machine to molecular activity association➞object](macromolecular_machine_to_molecular_activity_association_object.md)*  <sub>REQ</sub>  **[MolecularActivity](MolecularActivity.md)**

## Attributes


### Own

 * [molecular activity➞enabled by](molecular_activity_enabled_by.md)  <sub>0..*</sub>
    * Description: The gene product, gene, or complex that catalyzes the reaction
    * range: [MacromolecularMachine](MacromolecularMachine.md)
 * [molecular activity➞has input](molecular_activity_has_input.md)  <sub>0..*</sub>
    * Description: A chemical entity that is the input for the reaction
    * range: [ChemicalSubstance](ChemicalSubstance.md)
 * [molecular activity➞has output](molecular_activity_has_output.md)  <sub>0..*</sub>
    * Description: A chemical entity that is the output for the reaction
    * range: [ChemicalSubstance](ChemicalSubstance.md)

### Inherited from biological process or activity:

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
| **Aliases:** | | molecular function |
|  | | molecular event |
|  | | reaction |
| **Exact Mappings:** | | GO:0003674 |
|  | | UMLSSC:T044 |
|  | | UMLSST:moft |



# Class: BiologicalProcessOrActivity


Either an individual molecular activity, or a collection of causally connected molecular activities in a biological system.

URI: [biolink:BiologicalProcessOrActivity](https://w3id.org/biolink/vocab/BiologicalProcessOrActivity)


![img](http://yuml.me/diagram/nofunky;dir:TB/class/[PhysicalEntity],[OntologyClass],[Occurrent],[NamedThing],[MolecularActivity],[PhysicalEntity]<enabled%20by%200..*-%20[BiologicalProcessOrActivity&#124;id(i):string;iri(i):iri_type%20%3F;type(i):string%20%3F;name(i):label_type%20%3F;description(i):narrative_text%20%3F;source(i):label_type%20%3F],[NamedThing]<has%20output%200..*-%20[BiologicalProcessOrActivity],[NamedThing]<has%20input%200..*-%20[BiologicalProcessOrActivity],[BiologicalProcessOrActivity]uses%20-.->[Occurrent],[BiologicalProcessOrActivity]uses%20-.->[OntologyClass],[BiologicalProcessOrActivity]^-[MolecularActivity],[BiologicalProcessOrActivity]^-[BiologicalProcess],[BiologicalEntity]^-[BiologicalProcessOrActivity],[BiologicalProcess],[BiologicalEntity],[Attribute],[Agent])

## Identifier prefixes

 * GO
 * REACT

## Parents

 *  is_a: [BiologicalEntity](BiologicalEntity.md)

## Uses Mixins

 *  mixin: [Occurrent](Occurrent.md) - A processual entity.
 *  mixin: [OntologyClass](OntologyClass.md) - a concept or class in an ontology, vocabulary or thesaurus. Note that nodes in a biolink compatible KG can be considered both instances of biolink classes, and OWL classes in their own right. In general you should not need to use this class directly. Instead, use the appropriate biolink class. For example, for the GO concept of endocytosis (GO:0006897), use bl:BiologicalProcess as the type.

## Children

 * [BiologicalProcess](BiologicalProcess.md) - One or more causally connected executions of molecular functions
 * [MolecularActivity](MolecularActivity.md) - An execution of a molecular function carried out by a gene product or macromolecular complex.

## Referenced by class

 *  **[PhysicalEntity](PhysicalEntity.md)** *[enables](enables.md)*  <sub>0..*</sub>  **[BiologicalProcessOrActivity](BiologicalProcessOrActivity.md)**

## Attributes


### Own

 * [enabled by](enabled_by.md)  <sub>0..*</sub>
     * Description: holds between a process and a physical entity, where the physical entity executes the process
     * range: [PhysicalEntity](PhysicalEntity.md)
     * in subsets: (translator_minimal)
 * [has input](has_input.md)  <sub>0..*</sub>
     * Description: holds between a process and a continuant, where the continuant is an input into the process
     * range: [NamedThing](NamedThing.md)
     * in subsets: (translator_minimal)
 * [has output](has_output.md)  <sub>0..*</sub>
     * Description: holds between a process and a continuant, where the continuant is an output of the process
     * range: [NamedThing](NamedThing.md)
     * in subsets: (translator_minimal)

### Inherited from biological entity:

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

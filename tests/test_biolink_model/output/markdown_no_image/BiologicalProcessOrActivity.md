
# Type: biological process or activity


Either an individual molecular activity, or a collection of causally connected molecular activities

URI: [biolink:BiologicalProcessOrActivity](https://w3id.org/biolink/vocab/BiologicalProcessOrActivity)


![img](http://yuml.me/diagram/nofunky;dir:TB/class/[Occurrent],[NamedThing],[MolecularActivity],[NamedThing]<enabled%20by%200..*-%20[BiologicalProcessOrActivity&#124;id(i):string;name(i):label_type;category(i):category_type%20%2B],[NamedThing]<has%20output%200..*-%20[BiologicalProcessOrActivity],[NamedThing]<has%20input%200..*-%20[BiologicalProcessOrActivity],[BiologicalProcessOrActivity]uses%20-.->[Occurrent],[BiologicalProcessOrActivity]^-[MolecularActivity],[BiologicalProcessOrActivity]^-[BiologicalProcess],[BiologicalEntity]^-[BiologicalProcessOrActivity],[BiologicalProcess],[BiologicalEntity])

## Parents

 *  is_a: [BiologicalEntity](BiologicalEntity.md)

## Uses Mixins

 *  mixin: [Occurrent](Occurrent.md) - A processual entity

## Children

 * [BiologicalProcess](BiologicalProcess.md) - One or more causally connected executions of molecular functions
 * [MolecularActivity](MolecularActivity.md) - An execution of a molecular function carried out by a gene product or macromolecular complex.

## Referenced by class

 *  **[Occurrent](Occurrent.md)** *[enables](enables.md)*  <sub>0..*</sub>  **[BiologicalProcessOrActivity](BiologicalProcessOrActivity.md)**

## Attributes


### Own

 * [enabled by](enabled_by.md)  <sub>0..*</sub>
    * Description: holds between a process and a physical entity, where the physical entity executes the process
    * range: [NamedThing](NamedThing.md)
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

 * [category](category.md)  <sub>1..*</sub>
    * Description: Name of the high level ontology class in which this entity is categorized. Corresponds to the label for the biolink entity type class. In a neo4j database this MAY correspond to the neo4j label tag
    * range: [CategoryType](types/CategoryType.md)
    * in subsets: (translator_minimal)
 * [id](id.md)  <sub>REQ</sub>
    * Description: A unique identifier for a thing. Must be either a CURIE shorthand for a URI or a complete URI
    * range: [String](types/String.md)
    * in subsets: (translator_minimal)
 * [name](name.md)  <sub>REQ</sub>
    * Description: A human-readable name for a thing
    * range: [LabelType](types/LabelType.md)
    * in subsets: (translator_minimal)

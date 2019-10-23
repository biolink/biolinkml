
# Type: occurrent


A processual entity

URI: [biolink:Occurrent](https://w3id.org/biolink/vocab/Occurrent)


![img](http://yuml.me/diagram/nofunky;dir:TB/class/\[MolecularActivity]uses%20-.->\[Occurrent|id(i):identifier_type;name(i):label_type;category(i):iri_type%20%2B],%20\[EnvironmentalProcess]uses%20-.->\[Occurrent],%20\[BiologicalProcessOrActivity]uses%20-.->\[Occurrent],%20\[BiologicalProcess]uses%20-.->\[Occurrent],%20\[Occurrent]^-\[Procedure],%20\[Occurrent]^-\[Phenomenon],%20\[Occurrent]^-\[ActivityAndBehavior],%20\[NamedThing]^-\[Occurrent])

## Parents

 *  is_a: [named thing](named thing.md) - a databased entity or concept/class

## Children

 * [activity and behavior](activity and behavior.md) - Activity or behavior of any independent integral living, organization or mechanical actor in the world
 * [phenomenon](phenomenon.md) - a fact or situation that is observed to exist or happen, especially one whose cause or explanation is in question
 * [procedure](procedure.md) - A series of actions conducted in a certain order or manner

## Mixin for

 * [biological process](biological process.md) (mixin)  - One or more causally connected executions of molecular functions
 * [biological process or activity](biological process or activity.md) (mixin)  - Either an individual molecular activity, or a collection of causally connected molecular activities
 * [environmental process](environmental process.md) (mixin) 
 * [molecular activity](molecular activity.md) (mixin)  - An execution of a molecular function carried out by a gene product or macromolecular complex.

## Referenced by class

 *  **[named thing](named thing.md)** *[actively involved in](actively_involved_in.md)*  <sub>0..*</sub>  **[occurrent](occurrent.md)**
 *  **[named thing](named thing.md)** *[capable of](capable_of.md)*  <sub>0..*</sub>  **[occurrent](occurrent.md)**
 *  **[occurrent](occurrent.md)** *[negatively regulates, process to process](negatively_regulates_process_to_process.md)*  <sub>0..*</sub>  **[occurrent](occurrent.md)**
 *  **[named thing](named thing.md)** *[participates in](participates_in.md)*  <sub>0..*</sub>  **[occurrent](occurrent.md)**
 *  **[occurrent](occurrent.md)** *[positively regulates, process to process](positively_regulates_process_to_process.md)*  <sub>0..*</sub>  **[occurrent](occurrent.md)**
 *  **[occurrent](occurrent.md)** *[precedes](precedes.md)*  <sub>0..*</sub>  **[occurrent](occurrent.md)**
 *  **[occurrent](occurrent.md)** *[regulates, process to process](regulates_process_to_process.md)*  <sub>0..*</sub>  **[occurrent](occurrent.md)**

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

### Domain for slot:

 * [enabled by](enabled_by.md)  <sub>0..*</sub>
    * Description: holds between a process and a physical entity, where the physical entity executes the process
    * range: [biological process or activity](biological process or activity.md)
    * in subsets: (translator_minimal)
 * [has input](has_input.md)  <sub>0..*</sub>
    * Description: holds between a process and a continuant, where the continuant is an input into the process
    * range: [named thing](named thing.md)
    * in subsets: (translator_minimal)
 * [has output](has_output.md)  <sub>0..*</sub>
    * Description: holds between a process and a continuant, where the continuant is an output of the process
    * range: [named thing](named thing.md)
    * in subsets: (translator_minimal)
 * [has participant](has_participant.md)  <sub>0..*</sub>
    * Description: holds between a process and a continuant, where the continuant is somehow involved in the process
    * range: [named thing](named thing.md)
    * in subsets: (translator_minimal)
 * [negatively regulates, process to process](negatively_regulates_process_to_process.md)  <sub>0..*</sub>
    * range: [occurrent](occurrent.md)
 * [positively regulates, process to process](positively_regulates_process_to_process.md)  <sub>0..*</sub>
    * range: [occurrent](occurrent.md)
 * [precedes](precedes.md)  <sub>0..*</sub>
    * Description: holds between two processes, where one completes before the other begins
    * range: [occurrent](occurrent.md)
    * in subsets: (translator_minimal)
 * [regulates, process to process](regulates_process_to_process.md)  <sub>0..*</sub>
    * range: [occurrent](occurrent.md)

## Other properties

|  |  |  |
| --- | --- | --- |
| **Mappings:** | | BFO:0000003 |


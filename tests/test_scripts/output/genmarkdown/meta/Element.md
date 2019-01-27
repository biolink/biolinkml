# Class: element


a named element in the model

URI: [http://w3id.org/biolink/biolinkml/meta/Element](http://w3id.org/biolink/biolinkml/meta/Element)

![img](http://yuml.me/diagram/nofunky;dir:TB/class/\[Element|name(pk):string;description:string%20%3F;deprecated:string%20%3F;notes:string%20*;comments:string%20*;see_also:uri%20*;id_prefixes:ncname%20*]-%20from_schema%20%3F>\[SchemaDefinition],%20\[Element]-%20in_subset%20*>\[SubsetDefinition],%20\[Element]++-%20examples%20*>\[Example],%20\[SlotDefinition]-%20range%20%3F>\[Element],%20\[Element]^-\[TypeDefinition],%20\[Element]^-\[SubsetDefinition],%20\[Element]^-\[SchemaDefinition],%20\[Element]^-\[Definition])
## Inheritance

## Children

 * [Definition](Definition.md) - base class for definitions
 * [SchemaDefinition](SchemaDefinition.md) - a collection of subset, type, slot and class definitions
 * [SubsetDefinition](SubsetDefinition.md) - the name and description of a subset
 * [TypeDefinition](TypeDefinition.md) - A data type definition.
## Used by

 *  **[SlotDefinition](SlotDefinition.md)** *[range](range.md)<sub>opt</sub>*  **[Element](Element.md)**
## Fields

 * [comments](comments.md) *subsets*: (owl)<sub>opt</sub>
    * Description: notes and comments about an element intended for external consumption
    * range: [[String](String.md)]
 * [deprecated](deprecated.md)<sub>opt</sub>
    * Description: Description of why and when this element will no longer be used
    * range: [String](String.md)
 * [description](description.md) *subsets*: (owl)<sub>opt</sub>
    * Description: a description of the element's purpose and use
    * range: [String](String.md)
 * [examples](examples.md) *subsets*: (owl)<sub>opt</sub>
    * Description: example usages of an element
    * range: [[Example](Example.md)]
 * [from_schema](from_schema.md)<sub>opt</sub>
    * Description: id of the schema that defined the element
    * range: [SchemaDefinition](SchemaDefinition.md)
 * [id_prefixes](id_prefixes.md)<sub>opt</sub>
    * Description: a list of Curie prefixes that are used in the representation of instances of the model.  All prefixes in this list are added to the prefix sections of the target models.
    * range: [[Ncname](Ncname.md)]
 * [in_subset](in_subset.md)<sub>opt</sub>
    * Description: used to indicate membership of a term in a defined subset of biolink terms used for a particular domain or application (e.g. the translator_minimal subset holding the minimal set of predicates used in a translator knowledge graph)
    * range: [[SubsetDefinition](SubsetDefinition.md)]
 * [name](name.md) *subsets*: (owl)
    * Description: the unique name of the element within the context of the schema
    * range: [String](String.md)
 * [notes](notes.md) *subsets*: (owl)<sub>opt</sub>
    * Description: editorial notes about an element intended for internal consumption
    * range: [[String](String.md)]
 * [see_also](see_also.md) *subsets*: (owl)<sub>opt</sub>
    * Description: a reference
    * range: [[Uri](Uri.md)]

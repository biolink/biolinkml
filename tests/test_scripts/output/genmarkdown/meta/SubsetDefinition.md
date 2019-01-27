# Class: subset definition


the name and description of a subset

URI: [http://w3id.org/biolink/biolinkml/meta/SubsetDefinition](http://w3id.org/biolink/biolinkml/meta/SubsetDefinition)

![img](http://yuml.me/diagram/nofunky;dir:TB/class/\[SubsetDefinition|name(pk)(i):string;description(i):string%20%3F;deprecated(i):string%20%3F;notes(i):string%20*;comments(i):string%20*;see_also(i):uri%20*;id_prefixes(i):ncname%20*]-%20from_schema(i)%20%3F>\[SchemaDefinition],%20\[SubsetDefinition]-%20in_subset(i)%20*>\[SubsetDefinition],%20\[SubsetDefinition]++-%20examples(i)%20*>\[Example],%20\[Element]-%20in_subset%20*>\[SubsetDefinition],%20\[SchemaDefinition]++-%20subsets%20*>\[SubsetDefinition],%20\[Element]^-\[SubsetDefinition])
## Inheritance

 *  is_a: [Element](Element.md) - a named element in the model
## Children

## Used by

 *  **[Element](Element.md)** *[in_subset](in_subset.md)<sub>opt</sub>*  **[[SubsetDefinition](SubsetDefinition.md)]**
 *  **[SchemaDefinition](SchemaDefinition.md)** *[subsets](subsets.md)<sub>opt</sub>*  **[[SubsetDefinition](SubsetDefinition.md)]**
## Fields

 * [comments](comments.md) *subsets*: (owl)<sub>opt</sub>
    * Description: notes and comments about an element intended for external consumption
    * range: [[String](String.md)]
    * inherited from: [Element](Element.md)
 * [deprecated](deprecated.md)<sub>opt</sub>
    * Description: Description of why and when this element will no longer be used
    * range: [String](String.md)
    * inherited from: [Element](Element.md)
 * [description](description.md) *subsets*: (owl)<sub>opt</sub>
    * Description: a description of the element's purpose and use
    * range: [String](String.md)
    * inherited from: [Element](Element.md)
 * [examples](examples.md) *subsets*: (owl)<sub>opt</sub>
    * Description: example usages of an element
    * range: [[Example](Example.md)]
    * inherited from: [Element](Element.md)
 * [from_schema](from_schema.md)<sub>opt</sub>
    * Description: id of the schema that defined the element
    * range: [SchemaDefinition](SchemaDefinition.md)
    * inherited from: [Element](Element.md)
 * [id_prefixes](id_prefixes.md)<sub>opt</sub>
    * Description: a list of Curie prefixes that are used in the representation of instances of the model.  All prefixes in this list are added to the prefix sections of the target models.
    * range: [[Ncname](Ncname.md)]
    * inherited from: [Element](Element.md)
 * [in_subset](in_subset.md)<sub>opt</sub>
    * Description: used to indicate membership of a term in a defined subset of biolink terms used for a particular domain or application (e.g. the translator_minimal subset holding the minimal set of predicates used in a translator knowledge graph)
    * range: [[SubsetDefinition](SubsetDefinition.md)]
    * inherited from: [Element](Element.md)
 * [name](name.md) *subsets*: (owl)
    * Description: the unique name of the element within the context of the schema
    * range: [String](String.md)
    * inherited from: [Element](Element.md)
 * [notes](notes.md) *subsets*: (owl)<sub>opt</sub>
    * Description: editorial notes about an element intended for internal consumption
    * range: [[String](String.md)]
    * inherited from: [Element](Element.md)
 * [see_also](see_also.md) *subsets*: (owl)<sub>opt</sub>
    * Description: a reference
    * range: [[Uri](Uri.md)]
    * inherited from: [Element](Element.md)

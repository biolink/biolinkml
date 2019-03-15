# Class: element


a named element in the model

URI: [http://w3id.org/biolink/biolinkml/meta/Element](http://w3id.org/biolink/biolinkml/meta/Element)

![img](http://yuml.me/diagram/nofunky;dir:TB/class/\[SubsetDefinition]<in_subset%20*-%20\[Element|name(pk):string;singular_name:string%20%3F;aliases:string%20*;mappings:uriorcuri%20*;description:string%20%3F;deprecated:string%20%3F;todos:string%20*;notes:string%20*;comments:string%20*;from_schema:uri%20%3F;imported_from:string%20%3F;see_also:uri%20*],%20\[Example]<examples%20*-++\[Element],%20\[SlotDefinition]-%20range%20%3F>\[Element],%20\[Element]^-\[TypeDefinition],%20\[Element]^-\[SubsetDefinition],%20\[Element]^-\[SchemaDefinition],%20\[Element]^-\[Definition])
## Inheritance

## Children

 * [Definition](Definition.md) - base class for definitions
 * [SchemaDefinition](SchemaDefinition.md) - a collection of subset, type, slot and class definitions
 * [SubsetDefinition](SubsetDefinition.md) - the name and description of a subset
 * [TypeDefinition](TypeDefinition.md) - A data type definition.
## Used by

 *  **[SlotDefinition](SlotDefinition.md)** *[range](range.md)<sub>opt</sub>*  **[Element](Element.md)**
## Fields

 * [aliases](aliases.md)<sub>opt</sub>
    * range: [[String](String.md)]
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
    * range: [Uri](Uri.md)
 * [imported_from](imported_from.md)<sub>opt</sub>
    * Description: the imports entry that this element was derived from.  Empty means primary source
    * range: [String](String.md)
 * [in_subset](in_subset.md)<sub>opt</sub>
    * Description: used to indicate membership of a term in a defined subset of biolink terms used for a particular domain or application (e.g. the translator_minimal subset holding the minimal set of predicates used in a translator knowledge graph)
    * range: [[SubsetDefinition](SubsetDefinition.md)]
 * [mappings](mappings.md)<sub>opt</sub>
    * Description: A list of terms from different schemas or terminology systems that have comparable meaning. These may include terms that are precisely equivalent, broader or narrower in meaning, or otherwise semantically related but not equivalent from a strict ontological perspective.
    * range: [[Uriorcuri](Uriorcuri.md)]
 * [name](name.md) *subsets*: (owl)
    * Description: the unique name of the element within the context of the schema.  Name is combined with the default prefix to form the globally unique subject of the target class.
    * range: [String](String.md)
 * [notes](notes.md) *subsets*: (owl)<sub>opt</sub>
    * Description: editorial notes about an element intended for internal consumption
    * range: [[String](String.md)]
 * [notes](notes.md) *subsets*: (owl)<sub>opt</sub>
    * Description: editorial notes about an element intended for internal consumption
    * range: [[String](String.md)]
 * [see_also](see_also.md) *subsets*: (owl)<sub>opt</sub>
    * Description: a reference
    * range: [[Uri](Uri.md)]
 * [singular_name](singular_name.md)<sub>opt</sub>
    * Description: a name that is used in the singular form
    * range: [String](String.md)
 * [todos](todos.md)<sub>opt</sub>
    * Description: Outstanding issue that needs resolution
    * range: [[String](String.md)]

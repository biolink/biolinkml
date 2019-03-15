# Class: type_definition


A data type definition.

URI: [http://w3id.org/biolink/biolinkml/meta/TypeDefinition](http://w3id.org/biolink/biolinkml/meta/TypeDefinition)

![img](http://yuml.me/diagram/nofunky;dir:TB/class/\[SubsetDefinition]<in_subset(i)%20*-%20\[TypeDefinition|base:string%20%3F;uri:uri%20%3F;repr:string%20%3F;name(pk)(i):string;singular_name(i):string%20%3F;aliases(i):string%20*;mappings(i):uriorcuri%20*;description(i):string%20%3F;deprecated(i):string%20%3F;todos(i):string%20*;notes(i):string%20*;comments(i):string%20*;from_schema(i):uri%20%3F;imported_from(i):string%20%3F;see_also(i):uri%20*],%20\[Example]<examples(i)%20*-++\[TypeDefinition],%20\[TypeDefinition]<typeof%20%3F-%20\[TypeDefinition],%20\[SchemaDefinition]++-%20types%20*>\[TypeDefinition],%20\[Element]^-\[TypeDefinition])
## Inheritance

 *  is_a: [Element](Element.md) - a named element in the model
## Children

## Used by

 *  **[TypeDefinition](TypeDefinition.md)** *[typeof](typeof.md)<sub>opt</sub>*  **[TypeDefinition](TypeDefinition.md)**
 *  **[SchemaDefinition](SchemaDefinition.md)** *[types](types.md)<sub>opt</sub>*  **[[TypeDefinition](TypeDefinition.md)]**
## Fields

 * [aliases](aliases.md)<sub>opt</sub>
    * range: [[String](String.md)]
    * inherited from: [Element](Element.md)
 * [base](base.md)<sub>opt</sub>
    * Description: python base type that implements this type definition
    * range: [String](String.md)
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
    * range: [Uri](Uri.md)
    * inherited from: [Element](Element.md)
 * [imported_from](imported_from.md)<sub>opt</sub>
    * Description: the imports entry that this element was derived from.  Empty means primary source
    * range: [String](String.md)
    * inherited from: [Element](Element.md)
 * [in_subset](in_subset.md)<sub>opt</sub>
    * Description: used to indicate membership of a term in a defined subset of biolink terms used for a particular domain or application (e.g. the translator_minimal subset holding the minimal set of predicates used in a translator knowledge graph)
    * range: [[SubsetDefinition](SubsetDefinition.md)]
    * inherited from: [Element](Element.md)
 * [mappings](mappings.md)<sub>opt</sub>
    * Description: A list of terms from different schemas or terminology systems that have comparable meaning. These may include terms that are precisely equivalent, broader or narrower in meaning, or otherwise semantically related but not equivalent from a strict ontological perspective.
    * range: [[Uriorcuri](Uriorcuri.md)]
    * inherited from: [Element](Element.md)
 * [name](name.md) *subsets*: (owl)
    * Description: the unique name of the element within the context of the schema.  Name is combined with the default prefix to form the globally unique subject of the target class.
    * range: [String](String.md)
    * inherited from: [Element](Element.md)
 * [notes](notes.md) *subsets*: (owl)<sub>opt</sub>
    * Description: editorial notes about an element intended for internal consumption
    * range: [[String](String.md)]
    * inherited from: [Element](Element.md)
 * [repr](repr.md)<sub>opt</sub>
    * Description: the name of the python object that implements this type definition
    * range: [String](String.md)
 * [see_also](see_also.md) *subsets*: (owl)<sub>opt</sub>
    * Description: a reference
    * range: [[Uri](Uri.md)]
    * inherited from: [Element](Element.md)
 * [singular_name](singular_name.md)<sub>opt</sub>
    * Description: a name that is used in the singular form
    * range: [String](String.md)
    * inherited from: [Element](Element.md)
 * [todos](todos.md)<sub>opt</sub>
    * Description: Outstanding issue that needs resolution
    * range: [[String](String.md)]
    * inherited from: [Element](Element.md)
 * [type_definition.uri](type_uri.md)<sub>opt</sub>
    * Description: The uri that defines the possible values for the type definition
    * range: [Uri](Uri.md)
 * [typeof](typeof.md)<sub>opt</sub>
    * Description: Names a parent type
    * range: [TypeDefinition](TypeDefinition.md)

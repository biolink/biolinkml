
# Class: type_definition


A data type definition.

URI: [meta:TypeDefinition](https://w3id.org/biolink/biolinkml/meta/TypeDefinition)

![img](http://yuml.me/diagram/nofunky;dir:TB/class/\[SubsetDefinition]<in_subset(i)%200..*-%20\[TypeDefinition|base:string%20%3F;uri:uriorcurie%20%3F;repr:string%20%3F;id_prefixes(i):ncname%20*;name(pk)(i):string;aliases(i):string%20*;mappings(i):uriorcurie%20*;description(i):string%20%3F;deprecated(i):string%20%3F;todos(i):string%20*;notes(i):string%20*;comments(i):string%20*;from_schema(i):uri%20%3F;imported_from(i):string%20%3F;see_also(i):uriorcurie%20*],%20\[Example]<examples(i)%200..*-++\[TypeDefinition],%20\[AltDescription]<alt_descriptions(i)%200..*-++\[TypeDefinition],%20\[LocalName]<local_names(i)%200..*-++\[TypeDefinition],%20\[TypeDefinition]<typeof%200..1-%20\[TypeDefinition],%20\[SchemaDefinition]-%20default_range%200..1>\[TypeDefinition],%20\[SchemaDefinition]++-%20types%200..*>\[TypeDefinition],%20\[Element]^-\[TypeDefinition])

## Parents

 *  is_a: [Element](Element.md) - a named element in the model

## Referenced by class

 *  **[SchemaDefinition](SchemaDefinition.md)** *[default_range](default_range.md)*  <sub>OPT</sub>  **[TypeDefinition](TypeDefinition.md)**
 *  **[TypeDefinition](TypeDefinition.md)** *[typeof](typeof.md)*  <sub>OPT</sub>  **[TypeDefinition](TypeDefinition.md)**
 *  **[SchemaDefinition](SchemaDefinition.md)** *[types](types.md)*  <sub>0..*</sub>  **[TypeDefinition](TypeDefinition.md)**

## Attributes


### Own

 * [base](base.md)  <sub>OPT</sub>
    * Description: python base type that implements this type definition
    * range: [String](String.md)
 * [repr](repr.md)  <sub>OPT</sub>
    * Description: the name of the python object that implements this type definition
    * range: [String](String.md)
    * Example: None None
 * [uri](type_uri.md)  <sub>OPT</sub>
    * Description: The uri that defines the possible values for the type definition
    * range: [Uriorcurie](Uriorcurie.md)
 * [typeof](typeof.md)  <sub>OPT</sub>
    * Description: Names a parent type
    * range: [TypeDefinition](TypeDefinition.md)

### Inherited from element:

 * [id_prefixes](id_prefixes.md)  <sub>0..*</sub>
    * Description: the identifier of this class or slot must begin with one of the URIs referenced by this prefix
    * range: [Ncname](Ncname.md)
    * inherited from: [Element](Element.md)
 * [name](name.md)  <sub>REQ</sub>
    * Description: the unique name of the element within the context of the schema.  Name is combined with the default prefix to form the globally unique subject of the target class.
    * range: [String](String.md)
    * inherited from: [Element](Element.md)
    * in subsets: (owl)
 * [aliases](aliases.md)  <sub>0..*</sub>
    * range: [String](String.md)
    * inherited from: [Element](Element.md)
 * [local_names](local_names.md)  <sub>0..*</sub>
    * range: [LocalName](LocalName.md)
    * inherited from: [Element](Element.md)
 * [mappings](mappings.md)  <sub>0..*</sub>
    * Description: A list of terms from different schemas or terminology systems that have comparable meaning. These may include terms that are precisely equivalent, broader or narrower in meaning, or otherwise semantically related but not equivalent from a strict ontological perspective.
    * range: [Uriorcurie](Uriorcurie.md)
    * inherited from: [Element](Element.md)
 * [description](description.md)  <sub>OPT</sub>
    * Description: a description of the element's purpose and use
    * range: [String](String.md)
    * inherited from: [Element](Element.md)
    * in subsets: (owl)
 * [alt_descriptions](alt_descriptions.md)  <sub>0..*</sub>
    * range: [AltDescription](AltDescription.md)
    * inherited from: [Element](Element.md)
 * [deprecated](deprecated.md)  <sub>OPT</sub>
    * Description: Description of why and when this element will no longer be used
    * range: [String](String.md)
    * inherited from: [Element](Element.md)
 * [todos](todos.md)  <sub>0..*</sub>
    * Description: Outstanding issue that needs resolution
    * range: [String](String.md)
    * inherited from: [Element](Element.md)
 * [notes](notes.md)  <sub>0..*</sub>
    * Description: editorial notes about an element intended for internal consumption
    * range: [String](String.md)
    * inherited from: [Element](Element.md)
    * in subsets: (owl)
 * [comments](comments.md)  <sub>0..*</sub>
    * Description: notes and comments about an element intended for external consumption
    * range: [String](String.md)
    * inherited from: [Element](Element.md)
    * in subsets: (owl)
 * [notes](notes.md)  <sub>0..*</sub>
    * Description: editorial notes about an element intended for internal consumption
    * range: [String](String.md)
    * inherited from: [Element](Element.md)
    * in subsets: (owl)
 * [examples](examples.md)  <sub>0..*</sub>
    * Description: example usages of an element
    * range: [Example](Example.md)
    * inherited from: [Element](Element.md)
    * in subsets: (owl)
 * [in_subset](in_subset.md)  <sub>0..*</sub>
    * Description: used to indicate membership of a term in a defined subset of biolink terms used for a particular domain or application (e.g. the translator_minimal subset holding the minimal set of predicates used in a translator knowledge graph)
    * range: [SubsetDefinition](SubsetDefinition.md)
    * inherited from: [Element](Element.md)
 * [from_schema](from_schema.md)  <sub>OPT</sub>
    * Description: id of the schema that defined the element
    * range: [Uri](Uri.md)
    * inherited from: [Element](Element.md)
 * [imported_from](imported_from.md)  <sub>OPT</sub>
    * Description: the imports entry that this element was derived from.  Empty means primary source
    * range: [String](String.md)
    * inherited from: [Element](Element.md)
 * [see_also](see_also.md)  <sub>0..*</sub>
    * Description: a reference
    * range: [Uriorcurie](Uriorcurie.md)
    * inherited from: [Element](Element.md)
    * in subsets: (owl)

### Domain for slot:

 * [base](base.md)  <sub>OPT</sub>
    * Description: python base type that implements this type definition
    * range: [String](String.md)
 * [repr](repr.md)  <sub>OPT</sub>
    * Description: the name of the python object that implements this type definition
    * range: [String](String.md)
    * Example: None None
 * [uri](type_uri.md)  <sub>OPT</sub>
    * Description: The uri that defines the possible values for the type definition
    * range: [Uriorcurie](Uriorcurie.md)
 * [typeof](typeof.md)  <sub>OPT</sub>
    * Description: Names a parent type
    * range: [TypeDefinition](TypeDefinition.md)

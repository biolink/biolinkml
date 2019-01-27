# Class: schema definition


a collection of subset, type, slot and class definitions

URI: [http://w3id.org/biolink/biolinkml/meta/SchemaDefinition](http://w3id.org/biolink/biolinkml/meta/SchemaDefinition)

![img](http://yuml.me/diagram/nofunky;dir:TB/class/\[SchemaDefinition|description:string%20%3F;id:uri;title:string%20%3F;version:string%20%3F;imports:uri%20*;license:string%20%3F;default_curi_maps:string%20*;default_prefix:string%20%3F;metamodel_version:string%20%3F;source_file:string%20%3F;source_file_date:datetime%20%3F;source_file_size:integer%20%3F;generation_date:datetime%20%3F;name(pk)(i):string;deprecated(i):string%20%3F;notes(i):string%20*;comments(i):string%20*;see_also(i):uri%20*;id_prefixes(i):ncname%20*]-%20from_schema(i)%20%3F>\[SchemaDefinition],%20\[SchemaDefinition]-%20in_subset(i)%20*>\[SubsetDefinition],%20\[SchemaDefinition]++-%20examples(i)%20*>\[Example],%20\[SchemaDefinition]++-%20classes%20*>\[ClassDefinition],%20\[SchemaDefinition]++-%20slots%20*>\[SlotDefinition],%20\[SchemaDefinition]++-%20types%20*>\[TypeDefinition],%20\[SchemaDefinition]++-%20subsets%20*>\[SubsetDefinition],%20\[SchemaDefinition]-%20default_range%20%3F>\[Definition],%20\[SchemaDefinition]++-%20prefixes%20*>\[Prefix],%20\[Element]-%20from_schema%20%3F>\[SchemaDefinition],%20\[Element]^-\[SchemaDefinition])
## Inheritance

 *  is_a: [Element](Element.md) - a named element in the model
## Children

## Used by

 *  **[Element](Element.md)** *[from_schema](from_schema.md)<sub>opt</sub>*  **[SchemaDefinition](SchemaDefinition.md)**
## Fields

 * [classes](classes.md)<sub>opt</sub>
    * Description: class definitions
    * range: [[ClassDefinition](ClassDefinition.md)]
 * [comments](comments.md) *subsets*: (owl)<sub>opt</sub>
    * Description: notes and comments about an element intended for external consumption
    * range: [[String](String.md)]
    * inherited from: [Element](Element.md)
 * [default_curi_maps](default_curi_maps.md)<sub>opt</sub>
    * Description: ordered list of prefixcommon biocontexts to be fetched to resolve id_prefixes and inline prefix variables
    * range: [[String](String.md)]
 * [default_prefix](default_prefix.md)<sub>opt</sub>
    * Description: default and base prefix -- used for ':' identifiers, @base and @vocab
    * range: [String](String.md)
 * [default_range](default_range.md)<sub>opt</sub>
    * Description: default slot range to be used if range element is omitted from a slot definition
    * range: [Definition](Definition.md)
 * [deprecated](deprecated.md)<sub>opt</sub>
    * Description: Description of why and when this element will no longer be used
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
 * [generation_date](generation_date.md) *subsets*: (owl)<sub>opt</sub>
    * Description: date and time that the schema was loaded/generated
    * range: [Datetime](Datetime.md)
 * [id](id.md)
    * Description: a globally unique schema identifier
    * range: [Uri](Uri.md)
 * [id_prefixes](id_prefixes.md)<sub>opt</sub>
    * Description: a list of Curie prefixes that are used in the representation of instances of the model.  All prefixes in this list are added to the prefix sections of the target models.
    * range: [[Ncname](Ncname.md)]
    * inherited from: [Element](Element.md)
 * [imports](imports.md)<sub>opt</sub>
    * Description: other schemas that are included in this schema
    * range: [[Uri](Uri.md)]
 * [in_subset](in_subset.md)<sub>opt</sub>
    * Description: used to indicate membership of a term in a defined subset of biolink terms used for a particular domain or application (e.g. the translator_minimal subset holding the minimal set of predicates used in a translator knowledge graph)
    * range: [[SubsetDefinition](SubsetDefinition.md)]
    * inherited from: [Element](Element.md)
 * [license](license.md) *subsets*: (owl)<sub>opt</sub>
    * Description: license for the schema
    * range: [String](String.md)
 * [metamodel_version](metamodel_version.md) *subsets*: (owl)<sub>opt</sub>
    * Description: Version of the metamodel used to load the schema
    * range: [String](String.md)
 * [name](name.md) *subsets*: (owl)
    * Description: the unique name of the element within the context of the schema
    * range: [String](String.md)
    * inherited from: [Element](Element.md)
 * [notes](notes.md) *subsets*: (owl)<sub>opt</sub>
    * Description: editorial notes about an element intended for internal consumption
    * range: [[String](String.md)]
    * inherited from: [Element](Element.md)
 * [prefixes](prefixes.md)<sub>opt</sub>
    * Description: prefix / URI definitions to be added to the context beyond those fetched from prefixcommons in id_prefixes
    * range: [[Prefix](Prefix.md)]
 * [schema definition.description](schema_definition_description.md)<sub>opt</sub>
    * Description: a description of the element's purpose and use
    * range: [String](String.md)
 * [see_also](see_also.md) *subsets*: (owl)<sub>opt</sub>
    * Description: a reference
    * range: [[Uri](Uri.md)]
    * inherited from: [Element](Element.md)
 * [schema definition.slots](slot_definitions.md)<sub>opt</sub>
    * Description: slot definitions
    * range: [[SlotDefinition](SlotDefinition.md)]
 * [source_file](source_file.md) *subsets*: (owl)<sub>opt</sub>
    * Description: name, uri or description of the source of the schema
    * range: [String](String.md)
 * [source_file_date](source_file_date.md) *subsets*: (owl)<sub>opt</sub>
    * Description: modification date of the source of the schema
    * range: [Datetime](Datetime.md)
 * [source_file_size](source_file_size.md) *subsets*: (owl)<sub>opt</sub>
    * Description: size in bytes of the source of the schema
    * range: [Integer](Integer.md)
 * [subsets](subsets.md)<sub>opt</sub>
    * Description: list of subsets referenced in this model
    * range: [[SubsetDefinition](SubsetDefinition.md)]
 * [title](title.md) *subsets*: (owl)<sub>opt</sub>
    * Description: the official title of the schema
    * range: [String](String.md)
 * [types](types.md)<sub>opt</sub>
    * Description: data types used in the model
    * range: [[TypeDefinition](TypeDefinition.md)]
 * [version](version.md)<sub>opt</sub>
    * Description: particular version of schema
    * range: [String](String.md)

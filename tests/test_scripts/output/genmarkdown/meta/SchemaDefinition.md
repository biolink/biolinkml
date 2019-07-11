
# Class: schema_definition


a collection of subset, type, slot and class definitions

URI: [meta:SchemaDefinition](https://w3id.org/biolink/biolinkml/meta/SchemaDefinition)

![img](http://yuml.me/diagram/nofunky;dir:TB/class/\[SubsetDefinition]<in_subset(i)%200..*-%20\[SchemaDefinition|id:uri;title:string%20%3F;version:string%20%3F;imports:uriorcurie%20*;license:string%20%3F;emit_prefixes:ncname%20*;default_curi_maps:string%20*;default_prefix:string%20%3F;metamodel_version:string%20%3F;source_file:string%20%3F;source_file_date:datetime%20%3F;source_file_size:integer%20%3F;generation_date:datetime%20%3F;id_prefixes(i):ncname%20*;name(pk)(i):string;aliases(i):string%20*;mappings(i):uriorcurie%20*;description(i):string%20%3F;deprecated(i):string%20%3F;todos(i):string%20*;notes(i):string%20*;comments(i):string%20*;from_schema(i):uri%20%3F;imported_from(i):string%20%3F;see_also(i):uriorcurie%20*],%20\[Example]<examples(i)%200..*-++\[SchemaDefinition],%20\[AltDescription]<alt_descriptions(i)%200..*-++\[SchemaDefinition],%20\[LocalName]<local_names(i)%200..*-++\[SchemaDefinition],%20\[ClassDefinition]<classes%200..*-++\[SchemaDefinition],%20\[SlotDefinition]<slots%200..*-++\[SchemaDefinition],%20\[TypeDefinition]<types%200..*-++\[SchemaDefinition],%20\[SubsetDefinition]<subsets%200..*-++\[SchemaDefinition],%20\[TypeDefinition]<default_range%200..1-%20\[SchemaDefinition],%20\[Prefix]<prefixes%200..*-++\[SchemaDefinition],%20\[Element]^-\[SchemaDefinition])

## Parents

 *  is_a: [Element](Element.md) - a named element in the model

## Referenced by class


## Attributes


### Own

 * [classes](classes.md)  <sub>0..*</sub>
    * Description: class definitions
    * range: [ClassDefinition](ClassDefinition.md)
 * [default_curi_maps](default_curi_maps.md)  <sub>0..*</sub>
    * Description: ordered list of prefixcommon biocontexts to be fetched to resolve id prefixes and inline prefix variables
    * range: [String](String.md)
 * [default_prefix](default_prefix.md)  <sub>OPT</sub>
    * Description: default and base prefix -- used for ':' identifiers, @base and @vocab
    * range: [String](String.md)
 * [default_range](default_range.md)  <sub>OPT</sub>
    * Description: default slot range to be used if range element is omitted from a slot definition
    * range: [TypeDefinition](TypeDefinition.md)
 * [emit_prefixes](emit_prefixes.md)  <sub>0..*</sub>
    * Description: a list of Curie prefixes that are used in the representation of instances of the model.  All prefixes in this list are added to the prefix sections of the target models.
    * range: [Ncname](Ncname.md)
 * [generation_date](generation_date.md)  <sub>OPT</sub>
    * Description: date and time that the schema was loaded/generated
    * range: [Datetime](Datetime.md)
    * in subsets: (owl)
 * [id](id.md)  <sub>REQ</sub>
    * Description: The official schema URI
    * range: [Uri](Uri.md)
 * [imports](imports.md)  <sub>0..*</sub>
    * Description: other schemas that are included in this schema
    * range: [Uriorcurie](Uriorcurie.md)
 * [license](license.md)  <sub>OPT</sub>
    * Description: license for the schema
    * range: [String](String.md)
    * in subsets: (owl)
 * [metamodel_version](metamodel_version.md)  <sub>OPT</sub>
    * Description: Version of the metamodel used to load the schema
    * range: [String](String.md)
    * in subsets: (owl)
 * [prefixes](prefixes.md)  <sub>0..*</sub>
    * Description: prefix / URI definitions to be added to the context beyond those fetched from prefixcommons in id prefixes
    * range: [Prefix](Prefix.md)
 * [slots](slot_definitions.md)  <sub>0..*</sub>
    * Description: slot definitions
    * range: [SlotDefinition](SlotDefinition.md)
 * [source_file](source_file.md)  <sub>OPT</sub>
    * Description: name, uri or description of the source of the schema
    * range: [String](String.md)
    * in subsets: (owl)
 * [source_file_date](source_file_date.md)  <sub>OPT</sub>
    * Description: modification date of the source of the schema
    * range: [Datetime](Datetime.md)
    * in subsets: (owl)
 * [source_file_size](source_file_size.md)  <sub>OPT</sub>
    * Description: size in bytes of the source of the schema
    * range: [Integer](Integer.md)
    * in subsets: (owl)
 * [subsets](subsets.md)  <sub>0..*</sub>
    * Description: list of subsets referenced in this model
    * range: [SubsetDefinition](SubsetDefinition.md)
 * [title](title.md)  <sub>OPT</sub>
    * Description: the official title of the schema
    * range: [String](String.md)
    * in subsets: (owl)
 * [types](types.md)  <sub>0..*</sub>
    * Description: data types used in the model
    * range: [TypeDefinition](TypeDefinition.md)
 * [version](version.md)  <sub>OPT</sub>
    * Description: particular version of schema
    * range: [String](String.md)

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

 * [classes](classes.md)  <sub>0..*</sub>
    * Description: class definitions
    * range: [ClassDefinition](ClassDefinition.md)
 * [default_curi_maps](default_curi_maps.md)  <sub>0..*</sub>
    * Description: ordered list of prefixcommon biocontexts to be fetched to resolve id prefixes and inline prefix variables
    * range: [String](String.md)
 * [default_prefix](default_prefix.md)  <sub>OPT</sub>
    * Description: default and base prefix -- used for ':' identifiers, @base and @vocab
    * range: [String](String.md)
 * [default_range](default_range.md)  <sub>OPT</sub>
    * Description: default slot range to be used if range element is omitted from a slot definition
    * range: [TypeDefinition](TypeDefinition.md)
 * [emit_prefixes](emit_prefixes.md)  <sub>0..*</sub>
    * Description: a list of Curie prefixes that are used in the representation of instances of the model.  All prefixes in this list are added to the prefix sections of the target models.
    * range: [Ncname](Ncname.md)
 * [generation_date](generation_date.md)  <sub>OPT</sub>
    * Description: date and time that the schema was loaded/generated
    * range: [Datetime](Datetime.md)
    * in subsets: (owl)
 * [id](id.md)  <sub>REQ</sub>
    * Description: The official schema URI
    * range: [Uri](Uri.md)
 * [imports](imports.md)  <sub>0..*</sub>
    * Description: other schemas that are included in this schema
    * range: [Uriorcurie](Uriorcurie.md)
 * [license](license.md)  <sub>OPT</sub>
    * Description: license for the schema
    * range: [String](String.md)
    * in subsets: (owl)
 * [metamodel_version](metamodel_version.md)  <sub>OPT</sub>
    * Description: Version of the metamodel used to load the schema
    * range: [String](String.md)
    * in subsets: (owl)
 * [prefixes](prefixes.md)  <sub>0..*</sub>
    * Description: prefix / URI definitions to be added to the context beyond those fetched from prefixcommons in id prefixes
    * range: [Prefix](Prefix.md)
 * [slots](slot_definitions.md)  <sub>0..*</sub>
    * Description: slot definitions
    * range: [SlotDefinition](SlotDefinition.md)
 * [source_file](source_file.md)  <sub>OPT</sub>
    * Description: name, uri or description of the source of the schema
    * range: [String](String.md)
    * in subsets: (owl)
 * [source_file_date](source_file_date.md)  <sub>OPT</sub>
    * Description: modification date of the source of the schema
    * range: [Datetime](Datetime.md)
    * in subsets: (owl)
 * [source_file_size](source_file_size.md)  <sub>OPT</sub>
    * Description: size in bytes of the source of the schema
    * range: [Integer](Integer.md)
    * in subsets: (owl)
 * [subsets](subsets.md)  <sub>0..*</sub>
    * Description: list of subsets referenced in this model
    * range: [SubsetDefinition](SubsetDefinition.md)
 * [title](title.md)  <sub>OPT</sub>
    * Description: the official title of the schema
    * range: [String](String.md)
    * in subsets: (owl)
 * [types](types.md)  <sub>0..*</sub>
    * Description: data types used in the model
    * range: [TypeDefinition](TypeDefinition.md)
 * [version](version.md)  <sub>OPT</sub>
    * Description: particular version of schema
    * range: [String](String.md)


# Type: type_definition


A data type definition.

URI: [meta:TypeDefinition](https://w3id.org/biolink/biolinkml/meta/TypeDefinition)


![img](http://yuml.me/diagram/nofunky;dir:TB/class/\[SubsetDefinition]<in_subset(i)%200..*-%20\[TypeDefinition|base:string%20%3F;uri:uriorcurie%20%3F;repr:string%20%3F;id_prefixes(i):ncname%20*;name(pk)(i):string;definition_uri(i):uriorcurie%20%3F;aliases(i):string%20*;mappings(i):uriorcurie%20*;description(i):string%20%3F;deprecated(i):string%20%3F;todos(i):string%20*;notes(i):string%20*;comments(i):string%20*;from_schema(i):uri%20%3F;imported_from(i):string%20%3F;see_also(i):uriorcurie%20*;exact_mappings(i):uriorcurie%20*;close_mappings(i):uriorcurie%20*;related_mappings(i):uriorcurie%20*;deprecated_element_has_exact_replacement(i):uriorcurie%20%3F;deprecated_element_has_possible_replacement(i):uriorcurie%20%3F],%20\[Example]<examples(i)%200..*-++\[TypeDefinition],%20\[AltDescription]<alt_descriptions(i)%200..*-++\[TypeDefinition],%20\[LocalName]<local_names(i)%200..*-++\[TypeDefinition],%20\[TypeDefinition]<typeof%200..1-%20\[TypeDefinition],%20\[SchemaDefinition]-%20default_range%200..1>\[TypeDefinition],%20\[SchemaDefinition]++-%20types%200..*>\[TypeDefinition],%20\[Element]^-\[TypeDefinition])

## Parents

 *  is_a: [element](element.md) - a named element in the model

## Referenced by class

 *  **[schema_definition](schema_definition.md)** *[default_range](default_range.md)*  <sub>OPT</sub>  **[type_definition](type_definition.md)**
 *  **[type_definition](type_definition.md)** *[typeof](typeof.md)*  <sub>OPT</sub>  **[type_definition](type_definition.md)**
 *  **[schema_definition](schema_definition.md)** *[types](types.md)*  <sub>0..*</sub>  **[type_definition](type_definition.md)**

## Attributes


### Own

 * [base](base.md)  <sub>OPT</sub>
    * Description: python base type that implements this type definition
    * range: [String](type/String.md)
 * [repr](repr.md)  <sub>OPT</sub>
    * Description: the name of the python object that implements this type definition
    * range: [String](type/String.md)
    * Example: None None
 * [type_definition➞uri](type_uri.md)  <sub>OPT</sub>
    * Description: The uri that defines the possible values for the type definition
    * range: [Uriorcurie](type/Uriorcurie.md)
 * [typeof](typeof.md)  <sub>OPT</sub>
    * Description: Names a parent type
    * range: [type_definition](type_definition.md)

### Inherited from element:

 * [id_prefixes](id_prefixes.md)  <sub>0..*</sub>
    * Description: the identifier of this class or slot must begin with one of the URIs referenced by this prefix
    * range: [Ncname](type/Ncname.md)
    * inherited from: [element](element.md)
 * [name](name.md)  <sub>REQ</sub>
    * Description: the unique name of the element within the context of the schema.  Name is combined with the default prefix to form the globally unique subject of the target class.
    * range: [String](type/String.md)
    * inherited from: [element](element.md)
    * in subsets: (owl)
 * [definition_uri](definition_uri.md)  <sub>OPT</sub>
    * Description: the "native" URI of the element
    * range: [Uriorcurie](type/Uriorcurie.md)
    * inherited from: [element](element.md)
 * [aliases](aliases.md)  <sub>0..*</sub>
    * range: [String](type/String.md)
    * inherited from: [element](element.md)
 * [local_names](local_names.md)  <sub>0..*</sub>
    * range: [local_name](local_name.md)
    * inherited from: [element](element.md)
 * [mappings](mappings.md)  <sub>0..*</sub>
    * Description: A list of terms from different schemas or terminology systems that have comparable meaning. These may include terms that are precisely equivalent, broader or narrower in meaning, or otherwise semantically related but not equivalent from a strict ontological perspective.
    * range: [Uriorcurie](type/Uriorcurie.md)
    * inherited from: None
 * [description](description.md)  <sub>OPT</sub>
    * Description: a description of the element's purpose and use
    * range: [String](type/String.md)
    * inherited from: [element](element.md)
    * in subsets: (owl)
 * [alt_descriptions](alt_descriptions.md)  <sub>0..*</sub>
    * range: [alt_description](alt_description.md)
    * inherited from: [element](element.md)
 * [deprecated](deprecated.md)  <sub>OPT</sub>
    * Description: Description of why and when this element will no longer be used
    * range: [String](type/String.md)
    * inherited from: [element](element.md)
 * [todos](todos.md)  <sub>0..*</sub>
    * Description: Outstanding issue that needs resolution
    * range: [String](type/String.md)
    * inherited from: [element](element.md)
 * [notes](notes.md)  <sub>0..*</sub>
    * Description: editorial notes about an element intended for internal consumption
    * range: [String](type/String.md)
    * inherited from: [element](element.md)
    * in subsets: (owl)
 * [comments](comments.md)  <sub>0..*</sub>
    * Description: notes and comments about an element intended for external consumption
    * range: [String](type/String.md)
    * inherited from: [element](element.md)
    * in subsets: (owl)
 * [examples](examples.md)  <sub>0..*</sub>
    * Description: example usages of an element
    * range: [example](example.md)
    * inherited from: [element](element.md)
    * in subsets: (owl)
 * [in_subset](in_subset.md)  <sub>0..*</sub>
    * Description: used to indicate membership of a term in a defined subset of biolink terms used for a particular domain or application (e.g. the translator_minimal subset holding the minimal set of predicates used in a translator knowledge graph)
    * range: [subset_definition](subset_definition.md)
    * inherited from: [element](element.md)
 * [from_schema](from_schema.md)  <sub>OPT</sub>
    * Description: id of the schema that defined the element
    * range: [Uri](type/Uri.md)
    * inherited from: [element](element.md)
 * [imported_from](imported_from.md)  <sub>OPT</sub>
    * Description: the imports entry that this element was derived from.  Empty means primary source
    * range: [String](type/String.md)
    * inherited from: [element](element.md)
 * [see_also](see_also.md)  <sub>0..*</sub>
    * Description: a reference
    * range: [Uriorcurie](type/Uriorcurie.md)
    * inherited from: [element](element.md)
    * in subsets: (owl)
 * [exact mappings](exact_mappings.md)  <sub>0..*</sub>
    * Description: A list of terms from different schemas or terminology systems that have identical meaning.
    * range: [Uriorcurie](type/Uriorcurie.md)
    * inherited from: None
 * [close mappings](close_mappings.md)  <sub>0..*</sub>
    * Description: A list of terms from different schemas or terminology systems that have close meaning.
    * range: [Uriorcurie](type/Uriorcurie.md)
    * inherited from: None
 * [related mappings](related_mappings.md)  <sub>0..*</sub>
    * Description: A list of terms from different schemas or terminology systems that have related meaning.
    * range: [Uriorcurie](type/Uriorcurie.md)
    * inherited from: None
 * [deprecated element has exact replacement](deprecated_element_has_exact_replacement.md)  <sub>OPT</sub>
    * Description: When an element is deprecated, it can be automatically replaced by this uri or curie
    * range: [Uriorcurie](type/Uriorcurie.md)
    * inherited from: None
 * [deprecated element has possible replacement](deprecated_element_has_possible_replacement.md)  <sub>OPT</sub>
    * Description: When an element is deprecated, it can be potentially replaced by this uri or curie
    * range: [Uriorcurie](type/Uriorcurie.md)
    * inherited from: None

### Domain for slot:

 * [base](base.md)  <sub>OPT</sub>
    * Description: python base type that implements this type definition
    * range: [String](type/String.md)
 * [repr](repr.md)  <sub>OPT</sub>
    * Description: the name of the python object that implements this type definition
    * range: [String](type/String.md)
    * Example: None None
 * [type_definition➞uri](type_uri.md)  <sub>OPT</sub>
    * Description: The uri that defines the possible values for the type definition
    * range: [Uriorcurie](type/Uriorcurie.md)
 * [typeof](typeof.md)  <sub>OPT</sub>
    * Description: Names a parent type
    * range: [type_definition](type_definition.md)

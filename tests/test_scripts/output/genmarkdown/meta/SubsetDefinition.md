
# Type: subset_definition


the name and description of a subset

URI: [meta:SubsetDefinition](https://w3id.org/biolink/biolinkml/meta/SubsetDefinition)


![img](http://yuml.me/diagram/nofunky;dir:TB/class/[Element]-%20in_subset%200..*>[SubsetDefinition&#124;id_prefixes(i):ncname%20*;name(i):string;definition_uri(i):uriorcurie%20%3F;aliases(i):string%20*;mappings(i):uriorcurie%20*;description(i):string%20%3F;deprecated(i):string%20%3F;todos(i):string%20*;notes(i):string%20*;comments(i):string%20*;from_schema(i):uri%20%3F;imported_from(i):string%20%3F;see_also(i):uriorcurie%20*;exact_mappings(i):uriorcurie%20*;close_mappings(i):uriorcurie%20*;related_mappings(i):uriorcurie%20*;narrow_mappings(i):uriorcurie%20*;broad_mappings(i):uriorcurie%20*;deprecated_element_has_exact_replacement(i):uriorcurie%20%3F;deprecated_element_has_possible_replacement(i):uriorcurie%20%3F],[SchemaDefinition]++-%20subsets%200..*>[SubsetDefinition],[Element]^-[SubsetDefinition],[SchemaDefinition],[LocalName],[Extension],[Example],[Element],[Annotation],[AltDescription])

## Parents

 *  is_a: [Element](Element.md) - a named element in the model

## Referenced by class

 *  **[Element](Element.md)** *[in_subset](in_subset.md)*  <sub>0..*</sub>  **[SubsetDefinition](SubsetDefinition.md)**
 *  **[SchemaDefinition](SchemaDefinition.md)** *[subsets](subsets.md)*  <sub>0..*</sub>  **[SubsetDefinition](SubsetDefinition.md)**

## Attributes


### Inherited from element:

 * [aliases](aliases.md)  <sub>0..*</sub>
    * range: [String](types/String.md)
 * [alt_descriptions](alt_descriptions.md)  <sub>0..*</sub>
    * range: [AltDescription](AltDescription.md)
 * [broad mappings](broad_mappings.md)  <sub>0..*</sub>
    * Description: A list of terms from different schemas or terminology systems that have broader meaning.
    * range: [Uriorcurie](types/Uriorcurie.md)
 * [close mappings](close_mappings.md)  <sub>0..*</sub>
    * Description: A list of terms from different schemas or terminology systems that have close meaning.
    * range: [Uriorcurie](types/Uriorcurie.md)
 * [comments](comments.md)  <sub>0..*</sub>
    * Description: notes and comments about an element intended for external consumption
    * range: [String](types/String.md)
    * in subsets: (owl)
 * [definition_uri](definition_uri.md)  <sub>OPT</sub>
    * Description: the "native" URI of the element
    * range: [Uriorcurie](types/Uriorcurie.md)
 * [deprecated](deprecated.md)  <sub>OPT</sub>
    * Description: Description of why and when this element will no longer be used
    * range: [String](types/String.md)
 * [deprecated element has exact replacement](deprecated_element_has_exact_replacement.md)  <sub>OPT</sub>
    * Description: When an element is deprecated, it can be automatically replaced by this uri or curie
    * range: [Uriorcurie](types/Uriorcurie.md)
 * [deprecated element has possible replacement](deprecated_element_has_possible_replacement.md)  <sub>OPT</sub>
    * Description: When an element is deprecated, it can be potentially replaced by this uri or curie
    * range: [Uriorcurie](types/Uriorcurie.md)
 * [description](description.md)  <sub>OPT</sub>
    * Description: a description of the element's purpose and use
    * range: [String](types/String.md)
    * in subsets: (owl)
 * [exact mappings](exact_mappings.md)  <sub>0..*</sub>
    * Description: A list of terms from different schemas or terminology systems that have identical meaning.
    * range: [Uriorcurie](types/Uriorcurie.md)
 * [examples](examples.md)  <sub>0..*</sub>
    * Description: example usages of an element
    * range: [Example](Example.md)
    * in subsets: (owl)
 * [from_schema](from_schema.md)  <sub>OPT</sub>
    * Description: id of the schema that defined the element
    * range: [Uri](types/Uri.md)
 * [id_prefixes](id_prefixes.md)  <sub>0..*</sub>
    * Description: the identifier of this class or slot must begin with one of the URIs referenced by this prefix
    * range: [Ncname](types/Ncname.md)
 * [imported_from](imported_from.md)  <sub>OPT</sub>
    * Description: the imports entry that this element was derived from.  Empty means primary source
    * range: [String](types/String.md)
 * [in_subset](in_subset.md)  <sub>0..*</sub>
    * Description: used to indicate membership of a term in a defined subset of biolink terms used for a particular domain or application (e.g. the translator_minimal subset holding the minimal set of predicates used in a translator knowledge graph)
    * range: [SubsetDefinition](SubsetDefinition.md)
 * [local_names](local_names.md)  <sub>0..*</sub>
    * range: [LocalName](LocalName.md)
 * [mappings](mappings.md)  <sub>0..*</sub>
    * Description: A list of terms from different schemas or terminology systems that have comparable meaning. These may include terms that are precisely equivalent, broader or narrower in meaning, or otherwise semantically related but not equivalent from a strict ontological perspective.
    * range: [Uriorcurie](types/Uriorcurie.md)
 * [name](name.md)  <sub>REQ</sub>
    * Description: the unique name of the element within the context of the schema.  Name is combined with the default prefix to form the globally unique subject of the target class.
    * range: [String](types/String.md)
    * in subsets: (owl)
 * [narrow mappings](narrow_mappings.md)  <sub>0..*</sub>
    * Description: A list of terms from different schemas or terminology systems that have narrower meaning.
    * range: [Uriorcurie](types/Uriorcurie.md)
 * [notes](notes.md)  <sub>0..*</sub>
    * Description: editorial notes about an element intended for internal consumption
    * range: [String](types/String.md)
    * in subsets: (owl)
 * [related mappings](related_mappings.md)  <sub>0..*</sub>
    * Description: A list of terms from different schemas or terminology systems that have related meaning.
    * range: [Uriorcurie](types/Uriorcurie.md)
 * [see_also](see_also.md)  <sub>0..*</sub>
    * Description: a reference
    * range: [Uriorcurie](types/Uriorcurie.md)
    * in subsets: (owl)
 * [todos](todos.md)  <sub>0..*</sub>
    * Description: Outstanding issue that needs resolution
    * range: [String](types/String.md)

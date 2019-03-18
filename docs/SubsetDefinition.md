# Class: subset_definition


the name and description of a subset

URI: [http://w3id.org/biolink/biolinkml/meta/SubsetDefinition](http://w3id.org/biolink/biolinkml/meta/SubsetDefinition)

![img](images/SubsetDefinition.png)
## Inheritance

 *  is_a: [Element](Element.md) - a named element in the model
## Children

## Used by

 *  **[Element](Element.md)** *[in_subset](in_subset.md)*  <sub>0..*</sub>  **[SubsetDefinition](SubsetDefinition.md)**
 *  **[SchemaDefinition](SchemaDefinition.md)** *[subsets](subsets.md)*  <sub>0..*</sub>  **[SubsetDefinition](SubsetDefinition.md)**
## Fields

 * [aliases](aliases.md)  <sub>0..*</sub>
    * range: [String](String.md)
    * inherited from: [Element](Element.md)
 * [alt_descriptions](alt_descriptions.md)  <sub>0..*</sub>
    * range: [AltDescription](AltDescription.md)
    * inherited from: [Element](Element.md)
 * [comments](comments.md)  <sub>0..*</sub>
    * Description: notes and comments about an element intended for external consumption
    * range: [String](String.md)
    * inherited from: [Element](Element.md)
    * in subsets: (owl)
 * [deprecated](deprecated.md)  <sub>OPT</sub>
    * Description: Description of why and when this element will no longer be used
    * range: [String](String.md)
    * inherited from: [Element](Element.md)
 * [description](description.md)  <sub>OPT</sub>
    * Description: a description of the element's purpose and use
    * range: [String](String.md)
    * inherited from: [Element](Element.md)
    * in subsets: (owl)
 * [examples](examples.md)  <sub>0..*</sub>
    * Description: example usages of an element
    * range: [Example](Example.md)
    * inherited from: [Element](Element.md)
    * in subsets: (owl)
 * [from_schema](from_schema.md)  <sub>OPT</sub>
    * Description: id of the schema that defined the element
    * range: [Uri](Uri.md)
    * inherited from: [Element](Element.md)
 * [id_prefixes](id_prefixes.md)  <sub>0..*</sub>
    * Description: the identifier of this class or slot must begin with one of the URIs referenced by this prefix
    * range: [Ncname](Ncname.md)
    * inherited from: [Element](Element.md)
 * [imported_from](imported_from.md)  <sub>OPT</sub>
    * Description: the imports entry that this element was derived from.  Empty means primary source
    * range: [String](String.md)
    * inherited from: [Element](Element.md)
 * [in_subset](in_subset.md)  <sub>0..*</sub>
    * Description: used to indicate membership of a term in a defined subset of biolink terms used for a particular domain or application (e.g. the translator_minimal subset holding the minimal set of predicates used in a translator knowledge graph)
    * range: [SubsetDefinition](SubsetDefinition.md)
    * inherited from: [Element](Element.md)
 * [local_names](local_names.md)  <sub>0..*</sub>
    * range: [LocalName](LocalName.md)
    * inherited from: [Element](Element.md)
 * [mappings](mappings.md)  <sub>0..*</sub>
    * Description: A list of terms from different schemas or terminology systems that have comparable meaning. These may include terms that are precisely equivalent, broader or narrower in meaning, or otherwise semantically related but not equivalent from a strict ontological perspective.
    * range: [Uriorcurie](Uriorcurie.md)
    * inherited from: [Element](Element.md)
 * [name](name.md)  <sub>REQ</sub>
    * Description: the unique name of the element within the context of the schema.  Name is combined with the default prefix to form the globally unique subject of the target class.
    * range: [String](String.md)
    * inherited from: [Element](Element.md)
    * in subsets: (owl)
 * [notes](notes.md)  <sub>0..*</sub>
    * Description: editorial notes about an element intended for internal consumption
    * range: [String](String.md)
    * inherited from: [Element](Element.md)
    * in subsets: (owl)
 * [see_also](see_also.md)  <sub>0..*</sub>
    * Description: a reference
    * range: [Uriorcurie](Uriorcurie.md)
    * inherited from: [Element](Element.md)
    * in subsets: (owl)
 * [todos](todos.md)  <sub>0..*</sub>
    * Description: Outstanding issue that needs resolution
    * range: [String](String.md)
    * inherited from: [Element](Element.md)

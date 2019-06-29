
# Class: class_definition


the definition of a class or interface

URI: [meta:ClassDefinition](https://w3id.org/biolink/biolinkml/meta/ClassDefinition)

![img](http://yuml.me/diagram/nofunky;dir:TB/class/\[SubsetDefinition]<in_subset(i)%200..*-%20\[ClassDefinition|class_uri:uriorcurie%20%3F;subclass_of:uriorcurie%20%3F;abstract(i):boolean%20%3F;mixin(i):boolean%20%3F;values_from(i):uriorcurie%20*;id_prefixes(i):ncname%20*;name(pk)(i):string;aliases(i):string%20*;mappings(i):uriorcurie%20*;description(i):string%20%3F;deprecated(i):string%20%3F;todos(i):string%20*;notes(i):string%20*;comments(i):string%20*;from_schema(i):uri%20%3F;imported_from(i):string%20%3F;see_also(i):uriorcurie%20*],%20\[Example]<examples(i)%200..*-++\[ClassDefinition],%20\[AltDescription]<alt_descriptions(i)%200..*-++\[ClassDefinition],%20\[LocalName]<local_names(i)%200..*-++\[ClassDefinition],%20\[SlotDefinition]<defining_slots%200..*-%20\[ClassDefinition],%20\[ClassDefinition]<union_of%200..*-%20\[ClassDefinition],%20\[SlotDefinition]<slot_usage%200..*-++\[ClassDefinition],%20\[SlotDefinition]<slots%200..*-%20\[ClassDefinition],%20\[ClassDefinition]<apply_to%200..*-%20\[ClassDefinition],%20\[ClassDefinition]<mixins%200..*-%20\[ClassDefinition],%20\[ClassDefinition]<is_a%200..1-%20\[ClassDefinition],%20\[SchemaDefinition]++-%20classes%200..*>\[ClassDefinition],%20\[SlotDefinition]-%20domain%201..1>\[ClassDefinition],%20\[Definition]^-\[ClassDefinition])

## Parents

 *  is_a: [Definition](Definition.md) - base class for definitions

## Referenced by class

 *  **[ClassDefinition](ClassDefinition.md)** *[apply_to](class_definition_apply_to.md)*  <sub>0..*</sub>  **[ClassDefinition](ClassDefinition.md)**
 *  **[ClassDefinition](ClassDefinition.md)** *[is_a](class_definition_is_a.md)*  <sub>OPT</sub>  **[ClassDefinition](ClassDefinition.md)**
 *  **[ClassDefinition](ClassDefinition.md)** *[mixins](class_definition_mixins.md)*  <sub>0..*</sub>  **[ClassDefinition](ClassDefinition.md)**
 *  **[SchemaDefinition](SchemaDefinition.md)** *[classes](classes.md)*  <sub>0..*</sub>  **[ClassDefinition](ClassDefinition.md)**
 *  **[SlotDefinition](SlotDefinition.md)** *[domain](domain.md)*  <sub>REQ</sub>  **[ClassDefinition](ClassDefinition.md)**
 *  **[ClassDefinition](ClassDefinition.md)** *[union_of](union_of.md)*  <sub>0..*</sub>  **[ClassDefinition](ClassDefinition.md)**

## Attributes


### Own

 * [apply_to](class_definition_apply_to.md)  <sub>0..*</sub>
    * range: [ClassDefinition](ClassDefinition.md)
 * [is_a](class_definition_is_a.md)  <sub>OPT</sub>
    * range: [ClassDefinition](ClassDefinition.md)
 * [mixins](class_definition_mixins.md)  <sub>0..*</sub>
    * range: [ClassDefinition](ClassDefinition.md)
 * [class_uri](class_uri.md)  <sub>OPT</sub>
    * Description: URI of the class in an RDF environment
    * range: [Uriorcurie](Uriorcurie.md)
 * [defining_slots](defining_slots.md)  <sub>0..*</sub>
    * Description: The combination of is a plus defining slots form a genus-differentia definition, or the set of necessary and sufficient conditions that can be transformed into an OWL equivalence axiom
    * range: [SlotDefinition](SlotDefinition.md)
 * [slot_usage](slot_usage.md)  <sub>0..*</sub>
    * Description: the redefinition of a slot in the context of the containing class definition.
    * range: [SlotDefinition](SlotDefinition.md)
 * [slots](slots.md)  <sub>0..*</sub>
    * Description: list of slot names that are applicable to a class
    * range: [SlotDefinition](SlotDefinition.md)
 * [subclass_of](subclass_of.md)  <sub>OPT</sub>
    * Description: rdfs:subClassOf to be emitted in OWL generation
    * range: [Uriorcurie](Uriorcurie.md)
 * [union_of](union_of.md)  <sub>0..*</sub>
    * Description: indicates that the domain class consists exactly of the members of the classes in the range
    * range: [ClassDefinition](ClassDefinition.md)

### Inherited from definition:

 * [is_a](is_a.md)  <sub>OPT</sub>
    * Description: specifies single-inheritance between classes or slots. While multiple inheritance is not allowed, mixins can be provided effectively providing the same thing. The semantics are the same when translated to formalisms that allow MI (e.g. RDFS/OWL). When translating to a SI framework (e.g. java classes, python classes) then is a is used. When translating a framework without polymorphism (e.g. json-schema, solr document schema) then is a and mixins are recursively unfolded
    * range: [Definition](Definition.md)
    * inherited from: [Definition](Definition.md)
 * [abstract](abstract.md)  <sub>OPT</sub>
    * Description: an abstract class is a high level class or slot that is typically used to group common slots together and cannot be directly instantiated.
    * range: [Boolean](Boolean.md)
    * inherited from: [Definition](Definition.md)
 * [mixin](mixin.md)  <sub>OPT</sub>
    * Description: this slot or class can only be used as a mixin -- equivalent to abstract
    * range: [Boolean](Boolean.md)
    * inherited from: [Definition](Definition.md)
 * [mixins](mixins.md)  <sub>0..*</sub>
    * Description: List of definitions to be mixed in. Targets may be any definition of the same type
    * range: [Definition](Definition.md)
    * inherited from: [Definition](Definition.md)
 * [apply_to](apply_to.md)  <sub>0..*</sub>
    * Description: Used to extend class or slot definitions. For example, if we have a core schema where a gene has two slots for identifier and symbol, and we have a specialized schema for my_organism where we wish to add a slot systematic_name, we can avoid subclassing by defining a class gene_my_organism, adding the slot to this class, and then adding an apply_to pointing to the gene class. The new slot will be 'injected into' the gene class.
    * range: [Definition](Definition.md)
    * inherited from: [Definition](Definition.md)
 * [values_from](values_from.md)  <sub>0..*</sub>
    * Description: the identifier of a "value set" -- a set of identifiers that form the possible values for the range of a slot
    * range: [Uriorcurie](Uriorcurie.md)
    * inherited from: [Definition](Definition.md)

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

 * [apply_to](class_definition_apply_to.md)  <sub>0..*</sub>
    * range: [ClassDefinition](ClassDefinition.md)
 * [is_a](class_definition_is_a.md)  <sub>OPT</sub>
    * range: [ClassDefinition](ClassDefinition.md)
 * [mixins](class_definition_mixins.md)  <sub>0..*</sub>
    * range: [ClassDefinition](ClassDefinition.md)
 * [class_uri](class_uri.md)  <sub>OPT</sub>
    * Description: URI of the class in an RDF environment
    * range: [Uriorcurie](Uriorcurie.md)
 * [defining_slots](defining_slots.md)  <sub>0..*</sub>
    * Description: The combination of is a plus defining slots form a genus-differentia definition, or the set of necessary and sufficient conditions that can be transformed into an OWL equivalence axiom
    * range: [SlotDefinition](SlotDefinition.md)
 * [slot_usage](slot_usage.md)  <sub>0..*</sub>
    * Description: the redefinition of a slot in the context of the containing class definition.
    * range: [SlotDefinition](SlotDefinition.md)
 * [slots](slots.md)  <sub>0..*</sub>
    * Description: list of slot names that are applicable to a class
    * range: [SlotDefinition](SlotDefinition.md)
 * [subclass_of](subclass_of.md)  <sub>OPT</sub>
    * Description: rdfs:subClassOf to be emitted in OWL generation
    * range: [Uriorcurie](Uriorcurie.md)
 * [union_of](union_of.md)  <sub>0..*</sub>
    * Description: indicates that the domain class consists exactly of the members of the classes in the range
    * range: [ClassDefinition](ClassDefinition.md)

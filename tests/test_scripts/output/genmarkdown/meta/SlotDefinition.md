# Class: slot definition


the definition of a property or a slot

URI: [http://w3id.org/biolink/biolinkml/meta/SlotDefinition](http://w3id.org/biolink/biolinkml/meta/SlotDefinition)

![img](http://yuml.me/diagram/nofunky;dir:TB/class/\[SlotDefinition|slot_uri:uri%20%3F;multivalued:boolean%20%3F;inherited:boolean%20%3F;readonly:string%20%3F;ifabsent:string%20%3F;required:boolean%20%3F;inlined:boolean%20%3F;key:boolean%20%3F;identifier:boolean%20%3F;alias:string%20%3F;subclass_of:uri%20%3F;abstract(i):boolean%20%3F;local_names(i):string%20*;mixin(i):boolean%20%3F;values_from(i):uri%20*;name(pk)(i):string;description(i):string%20%3F;deprecated(i):string%20%3F;notes(i):string%20*;comments(i):string%20*;see_also(i):uri%20*;id_prefixes(i):ncname%20*]-%20from_schema(i)%20%3F>\[SchemaDefinition],%20\[SlotDefinition]-%20in_subset(i)%20*>\[SubsetDefinition],%20\[SlotDefinition]++-%20examples(i)%20*>\[Example],%20\[SlotDefinition]-%20inverse%20%3F>\[SlotDefinition],%20\[SlotDefinition]-%20range%20%3F>\[Element],%20\[SlotDefinition]-%20domain>\[ClassDefinition],%20\[SlotDefinition]-%20apply_to%20*>\[SlotDefinition],%20\[SlotDefinition]-%20mixins%20*>\[SlotDefinition],%20\[SlotDefinition]-%20is_a%20%3F>\[SlotDefinition],%20\[ClassDefinition]-%20defining_slots%20*>\[SlotDefinition],%20\[SchemaDefinition]++-%20slots%20*>\[SlotDefinition],%20\[ClassDefinition]++-%20slot_usage%20*>\[SlotDefinition],%20\[ClassDefinition]-%20slots%20*>\[SlotDefinition],%20\[Definition]^-\[SlotDefinition])
## Inheritance

 *  is_a: [Definition](Definition.md) - base class for definitions
## Children

## Used by

 *  **[ClassDefinition](ClassDefinition.md)** *[defining_slots](defining_slots.md)<sub>opt</sub>*  **[[SlotDefinition](SlotDefinition.md)]**
 *  **[SlotDefinition](SlotDefinition.md)** *[inverse](inverse.md)<sub>opt</sub>*  **[SlotDefinition](SlotDefinition.md)**
 *  **[SlotDefinition](SlotDefinition.md)** *[slot definition.apply_to](slot_definition_apply_to.md)<sub>opt</sub>*  **[[SlotDefinition](SlotDefinition.md)]**
 *  **[SlotDefinition](SlotDefinition.md)** *[slot definition.is_a](slot_definition_is_a.md)<sub>opt</sub>*  **[SlotDefinition](SlotDefinition.md)**
 *  **[SlotDefinition](SlotDefinition.md)** *[slot definition.mixins](slot_definition_mixins.md)<sub>opt</sub>*  **[[SlotDefinition](SlotDefinition.md)]**
 *  **[SchemaDefinition](SchemaDefinition.md)** *[schema definition.slots](slot_definitions.md)<sub>opt</sub>*  **[[SlotDefinition](SlotDefinition.md)]**
 *  **[ClassDefinition](ClassDefinition.md)** *[slot_usage](slot_usage.md)<sub>opt</sub>*  **[[SlotDefinition](SlotDefinition.md)]**
 *  **[ClassDefinition](ClassDefinition.md)** *[slots](slots.md)<sub>opt</sub>*  **[[SlotDefinition](SlotDefinition.md)]**
## Fields

 * [abstract](abstract.md)<sub>opt</sub>
    * Description: an abstract class is a high level class or slot that is typically used to group common slots together and cannot be directly instantiated.
    * range: [Boolean](Boolean.md)
    * inherited from: [Definition](Definition.md)
 * [alias](alias.md)<sub>opt</sub>
    * Description: the name used for a slot in the context of its owning class.  If present, this is used instead of the actual slot name.
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
 * [domain](domain.md)
    * Description: defines the type of the subject of the slot.  Given the following slot definition
  S1:
    domain: C1
    range:  C2
the declaration
  X:
    S1: Y

implicitly asserts that X is an instance of C1

    * range: [ClassDefinition](ClassDefinition.md)
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
 * [identifier](identifier.md)<sub>opt</sub>
    * Description: True means that this slot must be unique across the collection of slots
    * range: [Boolean](Boolean.md)
 * [ifabsent](ifabsent.md)<sub>opt</sub>
    * Description: description of special behavior if the slot is absent
    * range: [String](String.md)
 * [in_subset](in_subset.md)<sub>opt</sub>
    * Description: used to indicate membership of a term in a defined subset of biolink terms used for a particular domain or application (e.g. the translator_minimal subset holding the minimal set of predicates used in a translator knowledge graph)
    * range: [[SubsetDefinition](SubsetDefinition.md)]
    * inherited from: [Element](Element.md)
 * [inherited](inherited.md)<sub>opt</sub>
    * Description: true means that the *value* of a slot is inherited by subclasses
    * range: [Boolean](Boolean.md)
 * [inlined](inlined.md)<sub>opt</sub>
    * Description: an inlined definition a list of actual values rather than references.  Only applies to slots whose range is a class.
    * range: [Boolean](Boolean.md)
 * [inverse](inverse.md)<sub>opt</sub>
    * Description: used to indicate the inverse of a slot (e.g. 'expresses' is the inverse predicate of 'expressed in')
    * range: [SlotDefinition](SlotDefinition.md)
 * [key](key.md)<sub>opt</sub>
    * Description: true means that the slot uniquely identifies the element within the context of its container
    * range: [Boolean](Boolean.md)
 * [local_names](local_names.md)<sub>opt</sub>
    * Description: map from local identifier to slot
    * range: [[String](String.md)]
    * inherited from: [Definition](Definition.md)
 * [mixin](mixin.md)<sub>opt</sub>
    * Description: this slot or class can only be used as a mixin -- equivalent to abstract
    * range: [Boolean](Boolean.md)
    * inherited from: [Definition](Definition.md)
 * [multivalued](multivalued.md)<sub>opt</sub>
    * Description: true means that slot can have more than one value
    * range: [Boolean](Boolean.md)
 * [name](name.md) *subsets*: (owl)
    * Description: the unique name of the element within the context of the schema
    * range: [String](String.md)
    * inherited from: [Element](Element.md)
 * [notes](notes.md) *subsets*: (owl)<sub>opt</sub>
    * Description: editorial notes about an element intended for internal consumption
    * range: [[String](String.md)]
    * inherited from: [Element](Element.md)
 * [range](range.md)<sub>opt</sub>
    * Description: defines the type of the object of the slot.  Given the following slot definition
  S1:
    domain: C1
    range:  C2
the declaration
  X:
    S1: Y

implicitly asserts Y is an instance of C2

    * range: [Element](Element.md)
 * [slot definition.subclass_of](range_subclass.md)<sub>opt</sub>
    * Description: Constraint on the range of a property
    * range: [Uri](Uri.md)
 * [readonly](readonly.md)<sub>opt</sub>
    * Description: If present, slot is read only.  Text explains why
    * range: [String](String.md)
 * [required](required.md)<sub>opt</sub>
    * Description: true means that the slot must be present in the loaded definition
    * range: [Boolean](Boolean.md)
 * [see_also](see_also.md) *subsets*: (owl)<sub>opt</sub>
    * Description: a reference
    * range: [[Uri](Uri.md)]
    * inherited from: [Element](Element.md)
 * [slot definition.apply_to](slot_definition_apply_to.md)<sub>opt</sub>
    * Description: Used to extend class or slot definitions. For example, if we have a core schema where a gene has two slots for identifier and symbol, and we have a specialized schema for my_organism where we wish to add a slot systematic_name, we can avoid subclassing by defining a class gene_my_organism, adding the slot to this class, and then adding an apply_to pointing to the gene class. The new slot will be 'injected into' the gene class.
    * range: [[SlotDefinition](SlotDefinition.md)]
 * [slot definition.is_a](slot_definition_is_a.md)<sub>opt</sub>
    * Description: specifies single-inheritance between classes or slots. While multiple inheritance is not allowed, mixins can be provided effectively providing the same thing. The semantics are the same when translated to formalisms that allow MI (e.g. RDFS/OWL). When translating to a SI framework (e.g. java classes, python classes) then is_a is used. When translating a framework without polymorphism (e.g. json-schema, solr document schema) then is_a and mixins are recursively unfolded
    * range: [SlotDefinition](SlotDefinition.md)
 * [slot definition.mixins](slot_definition_mixins.md)<sub>opt</sub>
    * Description: List of definitions to be mixed in. Targets may be any definition of the same type
    * range: [[SlotDefinition](SlotDefinition.md)]
 * [slot_uri](slot_uri.md)<sub>opt</sub>
    * Description: predicate of this slot for semantic web application
    * range: [Uri](Uri.md)
 * [values_from](values_from.md)<sub>opt</sub>
    * Description: identifies the possible uri's of the range
    * range: [[Uri](Uri.md)]
    * inherited from: [Definition](Definition.md)

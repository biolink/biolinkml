# Class: slot_definition


the definition of a property or a slot

URI: [http://w3id.org/biolink/biolinkml/meta/SlotDefinition](http://w3id.org/biolink/biolinkml/meta/SlotDefinition)

![img](http://yuml.me/diagram/nofunky;dir:TB/class/\[SchemaDefinition]<from_schema(i)%20%3F-%20\[SlotDefinition|slot_uri:uri%20%3F;multivalued:boolean%20%3F;inherited:boolean%20%3F;readonly:string%20%3F;ifabsent:string%20%3F;required:boolean%20%3F;inlined:boolean%20%3F;key:boolean%20%3F;identifier:boolean%20%3F;alias:string%20%3F;abstract(i):boolean%20%3F;mixin(i):boolean%20%3F;name(pk)(i):string;singular_name(i):string%20%3F;aliases(i):string%20*;mappings(i):uriorcuri%20*;description(i):string%20%3F;deprecated(i):string%20%3F;todos(i):string%20*;notes(i):string%20*;comments(i):string%20*;imported_from(i):string%20%3F;see_also(i):uri%20*],%20\[SubsetDefinition]<in_subset(i)%20*-%20\[SlotDefinition],%20\[Example]<examples(i)%20*-++\[SlotDefinition],%20\[Element]<range%20%3F-%20\[SlotDefinition],%20\[ClassDefinition]<domain-%20\[SlotDefinition],%20\[SlotDefinition]<apply_to%20*-%20\[SlotDefinition],%20\[SlotDefinition]<mixins%20*-%20\[SlotDefinition],%20\[SlotDefinition]<is_a%20%3F-%20\[SlotDefinition],%20\[SchemaDefinition]++-%20slots%20*>\[SlotDefinition],%20\[ClassDefinition]++-%20slot_usage%20*>\[SlotDefinition],%20\[ClassDefinition]-%20slots%20*>\[SlotDefinition],%20\[Definition]^-\[SlotDefinition])
## Inheritance

 *  is_a: [Definition](Definition.md) - base class for definitions
## Children

## Used by

 *  **[SlotDefinition](SlotDefinition.md)** *[slot_definition.apply_to](slot_definition_apply_to.md)<sub>opt</sub>*  **[[SlotDefinition](SlotDefinition.md)]**
 *  **[SlotDefinition](SlotDefinition.md)** *[slot_definition.is_a](slot_definition_is_a.md)<sub>opt</sub>*  **[SlotDefinition](SlotDefinition.md)**
 *  **[SlotDefinition](SlotDefinition.md)** *[slot_definition.mixins](slot_definition_mixins.md)<sub>opt</sub>*  **[[SlotDefinition](SlotDefinition.md)]**
 *  **[SchemaDefinition](SchemaDefinition.md)** *[schema_definition.slots](slot_definitions.md)<sub>opt</sub>*  **[[SlotDefinition](SlotDefinition.md)]**
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
 * [aliases](aliases.md)<sub>opt</sub>
    * range: [[String](String.md)]
    * inherited from: [Element](Element.md)
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
 * [identifier](identifier.md)<sub>opt</sub>
    * Description: true means that this slot is the subject of a set of assertions.  Identifiers do not appear as predicates in the model
    * range: [Boolean](Boolean.md)
 * [ifabsent](ifabsent.md)<sub>opt</sub>
    * Description: description of special behavior if the slot is absent
    * range: [String](String.md)
 * [imported_from](imported_from.md)<sub>opt</sub>
    * Description: the imports entry that this element was derived from.  Empty means primary source
    * range: [String](String.md)
    * inherited from: [Element](Element.md)
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
 * [key](key.md)<sub>opt</sub>
    * Description: true means that the slot uniquely identifies the element within the context of its container.  Key slots are NOT identifiers - they do not serve as subjects
    * range: [Boolean](Boolean.md)
 * [mappings](mappings.md)<sub>opt</sub>
    * Description: A list of terms from different schemas or terminology systems that have comparable meaning. These may include terms that are precisely equivalent, broader or narrower in meaning, or otherwise semantically related but not equivalent from a strict ontological perspective.
    * range: [[Uriorcuri](Uriorcuri.md)]
    * inherited from: [Element](Element.md)
 * [mixin](mixin.md)<sub>opt</sub>
    * Description: this slot or class can only be used as a mixin -- equivalent to abstract
    * range: [Boolean](Boolean.md)
    * inherited from: [Definition](Definition.md)
 * [multivalued](multivalued.md)<sub>opt</sub>
    * Description: true means that slot can have more than one value
    * range: [Boolean](Boolean.md)
 * [name](name.md) *subsets*: (owl)
    * Description: the unique name of the element within the context of the schema.  Name is combined with the default prefix to form the globally unique subject of the target class.
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
 * [singular_name](singular_name.md)<sub>opt</sub>
    * Description: a name that is used in the singular form
    * range: [String](String.md)
    * inherited from: [Element](Element.md)
 * [slot_definition.apply_to](slot_definition_apply_to.md)<sub>opt</sub>
    * range: [[SlotDefinition](SlotDefinition.md)]
 * [slot_definition.is_a](slot_definition_is_a.md)<sub>opt</sub>
    * range: [SlotDefinition](SlotDefinition.md)
 * [slot_definition.mixins](slot_definition_mixins.md)<sub>opt</sub>
    * range: [[SlotDefinition](SlotDefinition.md)]
 * [slot_uri](slot_uri.md)<sub>opt</sub>
    * Description: predicate of this slot for semantic web application
    * range: [Uri](Uri.md)
 * [todos](todos.md)<sub>opt</sub>
    * Description: Outstanding issue that needs resolution
    * range: [[String](String.md)]
    * inherited from: [Element](Element.md)

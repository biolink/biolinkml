
# Type: slot_definition


the definition of a property or a slot

URI: [meta:SlotDefinition](https://w3id.org/biolink/biolinkml/meta/SlotDefinition)


![img](http://yuml.me/diagram/nofunky;dir:TB/class/\[SubsetDefinition]<in_subset(i)%200..*-%20\[SlotDefinition&#124;singular_name:string%20%3F;slot_uri:uriorcurie%20%3F;multivalued:boolean%20%3F;inherited:boolean%20%3F;readonly:string%20%3F;ifabsent:string%20%3F;required:boolean%20%3F;inlined:boolean%20%3F;key:boolean%20%3F;identifier:boolean%20%3F;alias:string%20%3F;subproperty_of:uriorcurie%20%3F;symmetric:boolean%20%3F;is_class_field:boolean%20%3F;role:string%20%3F;is_usage_slot:boolean%20%3F;abstract(i):boolean%20%3F;mixin(i):boolean%20%3F;values_from(i):uriorcurie%20*;id_prefixes(i):ncname%20*;name(pk)(i):string;definition_uri(i):uriorcurie%20%3F;aliases(i):string%20*;mappings(i):uriorcurie%20*;description(i):string%20%3F;deprecated(i):string%20%3F;todos(i):string%20*;notes(i):string%20*;comments(i):string%20*;from_schema(i):uri%20%3F;imported_from(i):string%20%3F;see_also(i):uriorcurie%20*;exact_mappings(i):uriorcurie%20*;close_mappings(i):uriorcurie%20*;related_mappings(i):uriorcurie%20*;deprecated_element_has_exact_replacement(i):uriorcurie%20%3F;deprecated_element_has_possible_replacement(i):uriorcurie%20%3F],%20\[Example]<examples(i)%200..*-++\[SlotDefinition],%20\[AltDescription]<alt_descriptions(i)%200..*-++\[SlotDefinition],%20\[LocalName]<local_names(i)%200..*-++\[SlotDefinition],%20\[SlotDefinition]<inverse%200..1-%20\[SlotDefinition],%20\[Definition]<owner%200..1-%20\[SlotDefinition],%20\[Element]<range%200..1-%20\[SlotDefinition],%20\[ClassDefinition]<domain%200..1-%20\[SlotDefinition],%20\[SlotDefinition]<apply_to%200..*-%20\[SlotDefinition],%20\[SlotDefinition]<mixins%200..*-%20\[SlotDefinition],%20\[SlotDefinition]<is_a%200..1-%20\[SlotDefinition],%20\[ClassDefinition]-%20defining_slots%200..*>\[SlotDefinition],%20\[SchemaDefinition]++-%20slots%200..*>\[SlotDefinition],%20\[ClassDefinition]++-%20slot_usage%200..*>\[SlotDefinition],%20\[ClassDefinition]-%20slots%200..*>\[SlotDefinition],%20\[Definition]^-\[SlotDefinition])

## Parents

 *  is_a: [Definition](Definition.md) - base class for definitions

## Referenced by class

 *  **[ClassDefinition](ClassDefinition.md)** *[defining_slots](defining_slots.md)*  <sub>0..*</sub>  **[SlotDefinition](SlotDefinition.md)**
 *  **[SlotDefinition](SlotDefinition.md)** *[inverse](inverse.md)*  <sub>OPT</sub>  **[SlotDefinition](SlotDefinition.md)**
 *  **[SlotDefinition](SlotDefinition.md)** *[slot_definition➞apply_to](slot_definition_apply_to.md)*  <sub>0..*</sub>  **[SlotDefinition](SlotDefinition.md)**
 *  **[SlotDefinition](SlotDefinition.md)** *[slot_definition➞is_a](slot_definition_is_a.md)*  <sub>OPT</sub>  **[SlotDefinition](SlotDefinition.md)**
 *  **[SlotDefinition](SlotDefinition.md)** *[slot_definition➞mixins](slot_definition_mixins.md)*  <sub>0..*</sub>  **[SlotDefinition](SlotDefinition.md)**
 *  **[SchemaDefinition](SchemaDefinition.md)** *[schema_definition➞slots](slot_definitions.md)*  <sub>0..*</sub>  **[SlotDefinition](SlotDefinition.md)**
 *  **[ClassDefinition](ClassDefinition.md)** *[slot_usage](slot_usage.md)*  <sub>0..*</sub>  **[SlotDefinition](SlotDefinition.md)**
 *  **[ClassDefinition](ClassDefinition.md)** *[slots](slots.md)*  <sub>0..*</sub>  **[SlotDefinition](SlotDefinition.md)**

## Attributes


### Own

 * [alias](alias.md)  <sub>OPT</sub>
    * Description: the name used for a slot in the context of its owning class.  If present, this is used instead of the actual slot name.
    * range: [String](types/String.md)
 * [domain](domain.md)  <sub>OPT</sub>
    * Description: defines the type of the subject of the slot.  Given the following slot definition
  S1:
    domain: C1
    range:  C2
the declaration
  X:
    S1: Y

implicitly asserts that X is an instance of C1

    * range: [ClassDefinition](ClassDefinition.md)
 * [identifier](identifier.md)  <sub>OPT</sub>
    * Description: true means that this slot is the subject of a set of assertions.  Identifiers do not appear as predicates in the model
    * range: [Boolean](types/Boolean.md)
 * [ifabsent](ifabsent.md)  <sub>OPT</sub>
    * Description: function that provides a default value for the slot.  Possible values for this slot are defined in biolink.utils.ifabsent_functions.default_library:
  * [Tt]rue -- boolean True
  * [Ff]alse -- boolean False
  * int(value) -- integer value
  * str(value) -- string value
  * default_range -- schema default range
  * bnode -- blank node identifier
  * slot_uri -- URI for the slot
  * class_curie -- CURIE for the containing class
  * class_uri -- URI for the containing class
    * range: [String](types/String.md)
 * [inherited](inherited.md)  <sub>OPT</sub>
    * Description: true means that the *value* of a slot is inherited by subclasses
    * range: [Boolean](types/Boolean.md)
 * [inlined](inlined.md)  <sub>OPT</sub>
    * Description: an inlined definition a list of actual values rather than references.  Only applies to slots whose range is a class.
    * range: [Boolean](types/Boolean.md)
 * [inverse](inverse.md)  <sub>OPT</sub>
    * Description: indicates that any instance of d s r implies that there is also an instance of r s' d
    * range: [SlotDefinition](SlotDefinition.md)
 * [is_class_field](is_class_field.md)  <sub>OPT</sub>
    * Description: indicates that any instance, i,  the domain of this slot will include an assert of i s range
    * range: [Boolean](types/Boolean.md)
 * [is_usage_slot](is_usage_slot.md)  <sub>OPT</sub>
    * Description: True means that this slot was defined in a slot_usage situation
    * range: [Boolean](types/Boolean.md)
 * [key](key.md)  <sub>OPT</sub>
    * Description: true means that the slot uniquely identifies the element within the context of its container.  Key slots are NOT identifiers - they do not serve as subjects
    * range: [Boolean](types/Boolean.md)
 * [multivalued](multivalued.md)  <sub>OPT</sub>
    * Description: true means that slot can have more than one value
    * range: [Boolean](types/Boolean.md)
 * [owner](owner.md)  <sub>OPT</sub>
    * Description: the "owner" of the slot. It is the class if it appears in the slots list, otherwise the declaring slot
    * range: [Definition](Definition.md)
 * [range](range.md)  <sub>OPT</sub>
    * Description: defines the type of the object of the slot.  Given the following slot definition
  S1:
    domain: C1
    range:  C2
the declaration
  X:
    S1: Y

implicitly asserts Y is an instance of C2

    * range: [Element](Element.md)
 * [readonly](readonly.md)  <sub>OPT</sub>
    * Description: If present, slot is read only.  Text explains why
    * range: [String](types/String.md)
 * [required](required.md)  <sub>OPT</sub>
    * Description: true means that the slot must be present in the loaded definition
    * range: [Boolean](types/Boolean.md)
 * [role](role.md)  <sub>OPT</sub>
    * Description: the role played by the slot range
    * range: [String](types/String.md)
 * [singular_name](singular_name.md)  <sub>OPT</sub>
    * Description: a name that is used in the singular form
    * range: [String](types/String.md)
 * [slot_definition➞apply_to](slot_definition_apply_to.md)  <sub>0..*</sub>
    * range: [SlotDefinition](SlotDefinition.md)
 * [slot_definition➞is_a](slot_definition_is_a.md)  <sub>OPT</sub>
    * range: [SlotDefinition](SlotDefinition.md)
 * [slot_definition➞mixins](slot_definition_mixins.md)  <sub>0..*</sub>
    * range: [SlotDefinition](SlotDefinition.md)
 * [slot_uri](slot_uri.md)  <sub>OPT</sub>
    * Description: predicate of this slot for semantic web application
    * range: [Uriorcurie](types/Uriorcurie.md)
 * [subproperty_of](subproperty_of.md)  <sub>OPT</sub>
    * Description: Ontology property which this slot is a subproperty of
    * range: [Uriorcurie](types/Uriorcurie.md)
 * [symmetric](symmetric.md)  <sub>OPT</sub>
    * Description: True means that any instance of  d s r implies that there is also an instance of r s d
    * range: [Boolean](types/Boolean.md)

### Inherited from definition:

 * [is_a](is_a.md)  <sub>OPT</sub>
    * Description: specifies single-inheritance between classes or slots. While multiple inheritance is not allowed, mixins can be provided effectively providing the same thing. The semantics are the same when translated to formalisms that allow MI (e.g. RDFS/OWL). When translating to a SI framework (e.g. java classes, python classes) then is a is used. When translating a framework without polymorphism (e.g. json-schema, solr document schema) then is a and mixins are recursively unfolded
    * range: [Definition](Definition.md)
    * inherited from: [Definition](Definition.md)
 * [abstract](abstract.md)  <sub>OPT</sub>
    * Description: an abstract class is a high level class or slot that is typically used to group common slots together and cannot be directly instantiated.
    * range: [Boolean](types/Boolean.md)
    * inherited from: [Definition](Definition.md)
 * [mixin](mixin.md)  <sub>OPT</sub>
    * Description: this slot or class can only be used as a mixin -- equivalent to abstract
    * range: [Boolean](types/Boolean.md)
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
    * range: [Uriorcurie](types/Uriorcurie.md)
    * inherited from: [Definition](Definition.md)

### Inherited from element:

 * [id_prefixes](id_prefixes.md)  <sub>0..*</sub>
    * Description: the identifier of this class or slot must begin with one of the URIs referenced by this prefix
    * range: [Ncname](types/Ncname.md)
    * inherited from: [Element](Element.md)
 * [name](name.md)  <sub>REQ</sub>
    * Description: the unique name of the element within the context of the schema.  Name is combined with the default prefix to form the globally unique subject of the target class.
    * range: [String](types/String.md)
    * inherited from: [Element](Element.md)
    * in subsets: (owl)
 * [definition_uri](definition_uri.md)  <sub>OPT</sub>
    * Description: the "native" URI of the element
    * range: [Uriorcurie](types/Uriorcurie.md)
    * inherited from: [Element](Element.md)
 * [aliases](aliases.md)  <sub>0..*</sub>
    * range: [String](types/String.md)
    * inherited from: [Element](Element.md)
 * [local_names](local_names.md)  <sub>0..*</sub>
    * range: [LocalName](LocalName.md)
    * inherited from: [Element](Element.md)
 * [mappings](mappings.md)  <sub>0..*</sub>
    * Description: A list of terms from different schemas or terminology systems that have comparable meaning. These may include terms that are precisely equivalent, broader or narrower in meaning, or otherwise semantically related but not equivalent from a strict ontological perspective.
    * range: [Uriorcurie](types/Uriorcurie.md)
    * inherited from: None
 * [description](description.md)  <sub>OPT</sub>
    * Description: a description of the element's purpose and use
    * range: [String](types/String.md)
    * inherited from: [Element](Element.md)
    * in subsets: (owl)
 * [alt_descriptions](alt_descriptions.md)  <sub>0..*</sub>
    * range: [AltDescription](AltDescription.md)
    * inherited from: [Element](Element.md)
 * [deprecated](deprecated.md)  <sub>OPT</sub>
    * Description: Description of why and when this element will no longer be used
    * range: [String](types/String.md)
    * inherited from: [Element](Element.md)
 * [todos](todos.md)  <sub>0..*</sub>
    * Description: Outstanding issue that needs resolution
    * range: [String](types/String.md)
    * inherited from: [Element](Element.md)
 * [notes](notes.md)  <sub>0..*</sub>
    * Description: editorial notes about an element intended for internal consumption
    * range: [String](types/String.md)
    * inherited from: [Element](Element.md)
    * in subsets: (owl)
 * [comments](comments.md)  <sub>0..*</sub>
    * Description: notes and comments about an element intended for external consumption
    * range: [String](types/String.md)
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
    * range: [Uri](types/Uri.md)
    * inherited from: [Element](Element.md)
 * [imported_from](imported_from.md)  <sub>OPT</sub>
    * Description: the imports entry that this element was derived from.  Empty means primary source
    * range: [String](types/String.md)
    * inherited from: [Element](Element.md)
 * [see_also](see_also.md)  <sub>0..*</sub>
    * Description: a reference
    * range: [Uriorcurie](types/Uriorcurie.md)
    * inherited from: [Element](Element.md)
    * in subsets: (owl)
 * [exact mappings](exact_mappings.md)  <sub>0..*</sub>
    * Description: A list of terms from different schemas or terminology systems that have identical meaning.
    * range: [Uriorcurie](types/Uriorcurie.md)
    * inherited from: None
 * [close mappings](close_mappings.md)  <sub>0..*</sub>
    * Description: A list of terms from different schemas or terminology systems that have close meaning.
    * range: [Uriorcurie](types/Uriorcurie.md)
    * inherited from: None
 * [related mappings](related_mappings.md)  <sub>0..*</sub>
    * Description: A list of terms from different schemas or terminology systems that have related meaning.
    * range: [Uriorcurie](types/Uriorcurie.md)
    * inherited from: None
 * [deprecated element has exact replacement](deprecated_element_has_exact_replacement.md)  <sub>OPT</sub>
    * Description: When an element is deprecated, it can be automatically replaced by this uri or curie
    * range: [Uriorcurie](types/Uriorcurie.md)
    * inherited from: None
 * [deprecated element has possible replacement](deprecated_element_has_possible_replacement.md)  <sub>OPT</sub>
    * Description: When an element is deprecated, it can be potentially replaced by this uri or curie
    * range: [Uriorcurie](types/Uriorcurie.md)
    * inherited from: None

### Domain for slot:

 * [alias](alias.md)  <sub>OPT</sub>
    * Description: the name used for a slot in the context of its owning class.  If present, this is used instead of the actual slot name.
    * range: [String](types/String.md)
 * [domain](domain.md)  <sub>OPT</sub>
    * Description: defines the type of the subject of the slot.  Given the following slot definition
  S1:
    domain: C1
    range:  C2
the declaration
  X:
    S1: Y

implicitly asserts that X is an instance of C1

    * range: [ClassDefinition](ClassDefinition.md)
 * [identifier](identifier.md)  <sub>OPT</sub>
    * Description: true means that this slot is the subject of a set of assertions.  Identifiers do not appear as predicates in the model
    * range: [Boolean](types/Boolean.md)
 * [ifabsent](ifabsent.md)  <sub>OPT</sub>
    * Description: function that provides a default value for the slot.  Possible values for this slot are defined in biolink.utils.ifabsent_functions.default_library:
  * [Tt]rue -- boolean True
  * [Ff]alse -- boolean False
  * int(value) -- integer value
  * str(value) -- string value
  * default_range -- schema default range
  * bnode -- blank node identifier
  * slot_uri -- URI for the slot
  * class_curie -- CURIE for the containing class
  * class_uri -- URI for the containing class
    * range: [String](types/String.md)
 * [inherited](inherited.md)  <sub>OPT</sub>
    * Description: true means that the *value* of a slot is inherited by subclasses
    * range: [Boolean](types/Boolean.md)
 * [inlined](inlined.md)  <sub>OPT</sub>
    * Description: an inlined definition a list of actual values rather than references.  Only applies to slots whose range is a class.
    * range: [Boolean](types/Boolean.md)
 * [inverse](inverse.md)  <sub>OPT</sub>
    * Description: indicates that any instance of d s r implies that there is also an instance of r s' d
    * range: [SlotDefinition](SlotDefinition.md)
 * [is_class_field](is_class_field.md)  <sub>OPT</sub>
    * Description: indicates that any instance, i,  the domain of this slot will include an assert of i s range
    * range: [Boolean](types/Boolean.md)
 * [is_usage_slot](is_usage_slot.md)  <sub>OPT</sub>
    * Description: True means that this slot was defined in a slot_usage situation
    * range: [Boolean](types/Boolean.md)
 * [key](key.md)  <sub>OPT</sub>
    * Description: true means that the slot uniquely identifies the element within the context of its container.  Key slots are NOT identifiers - they do not serve as subjects
    * range: [Boolean](types/Boolean.md)
 * [multivalued](multivalued.md)  <sub>OPT</sub>
    * Description: true means that slot can have more than one value
    * range: [Boolean](types/Boolean.md)
 * [owner](owner.md)  <sub>OPT</sub>
    * Description: the "owner" of the slot. It is the class if it appears in the slots list, otherwise the declaring slot
    * range: [Definition](Definition.md)
 * [range](range.md)  <sub>OPT</sub>
    * Description: defines the type of the object of the slot.  Given the following slot definition
  S1:
    domain: C1
    range:  C2
the declaration
  X:
    S1: Y

implicitly asserts Y is an instance of C2

    * range: [Element](Element.md)
 * [readonly](readonly.md)  <sub>OPT</sub>
    * Description: If present, slot is read only.  Text explains why
    * range: [String](types/String.md)
 * [required](required.md)  <sub>OPT</sub>
    * Description: true means that the slot must be present in the loaded definition
    * range: [Boolean](types/Boolean.md)
 * [role](role.md)  <sub>OPT</sub>
    * Description: the role played by the slot range
    * range: [String](types/String.md)
 * [singular_name](singular_name.md)  <sub>OPT</sub>
    * Description: a name that is used in the singular form
    * range: [String](types/String.md)
 * [slot_definition➞apply_to](slot_definition_apply_to.md)  <sub>0..*</sub>
    * range: [SlotDefinition](SlotDefinition.md)
 * [slot_definition➞is_a](slot_definition_is_a.md)  <sub>OPT</sub>
    * range: [SlotDefinition](SlotDefinition.md)
 * [slot_definition➞mixins](slot_definition_mixins.md)  <sub>0..*</sub>
    * range: [SlotDefinition](SlotDefinition.md)
 * [slot_uri](slot_uri.md)  <sub>OPT</sub>
    * Description: predicate of this slot for semantic web application
    * range: [Uriorcurie](types/Uriorcurie.md)
 * [subproperty_of](subproperty_of.md)  <sub>OPT</sub>
    * Description: Ontology property which this slot is a subproperty of
    * range: [Uriorcurie](types/Uriorcurie.md)
 * [symmetric](symmetric.md)  <sub>OPT</sub>
    * Description: True means that any instance of  d s r implies that there is also an instance of r s d
    * range: [Boolean](types/Boolean.md)

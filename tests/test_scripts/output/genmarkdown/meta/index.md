# Metamodel schema


A metamodel for defining biolink related schemas

### Classes

 * [Element](Element.md) - a named element in the model
    * [Definition](Definition.md) - base class for definitions
       * [ClassDefinition](ClassDefinition.md) - the definition of a class or interface
       * [SlotDefinition](SlotDefinition.md) - the definition of a property or a slot
    * [SchemaDefinition](SchemaDefinition.md) - a collection of subset, type, slot and class definitions
    * [SubsetDefinition](SubsetDefinition.md) - the name and description of a subset
    * [TypeDefinition](TypeDefinition.md) - A data type definition.
 * [Example](Example.md) - usage example and description
 * [Prefix](Prefix.md) - prefix URI tuple
### Mixins

### Slots

 * [abstract](abstract.md) - an abstract class is a high level class or slot that is typically used to group common slots together and cannot be directly instantiated.
 * [alias](alias.md) - the name used for a slot in the context of its owning class.  If present, this is used instead of the actual slot name.
 * [apply_to](apply_to.md) - Used to extend class or slot definitions. For example, if we have a core schema where a gene has two slots for identifier and symbol, and we have a specialized schema for my_organism where we wish to add a slot systematic_name, we can avoid subclassing by defining a class gene_my_organism, adding the slot to this class, and then adding an apply_to pointing to the gene class. The new slot will be 'injected into' the gene class.
    * [class definition.apply_to](class_definition_apply_to.md)
    * [slot definition.apply_to](slot_definition_apply_to.md)
 * [base](base.md) - python base type that implements this type definition
 * [class_uri](class_uri.md) - URI of the class in an RDF environment
 * [classes](classes.md) - class definitions
 * [comments](comments.md) *subsets*: (owl) - notes and comments about an element intended for external consumption
 * [default_curi_maps](default_curi_maps.md) - ordered list of prefixcommon biocontexts to be fetched to resolve id_prefixes and inline prefix variables
 * [default_prefix](default_prefix.md) - default and base prefix -- used for ':' identifiers, @base and @vocab
 * [default_range](default_range.md) - default slot range to be used if range element is omitted from a slot definition
 * [defining_slots](defining_slots.md) - The combination of is_a plus defining slots form a genus-differentia definition, or the set of necessary and sufficient conditions that can be transformed into an OWL equivalence axiom
 * [deprecated](deprecated.md) - Description of why and when this element will no longer be used
 * [description](description.md) *subsets*: (owl) - a description of the element's purpose and use
    * [schema definition.description](schema_definition_description.md)
 * [domain](domain.md) - defines the type of the subject of the slot.  Given the following slot definition
 * [examples](examples.md) *subsets*: (owl) - example usages of an element
 * [from_schema](from_schema.md) - id of the schema that defined the element
 * [generation_date](generation_date.md) *subsets*: (owl) - date and time that the schema was loaded/generated
 * [id](id.md) - a globally unique schema identifier
 * [id_prefixes](id_prefixes.md) - a list of Curie prefixes that are used in the representation of instances of the model.  All prefixes in this list are added to the prefix sections of the target models.
 * [identifier](identifier.md) - True means that this slot must be unique across the collection of slots
 * [ifabsent](ifabsent.md) - description of special behavior if the slot is absent
 * [imports](imports.md) - other schemas that are included in this schema
 * [in_subset](in_subset.md) - used to indicate membership of a term in a defined subset of biolink terms used for a particular domain or application (e.g. the translator_minimal subset holding the minimal set of predicates used in a translator knowledge graph)
 * [inherited](inherited.md) - true means that the *value* of a slot is inherited by subclasses
 * [inlined](inlined.md) - an inlined definition a list of actual values rather than references.  Only applies to slots whose range is a class.
 * [inverse](inverse.md) - used to indicate the inverse of a slot (e.g. 'expresses' is the inverse predicate of 'expressed in')
 * [is_a](is_a.md) - specifies single-inheritance between classes or slots. While multiple inheritance is not allowed, mixins can be provided effectively providing the same thing. The semantics are the same when translated to formalisms that allow MI (e.g. RDFS/OWL). When translating to a SI framework (e.g. java classes, python classes) then is_a is used. When translating a framework without polymorphism (e.g. json-schema, solr document schema) then is_a and mixins are recursively unfolded
    * [class definition.is_a](class_definition_is_a.md)
    * [slot definition.is_a](slot_definition_is_a.md)
 * [key](key.md) - true means that the slot uniquely identifies the element within the context of its container
 * [license](license.md) *subsets*: (owl) - license for the schema
 * [local name](local_name.md) - the nsname (sans ':' for a given prefix)
 * [local_names](local_names.md) - map from local identifier to slot
 * [metamodel_version](metamodel_version.md) *subsets*: (owl) - Version of the metamodel used to load the schema
 * [mixin](mixin.md) - this slot or class can only be used as a mixin -- equivalent to abstract
 * [mixins](mixins.md) - List of definitions to be mixed in. Targets may be any definition of the same type
    * [class definition.mixins](class_definition_mixins.md)
    * [slot definition.mixins](slot_definition_mixins.md)
 * [multivalued](multivalued.md) - true means that slot can have more than one value
 * [name](name.md) *subsets*: (owl) - the unique name of the element within the context of the schema
 * [notes](notes.md) *subsets*: (owl) - editorial notes about an element intended for internal consumption
 * [prefix uri](prefix_uri.md) - A URI associated with a given prefix
 * [prefixes](prefixes.md) - prefix / URI definitions to be added to the context beyond those fetched from prefixcommons in id_prefixes
 * [range](range.md) - defines the type of the object of the slot.  Given the following slot definition
 * [slot definition.subclass_of](range_subclass.md) - Constraint on the range of a property
 * [readonly](readonly.md) - If present, slot is read only.  Text explains why
 * [required](required.md) - true means that the slot must be present in the loaded definition
 * [see_also](see_also.md) *subsets*: (owl) - a reference
 * [schema definition.slots](slot_definitions.md) - slot definitions
 * [slot_uri](slot_uri.md) - predicate of this slot for semantic web application
 * [slot_usage](slot_usage.md) - the redefinition of a slot in the context of the containing class definition.
 * [slots](slots.md) - list of slot names that are applicable to a class
 * [source_file](source_file.md) *subsets*: (owl) - name, uri or description of the source of the schema
 * [source_file_date](source_file_date.md) *subsets*: (owl) - modification date of the source of the schema
 * [source_file_size](source_file_size.md) *subsets*: (owl) - size in bytes of the source of the schema
 * [subclass_of](subclass_of.md) - instances of this class are considered/required to be sub classes of the target URI
 * [subsets](subsets.md) - list of subsets referenced in this model
 * [title](title.md) *subsets*: (owl) - the official title of the schema
 * [type definition.uri](type_uri.md) - the URI to be used for the type in semantic web mappings
 * [typeof](typeof.md) - supertype
 * [types](types.md) - data types used in the model
 * [value](value.md)
 * [example.description](value_description.md)
 * [values_from](values_from.md) - identifies the possible uri's of the range
 * [version](version.md) - particular version of schema
### Types

#### Built in

 * **Bool**
 * **NCName**
 * **URIorCURIE**
 * **datetime.date**
 * **datetime.datetime**
 * **datetime.time**
 * **float**
 * **int**
 * **str**
#### Defined

 * [Boolean](Boolean.md)  (**Bool**)  - A binary (true or false) value
 * [Date](Date.md)  (**datetime.date**)  - a date (year, month and day) in an idealized calendar
 * [Datetime](Datetime.md)  (**datetime.datetime**) 
 * [Double](Double.md)  (**float**) 
 * [Float](Float.md)  (**float**) 
 * [Integer](Integer.md)  (**int**) 
 * [Ncname](Ncname.md)  (**NCName**)  - Prefix part of CURIE
 * [String](String.md)  (**str**) 
 * [Time](Time.md)  (**datetime.time**)  - A time object represents a (local) time of day, independent of any particular day
 * [Uri](Uri.md)  (**URIorCURIE**)  - a URI or a CURIE

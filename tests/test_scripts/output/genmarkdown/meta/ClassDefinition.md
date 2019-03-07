# Class: class_definition


the definition of a class or interface

URI: [http://w3id.org/biolink/biolinkml/meta/ClassDefinition](http://w3id.org/biolink/biolinkml/meta/ClassDefinition)

![img](http://yuml.me/diagram/nofunky;dir:TB/class/\[SchemaDefinition]<from_schema(i)%20%3F-%20\[ClassDefinition|class_uri:uri%20%3F;abstract(i):boolean%20%3F;mixin(i):boolean%20%3F;name(pk)(i):string;singular_name(i):string%20%3F;aliases(i):string%20*;mappings(i):uriorcuri%20*;description(i):string%20%3F;deprecated(i):string%20%3F;todos(i):string%20*;notes(i):string%20*;comments(i):string%20*;imported_from(i):string%20%3F;see_also(i):uri%20*],%20\[SubsetDefinition]<in_subset(i)%20*-%20\[ClassDefinition],%20\[Example]<examples(i)%20*-++\[ClassDefinition],%20\[SlotDefinition]<slot_usage%20*-++\[ClassDefinition],%20\[SlotDefinition]<slots%20*-%20\[ClassDefinition],%20\[ClassDefinition]<apply_to%20*-%20\[ClassDefinition],%20\[ClassDefinition]<mixins%20*-%20\[ClassDefinition],%20\[ClassDefinition]<is_a%20%3F-%20\[ClassDefinition],%20\[SchemaDefinition]++-%20classes%20*>\[ClassDefinition],%20\[SlotDefinition]-%20domain>\[ClassDefinition],%20\[Definition]^-\[ClassDefinition])
## Inheritance

 *  is_a: [Definition](Definition.md) - base class for definitions
## Children

## Used by

 *  **[ClassDefinition](ClassDefinition.md)** *[class_definition.apply_to](class_definition_apply_to.md)<sub>opt</sub>*  **[[ClassDefinition](ClassDefinition.md)]**
 *  **[ClassDefinition](ClassDefinition.md)** *[class_definition.is_a](class_definition_is_a.md)<sub>opt</sub>*  **[ClassDefinition](ClassDefinition.md)**
 *  **[ClassDefinition](ClassDefinition.md)** *[class_definition.mixins](class_definition_mixins.md)<sub>opt</sub>*  **[[ClassDefinition](ClassDefinition.md)]**
 *  **[SchemaDefinition](SchemaDefinition.md)** *[classes](classes.md)<sub>opt</sub>*  **[[ClassDefinition](ClassDefinition.md)]**
 *  **[SlotDefinition](SlotDefinition.md)** *[domain](domain.md)*  **[ClassDefinition](ClassDefinition.md)**
## Fields

 * [abstract](abstract.md)<sub>opt</sub>
    * Description: an abstract class is a high level class or slot that is typically used to group common slots together and cannot be directly instantiated.
    * range: [Boolean](Boolean.md)
    * inherited from: [Definition](Definition.md)
 * [aliases](aliases.md)<sub>opt</sub>
    * range: [[String](String.md)]
    * inherited from: [Element](Element.md)
 * [class_definition.apply_to](class_definition_apply_to.md)<sub>opt</sub>
    * range: [[ClassDefinition](ClassDefinition.md)]
 * [class_definition.is_a](class_definition_is_a.md)<sub>opt</sub>
    * range: [ClassDefinition](ClassDefinition.md)
 * [class_definition.mixins](class_definition_mixins.md)<sub>opt</sub>
    * range: [[ClassDefinition](ClassDefinition.md)]
 * [class_uri](class_uri.md)<sub>opt</sub>
    * Description: URI of the class in an RDF environment
    * range: [Uri](Uri.md)
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
 * [examples](examples.md) *subsets*: (owl)<sub>opt</sub>
    * Description: example usages of an element
    * range: [[Example](Example.md)]
    * inherited from: [Element](Element.md)
 * [from_schema](from_schema.md)<sub>opt</sub>
    * Description: id of the schema that defined the element
    * range: [SchemaDefinition](SchemaDefinition.md)
    * inherited from: [Element](Element.md)
 * [imported_from](imported_from.md)<sub>opt</sub>
    * Description: the imports entry that this element was derived from.  Empty means primary source
    * range: [String](String.md)
    * inherited from: [Element](Element.md)
 * [in_subset](in_subset.md)<sub>opt</sub>
    * Description: used to indicate membership of a term in a defined subset of biolink terms used for a particular domain or application (e.g. the translator_minimal subset holding the minimal set of predicates used in a translator knowledge graph)
    * range: [[SubsetDefinition](SubsetDefinition.md)]
    * inherited from: [Element](Element.md)
 * [mappings](mappings.md)<sub>opt</sub>
    * Description: A list of terms from different schemas or terminology systems that have comparable meaning. These may include terms that are precisely equivalent, broader or narrower in meaning, or otherwise semantically related but not equivalent from a strict ontological perspective.
    * range: [[Uriorcuri](Uriorcuri.md)]
    * inherited from: [Element](Element.md)
 * [mixin](mixin.md)<sub>opt</sub>
    * Description: this slot or class can only be used as a mixin -- equivalent to abstract
    * range: [Boolean](Boolean.md)
    * inherited from: [Definition](Definition.md)
 * [name](name.md) *subsets*: (owl)
    * Description: the unique name of the element within the context of the schema.  Name is combined with the default prefix to form the globally unique subject of the target class.
    * range: [String](String.md)
    * inherited from: [Element](Element.md)
 * [notes](notes.md) *subsets*: (owl)<sub>opt</sub>
    * Description: editorial notes about an element intended for internal consumption
    * range: [[String](String.md)]
    * inherited from: [Element](Element.md)
 * [see_also](see_also.md) *subsets*: (owl)<sub>opt</sub>
    * Description: a reference
    * range: [[Uri](Uri.md)]
    * inherited from: [Element](Element.md)
 * [singular_name](singular_name.md)<sub>opt</sub>
    * Description: a name that is used in the singular form
    * range: [String](String.md)
    * inherited from: [Element](Element.md)
 * [slot_usage](slot_usage.md)<sub>opt</sub>
    * Description: the redefinition of a slot in the context of the containing class definition.
    * range: [[SlotDefinition](SlotDefinition.md)]
 * [slots](slots.md)<sub>opt</sub>
    * Description: list of slot names that are applicable to a class
    * range: [[SlotDefinition](SlotDefinition.md)]
 * [todos](todos.md)<sub>opt</sub>
    * Description: Outstanding issue that needs resolution
    * range: [[String](String.md)]
    * inherited from: [Element](Element.md)

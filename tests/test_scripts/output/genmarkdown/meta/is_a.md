# Slot: is_a


specifies single-inheritance between classes or slots. While multiple inheritance is not allowed, mixins can be provided effectively providing the same thing. The semantics are the same when translated to formalisms that allow MI (e.g. RDFS/OWL). When translating to a SI framework (e.g. java classes, python classes) then is_a is used. When translating a framework without polymorphism (e.g. json-schema, solr document schema) then is_a and mixins are recursively unfolded

URI: [http://w3id.org/biolink/biolinkml/meta/is_a](slot_uri)
## Domain and Range

[Definition](Definition.md) -><sub>opt</sub> [Definition](Definition.md)
## Inheritance

## Children

 *  [class definition.is_a](class_definition_is_a.md)
 *  [slot definition.is_a](slot_definition_is_a.md)
## Used by

 * [ClassDefinition](ClassDefinition.md)
 * [Definition](Definition.md)
 * [SlotDefinition](SlotDefinition.md)

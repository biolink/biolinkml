
# Type: is_a


specifies single-inheritance from a class to a class or a slot to a slot

URI: [meta:is_a](https://w3id.org/biolink/biolinkml/meta/is_a)


## Domain and Range

[Definition](Definition.md) ->  <sub>OPT</sub> [Definition](Definition.md)

## Parents


## Children

 *  [class_definition➞is_a](class_definition_is_a.md)
 *  [slot_definition➞is_a](slot_definition_is_a.md)

## Used by

 * [Definition](Definition.md)

## Other properties

|  |  |  |
| --- | --- | --- |
| **Comments:** | | While multiple inheritance is not allowed, mixins can be provided effectively providing the same thing. The semantics are the same when translated to formalisms that allow MI (e.g. RDFS/OWL). When translating to a SI framework (e.g. java classes, python classes) then is a is used. When translating a framework without polymorphism (e.g. json-schema, solr document schema) then is a and mixins are recursively unfolded |
|  | | RULE: if the domain is a class, the range MUST be a class |
|  | | RULE: if the domain is a slot, the range MUST be a slot |
|  | | RULE: if the domain is a mixin, the range SHOULD be a mixin |
|  | | RULE: if the domain is NOT a mixin, the range SHOULD NOT be a mixin |


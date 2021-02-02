
# Slot: inlined_as_list


True means that an inlined slot is represented as a list of range instances.  False means that an inlined slot is represented as a dictionary, whose key is the slot key or identifier and whose value is the range instance.

URI: [meta:inlined_as_list](https://w3id.org/biolink/biolinkml/meta/inlined_as_list)


## Domain and Range

[SlotDefinition](SlotDefinition.md) ->  <sub>OPT</sub> [Boolean](types/Boolean.md)

## Parents


## Children


## Used by

 * [SlotDefinition](SlotDefinition.md)

## Other properties

|  |  |  |
| --- | --- | --- |
| **Comments:** | | The default loader will accept either list or dictionary form as input.  This parameter controls internal
representation and output. |
|  | | A keyed or identified class with one additional slot can be input in a third form, a dictionary whose key
is the key or identifier and whose value is the one additional element.  This form is still stored according
to the inlined_as_list setting. |


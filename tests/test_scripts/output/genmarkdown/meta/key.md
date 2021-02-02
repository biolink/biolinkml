
# Slot: key


True means that the key slot(s) uniquely identify the container. In future releases, it will be possible for there to be compound keys, where several slots combine to produce a unique identifier

URI: [meta:key](https://w3id.org/biolink/biolinkml/meta/key)


## Domain and Range

[SlotDefinition](SlotDefinition.md) ->  <sub>OPT</sub> [Boolean](types/Boolean.md)

## Parents


## Children


## Used by

 * [SlotDefinition](SlotDefinition.md)

## Other properties

|  |  |  |
| --- | --- | --- |
| **Comments:** | | key is inherited |
|  | | a given domain can have at most one key slot (restriction to be removed in the future) |
|  | | identifiers and keys are mutually exclusive.  A given domain cannot have bot |
|  | | a key slot is automatically required.  Keys cannot be optional |



# Type: ifabsent


function that provides a default value for the slot.  Possible values for this slot are defined in biolink.utils.ifabsent_functions.default_library:
  * [Tt]rue -- boolean True
  * [Ff]alse -- boolean False
  * int(value) -- integer value
  * str(value) -- string value
  * default_range -- schema default range
  * bnode -- blank node identifier
  * slot_uri -- URI for the slot
  * class_curie -- CURIE for the containing class
  * class_uri -- URI for the containing class

URI: [meta:ifabsent](https://w3id.org/biolink/biolinkml/meta/ifabsent)


## Domain and Range

[SlotDefinition](SlotDefinition.md) ->  <sub>OPT</sub> [String](types/String.md)

## Parents


## Children


## Used by

 * [SlotDefinition](SlotDefinition.md)

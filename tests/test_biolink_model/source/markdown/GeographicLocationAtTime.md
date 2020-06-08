
# Type: geographic location at time


a location that can be described in lat/long coordinates, for a particular time

URI: [biolink:GeographicLocationAtTime](https://w3id.org/biolink/vocab/GeographicLocationAtTime)


![img](http://yuml.me/diagram/nofunky;dir:TB/class/\[GeographicLocation]^-\[GeographicLocationAtTime&#124;timepoint:time_type%20%3F;latitude(i):float%20%3F;longitude(i):float%20%3F;id(i):identifier_type;name(i):label_type;category(i):iri_type%20%2B])

## Parents

 *  is_a: [GeographicLocation](GeographicLocation.md) - a location that can be described in lat/long coordinates

## Attributes


### Own

 * [timepoint](timepoint.md)  <sub>OPT</sub>
    * Description: a point in time
    * range: [TimeType](types/TimeType.md)

### Inherited from geographic location:

 * [latitude](latitude.md)  <sub>OPT</sub>
    * Description: latitude
    * range: [Float](types/Float.md)
    * inherited from: [NamedThing](NamedThing.md)
 * [longitude](longitude.md)  <sub>OPT</sub>
    * Description: longitude
    * range: [Float](types/Float.md)
    * inherited from: [NamedThing](NamedThing.md)

### Inherited from named thing:

 * [id](id.md)  <sub>REQ</sub>
    * Description: A unique identifier for a thing. Must be either a CURIE shorthand for a URI or a complete URI
    * range: [IdentifierType](types/IdentifierType.md)
    * inherited from: [NamedThing](NamedThing.md)
    * in subsets: (translator_minimal)
 * [name](name.md)  <sub>REQ</sub>
    * Description: A human-readable name for a thing
    * range: [LabelType](types/LabelType.md)
    * inherited from: [NamedThing](NamedThing.md)
    * in subsets: (translator_minimal)
 * [category](category.md)  <sub>1..*</sub>
    * Description: Name of the high level ontology class in which this entity is categorized. Corresponds to the label for the biolink entity type class. In a neo4j database this MAY correspond to the neo4j label tag
    * range: [IriType](types/IriType.md)
    * inherited from: [NamedThing](NamedThing.md)
    * in subsets: (translator_minimal)

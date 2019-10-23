
# Type: planetary entity


Any entity or process that exists at the level of the whole planet

URI: [biolink:PlanetaryEntity](https://w3id.org/biolink/vocab/PlanetaryEntity)


![img](http://yuml.me/diagram/nofunky;dir:TB/class/\[PlanetaryEntity|id(i):identifier_type;name(i):label_type;category(i):iri_type%20%2B]^-\[GeographicLocation],%20\[PlanetaryEntity]^-\[EnvironmentalProcess],%20\[PlanetaryEntity]^-\[EnvironmentalFeature],%20\[NamedThing]^-\[PlanetaryEntity])

## Parents

 *  is_a: [named thing](named thing.md) - a databased entity or concept/class

## Children

 * [environmental feature](environmental feature.md)
 * [environmental process](environmental process.md)
 * [geographic location](geographic location.md) - a location that can be described in lat/long coordinates

## Referenced by class


## Attributes


### Inherited from named thing:

 * [id](id.md)  <sub>REQ</sub>
    * Description: A unique identifier for a thing. Must be either a CURIE shorthand for a URI or a complete URI
    * range: [IdentifierType](type/IdentifierType.md)
    * inherited from: [named thing](named thing.md)
    * in subsets: (translator_minimal)
 * [name](name.md)  <sub>REQ</sub>
    * Description: A human-readable name for a thing
    * range: [LabelType](type/LabelType.md)
    * inherited from: [named thing](named thing.md)
    * in subsets: (translator_minimal)
 * [category](category.md)  <sub>1..*</sub>
    * Description: Name of the high level ontology class in which this entity is categorized. Corresponds to the label for the biolink entity type class. In a neo4j database this MAY correspond to the neo4j label tag
    * range: [IriType](type/IriType.md)
    * inherited from: [named thing](named thing.md)
    * in subsets: (translator_minimal)

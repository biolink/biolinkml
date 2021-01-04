
# Type: geographic location


a location that can be described in lat/long coordinates

URI: [biolink:GeographicLocation](https://w3id.org/biolink/vocab/GeographicLocation)


![img](http://yuml.me/diagram/nofunky;dir:TB/class/[PlanetaryEntity],[GeographicLocationAtTime],[GeographicLocation&#124;latitude:float%20%3F;longitude:float%20%3F;id(i):string;name(i):label_type;category(i):category_type%20%2B]^-[GeographicLocationAtTime],[PlanetaryEntity]^-[GeographicLocation])

## Parents

 *  is_a: [PlanetaryEntity](PlanetaryEntity.md) - Any entity or process that exists at the level of the whole planet

## Children

 * [GeographicLocationAtTime](GeographicLocationAtTime.md) - a location that can be described in lat/long coordinates, for a particular time

## Referenced by class


## Attributes


### Own

 * [latitude](latitude.md)  <sub>OPT</sub>
    * Description: latitude
    * range: [Float](types/Float.md)
 * [longitude](longitude.md)  <sub>OPT</sub>
    * Description: longitude
    * range: [Float](types/Float.md)

### Inherited from planetary entity:

 * [category](category.md)  <sub>1..*</sub>
    * Description: Name of the high level ontology class in which this entity is categorized. Corresponds to the label for the biolink entity type class.
 * In a neo4j database this MAY correspond to the neo4j label tag.
 * In an RDF database it should be a biolink model class URI.
This field is multi-valued. It should include values for ancestors of the biolink class; for example, a protein such as Shh would have category values `bl:Protein`, `bl:GeneProduct`, `bl:MolecularEntity`, ...
In an RDF database, nodes will typically have an rdf:type triples. This can be to the most specific biolink class, or potentially to a class more specific than something in biolink. For example, a sequence feature `f` may have a rdf:type assertion to a SO class such as TF_binding_site, which is more specific than anything in biolink. Here we would have categories {bl:GenomicEntity, bl:MolecularEntity, bl:NamedThing}
    * range: [CategoryType](types/CategoryType.md)
    * in subsets: (translator_minimal)
 * [id](id.md)  <sub>REQ</sub>
    * Description: A unique identifier for a thing. Must be either a CURIE shorthand for a URI or a complete URI
    * range: [String](types/String.md)
    * in subsets: (translator_minimal)
 * [name](name.md)  <sub>REQ</sub>
    * Description: A human-readable name for a thing
    * range: [LabelType](types/LabelType.md)
    * in subsets: (translator_minimal)

## Other properties

|  |  |  |
| --- | --- | --- |
| **Mappings:** | | UMLSSG:GEOG |
|  | | UMLSST:geoa |
|  | | UMLSSC:T083 |


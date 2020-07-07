
# Type: data set




URI: [biolink:DataSet](https://w3id.org/biolink/vocab/DataSet)


![img](http://yuml.me/diagram/nofunky;dir:TB/class/[NamedThing],[DataSetVersion],[DataSetVersion]-%20versionOf%200..1>[DataSet&#124;id(i):string;name(i):label_type;category(i):iri_type%20%2B],[DataSet]^-[DataSetVersion],[NamedThing]^-[DataSet])

## Parents

 *  is_a: [NamedThing](NamedThing.md) - a databased entity or concept/class

## Children

 * [DataSetVersion](DataSetVersion.md)

## Referenced by class

 *  **[DataSetVersion](DataSetVersion.md)** *[versionOf](versionOf.md)*  <sub>OPT</sub>  **[DataSet](DataSet.md)**

## Attributes


### Inherited from named thing:

 * [category](category.md)  <sub>1..*</sub>
    * Description: Name of the high level ontology class in which this entity is categorized. Corresponds to the label for the biolink entity type class. In a neo4j database this MAY correspond to the neo4j label tag
    * range: [IriType](types/IriType.md)
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
| **Mappings:** | | IAO:0000100 |


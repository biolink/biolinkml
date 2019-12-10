
# Type: data set




URI: [biolink:DataSet](https://w3id.org/biolink/vocab/DataSet)


![img](http://yuml.me/diagram/nofunky;dir:TB/class/\[DataSetVersion]-%20versionOf%200..1>\[DataSet&#124;id(i):identifier_type;name(i):label_type;category(i):iri_type%20%2B],%20\[DataSet]^-\[DataSetVersion],%20\[NamedThing]^-\[DataSet])

## Parents

 *  is_a: [named thing](named thing.md) - a databased entity or concept/class

## Children

 * [data set version](data set version.md)

## Referenced by class

 *  **[data set version](data set version.md)** *[versionOf](versionOf.md)*  <sub>OPT</sub>  **[data set](data set.md)**

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

## Other properties

|  |  |  |
| --- | --- | --- |
| **Mappings:** | | IAO:0000100 |


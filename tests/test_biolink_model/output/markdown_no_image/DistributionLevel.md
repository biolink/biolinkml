
# Type: distribution level




URI: [biolink:DistributionLevel](https://w3id.org/biolink/vocab/DistributionLevel)


![img](http://yuml.me/diagram/nofunky;dir:TB/class/[DataSetVersion]-%20distribution%200..1>[DistributionLevel&#124;downloadURL:string%20%3F;title(i):string%20%3F;type(i):string%20%3F;id(i):string;name(i):label_type;category(i):category_type%20%2B],[DataSetVersion]^-[DistributionLevel],[DataSetVersion],[DataSet],[DataFile])

## Parents

 *  is_a: [DataSetVersion](DataSetVersion.md)

## Referenced by class

 *  **[DataSetVersion](DataSetVersion.md)** *[distribution](distribution.md)*  <sub>OPT</sub>  **[DistributionLevel](DistributionLevel.md)**

## Attributes


### Own

 * [downloadURL](downloadURL.md)  <sub>OPT</sub>
    * range: [String](types/String.md)

### Inherited from data set version:

 * [category](category.md)  <sub>1..*</sub>
    * Description: Name of the high level ontology class in which this entity is categorized. Corresponds to the label for the biolink entity type class. In a neo4j database this MAY correspond to the neo4j label tag
    * range: [CategoryType](types/CategoryType.md)
    * in subsets: (translator_minimal)
 * [distribution](distribution.md)  <sub>OPT</sub>
    * range: [DistributionLevel](DistributionLevel.md)
 * [id](id.md)  <sub>REQ</sub>
    * Description: A unique identifier for a thing. Must be either a CURIE shorthand for a URI or a complete URI
    * range: [String](types/String.md)
    * in subsets: (translator_minimal)
 * [name](name.md)  <sub>REQ</sub>
    * Description: A human-readable name for a thing
    * range: [LabelType](types/LabelType.md)
    * in subsets: (translator_minimal)
 * [source data file](source_data_file.md)  <sub>OPT</sub>
    * range: [DataFile](DataFile.md)
 * [title](title.md)  <sub>OPT</sub>
    * range: [String](types/String.md)
 * [type](type.md)  <sub>OPT</sub>
    * range: [String](types/String.md)
 * [versionOf](versionOf.md)  <sub>OPT</sub>
    * range: [DataSet](DataSet.md)

## Other properties

|  |  |  |
| --- | --- | --- |
| **Mappings:** | | dcat:Distribution |


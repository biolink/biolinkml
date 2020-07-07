
# Type: data set version




URI: [biolink:DataSetVersion](https://w3id.org/biolink/vocab/DataSetVersion)


![img](http://yuml.me/diagram/nofunky;dir:TB/class/[DistributionLevel],[DistributionLevel]<distribution%200..1-%20[DataSetVersion&#124;title:string%20%3F;type:string%20%3F;id(i):string;name(i):label_type;category(i):iri_type%20%2B],[DataSet]<versionOf%200..1-%20[DataSetVersion],[DataFile]<source%20data%20file%200..1-%20[DataSetVersion],[DataSetVersion]^-[DistributionLevel],[DataSetVersion]^-[DataSetSummary],[DataSet]^-[DataSetVersion],[DataSetSummary],[DataSet],[DataFile])

## Parents

 *  is_a: [DataSet](DataSet.md)

## Children

 * [DataSetSummary](DataSetSummary.md)
 * [DistributionLevel](DistributionLevel.md)

## Referenced by class


## Attributes


### Own

 * [distribution](distribution.md)  <sub>OPT</sub>
    * range: [DistributionLevel](DistributionLevel.md)
 * [source data file](source_data_file.md)  <sub>OPT</sub>
    * range: [DataFile](DataFile.md)
 * [title](title.md)  <sub>OPT</sub>
    * range: [String](types/String.md)
 * [type](type.md)  <sub>OPT</sub>
    * range: [String](types/String.md)
 * [versionOf](versionOf.md)  <sub>OPT</sub>
    * range: [DataSet](DataSet.md)

### Inherited from data set:

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

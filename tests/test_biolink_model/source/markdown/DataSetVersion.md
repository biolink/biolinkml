
# Type: data set version




URI: [biolink:DataSetVersion](https://w3id.org/biolink/vocab/DataSetVersion)


![img](http://yuml.me/diagram/nofunky;dir:TB/class/\[DistributionLevel]<distribution%200..1-%20\[DataSetVersion&#124;title:string%20%3F;id(i):identifier_type;name(i):label_type;category(i):iri_type%20%2B],%20\[DataSet]<versionOf%200..1-%20\[DataSetVersion],%20\[DataFile]<source%20data%20file%200..1-%20\[DataSetVersion],%20\[DataSetVersion]^-\[DistributionLevel],%20\[DataSetVersion]^-\[DataSetSummary],%20\[DataSet]^-\[DataSetVersion])

## Parents

 *  is_a: [data set](data set.md)

## Children

 * [data set summary](data set summary.md)
 * [distribution level](distribution level.md)

## Referenced by class


## Attributes


### Own

 * [distribution](distribution.md)  <sub>OPT</sub>
    * range: [distribution level](distribution level.md)
 * [source data file](source_data_file.md)  <sub>OPT</sub>
    * range: [data file](data file.md)
 * [title](title.md)  <sub>OPT</sub>
    * range: [String](type/String.md)
 * [versionOf](versionOf.md)  <sub>OPT</sub>
    * range: [data set](data set.md)

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

### Domain for slot:

 * [distribution](distribution.md)  <sub>OPT</sub>
    * range: [distribution level](distribution level.md)
 * [source data file](source_data_file.md)  <sub>OPT</sub>
    * range: [data file](data file.md)
 * [title](title.md)  <sub>OPT</sub>
    * range: [String](type/String.md)
 * [versionOf](versionOf.md)  <sub>OPT</sub>
    * range: [data set](data set.md)

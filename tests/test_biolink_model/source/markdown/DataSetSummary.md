
# Type: data set summary




URI: [biolink:DataSetSummary](https://w3id.org/biolink/vocab/DataSetSummary)


![img](http://yuml.me/diagram/nofunky;dir:TB/class/\[DistributionLevel]<distribution(i)%200..1-%20\[DataSetSummary&#124;source_web_page:string%20%3F;title(i):string%20%3F;id(i):identifier_type;name(i):label_type;category(i):iri_type%20%2B],%20\[DataSet]<versionOf(i)%200..1-%20\[DataSetSummary],%20\[DataFile]<source%20data%20file(i)%200..1-%20\[DataSetSummary],%20\[DataSetVersion]^-\[DataSetSummary])

## Parents

 *  is_a: [data set version](data set version.md)

## Referenced by class


## Attributes


### Own

 * [source web page](source_web_page.md)  <sub>OPT</sub>
    * range: [String](type/String.md)

### Inherited from data set version:

 * [title](title.md)  <sub>OPT</sub>
    * range: [String](type/String.md)
    * inherited from: [data set version](data set version.md)
 * [source data file](source_data_file.md)  <sub>OPT</sub>
    * range: [data file](data file.md)
    * inherited from: [data set version](data set version.md)
 * [versionOf](versionOf.md)  <sub>OPT</sub>
    * range: [data set](data set.md)
    * inherited from: [data set version](data set version.md)
 * [distribution](distribution.md)  <sub>OPT</sub>
    * range: [distribution level](distribution level.md)
    * inherited from: [data set version](data set version.md)

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

 * [source web page](source_web_page.md)  <sub>OPT</sub>
    * range: [String](type/String.md)

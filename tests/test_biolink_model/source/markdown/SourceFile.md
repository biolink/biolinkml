
# Type: source file




URI: [biolink:SourceFile](https://w3id.org/biolink/vocab/SourceFile)


![img](http://yuml.me/diagram/nofunky;dir:TB/class/\[DataFile]^-\[SourceFile&#124;source_version:string%20%3F;retrievedOn:date%20%3F;id(i):identifier_type;name(i):label_type;category(i):iri_type%20%2B])

## Parents

 *  is_a: [data file](data file.md)

## Referenced by class


## Attributes


### Own

 * [retrievedOn](retrievedOn.md)  <sub>OPT</sub>
    * range: [Date](type/Date.md)
 * [source version](source_version.md)  <sub>OPT</sub>
    * range: [String](type/String.md)

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

 * [retrievedOn](retrievedOn.md)  <sub>OPT</sub>
    * range: [Date](type/Date.md)
 * [source version](source_version.md)  <sub>OPT</sub>
    * range: [String](type/String.md)

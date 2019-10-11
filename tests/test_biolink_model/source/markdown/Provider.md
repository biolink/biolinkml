
# Type: provider


person, group, organization or project that provides a piece of information

URI: [biolink:Provider](https://w3id.org/biolink/vocab/Provider)


![img](http://yuml.me/diagram/nofunky;dir:TB/class/\[Association]-%20provided%20by%200..1>\[Provider|id(i):identifier_type;name(i):label_type;category(i):iri_type%20%2B],%20\[AdministrativeEntity]^-\[Provider])

## Parents

 *  is_a: [administrative entity](administrative entity.md)

## Referenced by class

 *  **[association](association.md)** *[provided by](provided_by.md)*  <sub>OPT</sub>  **[provider](provider.md)**

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
| **Aliases:** | | agent |
|  | | group |
| **Mappings:** | | UMLSSG:ORGA |
|  | | UMLSSC:T092 |
|  | | UMLSST:orgt |
|  | | UMLSSC:T093 |
|  | | UMLSST:hcro |
|  | | UMLSSC:T094 |
|  | | UMLSST:pros |
|  | | UMLSSC:T095 |
|  | | UMLSST:shro |


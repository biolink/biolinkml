
# Type: cell line




URI: [biolink:CellLine](https://w3id.org/biolink/vocab/CellLine)


![img](http://yuml.me/diagram/nofunky;dir:TB/class/\[CellLineToThingAssociation]-%20subject%201..1>\[CellLine|id(i):identifier_type;name(i):label_type;category(i):iri_type%20%2B],%20\[OrganismalEntity]^-\[CellLine])

## Parents

 *  is_a: [organismal entity](organismal entity.md) - A named entity that is either a part of an organism, a whole organism, population or clade of organisms, excluding molecular entities

## Referenced by class

 *  **[cell line to thing association](cell line to thing association.md)** *[subject](cell_line_to_thing_association_subject.md)*  <sub>REQ</sub>  **[cell line](cell line.md)**

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
| **Mappings:** | | CLO:0000031 |


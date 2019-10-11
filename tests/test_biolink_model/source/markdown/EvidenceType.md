
# Type: evidence type


Class of evidence that supports an association

URI: [biolink:EvidenceType](https://w3id.org/biolink/vocab/EvidenceType)


![img](http://yuml.me/diagram/nofunky;dir:TB/class/\[InformationContentEntity]^-\[EvidenceType|id(i):identifier_type;name(i):label_type;category(i):iri_type%20%2B])

## Parents

 *  is_a: [information content entity](information content entity.md) - a piece of information that typically describes some piece of biology or is used as support.

## Referenced by class

 *  **[association](association.md)** *[has evidence](has_evidence.md)*  <sub>OPT</sub>  **[evidence type](evidence type.md)**

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
| **Aliases:** | | evidence code |
| **Mappings:** | | ECO:0000000 |


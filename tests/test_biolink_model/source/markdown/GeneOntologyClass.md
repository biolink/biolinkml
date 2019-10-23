
# Type: gene ontology class


an ontology class that describes a functional aspect of a gene, gene prodoct or complex

URI: [biolink:GeneOntologyClass](https://w3id.org/biolink/vocab/GeneOntologyClass)


![img](http://yuml.me/diagram/nofunky;dir:TB/class/\[FunctionalAssociation]-%20object%201..1>\[GeneOntologyClass|id(i):identifier_type;name(i):label_type;category(i):iri_type%20%2B],%20\[GeneToGoTermAssociation]-%20object%201..1>\[GeneOntologyClass],%20\[OntologyClass]^-\[GeneOntologyClass])

## Parents

 *  is_a: [ontology class](ontology class.md) - a concept or class in an ontology, vocabulary or thesaurus

## Referenced by class

 *  **[functional association](functional association.md)** *[object](functional_association_object.md)*  <sub>REQ</sub>  **[gene ontology class](gene ontology class.md)**
 *  **[gene to go term association](gene to go term association.md)** *[object](gene_to_go_term_association_object.md)*  <sub>REQ</sub>  **[gene ontology class](gene ontology class.md)**

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
| **In Subsets:** | | testing |



# Type: gene ontology class


an ontology class that describes a functional aspect of a gene, gene prodoct or complex

URI: [biolink:GeneOntologyClass](https://w3id.org/biolink/vocab/GeneOntologyClass)


![img](http://yuml.me/diagram/nofunky;dir:TB/class/[OntologyClass],[GeneToGoTermAssociation],[FunctionalAssociation]-%20object%201..1>[GeneOntologyClass&#124;id(i):string;name(i):label_type;category(i):iri_type%20%2B],[GeneToGoTermAssociation]-%20object%201..1>[GeneOntologyClass],[OntologyClass]^-[GeneOntologyClass],[FunctionalAssociation])

## Parents

 *  is_a: [OntologyClass](OntologyClass.md) - a concept or class in an ontology, vocabulary or thesaurus

## Referenced by class

 *  **[FunctionalAssociation](FunctionalAssociation.md)** *[functional association➞object](functional_association_object.md)*  <sub>REQ</sub>  **[GeneOntologyClass](GeneOntologyClass.md)**
 *  **[GeneToGoTermAssociation](GeneToGoTermAssociation.md)** *[gene to go term association➞object](gene_to_go_term_association_object.md)*  <sub>REQ</sub>  **[GeneOntologyClass](GeneOntologyClass.md)**

## Attributes


### Inherited from ontology class:

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

## Other properties

|  |  |  |
| --- | --- | --- |
| **In Subsets:** | | testing |


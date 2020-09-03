
# Type: gene to go term association




URI: [biolink:GeneToGoTermAssociation](https://w3id.org/biolink/vocab/GeneToGoTermAssociation)


![img](http://yuml.me/diagram/nofunky;dir:TB/class/[Publication],[Provider],[OntologyClass],[MolecularEntity],[GeneOntologyClass]<object%201..1-%20[GeneToGoTermAssociation&#124;relation(i):uriorcurie;id(i):string;negated(i):boolean%20%3F],[MolecularEntity]<subject%201..1-%20[GeneToGoTermAssociation],[FunctionalAssociation]^-[GeneToGoTermAssociation],[GeneOntologyClass],[FunctionalAssociation])

## Parents

 *  is_a: [FunctionalAssociation](FunctionalAssociation.md) - An association between a macromolecular machine (gene, gene product or complex of gene products) and either a molecular activity, a biological process or a cellular location in which a function is executed

## Referenced by class


## Attributes


### Own

 * [gene to go term association➞object](gene_to_go_term_association_object.md)  <sub>REQ</sub>
    * Description: class describing the activity, process or localization of the gene product
    * range: [GeneOntologyClass](GeneOntologyClass.md)
    * Example:    
 * [gene to go term association➞subject](gene_to_go_term_association_subject.md)  <sub>REQ</sub>
    * Description: gene, product or macromolecular complex that has the function associated with the GO term
    * range: [MolecularEntity](MolecularEntity.md)
    * Example:    

### Inherited from functional association:

 * [association type](association_type.md)  <sub>OPT</sub>
    * Description: connects an association to the type of association (e.g. gene to phenotype)
    * range: [OntologyClass](OntologyClass.md)
 * [association➞id](association_id.md)  <sub>REQ</sub>
    * Description: A unique identifier for an association
    * range: [String](types/String.md)
    * in subsets: (translator_minimal)
 * [negated](negated.md)  <sub>OPT</sub>
    * Description: if set to true, then the association is negated i.e. is not true
    * range: [Boolean](types/Boolean.md)
 * [provided by](provided_by.md)  <sub>0..*</sub>
    * Description: connects an association to the agent (person, organization or group) that provided it
    * range: [Provider](Provider.md)
 * [publications](publications.md)  <sub>0..*</sub>
    * Description: connects an association to publications supporting the association
    * range: [Publication](Publication.md)
 * [qualifiers](qualifiers.md)  <sub>0..*</sub>
    * Description: connects an association to qualifiers that modify or qualify the meaning of that association
    * range: [OntologyClass](OntologyClass.md)
 * [relation](relation.md)  <sub>REQ</sub>
    * Description: The relation which describes an association between a subject and an object in a more granular manner. Usually this is a term from Relation Ontology, but it can be any edge CURIE.
    * range: [Uriorcurie](types/Uriorcurie.md)

## Other properties

|  |  |  |
| --- | --- | --- |
| **Aliases:** | | functional association |
| **Mappings:** | | http://bio2rdf.org/wormbase_vocabulary:Gene-GO-Association |


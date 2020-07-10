
# Type: genotype to gene association


Any association between a genotype and a gene. The genotype have have multiple variants in that gene or a single one. There is no assumption of cardinality

URI: [biolink:GenotypeToGeneAssociation](https://w3id.org/biolink/vocab/GenotypeToGeneAssociation)


![img](http://yuml.me/diagram/nofunky;dir:TB/class/[Publication],[Provider],[OntologyClass],[Gene]<object%201..1-%20[GenotypeToGeneAssociation&#124;relation:uriorcurie;id(i):string;negated(i):boolean%20%3F],[Genotype]<subject%201..1-%20[GenotypeToGeneAssociation],[Association]^-[GenotypeToGeneAssociation],[Genotype],[Gene],[Association])

## Parents

 *  is_a: [Association](Association.md) - A typed association between two entities, supported by evidence

## Referenced by class


## Attributes


### Own

 * [genotype to gene association➞object](genotype_to_gene_association_object.md)  <sub>REQ</sub>
    * range: [Gene](Gene.md)
 * [genotype to gene association➞relation](genotype_to_gene_association_relation.md)  <sub>REQ</sub>
    * range: [Uriorcurie](types/Uriorcurie.md)
 * [genotype to gene association➞subject](genotype_to_gene_association_subject.md)  <sub>REQ</sub>
    * range: [Genotype](Genotype.md)

### Inherited from association:

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

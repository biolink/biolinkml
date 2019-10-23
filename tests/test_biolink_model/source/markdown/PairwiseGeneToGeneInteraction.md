
# Type: pairwise gene to gene interaction


An interaction between two genes or two gene products. May be physical (e.g. protein binding) or genetic (between genes). May be symmetric (e.g. protein interaction) or directed (e.g. phosphorylation)

URI: [biolink:PairwiseGeneToGeneInteraction](https://w3id.org/biolink/vocab/PairwiseGeneToGeneInteraction)


![img](http://yuml.me/diagram/nofunky;dir:TB/class/\[Provider]<provided%20by(i)%200..1-%20\[PairwiseGeneToGeneInteraction|relation:uriorcurie;id(i):nodeidentifier;negated(i):boolean%20%3F],%20\[Publication]<publications(i)%200..*-%20\[PairwiseGeneToGeneInteraction],%20\[OntologyClass]<qualifiers(i)%200..*-%20\[PairwiseGeneToGeneInteraction],%20\[OntologyClass]<association%20type(i)%200..1-%20\[PairwiseGeneToGeneInteraction],%20\[GeneOrGeneProduct]<object(i)%201..1-%20\[PairwiseGeneToGeneInteraction],%20\[GeneOrGeneProduct]<subject(i)%201..1-%20\[PairwiseGeneToGeneInteraction],%20\[PairwiseGeneToGeneInteraction]uses%20-.->\[PairwiseInteractionAssociation],%20\[GeneToGeneAssociation]^-\[PairwiseGeneToGeneInteraction])

## Parents

 *  is_a: [gene to gene association](gene to gene association.md) - abstract parent class for different kinds of gene-gene or gene product to gene product relationships. Includes homology and interaction.

## Uses Mixins

 *  mixin: [pairwise interaction association](pairwise interaction association.md) - An interaction at the molecular level between two physical entities

## Referenced by class


## Attributes


### Own

 * [pairwise gene to gene interaction➞relation](pairwise_gene_to_gene_interaction_relation.md)  <sub>REQ</sub>
    * range: [Uriorcurie](type/Uriorcurie.md)

### Inherited from association:

 * [subject](subject.md)  <sub>REQ</sub>
    * Description: connects an association to the subject of the association. For example, in a gene-to-phenotype association, the gene is subject and phenotype is object.
    * range: [named thing](named thing.md)
    * inherited from: [association](association.md)
 * [relation](relation.md)  <sub>REQ</sub>
    * Description: the relationship type by which a subject is connected to an object in an association
    * range: [Uriorcurie](type/Uriorcurie.md)
    * inherited from: [association](association.md)
 * [object](object.md)  <sub>REQ</sub>
    * Description: connects an association to the object of the association. For example, in a gene-to-phenotype association, the gene is subject and phenotype is object.
    * range: [named thing](named thing.md)
    * inherited from: [association](association.md)
 * [association➞id](association_id.md)  <sub>REQ</sub>
    * Description: A unique identifier for an association
    * range: [Nodeidentifier](type/Nodeidentifier.md)
    * inherited from: [association](association.md)
    * in subsets: (translator_minimal)
 * [negated](negated.md)  <sub>OPT</sub>
    * Description: if set to true, then the association is negated i.e. is not true
    * range: [Boolean](type/Boolean.md)
    * inherited from: [association](association.md)
 * [association type](association_type.md)  <sub>OPT</sub>
    * Description: connects an association to the type of association (e.g. gene to phenotype)
    * range: [ontology class](ontology class.md)
    * inherited from: [association](association.md)
 * [qualifiers](qualifiers.md)  <sub>0..*</sub>
    * Description: connects an association to qualifiers that modify or qualify the meaning of that association
    * range: [ontology class](ontology class.md)
    * inherited from: [association](association.md)
 * [publications](publications.md)  <sub>0..*</sub>
    * Description: connects an association to publications supporting the association
    * range: [publication](publication.md)
    * inherited from: [association](association.md)
 * [provided by](provided_by.md)  <sub>OPT</sub>
    * Description: connects an association to the agent (person, organization or group) that provided it
    * range: [provider](provider.md)
    * inherited from: [association](association.md)

### Inherited from gene to gene association:

 * [gene to gene association➞subject](gene_to_gene_association_subject.md)  <sub>REQ</sub>
    * range: [gene or gene product](gene or gene product.md)
    * inherited from: [gene to gene association](gene to gene association.md)
 * [gene to gene association➞object](gene_to_gene_association_object.md)  <sub>REQ</sub>
    * range: [gene or gene product](gene or gene product.md)
    * inherited from: [gene to gene association](gene to gene association.md)

### Domain for slot:

 * [pairwise gene to gene interaction➞relation](pairwise_gene_to_gene_interaction_relation.md)  <sub>REQ</sub>
    * range: [Uriorcurie](type/Uriorcurie.md)

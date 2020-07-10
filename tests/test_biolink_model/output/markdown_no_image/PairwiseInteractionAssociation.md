
# Type: pairwise interaction association


An interaction at the molecular level between two physical entities

URI: [biolink:PairwiseInteractionAssociation](https://w3id.org/biolink/vocab/PairwiseInteractionAssociation)


![img](http://yuml.me/diagram/nofunky;dir:TB/class/[Publication],[Provider],[MolecularEntity]<object%201..1-%20[PairwiseInteractionAssociation&#124;relation:uriorcurie;id:string;negated(i):boolean%20%3F],[MolecularEntity]<subject%201..1-%20[PairwiseInteractionAssociation],[PairwiseGeneToGeneInteraction]uses%20-.->[PairwiseInteractionAssociation],[Association]^-[PairwiseInteractionAssociation],[PairwiseGeneToGeneInteraction],[OntologyClass],[MolecularEntity],[Association])

## Parents

 *  is_a: [Association](Association.md) - A typed association between two entities, supported by evidence

## Mixin for

 * [PairwiseGeneToGeneInteraction](PairwiseGeneToGeneInteraction.md) (mixin)  - An interaction between two genes or two gene products. May be physical (e.g. protein binding) or genetic (between genes). May be symmetric (e.g. protein interaction) or directed (e.g. phosphorylation)

## Referenced by class


## Attributes


### Own

 * [pairwise interaction association➞id](pairwise_interaction_association_id.md)  <sub>REQ</sub>
    * range: [String](types/String.md)
 * [pairwise interaction association➞object](pairwise_interaction_association_object.md)  <sub>REQ</sub>
    * range: [MolecularEntity](MolecularEntity.md)
 * [pairwise interaction association➞relation](pairwise_interaction_association_relation.md)  <sub>REQ</sub>
    * range: [Uriorcurie](types/Uriorcurie.md)
 * [pairwise interaction association➞subject](pairwise_interaction_association_subject.md)  <sub>REQ</sub>
    * range: [MolecularEntity](MolecularEntity.md)

### Inherited from association:

 * [association type](association_type.md)  <sub>OPT</sub>
    * Description: connects an association to the type of association (e.g. gene to phenotype)
    * range: [OntologyClass](OntologyClass.md)
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


# Type: anatomical entity to anatomical entity association




URI: [biolink:AnatomicalEntityToAnatomicalEntityAssociation](https://w3id.org/biolink/vocab/AnatomicalEntityToAnatomicalEntityAssociation)


![img](http://yuml.me/diagram/nofunky;dir:TB/class/\[Provider]<provided%20by(i)%200..1-%20\[AnatomicalEntityToAnatomicalEntityAssociation|relation(i):uriorcurie;id(i):nodeidentifier;negated(i):boolean%20%3F],%20\[Publication]<publications(i)%200..*-%20\[AnatomicalEntityToAnatomicalEntityAssociation],%20\[OntologyClass]<qualifiers(i)%200..*-%20\[AnatomicalEntityToAnatomicalEntityAssociation],%20\[OntologyClass]<association%20type(i)%200..1-%20\[AnatomicalEntityToAnatomicalEntityAssociation],%20\[AnatomicalEntity]<object%201..1-%20\[AnatomicalEntityToAnatomicalEntityAssociation],%20\[AnatomicalEntity]<subject%201..1-%20\[AnatomicalEntityToAnatomicalEntityAssociation],%20\[AnatomicalEntityToAnatomicalEntityAssociation]^-\[AnatomicalEntityToAnatomicalEntityPartOfAssociation],%20\[AnatomicalEntityToAnatomicalEntityAssociation]^-\[AnatomicalEntityToAnatomicalEntityOntogenicAssociation],%20\[Association]^-\[AnatomicalEntityToAnatomicalEntityAssociation])

## Parents

 *  is_a: [association](association.md) - A typed association between two entities, supported by evidence

## Children

 * [anatomical entity to anatomical entity ontogenic association](anatomical entity to anatomical entity ontogenic association.md) - A relationship between two anatomical entities where the relationship is ontogenic, i.e the two entities are related by development. A number of different relationship types can be used to specify the precise nature of the relationship
 * [anatomical entity to anatomical entity part of association](anatomical entity to anatomical entity part of association.md) - A relationship between two anatomical entities where the relationship is mereological, i.e the two entities are related by parthood. This includes relationships between cellular components and cells, between cells and tissues, tissues and whole organisms

## Referenced by class


## Attributes


### Own

 * [anatomical entity to anatomical entity association➞object](anatomical_entity_to_anatomical_entity_association_object.md)  <sub>REQ</sub>
    * range: [anatomical entity](anatomical entity.md)
 * [anatomical entity to anatomical entity association➞subject](anatomical_entity_to_anatomical_entity_association_subject.md)  <sub>REQ</sub>
    * range: [anatomical entity](anatomical entity.md)

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

### Domain for slot:

 * [anatomical entity to anatomical entity association➞object](anatomical_entity_to_anatomical_entity_association_object.md)  <sub>REQ</sub>
    * range: [anatomical entity](anatomical entity.md)
 * [anatomical entity to anatomical entity association➞subject](anatomical_entity_to_anatomical_entity_association_subject.md)  <sub>REQ</sub>
    * range: [anatomical entity](anatomical entity.md)


# Type: anatomical entity to anatomical entity association




URI: [biolink:AnatomicalEntityToAnatomicalEntityAssociation](https://w3id.org/biolink/vocab/AnatomicalEntityToAnatomicalEntityAssociation)


![img](http://yuml.me/diagram/nofunky;dir:TB/class/[Publication],[Provider],[OntologyClass],[Association],[AnatomicalEntityToAnatomicalEntityPartOfAssociation],[AnatomicalEntityToAnatomicalEntityOntogenicAssociation],[AnatomicalEntity]<object%201..1-%20[AnatomicalEntityToAnatomicalEntityAssociation&#124;relation(i):uriorcurie;id(i):string;negated(i):boolean%20%3F],[AnatomicalEntity]<subject%201..1-%20[AnatomicalEntityToAnatomicalEntityAssociation],[AnatomicalEntityToAnatomicalEntityAssociation]^-[AnatomicalEntityToAnatomicalEntityPartOfAssociation],[AnatomicalEntityToAnatomicalEntityAssociation]^-[AnatomicalEntityToAnatomicalEntityOntogenicAssociation],[Association]^-[AnatomicalEntityToAnatomicalEntityAssociation],[AnatomicalEntity])

## Parents

 *  is_a: [Association](Association.md) - A typed association between two entities, supported by evidence

## Children

 * [AnatomicalEntityToAnatomicalEntityOntogenicAssociation](AnatomicalEntityToAnatomicalEntityOntogenicAssociation.md) - A relationship between two anatomical entities where the relationship is ontogenic, i.e the two entities are related by development. A number of different relationship types can be used to specify the precise nature of the relationship
 * [AnatomicalEntityToAnatomicalEntityPartOfAssociation](AnatomicalEntityToAnatomicalEntityPartOfAssociation.md) - A relationship between two anatomical entities where the relationship is mereological, i.e the two entities are related by parthood. This includes relationships between cellular components and cells, between cells and tissues, tissues and whole organisms

## Referenced by class


## Attributes


### Own

 * [anatomical entity to anatomical entity association➞object](anatomical_entity_to_anatomical_entity_association_object.md)  <sub>REQ</sub>
    * range: [AnatomicalEntity](AnatomicalEntity.md)
 * [anatomical entity to anatomical entity association➞subject](anatomical_entity_to_anatomical_entity_association_subject.md)  <sub>REQ</sub>
    * range: [AnatomicalEntity](AnatomicalEntity.md)

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
 * [relation](relation.md)  <sub>REQ</sub>
    * Description: the relationship type by which a subject is connected to an object in an association
    * range: [Uriorcurie](types/Uriorcurie.md)

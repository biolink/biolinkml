
# Type: case to phenotypic feature association


An association between a case (e.g. individual patient) and a phenotypic feature in which the individual has or has had the phenotype

URI: [biolink:CaseToPhenotypicFeatureAssociation](https://w3id.org/biolink/vocab/CaseToPhenotypicFeatureAssociation)


![img](http://yuml.me/diagram/nofunky;dir:TB/class/\[Provider]<provided%20by(i)%200..1-%20\[CaseToPhenotypicFeatureAssociation|relation(i):uriorcurie;id(i):identifier_type;negated(i):boolean%20%3F],%20\[Publication]<publications(i)%200..*-%20\[CaseToPhenotypicFeatureAssociation],%20\[OntologyClass]<qualifiers(i)%200..*-%20\[CaseToPhenotypicFeatureAssociation],%20\[OntologyClass]<association%20type(i)%200..1-%20\[CaseToPhenotypicFeatureAssociation],%20\[NamedThing]<object(i)%201..1-%20\[CaseToPhenotypicFeatureAssociation],%20\[NamedThing]<subject(i)%201..1-%20\[CaseToPhenotypicFeatureAssociation],%20\[CaseToPhenotypicFeatureAssociation]uses%20-.->\[EntityToPhenotypicFeatureAssociation],%20\[CaseToPhenotypicFeatureAssociation]uses%20-.->\[CaseToThingAssociation],%20\[Association]^-\[CaseToPhenotypicFeatureAssociation])

## Parents

 *  is_a: [association](association.md) - A typed association between two entities, supported by evidence

## Uses Mixins

 *  mixin: [entity to phenotypic feature association](entity to phenotypic feature association.md)
 *  mixin: [case to thing association](case to thing association.md) - An abstract association for use where the case is the subject

## Attributes


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
 * [id](association_id.md)  <sub>REQ</sub>
    * Description: A unique identifier for an association
    * range: [IdentifierType](type/IdentifierType.md)
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

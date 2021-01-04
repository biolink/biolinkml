
# Type: chemical to chemical association


A relationship between two chemical entities. This can encompass actual interactions as well as temporal causal edges, e.g. one chemical converted to another.

URI: [biolink:ChemicalToChemicalAssociation](https://w3id.org/biolink/vocab/ChemicalToChemicalAssociation)


![img](http://yuml.me/diagram/nofunky;dir:TB/class/[Publication],[Provider],[OntologyClass],[NamedThing],[ChemicalToThingAssociation],[ChemicalToChemicalDerivationAssociation],[ChemicalSubstance]<object%201..1-%20[ChemicalToChemicalAssociation&#124;relation(i):uriorcurie;id(i):string;negated(i):boolean%20%3F],[ChemicalToChemicalAssociation]uses%20-.->[ChemicalToThingAssociation],[ChemicalToChemicalAssociation]^-[ChemicalToChemicalDerivationAssociation],[Association]^-[ChemicalToChemicalAssociation],[ChemicalSubstance],[Association])

## Parents

 *  is_a: [Association](Association.md) - A typed association between two entities, supported by evidence

## Uses Mixins

 *  mixin: [ChemicalToThingAssociation](ChemicalToThingAssociation.md) - An interaction between a chemical entity and another entity

## Children

 * [ChemicalToChemicalDerivationAssociation](ChemicalToChemicalDerivationAssociation.md) - A causal relationship between two chemical entities, where the subject represents the upstream entity and the object represents the downstream. For any such association there is an implicit reaction:

## Referenced by class


## Attributes


### Own

 * [chemical to chemical association➞object](chemical_to_chemical_association_object.md)  <sub>REQ</sub>
    * Description: the chemical element that is the target of the statement
    * range: [ChemicalSubstance](ChemicalSubstance.md)

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
    * Description: The relation which describes an association between a subject and an object in a more granular manner. Usually this is a term from Relation Ontology, but it can be any edge CURIE.
    * range: [Uriorcurie](types/Uriorcurie.md)
 * [subject](subject.md)  <sub>REQ</sub>
    * Description: connects an association to the subject of the association. For example, in a gene-to-phenotype association, the gene is subject and phenotype is object.
    * range: [NamedThing](NamedThing.md)

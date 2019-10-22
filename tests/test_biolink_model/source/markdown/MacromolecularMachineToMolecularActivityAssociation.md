
# Type: macromolecular machine to molecular activity association


A functional association between a macromolecular machine (gene, gene product or complex) and a molecular activity (as represented in the GO molecular function branch), where the entity carries out the activity, or contributes to its execution

URI: [biolink:MacromolecularMachineToMolecularActivityAssociation](https://w3id.org/biolink/vocab/MacromolecularMachineToMolecularActivityAssociation)


![img](http://yuml.me/diagram/nofunky;dir:TB/class/\[Provider]<provided%20by(i)%200..1-%20\[MacromolecularMachineToMolecularActivityAssociation|relation(i):uriorcurie;id(i):nodeidentifier;negated(i):boolean%20%3F],%20\[Publication]<publications(i)%200..*-%20\[MacromolecularMachineToMolecularActivityAssociation],%20\[OntologyClass]<qualifiers(i)%200..*-%20\[MacromolecularMachineToMolecularActivityAssociation],%20\[OntologyClass]<association%20type(i)%200..1-%20\[MacromolecularMachineToMolecularActivityAssociation],%20\[MacromolecularMachine]<subject(i)%201..1-%20\[MacromolecularMachineToMolecularActivityAssociation],%20\[MolecularActivity]<object%201..1-%20\[MacromolecularMachineToMolecularActivityAssociation],%20\[FunctionalAssociation]^-\[MacromolecularMachineToMolecularActivityAssociation])

## Parents

 *  is_a: [functional association](functional association.md) - An association between a macromolecular machine (gene, gene product or complex of gene products) and either a molecular activity, a biological process or a cellular location in which a function is executed

## Referenced by class


## Attributes


### Own

 * [macromolecular machine to molecular activity association➞object](macromolecular_machine_to_molecular_activity_association_object.md)  <sub>REQ</sub>
    * range: [molecular activity](molecular activity.md)

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

### Inherited from functional association:

 * [functional association➞subject](functional_association_subject.md)  <sub>REQ</sub>
    * range: [macromolecular machine](macromolecular machine.md)
    * inherited from: [functional association](functional association.md)
 * [functional association➞object](functional_association_object.md)  <sub>REQ</sub>
    * range: [gene ontology class](gene ontology class.md)
    * inherited from: [functional association](functional association.md)

### Domain for slot:

 * [macromolecular machine to molecular activity association➞object](macromolecular_machine_to_molecular_activity_association_object.md)  <sub>REQ</sub>
    * range: [molecular activity](molecular activity.md)

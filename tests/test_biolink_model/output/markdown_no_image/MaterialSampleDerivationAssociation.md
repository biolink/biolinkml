
# Type: material sample derivation association


An association between a material sample and the material entity it is derived from

URI: [biolink:MaterialSampleDerivationAssociation](https://w3id.org/biolink/vocab/MaterialSampleDerivationAssociation)


![img](http://yuml.me/diagram/nofunky;dir:TB/class/[Publication],[Provider],[OntologyClass],[NamedThing],[NamedThing]<object%201..1-%20[MaterialSampleDerivationAssociation&#124;relation:uriorcurie;id(i):string;negated(i):boolean%20%3F],[MaterialSample]<subject%201..1-%20[MaterialSampleDerivationAssociation],[Association]^-[MaterialSampleDerivationAssociation],[MaterialSample],[Association])

## Parents

 *  is_a: [Association](Association.md) - A typed association between two entities, supported by evidence

## Referenced by class


## Attributes


### Own

 * [material sample derivation association➞object](material_sample_derivation_association_object.md)  <sub>REQ</sub>
    * range: [NamedThing](NamedThing.md)
 * [material sample derivation association➞relation](material_sample_derivation_association_relation.md)  <sub>REQ</sub>
    * range: [Uriorcurie](types/Uriorcurie.md)
 * [material sample derivation association➞subject](material_sample_derivation_association_subject.md)  <sub>REQ</sub>
    * range: [MaterialSample](MaterialSample.md)

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


# Type: genomic sequence localization


A relationship between a sequence feature and an entity it is localized to. The reference entity may be a chromosome, chromosome region or information entity such as a contig

URI: [biolink:GenomicSequenceLocalization](https://w3id.org/biolink/vocab/GenomicSequenceLocalization)


![img](images/GenomicSequenceLocalization.svg)

## Parents

 *  is_a: [Association](Association.md) - A typed association between two entities, supported by evidence

## Referenced by class


## Attributes


### Own

 * [end interbase coordinate](end_interbase_coordinate.md)  <sub>OPT</sub>
    * range: [String](types/String.md)
 * [genome build](genome_build.md)  <sub>OPT</sub>
    * Description: TODO
    * range: [String](types/String.md)
 * [genomic sequence localization➞object](genomic_sequence_localization_object.md)  <sub>REQ</sub>
    * range: [GenomicEntity](GenomicEntity.md)
 * [genomic sequence localization➞subject](genomic_sequence_localization_subject.md)  <sub>REQ</sub>
    * range: [GenomicEntity](GenomicEntity.md)
 * [phase](phase.md)  <sub>OPT</sub>
    * Description: TODO
    * range: [String](types/String.md)
 * [start interbase coordinate](start_interbase_coordinate.md)  <sub>OPT</sub>
    * range: [String](types/String.md)

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

## Other properties

|  |  |  |
| --- | --- | --- |
| **Mappings:** | | faldo:location |


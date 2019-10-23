
# Type: attribute


A property or characteristic of an entity. For example, an apple may have properties such as color, shape, age, crispiness. An environmental sample may have attributes such as depth, lat, long, material.

URI: [biolink:Attribute](https://w3id.org/biolink/vocab/Attribute)


![img](http://yuml.me/diagram/nofunky;dir:TB/class/\[NamedThing]<has%20qualitative%20value%200..1-%20\[Attribute|id:identifier_type;name:label_type;category:iri_type%20%2B],%20\[QuantityValue]<has%20quantitative%20value%200..*-++\[Attribute],%20\[OntologyClass]<has%20attribute%20type%200..1-%20\[Attribute],%20\[Attribute]uses%20-.->\[OntologyClass],%20\[Attribute]^-\[Zygosity],%20\[Attribute]^-\[SeverityValue],%20\[Attribute]^-\[Onset],%20\[Attribute]^-\[FrequencyValue],%20\[Attribute]^-\[ClinicalModifier],%20\[Attribute]^-\[BiologicalSex],%20\[AbstractEntity]^-\[Attribute])

## Parents

 *  is_a: [abstract entity](abstract entity.md) - Any thing that is not a process or a physical mass-bearing entity

## Uses Mixins

 *  mixin: [ontology class](ontology class.md) - a concept or class in an ontology, vocabulary or thesaurus

## Children

 * [biological sex](biological sex.md)
 * [clinical modifier](clinical modifier.md) - Used to characterize and specify the phenotypic abnormalities defined in the Phenotypic abnormality subontology, with respect to severity, laterality, age of onset, and other aspects
 * [frequency value](frequency value.md) - describes the frequency of occurrence of an event or condition
 * [onset](onset.md) - The age group in which manifestations appear
 * [severity value](severity value.md) - describes the severity of a phenotypic feature or disease
 * [zygosity](zygosity.md)

## Referenced by class

 *  **None** *[has attribute](has_attribute.md)*  <sub>0..*</sub>  **[attribute](attribute.md)**

## Attributes


### Own

 * [has attribute type](has_attribute_type.md)  <sub>OPT</sub>
    * Description: connects an attribute to a class that describes it
    * range: [ontology class](ontology class.md)
    * in subsets: (samples)
 * [has qualitative value](has_qualitative_value.md)  <sub>OPT</sub>
    * Description: connects an attribute to a value
    * range: [named thing](named thing.md)
    * in subsets: (samples)
 * [has quantitative value](has_quantitative_value.md)  <sub>0..*</sub>
    * Description: connects an attribute to a value
    * range: [quantity value](quantity value.md)
    * in subsets: (samples)

### Inherited from named thing:

 * [id](id.md)  <sub>REQ</sub>
    * Description: A unique identifier for a thing. Must be either a CURIE shorthand for a URI or a complete URI
    * range: [IdentifierType](type/IdentifierType.md)
    * in subsets: (translator_minimal)
 * [name](name.md)  <sub>REQ</sub>
    * Description: A human-readable name for a thing
    * range: [LabelType](type/LabelType.md)
    * in subsets: (translator_minimal)
 * [category](category.md)  <sub>1..*</sub>
    * Description: Name of the high level ontology class in which this entity is categorized. Corresponds to the label for the biolink entity type class. In a neo4j database this MAY correspond to the neo4j label tag
    * range: [IriType](type/IriType.md)
    * in subsets: (translator_minimal)

### Domain for slot:

 * [has attribute type](has_attribute_type.md)  <sub>OPT</sub>
    * Description: connects an attribute to a class that describes it
    * range: [ontology class](ontology class.md)
    * in subsets: (samples)
 * [has qualitative value](has_qualitative_value.md)  <sub>OPT</sub>
    * Description: connects an attribute to a value
    * range: [named thing](named thing.md)
    * in subsets: (samples)
 * [has quantitative value](has_quantitative_value.md)  <sub>0..*</sub>
    * Description: connects an attribute to a value
    * range: [quantity value](quantity value.md)
    * in subsets: (samples)

## Other properties

|  |  |  |
| --- | --- | --- |
| **Mappings:** | | SIO:000614 |
| **In Subsets:** | | samples |


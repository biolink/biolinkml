
# Type: attribute


A property or characteristic of an entity. For example, an apple may have properties such as color, shape, age, crispiness. An environmental sample may have attributes such as depth, lat, long, material.

URI: [biolink:Attribute](https://w3id.org/biolink/vocab/Attribute)


![img](http://yuml.me/diagram/nofunky;dir:TB/class/[Zygosity],[SeverityValue],[QuantityValue],[OntologyClass],[NamedThing],[Inheritance],[FrequencyValue],[ClinicalModifier],[ClinicalCourse],[BiologicalSex],[NamedThing]<has%20qualitative%20value%200..1-%20[Attribute&#124;id:string;name:label_type;category:category_type%20%2B],[QuantityValue]<has%20quantitative%20value%200..*-++[Attribute],[OntologyClass]<has%20attribute%20type%200..1-%20[Attribute],[MaterialSample]-%20has%20attribute%200..*>[Attribute],[Attribute]uses%20-.->[OntologyClass],[Attribute]^-[Zygosity],[Attribute]^-[SeverityValue],[Attribute]^-[Inheritance],[Attribute]^-[FrequencyValue],[Attribute]^-[ClinicalModifier],[Attribute]^-[ClinicalCourse],[Attribute]^-[BiologicalSex],[AbstractEntity]^-[Attribute],[MaterialSample],[AbstractEntity])

## Parents

 *  is_a: [AbstractEntity](AbstractEntity.md) - Any thing that is not a process or a physical mass-bearing entity

## Uses Mixins

 *  mixin: [OntologyClass](OntologyClass.md) - a concept or class in an ontology, vocabulary or thesaurus

## Children

 * [BiologicalSex](BiologicalSex.md)
 * [ClinicalCourse](ClinicalCourse.md) - The course a disease typically takes from its onset, progression in time, and eventual resolution or death of the affected individual
 * [ClinicalModifier](ClinicalModifier.md) - Used to characterize and specify the phenotypic abnormalities defined in the Phenotypic abnormality subontology, with respect to severity, laterality, and other aspects
 * [FrequencyValue](FrequencyValue.md) - describes the frequency of occurrence of an event or condition
 * [Inheritance](Inheritance.md) - The pattern in which a particular genetic trait or disorder is passed from one generation to the next
 * [SeverityValue](SeverityValue.md) - describes the severity of a phenotypic feature or disease
 * [Zygosity](Zygosity.md)

## Referenced by class

 *  **None** *[has attribute](has_attribute.md)*  <sub>0..*</sub>  **[Attribute](Attribute.md)**

## Attributes


### Own

 * [has attribute type](has_attribute_type.md)  <sub>OPT</sub>
    * Description: connects an attribute to a class that describes it
    * range: [OntologyClass](OntologyClass.md)
    * in subsets: (samples)
 * [has qualitative value](has_qualitative_value.md)  <sub>OPT</sub>
    * Description: connects an attribute to a value
    * range: [NamedThing](NamedThing.md)
    * in subsets: (samples)
 * [has quantitative value](has_quantitative_value.md)  <sub>0..*</sub>
    * Description: connects an attribute to a value
    * range: [QuantityValue](QuantityValue.md)
    * in subsets: (samples)

### Mixed in from named thing:

 * [category](category.md)  <sub>1..*</sub>
    * Description: Name of the high level ontology class in which this entity is categorized. Corresponds to the label for the biolink entity type class.
 * In a neo4j database this MAY correspond to the neo4j label tag.
 * In an RDF database it should be a biolink model class URI.
This field is multi-valued. It should include values for ancestors of the biolink class; for example, a protein such as Shh would have category values `bl:Protein`, `bl:GeneProduct`, `bl:MolecularEntity`, ...
In an RDF database, nodes will typically have an rdf:type triples. This can be to the most specific biolink class, or potentially to a class more specific than something in biolink. For example, a sequence feature `f` may have a rdf:type assertion to a SO class such as TF_binding_site, which is more specific than anything in biolink. Here we would have categories {bl:GenomicEntity, bl:MolecularEntity, bl:NamedThing}
    * range: [CategoryType](types/CategoryType.md)
    * in subsets: (translator_minimal)

### Mixed in from named thing:

 * [id](id.md)  <sub>REQ</sub>
    * Description: A unique identifier for a thing. Must be either a CURIE shorthand for a URI or a complete URI
    * range: [String](types/String.md)
    * in subsets: (translator_minimal)

### Mixed in from named thing:

 * [name](name.md)  <sub>REQ</sub>
    * Description: A human-readable name for a thing
    * range: [LabelType](types/LabelType.md)
    * in subsets: (translator_minimal)

## Other properties

|  |  |  |
| --- | --- | --- |
| **Mappings:** | | SIO:000614 |
| **In Subsets:** | | samples |


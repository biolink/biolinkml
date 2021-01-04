
# Type: material sample


A sample is a limited quantity of something (e.g. an individual or set of individuals from a population, or a portion of a substance) to be used for testing, analysis, inspection, investigation, demonstration, or trial use. [SIO]

URI: [biolink:MaterialSample](https://w3id.org/biolink/vocab/MaterialSample)


![img](http://yuml.me/diagram/nofunky;dir:TB/class/[SubjectOfInvestigation],[PhysicalEntity],[NamedThing],[MaterialSampleToThingAssociation],[MaterialSampleDerivationAssociation],[Attribute]<has%20attribute%200..*-%20[MaterialSample&#124;id(i):string;name(i):label_type;category(i):category_type%20%2B],[MaterialSampleDerivationAssociation]-%20subject%201..1>[MaterialSample],[MaterialSampleToThingAssociation]-%20subject%201..1>[MaterialSample],[MaterialSample]uses%20-.->[SubjectOfInvestigation],[MaterialSample]uses%20-.->[PhysicalEntity],[NamedThing]^-[MaterialSample],[Attribute])

## Parents

 *  is_a: [NamedThing](NamedThing.md) - a databased entity or concept/class

## Uses Mixins

 *  mixin: [SubjectOfInvestigation](SubjectOfInvestigation.md) - An entity that has the role of being studied in an investigation, study, or experiment
 *  mixin: [PhysicalEntity](PhysicalEntity.md) - An entity that has physical properties such as mass, volume, or charge

## Referenced by class

 *  **[MaterialSampleDerivationAssociation](MaterialSampleDerivationAssociation.md)** *[material sample derivation association➞subject](material_sample_derivation_association_subject.md)*  <sub>REQ</sub>  **[MaterialSample](MaterialSample.md)**
 *  **[MaterialSampleToThingAssociation](MaterialSampleToThingAssociation.md)** *[material sample to thing association➞subject](material_sample_to_thing_association_subject.md)*  <sub>REQ</sub>  **[MaterialSample](MaterialSample.md)**

## Attributes


### Own

 * [has attribute](has_attribute.md)  <sub>0..*</sub>
    * Description: connects any named thing to an attribute
    * range: [Attribute](Attribute.md)
    * in subsets: (samples)

### Inherited from named thing:

 * [category](category.md)  <sub>1..*</sub>
    * Description: Name of the high level ontology class in which this entity is categorized. Corresponds to the label for the biolink entity type class.
 * In a neo4j database this MAY correspond to the neo4j label tag.
 * In an RDF database it should be a biolink model class URI.
This field is multi-valued. It should include values for ancestors of the biolink class; for example, a protein such as Shh would have category values `bl:Protein`, `bl:GeneProduct`, `bl:MolecularEntity`, ...
In an RDF database, nodes will typically have an rdf:type triples. This can be to the most specific biolink class, or potentially to a class more specific than something in biolink. For example, a sequence feature `f` may have a rdf:type assertion to a SO class such as TF_binding_site, which is more specific than anything in biolink. Here we would have categories {bl:GenomicEntity, bl:MolecularEntity, bl:NamedThing}
    * range: [CategoryType](types/CategoryType.md)
    * in subsets: (translator_minimal)
 * [id](id.md)  <sub>REQ</sub>
    * Description: A unique identifier for a thing. Must be either a CURIE shorthand for a URI or a complete URI
    * range: [String](types/String.md)
    * in subsets: (translator_minimal)
 * [name](name.md)  <sub>REQ</sub>
    * Description: A human-readable name for a thing
    * range: [LabelType](types/LabelType.md)
    * in subsets: (translator_minimal)

## Other properties

|  |  |  |
| --- | --- | --- |
| **Aliases:** | | biospecimen |
|  | | sample |
|  | | biosample |
|  | | physical sample |
| **Mappings:** | | OBI:0000747 |
|  | | SIO:001050 |


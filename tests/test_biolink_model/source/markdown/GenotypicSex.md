
# Type: genotypic sex


An attribute corresponding to the genotypic sex of the individual, based upon genotypic composition of sex chromosomes.

URI: [biolink:GenotypicSex](https://w3id.org/biolink/vocab/GenotypicSex)


![img](http://yuml.me/diagram/nofunky;dir:TB/class/\[NamedThing]<has%20qualitative%20value(i)%200..1-%20\[GenotypicSex|id(i):identifier_type;name(i):label_type;category(i):iri_type%20%2B],%20\[QuantityValue]<has%20quantitative%20value(i)%200..*-++\[GenotypicSex],%20\[OntologyClass]<has%20attribute%20type(i)%200..1-%20\[GenotypicSex],%20\[BiologicalSex]^-\[GenotypicSex])

## Parents

 *  is_a: [biological sex](biological sex.md)

## Attributes


### Inherited from attribute:

 * [has attribute type](has_attribute_type.md)  <sub>OPT</sub>
    * Description: connects an attribute to a class that describes it
    * range: [ontology class](ontology class.md)
    * inherited from: [attribute](attribute.md)
    * in subsets: (samples)
 * [has quantitative value](has_quantitative_value.md)  <sub>0..*</sub>
    * Description: connects an attribute to a value
    * range: [quantity value](quantity value.md)
    * inherited from: [attribute](attribute.md)
    * in subsets: (samples)
 * [has qualitative value](has_qualitative_value.md)  <sub>OPT</sub>
    * Description: connects an attribute to a value
    * range: [named thing](named thing.md)
    * inherited from: [attribute](attribute.md)
    * in subsets: (samples)

### Inherited from named thing:

 * [id](id.md)  <sub>REQ</sub>
    * Description: A unique identifier for a thing. Must be either a CURIE shorthand for a URI or a complete URI
    * range: [IdentifierType](type/IdentifierType.md)
    * inherited from: [named thing](named thing.md)
    * in subsets: (translator_minimal)
 * [name](name.md)  <sub>REQ</sub>
    * Description: A human-readable name for a thing
    * range: [LabelType](type/LabelType.md)
    * inherited from: [named thing](named thing.md)
    * in subsets: (translator_minimal)
 * [category](category.md)  <sub>1..*</sub>
    * Description: Name of the high level ontology class in which this entity is categorized. Corresponds to the label for the biolink entity type class. In a neo4j database this MAY correspond to the neo4j label tag
    * range: [IriType](type/IriType.md)
    * inherited from: [named thing](named thing.md)
    * in subsets: (translator_minimal)

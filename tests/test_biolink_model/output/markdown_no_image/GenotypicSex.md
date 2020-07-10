
# Type: genotypic sex


An attribute corresponding to the genotypic sex of the individual, based upon genotypic composition of sex chromosomes.

URI: [biolink:GenotypicSex](https://w3id.org/biolink/vocab/GenotypicSex)


![img](http://yuml.me/diagram/nofunky;dir:TB/class/[QuantityValue],[OntologyClass],[NamedThing],[BiologicalSex]^-[GenotypicSex&#124;id(i):string;name(i):label_type;category(i):iri_type%20%2B],[BiologicalSex])

## Parents

 *  is_a: [BiologicalSex](BiologicalSex.md)

## Attributes


### Inherited from biological sex:

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

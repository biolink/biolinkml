
# Type: metabolite


Any intermediate or product resulting from metabolism. Includes primary and secondary metabolites.

URI: [biolink:Metabolite](https://w3id.org/biolink/vocab/Metabolite)


![img](http://yuml.me/diagram/nofunky;dir:TB/class/[OrganismTaxon],[ChemicalSubstance]^-[Metabolite&#124;id(i):string;name(i):label_type;category(i):iri_type%20%2B],[ChemicalSubstance])

## Parents

 *  is_a: [ChemicalSubstance](ChemicalSubstance.md) - May be a chemical entity or a formulation with a chemical entity as active ingredient, or a complex material with multiple chemical entities as part

## Attributes


### Inherited from chemical substance:

 * [category](category.md)  <sub>1..*</sub>
    * Description: Name of the high level ontology class in which this entity is categorized. Corresponds to the label for the biolink entity type class. In a neo4j database this MAY correspond to the neo4j label tag
    * range: [IriType](types/IriType.md)
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
| **Mappings:** | | CHEBI:25212 |
| **Comments:** | | The CHEBI ID represents a role rather than a substance |


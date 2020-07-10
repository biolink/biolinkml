
# Type: gene family


any grouping of multiple genes or gene products related by common descent

URI: [biolink:GeneFamily](https://w3id.org/biolink/vocab/GeneFamily)


![img](http://yuml.me/diagram/nofunky;dir:TB/class/[OrganismTaxon],[MolecularEntity],[GeneGrouping],[GeneFamily&#124;id(i):string;name(i):label_type;category(i):iri_type%20%2B]uses%20-.->[GeneGrouping],[MolecularEntity]^-[GeneFamily])

## Parents

 *  is_a: [MolecularEntity](MolecularEntity.md) - A gene, gene product, small molecule or macromolecule (including protein complex)

## Uses Mixins

 *  mixin: [GeneGrouping](GeneGrouping.md) - any grouping of multiple genes or gene products

## Attributes


### Inherited from molecular entity:

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
| **Mappings:** | | SIO:001380 |
|  | | NCIT:C20130 |
|  | | WD:Q417841 |


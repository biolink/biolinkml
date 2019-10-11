
# Type: gene product


The functional molecular product of a single gene. Gene products are either proteins or functional RNA molecules

URI: [biolink:GeneProduct](https://w3id.org/biolink/vocab/GeneProduct)


![img](http://yuml.me/diagram/nofunky;dir:TB/class/\[OrganismTaxon]<in%20taxon(i)%200..*-%20\[GeneProduct|name(i):symbol_type;id(i):identifier_type;category(i):iri_type%20%2B],%20\[GeneToGeneProductRelationship]-%20object%201..1>\[GeneProduct],%20\[GeneProduct]^-\[Protein],%20\[GeneProduct]^-\[GeneProductIsoform],%20\[GeneProduct]^-\[RNAProduct],%20\[GeneOrGeneProduct]^-\[GeneProduct])

## Parents

 *  is_a: [gene or gene product](gene or gene product.md) - a union of genes or gene products. Frequently an identifier for one will be used as proxy for another

## Children

 * [RNA product](RNA product.md)
 * [gene product isoform](gene product isoform.md) - This is an abstract class that can be mixed in with different kinds of gene products to indicate that the gene product is intended to represent a specific isoform rather than a canonical or reference or generic product. The designation of canonical or reference may be arbitrary, or it may represent the superclass of all isoforms.
 * [protein](protein.md) - A gene product that is composed of a chain of amino acid sequences and is produced by ribosome-mediated translation of mRNA

## Referenced by class

 *  **[gene to gene product relationship](gene to gene product relationship.md)** *[object](gene_to_gene_product_relationship_object.md)*  <sub>REQ</sub>  **[gene product](gene product.md)**
 *  **[gene](gene.md)** *[has gene product](has_gene_product.md)*  <sub>0..*</sub>  **[gene product](gene product.md)**

## Attributes


### Inherited from macromolecular machine:

 * [name](macromolecular_machine_name.md)  <sub>REQ</sub>
    * range: [SymbolType](type/SymbolType.md)
    * inherited from: [macromolecular machine](macromolecular machine.md)

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

### Inherited from thing with taxon:

 * [in taxon](in_taxon.md)  <sub>0..*</sub>
    * Description: connects a thing to a class representing a taxon
    * range: [organism taxon](organism taxon.md)
    * inherited from: [thing with taxon](thing with taxon.md)
    * in subsets: (translator_minimal)

## Other properties

|  |  |  |
| --- | --- | --- |
| **Mappings:** | | WD:Q424689 |


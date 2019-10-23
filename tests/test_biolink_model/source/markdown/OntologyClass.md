
# Type: ontology class


a concept or class in an ontology, vocabulary or thesaurus

URI: [biolink:OntologyClass](https://w3id.org/biolink/vocab/OntologyClass)


![img](http://yuml.me/diagram/nofunky;dir:TB/class/\[Association]-%20association%20type%200..1>\[OntologyClass|id(i):identifier_type;name(i):label_type;category(i):iri_type%20%2B],%20\[GeneToExpressionSiteAssociation]-%20quantifier%20qualifier%200..1>\[OntologyClass],%20\[Attribute]-%20has%20attribute%20type%200..1>\[OntologyClass],%20\[Association]-%20qualifiers%200..*>\[OntologyClass],%20\[Attribute]uses%20-.->\[OntologyClass],%20\[OntologyClass]^-\[RelationshipType],%20\[OntologyClass]^-\[OrganismTaxon],%20\[OntologyClass]^-\[GeneOntologyClass],%20\[NamedThing]^-\[OntologyClass])

## Parents

 *  is_a: [named thing](named thing.md) - a databased entity or concept/class

## Children

 * [gene ontology class](gene ontology class.md) - an ontology class that describes a functional aspect of a gene, gene prodoct or complex
 * [organism taxon](organism taxon.md)
 * [relationship type](relationship type.md) - An OWL property used as an edge label

## Mixin for

 * [attribute](attribute.md) (mixin)  - A property or characteristic of an entity. For example, an apple may have properties such as color, shape, age, crispiness. An environmental sample may have attributes such as depth, lat, long, material.

## Referenced by class

 *  **[association](association.md)** *[association type](association_type.md)*  <sub>OPT</sub>  **[ontology class](ontology class.md)**
 *  **[gene to expression site association](gene to expression site association.md)** *[gene to expression site association➞quantifier qualifier](gene_to_expression_site_association_quantifier_qualifier.md)*  <sub>OPT</sub>  **[ontology class](ontology class.md)**
 *  **[attribute](attribute.md)** *[has attribute type](has_attribute_type.md)*  <sub>OPT</sub>  **[ontology class](ontology class.md)**
 *  **[named thing](named thing.md)** *[has molecular consequence](has_molecular_consequence.md)*  <sub>0..*</sub>  **[ontology class](ontology class.md)**
 *  **[pairwise interaction association](pairwise interaction association.md)** *[interacting molecules category](interacting_molecules_category.md)*  <sub>OPT</sub>  **[ontology class](ontology class.md)**
 *  **[association](association.md)** *[qualifiers](qualifiers.md)*  <sub>0..*</sub>  **[ontology class](ontology class.md)**
 *  **[association](association.md)** *[quantifier qualifier](quantifier_qualifier.md)*  <sub>OPT</sub>  **[ontology class](ontology class.md)**

## Attributes


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

### Domain for slot:

 * [subclass of](subclass_of.md)  <sub>0..*</sub>
    * Description: holds between two classes where the domain class is a specialization of the range class
    * range: [IriType](type/IriType.md)
    * in subsets: (translator_minimal)

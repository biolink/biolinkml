
# Type: life stage


A stage of development or growth of an organism, including post-natal adult stages

URI: [biolink:LifeStage](https://w3id.org/biolink/vocab/LifeStage)


![img](http://yuml.me/diagram/nofunky;dir:TB/class/\[OrganismTaxon]<in%20taxon%200..*-%20\[LifeStage|id(i):identifier_type;name(i):label_type;category(i):iri_type%20%2B],%20\[GeneToExpressionSiteAssociation]-%20stage%20qualifier%200..1>\[LifeStage],%20\[LifeStage]uses%20-.->\[ThingWithTaxon],%20\[OrganismalEntity]^-\[LifeStage])

## Parents

 *  is_a: [organismal entity](organismal entity.md) - A named entity that is either a part of an organism, a whole organism, population or clade of organisms, excluding molecular entities

## Uses Mixins

 *  mixin: [thing with taxon](thing with taxon.md) - A mixin that can be used on any entity with a taxon

## Referenced by class

 *  **[gene to expression site association](gene to expression site association.md)** *[stage qualifier](gene_to_expression_site_association_stage_qualifier.md)*  <sub>OPT</sub>  **[life stage](life stage.md)**
 *  **[association](association.md)** *[stage qualifier](stage_qualifier.md)*  <sub>OPT</sub>  **[life stage](life stage.md)**

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

### Inherited from thing with taxon:

 * [in taxon](in_taxon.md)  <sub>0..*</sub>
    * Description: connects a thing to a class representing a taxon
    * range: [organism taxon](organism taxon.md)
    * in subsets: (translator_minimal)

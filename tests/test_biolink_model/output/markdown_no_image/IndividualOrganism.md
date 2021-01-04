
# Type: individual organism




URI: [biolink:IndividualOrganism](https://w3id.org/biolink/vocab/IndividualOrganism)


![img](http://yuml.me/diagram/nofunky;dir:TB/class/[ThingWithTaxon],[OrganismalEntity],[OrganismTaxon],[IndividualOrganism&#124;id(i):string;name(i):label_type;category(i):category_type%20%2B]uses%20-.->[ThingWithTaxon],[IndividualOrganism]^-[Case],[OrganismalEntity]^-[IndividualOrganism],[Case])

## Parents

 *  is_a: [OrganismalEntity](OrganismalEntity.md) - A named entity that is either a part of an organism, a whole organism, population or clade of organisms, excluding molecular entities

## Uses Mixins

 *  mixin: [ThingWithTaxon](ThingWithTaxon.md) - A mixin that can be used on any entity with a taxon

## Children

 * [Case](Case.md) - An individual organism that has a patient role in some clinical context.

## Referenced by class


## Attributes


### Inherited from organismal entity:

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

### Mixed in from thing with taxon:

 * [in taxon](in_taxon.md)  <sub>0..*</sub>
    * Description: connects a thing to a class representing a taxon
    * range: [OrganismTaxon](OrganismTaxon.md)
    * in subsets: (translator_minimal)

## Other properties

|  |  |  |
| --- | --- | --- |
| **Mappings:** | | SIO:010000 |
|  | | WIKIDATA:Q795052 |
|  | | UMLSSG:LIVB |
|  | | UMLSSC:T001 |
|  | | UMLSST:orgm |
|  | | UMLSSC:T002 |
|  | | UMLSST:plnt |
|  | | UMLSSC:T004 |
|  | | UMLSST:fngs |
|  | | UMLSSC:T005 |
|  | | UMLSST:virs |
|  | | UMLSSC:T007 |
|  | | UMLSST:bact |
|  | | UMLSSC:T008 |
|  | | UMLSST:anim |
|  | | UMLSSC:T010 |
|  | | UMLSST:vtbt |
|  | | UMLSSC:T011 |
|  | | UMLSST:amph |
|  | | UMLSSC:T012 |
|  | | UMLSST:bird |
|  | | UMLSSC:T013 |
|  | | UMLSST:fish |
|  | | UMLSSC:T014 |
|  | | UMLSST:rept |
|  | | UMLSSC:T015 |
|  | | UMLSST:mamm |
|  | | UMLSSC:T016 |
|  | | UMLSST:humn |
|  | | UMLSSC:T096 |
|  | | UMLSST:grup |
|  | | UMLSSC:T097 |
|  | | UMLSST:prog |
|  | | UMLSSC:T099 |
|  | | UMLSST:famg |
|  | | UMLSSC:T100 |
|  | | UMLSST:aggp |
|  | | UMLSSC:T101 |
|  | | UMLSST:podg |
|  | | UMLSSC:T194 |
|  | | UMLSST:arch |
|  | | UMLSSC:T204 |
|  | | UMLSST:euka |


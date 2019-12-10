
# Type: biological entity




URI: [biolink:BiologicalEntity](https://w3id.org/biolink/vocab/BiologicalEntity)


![img](http://yuml.me/diagram/nofunky;dir:TB/class/\[BiologicalEntity&#124;id(i):identifier_type;name(i):label_type;category(i):iri_type%20%2B]^-\[OrganismalEntity],%20\[BiologicalEntity]^-\[MolecularEntity],%20\[BiologicalEntity]^-\[ExposureEvent],%20\[BiologicalEntity]^-\[DiseaseOrPhenotypicFeature],%20\[BiologicalEntity]^-\[BiologicalProcessOrActivity],%20\[NamedThing]^-\[BiologicalEntity])

## Parents

 *  is_a: [named thing](named thing.md) - a databased entity or concept/class

## Children

 * [biological process or activity](biological process or activity.md) - Either an individual molecular activity, or a collection of causally connected molecular activities
 * [disease or phenotypic feature](disease or phenotypic feature.md) - Either one of a disease or an individual phenotypic feature. Some knowledge resources such as Monarch treat these as distinct, others such as MESH conflate.
 * [exposure event](exposure event.md) - A feature of the environment of an organism that influences one or more phenotypic features of that organism, potentially mediated by genes
 * [molecular entity](molecular entity.md) - A gene, gene product, small molecule or macromolecule (including protein complex)
 * [organismal entity](organismal entity.md) - A named entity that is either a part of an organism, a whole organism, population or clade of organisms, excluding molecular entities

## Referenced by class


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

 * [has phenotype](has_phenotype.md)  <sub>0..*</sub>
    * Description: holds between a biological entity and a phenotype, where a phenotype is construed broadly as any kind of quality of an organism part, a collection of these qualities, or a change in quality or qualities (e.g. abnormally increased temperature).
    * range: [phenotypic feature](phenotypic feature.md)
    * in subsets: (translator_minimal)

## Other properties

|  |  |  |
| --- | --- | --- |
| **Mappings:** | | WD:Q28845870 |
|  | | UMLSSC:T050 |
|  | | UMLSST:emod |


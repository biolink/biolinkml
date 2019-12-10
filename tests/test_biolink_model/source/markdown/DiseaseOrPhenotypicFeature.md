
# Type: disease or phenotypic feature


Either one of a disease or an individual phenotypic feature. Some knowledge resources such as Monarch treat these as distinct, others such as MESH conflate.

URI: [biolink:DiseaseOrPhenotypicFeature](https://w3id.org/biolink/vocab/DiseaseOrPhenotypicFeature)


![img](http://yuml.me/diagram/nofunky;dir:TB/class/\[OrganismTaxon]<in%20taxon%200..*-%20\[DiseaseOrPhenotypicFeature&#124;id(i):identifier_type;name(i):label_type;category(i):iri_type%20%2B],%20\[CellLineToDiseaseOrPhenotypicFeatureAssociation]-%20subject%201..1>\[DiseaseOrPhenotypicFeature],%20\[ChemicalToDiseaseOrPhenotypicFeatureAssociation]-%20object%201..1>\[DiseaseOrPhenotypicFeature],%20\[DiseaseOrPhenotypicFeatureAssociationToThingAssociation]-%20subject%201..1>\[DiseaseOrPhenotypicFeature],%20\[ThingToDiseaseOrPhenotypicFeatureAssociation]-%20object%201..1>\[DiseaseOrPhenotypicFeature],%20\[DiseaseOrPhenotypicFeature]uses%20-.->\[ThingWithTaxon],%20\[DiseaseOrPhenotypicFeature]^-\[PhenotypicFeature],%20\[DiseaseOrPhenotypicFeature]^-\[Disease],%20\[BiologicalEntity]^-\[DiseaseOrPhenotypicFeature])

## Parents

 *  is_a: [biological entity](biological entity.md)

## Uses Mixins

 *  mixin: [thing with taxon](thing with taxon.md) - A mixin that can be used on any entity with a taxon

## Children

 * [disease](disease.md)
 * [phenotypic feature](phenotypic feature.md)

## Referenced by class

 *  **[molecular entity](molecular entity.md)** *[biomarker for](biomarker_for.md)*  <sub>0..*</sub>  **[disease or phenotypic feature](disease or phenotypic feature.md)**
 *  **[cell line to disease or phenotypic feature association](cell line to disease or phenotypic feature association.md)** *[cell line to disease or phenotypic feature association➞subject](cell_line_to_disease_or_phenotypic_feature_association_subject.md)*  <sub>REQ</sub>  **[disease or phenotypic feature](disease or phenotypic feature.md)**
 *  **[chemical to disease or phenotypic feature association](chemical to disease or phenotypic feature association.md)** *[chemical to disease or phenotypic feature association➞object](chemical_to_disease_or_phenotypic_feature_association_object.md)*  <sub>REQ</sub>  **[disease or phenotypic feature](disease or phenotypic feature.md)**
 *  **[disease or phenotypic feature association to thing association](disease or phenotypic feature association to thing association.md)** *[disease or phenotypic feature association to thing association➞subject](disease_or_phenotypic_feature_association_to_thing_association_subject.md)*  <sub>REQ</sub>  **[disease or phenotypic feature](disease or phenotypic feature.md)**
 *  **[gene](gene.md)** *[gene associated with condition](gene_associated_with_condition.md)*  <sub>0..*</sub>  **[disease or phenotypic feature](disease or phenotypic feature.md)**
 *  **[thing to disease or phenotypic feature association](thing to disease or phenotypic feature association.md)** *[thing to disease or phenotypic feature association➞object](thing_to_disease_or_phenotypic_feature_association_object.md)*  <sub>REQ</sub>  **[disease or phenotypic feature](disease or phenotypic feature.md)**
 *  **[treatment](treatment.md)** *[treats](treats.md)*  <sub>1..*</sub>  **[disease or phenotypic feature](disease or phenotypic feature.md)**

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

### Domain for slot:

 * [correlated with](correlated_with.md)  <sub>0..*</sub>
    * Description: holds between a disease or phenotypic feature and a measurable molecular entity that is used as an indicator of the presence or state of the disease or feature.
    * range: [molecular entity](molecular entity.md)
    * in subsets: (translator_minimal)
 * [has biomarker](has_biomarker.md)  <sub>0..*</sub>
    * Description: holds between a disease or phenotypic feature and a measurable molecular entity that is used as an indicator of the presence or state of the disease or feature.
    * range: [molecular entity](molecular entity.md)
    * in subsets: (translator_minimal)
 * [treated by](treated_by.md)  <sub>0..*</sub>
    * Description: holds between a disease or phenotypic feature and a therapeutic process or chemical substance that is used to treat the condition
    * range: [named thing](named thing.md)
    * in subsets: (translator_minimal)

## Other properties

|  |  |  |
| --- | --- | --- |
| **Aliases:** | | phenome |
| **Mappings:** | | UMLSSC:T033 |
|  | | UMLSST:fndg |


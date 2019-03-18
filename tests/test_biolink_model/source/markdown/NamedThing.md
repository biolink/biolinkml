# Class: named thing


a databased entity or concept/class

URI: [https://biolink.github.io/biolink-model/ontology/biolink.ttl/NamedThing](https://biolink.github.io/biolink-model/ontology/biolink.ttl/NamedThing)

![img](http://yuml.me/diagram/nofunky;dir:TB/class/\[NamedThing]<interacts%20with%200..*-%20\[NamedThing|id:identifier_type;name:label_type%20%3F;category:iri_type%20*;node_property:string%20%3F;iri:iri_type%20%3F;synonym:label_type%20*;full_name:label_type%20%3F;description:narrative_text%20%3F;systematic_synonym:label_type%20%3F],%20\[NamedThing]<related%20to%200..*-%20\[NamedThing],%20\[NamedThing]^-\[PlanetaryEntity],%20\[NamedThing]^-\[OntologyClass],%20\[NamedThing]^-\[Occurrent],%20\[NamedThing]^-\[InformationContentEntity],%20\[NamedThing]^-\[Device],%20\[NamedThing]^-\[ClinicalEntity],%20\[NamedThing]^-\[BiologicalEntity],%20\[NamedThing]^-\[AdministrativeEntity])
## Inheritance

## Children

 * [AdministrativeEntity](AdministrativeEntity.md)
 * [BiologicalEntity](BiologicalEntity.md)
 * [ClinicalEntity](ClinicalEntity.md) - Any entity or process that exists in the clinical domain and outside the biological realm. Diseases are placed under biological entities
 * [Device](Device.md) - A thing made or adapted for a particular purpose, especially a piece of mechanical or electronic equipment
 * [InformationContentEntity](InformationContentEntity.md) - a piece of information that typically describes some piece of biology or is used as support.
 * [Occurrent](Occurrent.md) - A processual entity
 * [OntologyClass](OntologyClass.md) - a concept or class in an ontology, vocabulary or thesaurus
 * [PlanetaryEntity](PlanetaryEntity.md) - Any entity or process that exists at the level of the whole planet
## Used by

 *  **[NamedThing](NamedThing.md)** *[filler](filler.md)*  <sub>OPT</sub>  **[NamedThing](NamedThing.md)**
 *  **[NamedThing](NamedThing.md)** *[interacts with](interacts_with.md)*  <sub>0..*</sub>  **[NamedThing](NamedThing.md)**
 *  **[NamedThing](NamedThing.md)** *[related to](related_to.md)*  <sub>0..*</sub>  **[NamedThing](NamedThing.md)**
## Fields

 * [category](category.md)  <sub>0..*</sub>
    * Description: Name of the high level ontology class in which this entity is categorized. Corresponds to the label for the biolink entity type class. In a neo4j database this MAY correspond to the neo4j label tag
    * range: [IriType](IriType.md)
    * in subsets: (translator_minimal)
 * [description](description.md)  <sub>OPT</sub>
    * Description: a human-readable description of a thing
    * range: [NarrativeText](NarrativeText.md)
    * in subsets: (translator_minimal)
 * [full name](full_name.md)  <sub>OPT</sub>
    * Description: a long-form human readable name for a thing
    * range: [LabelType](LabelType.md)
 * [id](id.md)  <sub>REQ</sub>
    * Description: A unique identifier for a thing. Must be either a CURIE shorthand for a URI or a complete URI
    * range: [IdentifierType](IdentifierType.md)
    * in subsets: (translator_minimal)
 * [interacts with](interacts_with.md)  <sub>0..*</sub>
    * Description: holds between any two entities that directly or indirectly interact with each other
    * range: [NamedThing](NamedThing.md)
    * in subsets: (translator_minimal)
 * [iri](iri.md)  <sub>OPT</sub>
    * Description: An IRI for the node. This is determined by the id using expansion rules.
    * range: [IriType](IriType.md)
    * in subsets: (translator_minimal)
 * [name](name.md)  <sub>OPT</sub>
    * Description: A human-readable name for a thing
    * range: [LabelType](LabelType.md)
    * in subsets: (translator_minimal)
 * [node property](node_property.md)  <sub>OPT</sub>
    * Description: A grouping for any property that holds between a node and a value
    * range: [String](String.md)
 * [related to](related_to.md)  <sub>0..*</sub>
    * Description: A relationship that is asserted between two named things
    * range: [NamedThing](NamedThing.md)
 * [synonym](synonym.md)  <sub>0..*</sub>
    * Description: Alternate human-readable names for a thing
    * range: [LabelType](LabelType.md)
    * in subsets: (translator_minimal)
 * [systematic synonym](systematic_synonym.md)  <sub>OPT</sub>
    * Description: more commonly used for gene symbols in yeast
    * range: [LabelType](LabelType.md)

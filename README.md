[![Build Status](https://travis-ci.org/biolink/biolinkml.svg?branch=master)](https://travis-ci.org/biolink/biolinkml)
[![DOI](https://zenodo.org/badge/112995625.svg)](https://zenodo.org/badge/latestdoi/112995625)

# biolinkml - biolink modeling language

Quickstart docs:

 * Browse the model: [https://biolink.github.io/biolinkml](https://biolink.github.io/biolikml)
    * [class definition](docs/ClassDefinition.html) Class definitions
    * [slot definition](docs/SlotDefinition.html) Class properties
    * [type definition](docs/TypeDefinition.html) Data types
    * [schema ddefinition](docs/SchemaDefinition.html) Schema definition



## Installation
```bash
> pipenv install biolinkml
```

## Examples
See: 

Conversion/validation code: https://github.com/NCATS-Tangerine/kgx

Protege view:
![img](images/protege-entities.png)


### Property and Edge Types

 * [predicates](docs#slots)

We divide these into *relationship types* which connect two nodes together, and *node or edge properties*


### Association Hierarchy

 * [association](docs/Association.html) (root class for association types)

## Identifiers

See [biolink json-ld context](context.jsonld)

## Mapping to specific database and modeling platforms

### Neo4J Mapping

See [mapping to neo4j](https://biolink.github.io/biolink-model/about/mapping-neo4j.html)

### RDF Mapping

See [mapping to neo4j](https://biolink.github.io/biolink-model/about/mapping-rdf.html)




## Metamodel

See [metamodel](metamodel) for details of the metamodel.

## Usage in existing projects

### Case study: gene expression in Monarch

Currently this is documented in the [ingest
artefacts](https://github.com/monarch-initiative/ingest-artifacts/tree/master/sources)
repo, using non-computable cmap images:

![bgee model](https://raw.githubusercontent.com/monarch-initiative/ingest-artifacts/master/sources/BGee/Bgee_20170112.jpg)

And also by the [gene-anatomy cypher query](https://github.com/monarch-initiative/monarch-cypher-queries/blob/master/src/main/cypher/golr-loader/gene-anatomy.yaml)
which maps graphs conforming to the pattern to denormalized tuples for indexing in solr

in the biolink model this is explicitly represented using the `gene to expression site association` class definition [in the model](biolink-model.yaml)

```yaml
  - name: gene to expression site association
    is_a: association
    description: >-
      An association between a gene and an expression site, possibly qualified by stage/timing info
    see_also: "https://github.com/monarch-initiative/ingest-artifacts/tree/master/sources/BGee"
    slot_usage:
      - slot: subject
        type: gene or gene product
        description: "gene in which variation is correlated with the phenotypic feature"
      - slot: object
        type: anatomical entity
        description: "location in which the gene is expressed"
        subclass_of: UBERON:0001062
        examples:
          - value: UBERON:0002037
            description: cerebellum
      - slot: relation
        description: "expression relationship"
        subproperty_of: "RO:0002206"
      - slot: stage
        type: developmental stage
        description: "stage at which the gene is expressed in the site"
        examples:
          - value: UBERON:0000069
            description: larval stage
      - slot: quantifier
        description: >-
          can be used to indicate magnitude, or also ranking
```

This is used to generate various artefacts such as

 - [golr view definition](monarch/golr-views/gene_to_expression_site_association-config.yaml)
    - (which is itself later compiled to solr xml using the bbop-golr framework)
 - [java class](monarch/java-gen/GeneToExpressionSiteAssociation.java)
    - generated from json-schema, so inheritance is unfolded
    - in future we may generate directly

Auto-generated image:

![img](../graphviz/GeneToExpressionSiteAssociation.png)

```graphql
type GeneToExpressionSiteAssociation {
  qualifiers: [String]
  stageQualifier: LifeStage
  objectExtensions: [PropertyValuePair]
  hasEvidence: String
  publications: [Publication]
  object: AnatomicalEntity!
  hasEvidenceType: EvidenceType
  hasEvidenceGraph: String
  providedBy: Provider
  label: String
  relation: String!
  negated: String
  subject: GeneOrGeneProduct!
  id: String!
  quantifierQualifier: String
  associationType: String
  subjectExtensions: [PropertyValuePair]
}
```

snippet of [generated json-schema](../json-schema)

```json
        "GeneToExpressionSiteAssociation": {
            "description": "An association between a gene and an expression site, possibly qualified by stage/timing info. TBD: introduce subclasses for distinction between wild-type and experimental conditions?",
            "properties": {
                "association_type": {
                    "description": "connects an association to the type of association (e.g. gene to phenotype)",
                    "type": "string"
                },
                "has_evidence": {
                    "description": "connects an association to an instance of supporting evidence",
                    "type": "string"
                },
                "has_evidence_graph": {
                    "description": "connects an association to a graph object including a path from subject to object",
                    "type": "string"
                },
                "has_evidence_type": {
                    "description": "connects an association to the class of evidence used",
                    "type": "string"
                },
                "id": {
                    "type": "string"
                },
                "label": {
                    "description": "A human-readable name for a thing",
                    "type": "string"
                },
                "negated": {
                    "description": "if set to true, then the association is negated i.e. is not true",
                    "type": "string"
                },
                "object": {
                    "description": "connects an association to the object of the association. For example, in a gene-to-phenotype association, the gene is subject and phenotype is object.",
                    "type": "string"
                },
                "object_extensions": {
                    "description": "Additional relationships that are true of the object in the context of the association. For example, if the object is an anatomical term in an expression association, the object extensions may include part-of links",
                    "items": {
                        "type": "string"
                    },
                    "type": "array"
                },
                "provided_by": {
                    "description": "connects an association to the agent (person, organization or group) that provided it",
                    "type": "string"
                },
                "publications": {
                    "description": "connects an association to publications supporting the association",
                    "items": {
                        "type": "string"
                    },
                    "type": "array"
                },
                "qualifiers": {
                    "description": "connects an association to qualifiers that modify or qualify the meaning of that association",
                    "items": {
                        "type": "string"
                    },
                    "type": "array"
                },
                "quantifier_qualifier": {
                    "description": "A measurable quantity for the object of the association",
                    "type": "string"
                },
                "relation": {
                    "description": "the relationship type by which a subject is connected to an object in an association",
                    "type": "string"
                },
                "stage_qualifier": {
                    "description": "stage at which expression takes place",
                    "type": "string"
                },
                "subject": {
                    "description": "connects an association to the subject of the association. For example, in a gene-to-phenotype association, the gene is subject and phenotype is object.",
                    "type": "string"
                },
                "subject_extensions": {
                    "description": "Additional relationships that are true of the subject in the context of the association. For example, if the subject is a gene product in a functional association, the subject extensions may represent  an isoform or a specific post-translational state",
                    "items": {
                        "type": "string"
                    },
                    "type": "array"
                }
            },
            "required": [],
            "title": "GeneToExpressionSiteAssociation",
            "type": "object"
        },
```

## FAQ

### Why not use X as the modeling framework?

Why invent our own yaml and not use JSON-Schema, SQL, UML, ProtoBuf,
OWL, ...

each of these is tied to a particular formalisms. E.g. JSON-Schema to
trees. OWL to open world logic. There are various impedance mismatches
in converting between these. The goal was to develop something simple
and more general that is not tied to any one serialization format or
set of assumptions.

There are other projects with similar goals, e.g
https://github.com/common-workflow-language/schema_salad

It may be possible to align with these.

### Why not use X as the datamodel

Here X may be bioschemas, some upper ontology (BioTop), UMLS
metathesaurus, bio*, various other attempts to model all of biology in
an object model.

Currently as far as we know there is no existing reference datamodel
that is flexible enough to be used here.


### Make and build instructions
Note: the make file requires jsonschema2pojo -- see https://github.com/joelittlejohn/jsonschema2pojo.  If you
are on a Mac, it can be installed using `brew`.

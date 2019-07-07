# Auto generated from .yaml by pythongen.py version:
# Generation date:
# Schema: biolink_model
#
# id: https://w3id.org/biolink/biolink-model
# description: Entity and association taxonomy and datamodel for life-sciences data
# license: https://creativecommons.org/publicdomain/zero/1.0/

from typing import Optional, List, Union, Dict, ClassVar
from dataclasses import dataclass
from biolinkml.utils.metamodelcore import empty_list, empty_dict, bnode
from biolinkml.utils.yamlutils import YAMLRoot
from biolinkml.utils.formatutils import camelcase, underscore, sfx
from rdflib import Namespace
from biolinkml.utils.metamodelcore import Bool, ElementIdentifier, URIorCURIE, XSDDate, XSDTime
from includes.types import Boolean, Date, Double, Float, Integer, String, Time, Uriorcurie

metamodel_version = "1.4.0"


# Namespaces
BFO = Namespace('http://purl.obolibrary.org/obo/BFO_')
BIOGRID = Namespace('http://thebiogrid.org/')
CHEBI = Namespace('http://purl.obolibrary.org/obo/CHEBI_')
CHEMBL_COMPOUND = Namespace('http://identifiers.org/chembl.compound/')
CHEMBL_TARGET = Namespace('http://identifiers.org/chembl.target/')
CIO = Namespace('http://purl.obolibrary.org/obo/CIO_')
CIVIC = Namespace('http://example.org/UNKNOWN/CIViC/')
CL = Namespace('http://purl.obolibrary.org/obo/CL_')
CLO = Namespace('http://purl.obolibrary.org/obo/CLO_')
CLINVAR = Namespace('http://www.ncbi.nlm.nih.gov/clinvar/')
ECO = Namespace('http://purl.obolibrary.org/obo/ECO_')
ECTO = Namespace('http://example.org/UNKNOWN/ECTO/')
ENSEMBL = Namespace('http://ensembl.org/id/')
FAO = Namespace('http://purl.obolibrary.org/obo/FAO_')
GENO = Namespace('http://purl.obolibrary.org/obo/GENO_')
GO = Namespace('http://purl.obolibrary.org/obo/GO_')
HANCESTRO = Namespace('http://example.org/UNKNOWN/HANCESTRO/')
HGNC = Namespace('http://www.genenames.org/cgi-bin/gene_symbol_report?hgnc_id=')
HP = Namespace('http://purl.obolibrary.org/obo/HP_')
IAO = Namespace('http://purl.obolibrary.org/obo/IAO_')
INTACT = Namespace('http://example.org/UNKNOWN/IntAct/')
MGI = Namespace('http://www.informatics.jax.org/accession/MGI:')
MIR = Namespace('http://identifiers.org/mir/')
MONDO = Namespace('http://purl.obolibrary.org/obo/MONDO_')
NCBIGENE = Namespace('http://www.ncbi.nlm.nih.gov/gene/')
NCIT = Namespace('http://purl.obolibrary.org/obo/NCIT_')
OBAN = Namespace('http://purl.org/oban/')
OGMS = Namespace('http://purl.obolibrary.org/obo/OGMS_')
OIO = Namespace('http://www.geneontology.org/formats/oboInOwl#')
PANTHER = Namespace('http://www.pantherdb.org/panther/family.do?clsAccession=')
PMID = Namespace('http://www.ncbi.nlm.nih.gov/pubmed/')
PO = Namespace('http://purl.obolibrary.org/obo/PO_')
PR = Namespace('http://purl.obolibrary.org/obo/PR_')
PW = Namespace('http://purl.obolibrary.org/obo/PW_')
POMBASE = Namespace('https://www.pombase.org/spombe/result/')
RNACENTRAL = Namespace('http://example.org/UNKNOWN/RNAcentral/')
RO = Namespace('http://purl.obolibrary.org/obo/RO_')
REACTOME = Namespace('http://example.org/UNKNOWN/Reactome/')
SEMMEDDB = Namespace('http://example.org/UNKNOWN/SEMMEDDB/')
SGD = Namespace('https://www.yeastgenome.org/locus/')
SIO = Namespace('http://semanticscience.org/resource/SIO_')
SO = Namespace('http://purl.obolibrary.org/obo/SO_')
UBERON = Namespace('http://purl.obolibrary.org/obo/UBERON_')
UMLSSC = Namespace('https://uts-ws.nlm.nih.gov/rest/semantic-network/semantic-network/current/TUI/')
UMLSSG = Namespace('https://uts-ws.nlm.nih.gov/rest/semantic-network/semantic-network/current/GROUP/')
UMLSST = Namespace('https://uts-ws.nlm.nih.gov/rest/semantic-network/semantic-network/current/STY/')
UPHENO = Namespace('http://purl.obolibrary.org/obo/UPHENO_')
UNIPROTKB = Namespace('http://identifiers.org/uniprot/')
VMC = Namespace('http://example.org/UNKNOWN/VMC/')
WB = Namespace('http://identifiers.org/wb/')
WD = Namespace('http://example.org/UNKNOWN/WD/')
ZFIN = Namespace('http://zfin.org/')
BIOLINK = Namespace('https://w3id.org/biolink/vocab/')
DCTERMS = Namespace('http://purl.org/dc/terms/')
DICTYBASE = Namespace('http://dictybase.org/gene/')
FALDO = Namespace('http://biohackathon.org/resource/faldo#')
OBAN = Namespace('http://example.org/UNKNOWN/oban/')
OWL = Namespace('http://www.w3.org/2002/07/owl#')
PAV = Namespace('http://purl.org/pav/')
RDF = Namespace('http://www.w3.org/1999/02/22-rdf-syntax-ns#')
RDFS = Namespace('http://www.w3.org/2000/01/rdf-schema#')
SKOS = Namespace('https://www.w3.org/TR/skos-reference/#')
WGS = Namespace('http://www.w3.org/2003/01/geo/wgs84_pos')
XSD = Namespace('http://www.w3.org/2001/XMLSchema#')
DEFAULT_ = BIOLINK


# Types
class ChemicalFormulaValue(str):
    """ A chemical formula """
    pass


class IdentifierType(ElementIdentifier):
    """ A string that is intended to uniquely identify a thing May be URI in full or compact (CURIE) form """
    pass


class IriType(Uriorcurie):
    """ An IRI """
    pass


class LabelType(String):
    """ A string that provides a human-readable name for a thing """
    pass


class NarrativeText(String):
    """ A string that provides a human-readable description of something """
    pass


class SymbolType(String):
    pass


class Frequency(String):
    pass


class PerecentageFrequencyValue(Double):
    pass


class Quotient(Double):
    pass


class Unit(String):
    pass


class TimeType(Time):
    pass


class BiologicalSequence(String):
    pass


# Class references
class AttributeId(ElementIdentifier):
    pass


class BiologicalSexId(AttributeId):
    pass


class PhenotypicSexId(BiologicalSexId):
    pass


class GenotypicSexId(BiologicalSexId):
    pass


class SeverityValueId(AttributeId):
    pass


class FrequencyValueId(AttributeId):
    pass


class ClinicalModifierId(AttributeId):
    pass


class OnsetId(AttributeId):
    pass


class NamedThingId(ElementIdentifier):
    pass


class BiologicalEntityId(NamedThingId):
    pass


class OntologyClassId(NamedThingId):
    pass


class RelationshipTypeId(OntologyClassId):
    pass


class GeneOntologyClassId(OntologyClassId):
    pass


class OrganismTaxonId(OntologyClassId):
    pass


class OrganismalEntityId(BiologicalEntityId):
    pass


class IndividualOrganismId(OrganismalEntityId):
    pass


class CaseId(IndividualOrganismId):
    pass


class PopulationOfIndividualOrganismsId(OrganismalEntityId):
    pass


class BiosampleId(OrganismalEntityId):
    pass


class DiseaseOrPhenotypicFeatureId(BiologicalEntityId):
    pass


class DiseaseId(DiseaseOrPhenotypicFeatureId):
    pass


class PhenotypicFeatureId(DiseaseOrPhenotypicFeatureId):
    pass


class EnvironmentId(BiologicalEntityId):
    pass


class InformationContentEntityId(NamedThingId):
    pass


class ConfidenceLevelId(InformationContentEntityId):
    pass


class EvidenceTypeId(InformationContentEntityId):
    pass


class PublicationId(InformationContentEntityId):
    pass


class AdministrativeEntityId(NamedThingId):
    pass


class ProviderId(AdministrativeEntityId):
    pass


class MolecularEntityId(BiologicalEntityId):
    pass


class ChemicalSubstanceId(MolecularEntityId):
    pass


class CarbohydrateId(ChemicalSubstanceId):
    pass


class DrugId(ChemicalSubstanceId):
    pass


class MetaboliteId(ChemicalSubstanceId):
    pass


class AnatomicalEntityId(OrganismalEntityId):
    pass


class LifeStageId(OrganismalEntityId):
    pass


class PlanetaryEntityId(NamedThingId):
    pass


class EnvironmentalProcessId(PlanetaryEntityId):
    pass


class EnvironmentalFeatureId(PlanetaryEntityId):
    pass


class ClinicalEntityId(NamedThingId):
    pass


class ClinicalTrialId(ClinicalEntityId):
    pass


class ClinicalInterventionId(ClinicalEntityId):
    pass


class DeviceId(NamedThingId):
    pass


class GenomicEntityId(MolecularEntityId):
    pass


class GenomeId(GenomicEntityId):
    pass


class TranscriptId(GenomicEntityId):
    pass


class ExonId(GenomicEntityId):
    pass


class CodingSequenceId(GenomicEntityId):
    pass


class MacromolecularMachineId(GenomicEntityId):
    pass


class GeneOrGeneProductId(MacromolecularMachineId):
    pass


class GeneId(GeneOrGeneProductId):
    pass


class GeneProductId(GeneOrGeneProductId):
    pass


class ProteinId(GeneProductId):
    pass


class GeneProductIsoformId(GeneProductId):
    pass


class ProteinIsoformId(ProteinId):
    pass


class RNAProductId(GeneProductId):
    pass


class RNAProductIsoformId(RNAProductId):
    pass


class NoncodingRNAProductId(RNAProductId):
    pass


class MicroRNAId(NoncodingRNAProductId):
    pass


class MacromolecularComplexId(MacromolecularMachineId):
    pass


class GeneFamilyId(MolecularEntityId):
    pass


class ZygosityId(AttributeId):
    pass


class GenotypeId(GenomicEntityId):
    pass


class HaplotypeId(GenomicEntityId):
    pass


class SequenceVariantId(GenomicEntityId):
    pass


class DrugExposureId(EnvironmentId):
    pass


class TreatmentId(EnvironmentId):
    pass


class GeographicLocationId(PlanetaryEntityId):
    pass


class GeographicLocationAtTimeId(GeographicLocationId):
    pass


class AssociationId(ElementIdentifier):
    pass


class GenotypeToGenotypePartAssociationId(AssociationId):
    pass


class GenotypeToGeneAssociationId(AssociationId):
    pass


class GenotypeToVariantAssociationId(AssociationId):
    pass


class GeneToGeneAssociationId(AssociationId):
    pass


class GeneToGeneHomologyAssociationId(GeneToGeneAssociationId):
    pass


class PairwiseInteractionAssociationId(AssociationId):
    pass


class PairwiseGeneToGeneInteractionId(GeneToGeneAssociationId):
    pass


class CellLineToThingAssociationId(AssociationId):
    pass


class CellLineToDiseaseOrPhenotypicFeatureAssociationId(AssociationId):
    pass


class ChemicalToThingAssociationId(AssociationId):
    pass


class CaseToThingAssociationId(AssociationId):
    pass


class ChemicalToDiseaseOrPhenotypicFeatureAssociationId(AssociationId):
    pass


class ChemicalToPathwayAssociationId(AssociationId):
    pass


class ChemicalToGeneAssociationId(AssociationId):
    pass


class BiosampleToThingAssociationId(AssociationId):
    pass


class BiosampleToDiseaseOrPhenotypicFeatureAssociationId(AssociationId):
    pass


class EntityToPhenotypicFeatureAssociationId(AssociationId):
    pass


class DiseaseOrPhenotypicFeatureAssociationToThingAssociationId(AssociationId):
    pass


class DiseaseOrPhenotypicFeatureAssociationToLocationAssociationId(DiseaseOrPhenotypicFeatureAssociationToThingAssociationId):
    pass


class ThingToDiseaseOrPhenotypicFeatureAssociationId(AssociationId):
    pass


class DiseaseToThingAssociationId(AssociationId):
    pass


class GenotypeToPhenotypicFeatureAssociationId(AssociationId):
    pass


class EnvironmentToPhenotypicFeatureAssociationId(AssociationId):
    pass


class DiseaseToPhenotypicFeatureAssociationId(AssociationId):
    pass


class CaseToPhenotypicFeatureAssociationId(AssociationId):
    pass


class GeneToThingAssociationId(AssociationId):
    pass


class VariantToThingAssociationId(AssociationId):
    pass


class GeneToPhenotypicFeatureAssociationId(AssociationId):
    pass


class GeneToDiseaseAssociationId(AssociationId):
    pass


class VariantToPopulationAssociationId(AssociationId):
    pass


class PopulationToPopulationAssociationId(AssociationId):
    pass


class VariantToPhenotypicFeatureAssociationId(AssociationId):
    pass


class VariantToDiseaseAssociationId(AssociationId):
    pass


class GeneAsAModelOfDiseaseAssociationId(GeneToDiseaseAssociationId):
    pass


class GeneHasVariantThatContributesToDiseaseAssociationId(GeneToDiseaseAssociationId):
    pass


class GenotypeToThingAssociationId(AssociationId):
    pass


class GeneToExpressionSiteAssociationId(AssociationId):
    pass


class SequenceVariantModulatesTreatmentAssociationId(AssociationId):
    pass


class FunctionalAssociationId(AssociationId):
    pass


class MacromolecularMachineToMolecularActivityAssociationId(FunctionalAssociationId):
    pass


class MacromolecularMachineToBiologicalProcessAssociationId(FunctionalAssociationId):
    pass


class MacromolecularMachineToCellularComponentAssociationId(FunctionalAssociationId):
    pass


class GeneToGoTermAssociationId(FunctionalAssociationId):
    pass


class GenomicSequenceLocalizationId(AssociationId):
    pass


class SequenceFeatureRelationshipId(AssociationId):
    pass


class TranscriptToGeneRelationshipId(SequenceFeatureRelationshipId):
    pass


class GeneToGeneProductRelationshipId(SequenceFeatureRelationshipId):
    pass


class ExonToTranscriptRelationshipId(SequenceFeatureRelationshipId):
    pass


class GeneRegulatoryRelationshipId(AssociationId):
    pass


class AnatomicalEntityToAnatomicalEntityAssociationId(AssociationId):
    pass


class AnatomicalEntityToAnatomicalEntityPartOfAssociationId(AnatomicalEntityToAnatomicalEntityAssociationId):
    pass


class AnatomicalEntityToAnatomicalEntityOntogenicAssociationId(AnatomicalEntityToAnatomicalEntityAssociationId):
    pass


class OccurrentId(NamedThingId):
    pass


class BiologicalProcessOrActivityId(BiologicalEntityId):
    pass


class MolecularActivityId(BiologicalProcessOrActivityId):
    pass


class ActivityAndBehaviorId(OccurrentId):
    pass


class ProcedureId(OccurrentId):
    pass


class PhenomenonId(OccurrentId):
    pass


class BiologicalProcessId(BiologicalProcessOrActivityId):
    pass


class PathwayId(BiologicalProcessId):
    pass


class PhysiologicalProcessId(BiologicalProcessId):
    pass


class CellularComponentId(AnatomicalEntityId):
    pass


class CellId(AnatomicalEntityId):
    pass


class CellLineId(BiosampleId):
    pass


class GrossAnatomicalStructureId(AnatomicalEntityId):
    pass


@dataclass
class Attribute(YAMLRoot):
    """
    A property or characteristic of an entity
    """
    _inherited_slots: ClassVar[List[str]] = ["related_to", "interacts_with", "subclass_of"]

    type_uri: ClassVar[str] = "https://w3id.org/biolink/vocab/Attribute"
    type_curie: ClassVar[str] = "biolink:Attribute"
    type_name: ClassVar[str] = "attribute"

    id: Union[ElementIdentifier, AttributeId]
    name: Union[str, LabelType]
    category: List[Union[str, IriType]] = empty_list()

    def __post_init__(self):
        if not isinstance(self.id, AttributeId):
            self.id = AttributeId(self.id)
        super().__post_init__()


@dataclass
class BiologicalSex(Attribute):
    _inherited_slots: ClassVar[List[str]] = ["related_to", "interacts_with", "subclass_of"]

    type_uri: ClassVar[str] = "https://w3id.org/biolink/vocab/BiologicalSex"
    type_curie: ClassVar[str] = "biolink:BiologicalSex"
    type_name: ClassVar[str] = "biological sex"

    id: Union[ElementIdentifier, BiologicalSexId] = None
    name: Union[str, LabelType] = None
    category: List[Union[str, IriType]] = empty_list()

    def __post_init__(self):
        if self.id is not None and not isinstance(self.id, BiologicalSexId):
            self.id = BiologicalSexId(self.id)
        super().__post_init__()


@dataclass
class PhenotypicSex(BiologicalSex):
    """
    An attribute corresponding to the phenotypic sex of the individual, based upon the reproductive organs present.
    """
    _inherited_slots: ClassVar[List[str]] = ["related_to", "interacts_with", "subclass_of"]

    type_uri: ClassVar[str] = "https://w3id.org/biolink/vocab/PhenotypicSex"
    type_curie: ClassVar[str] = "biolink:PhenotypicSex"
    type_name: ClassVar[str] = "phenotypic sex"

    id: Union[ElementIdentifier, PhenotypicSexId] = None
    name: Union[str, LabelType] = None
    category: List[Union[str, IriType]] = empty_list()

    def __post_init__(self):
        if self.id is not None and not isinstance(self.id, PhenotypicSexId):
            self.id = PhenotypicSexId(self.id)
        super().__post_init__()


@dataclass
class GenotypicSex(BiologicalSex):
    """
    An attribute corresponding to the genotypic sex of the individual, based upon genotypic composition of sex
    chromosomes.
    """
    _inherited_slots: ClassVar[List[str]] = ["related_to", "interacts_with", "subclass_of"]

    type_uri: ClassVar[str] = "https://w3id.org/biolink/vocab/GenotypicSex"
    type_curie: ClassVar[str] = "biolink:GenotypicSex"
    type_name: ClassVar[str] = "genotypic sex"

    id: Union[ElementIdentifier, GenotypicSexId] = None
    name: Union[str, LabelType] = None
    category: List[Union[str, IriType]] = empty_list()

    def __post_init__(self):
        if self.id is not None and not isinstance(self.id, GenotypicSexId):
            self.id = GenotypicSexId(self.id)
        super().__post_init__()


@dataclass
class SeverityValue(Attribute):
    """
    describes the severity of a phenotypic feature or disease
    """
    _inherited_slots: ClassVar[List[str]] = ["related_to", "interacts_with", "subclass_of"]

    type_uri: ClassVar[str] = "https://w3id.org/biolink/vocab/SeverityValue"
    type_curie: ClassVar[str] = "biolink:SeverityValue"
    type_name: ClassVar[str] = "severity value"

    id: Union[ElementIdentifier, SeverityValueId] = None
    name: Union[str, LabelType] = None
    category: List[Union[str, IriType]] = empty_list()

    def __post_init__(self):
        if self.id is not None and not isinstance(self.id, SeverityValueId):
            self.id = SeverityValueId(self.id)
        super().__post_init__()


@dataclass
class FrequencyValue(Attribute):
    """
    describes the frequency of occurrence of an event or condition
    """
    _inherited_slots: ClassVar[List[str]] = ["related_to", "interacts_with", "subclass_of"]

    type_uri: ClassVar[str] = "https://w3id.org/biolink/vocab/FrequencyValue"
    type_curie: ClassVar[str] = "biolink:FrequencyValue"
    type_name: ClassVar[str] = "frequency value"

    id: Union[ElementIdentifier, FrequencyValueId] = None
    name: Union[str, LabelType] = None
    category: List[Union[str, IriType]] = empty_list()

    def __post_init__(self):
        if self.id is not None and not isinstance(self.id, FrequencyValueId):
            self.id = FrequencyValueId(self.id)
        super().__post_init__()


@dataclass
class ClinicalModifier(Attribute):
    """
    Used to characterize and specify the phenotypic abnormalities defined in the Phenotypic abnormality subontology,
    with respect to severity, laterality, age of onset, and other aspects
    """
    _inherited_slots: ClassVar[List[str]] = ["related_to", "interacts_with", "subclass_of"]

    type_uri: ClassVar[str] = "https://w3id.org/biolink/vocab/ClinicalModifier"
    type_curie: ClassVar[str] = "biolink:ClinicalModifier"
    type_name: ClassVar[str] = "clinical modifier"

    id: Union[ElementIdentifier, ClinicalModifierId] = None
    name: Union[str, LabelType] = None
    category: List[Union[str, IriType]] = empty_list()

    def __post_init__(self):
        if self.id is not None and not isinstance(self.id, ClinicalModifierId):
            self.id = ClinicalModifierId(self.id)
        super().__post_init__()


@dataclass
class Onset(Attribute):
    """
    The age group in which manifestations appear
    """
    _inherited_slots: ClassVar[List[str]] = ["related_to", "interacts_with", "subclass_of"]

    type_uri: ClassVar[str] = "http://purl.obolibrary.org/obo/HP_0003674"
    type_curie: ClassVar[str] = "HP:0003674"
    type_name: ClassVar[str] = "onset"

    id: Union[ElementIdentifier, OnsetId] = None
    name: Union[str, LabelType] = None
    category: List[Union[str, IriType]] = empty_list()

    def __post_init__(self):
        if self.id is not None and not isinstance(self.id, OnsetId):
            self.id = OnsetId(self.id)
        super().__post_init__()


@dataclass
class NamedThing(YAMLRoot):
    """
    a databased entity or concept/class
    """
    _inherited_slots: ClassVar[List[str]] = ["related_to", "interacts_with", "physically_interacts_with", "affects", "regulates", "positively_regulates", "negatively_regulates", "disrupts", "homologous_to", "paralogous_to", "orthologous_to", "xenologous_to", "coexists_with", "colocalizes_with", "affects_risk_for", "predisposes", "contributes_to", "causes", "prevents", "occurs_in", "located_in", "location_of", "model_of", "overlaps", "has_part", "part_of", "participates_in", "actively_involved_in", "capable_of", "derives_into", "derives_from", "manifestation_of", "produces", "same_as", "has_molecular_consequence"]

    type_uri: ClassVar[str] = "http://example.org/UNKNOWN/WD/Q35120"
    type_curie: ClassVar[str] = "WD:Q35120"
    type_name: ClassVar[str] = "named thing"

    id: Union[ElementIdentifier, NamedThingId]
    name: Union[str, LabelType]
    category: List[Union[str, IriType]] = empty_list()

    def __post_init__(self):
        if not isinstance(self.id, NamedThingId):
            self.id = NamedThingId(self.id)
        if not isinstance(self.name, LabelType):
            self.name = LabelType(self.name)
        if not isinstance(self.category, IriType):
            self.category = IriType(self.category)
        super().__post_init__()


@dataclass
class BiologicalEntity(NamedThing):
    _inherited_slots: ClassVar[List[str]] = ["related_to", "interacts_with", "has_phenotype"]

    type_uri: ClassVar[str] = "http://example.org/UNKNOWN/WD/Q28845870"
    type_curie: ClassVar[str] = "WD:Q28845870"
    type_name: ClassVar[str] = "biological entity"

    id: Union[ElementIdentifier, BiologicalEntityId] = None
    name: Union[str, LabelType] = None
    category: List[Union[str, IriType]] = empty_list()

@dataclass
class OntologyClass(NamedThing):
    """
    a concept or class in an ontology, vocabulary or thesaurus
    """
    _inherited_slots: ClassVar[List[str]] = ["related_to", "interacts_with", "subclass_of"]

    type_uri: ClassVar[str] = "https://w3id.org/biolink/vocab/OntologyClass"
    type_curie: ClassVar[str] = "biolink:OntologyClass"
    type_name: ClassVar[str] = "ontology class"

    id: Union[ElementIdentifier, OntologyClassId] = None
    name: Union[str, LabelType] = None
    category: List[Union[str, IriType]] = empty_list()

    def __post_init__(self):
        if self.id is not None and not isinstance(self.id, OntologyClassId):
            self.id = OntologyClassId(self.id)
        super().__post_init__()


@dataclass
class RelationshipType(OntologyClass):
    """
    An OWL property used as an edge label
    """
    _inherited_slots: ClassVar[List[str]] = ["related_to", "interacts_with", "subclass_of"]

    type_uri: ClassVar[str] = "https://w3id.org/biolink/vocab/RelationshipType"
    type_curie: ClassVar[str] = "biolink:RelationshipType"
    type_name: ClassVar[str] = "relationship type"

    id: Union[ElementIdentifier, RelationshipTypeId] = None
    name: Union[str, LabelType] = None
    category: List[Union[str, IriType]] = empty_list()

    def __post_init__(self):
        if self.id is not None and not isinstance(self.id, RelationshipTypeId):
            self.id = RelationshipTypeId(self.id)
        super().__post_init__()


@dataclass
class GeneOntologyClass(OntologyClass):
    """
    an ontology class that describes a functional aspect of a gene, gene prodoct or complex
    """
    _inherited_slots: ClassVar[List[str]] = ["related_to", "interacts_with", "subclass_of"]

    type_uri: ClassVar[str] = "https://w3id.org/biolink/vocab/GeneOntologyClass"
    type_curie: ClassVar[str] = "biolink:GeneOntologyClass"
    type_name: ClassVar[str] = "gene ontology class"

    id: Union[ElementIdentifier, GeneOntologyClassId] = None
    name: Union[str, LabelType] = None
    category: List[Union[str, IriType]] = empty_list()

    def __post_init__(self):
        if self.id is not None and not isinstance(self.id, GeneOntologyClassId):
            self.id = GeneOntologyClassId(self.id)
        super().__post_init__()


@dataclass
class OrganismTaxon(OntologyClass):
    _inherited_slots: ClassVar[List[str]] = ["related_to", "interacts_with", "subclass_of"]

    type_uri: ClassVar[str] = "http://example.org/UNKNOWN/WD/Q16521"
    type_curie: ClassVar[str] = "WD:Q16521"
    type_name: ClassVar[str] = "organism taxon"

    id: Union[ElementIdentifier, OrganismTaxonId] = None
    name: Union[str, LabelType] = None
    category: List[Union[str, IriType]] = empty_list()

    def __post_init__(self):
        if self.id is not None and not isinstance(self.id, OrganismTaxonId):
            self.id = OrganismTaxonId(self.id)
        super().__post_init__()


@dataclass
class OrganismalEntity(BiologicalEntity):
    """
    A named entity that is either a part of an organism, a whole organism, population or clade of organisms, excluding
    molecular entities
    """
    _inherited_slots: ClassVar[List[str]] = ["related_to", "interacts_with", "has_phenotype"]

    type_uri: ClassVar[str] = "http://example.org/UNKNOWN/WD/Q7239"
    type_curie: ClassVar[str] = "WD:Q7239"
    type_name: ClassVar[str] = "organismal entity"

    id: Union[ElementIdentifier, OrganismalEntityId] = None
    name: Union[str, LabelType] = None
    category: List[Union[str, IriType]] = empty_list()

@dataclass
class IndividualOrganism(OrganismalEntity):
    _inherited_slots: ClassVar[List[str]] = ["related_to", "interacts_with", "has_phenotype", "in_taxon"]

    type_uri: ClassVar[str] = "http://semanticscience.org/resource/SIO_010000"
    type_curie: ClassVar[str] = "SIO:010000"
    type_name: ClassVar[str] = "individual organism"

    id: Union[ElementIdentifier, IndividualOrganismId] = None
    name: Union[str, LabelType] = None
    category: List[Union[str, IriType]] = empty_list()

    def __post_init__(self):
        if self.id is not None and not isinstance(self.id, IndividualOrganismId):
            self.id = IndividualOrganismId(self.id)
        super().__post_init__()


@dataclass
class Case(IndividualOrganism):
    """
    An individual organism that has a patient role in some clinical context.
    """
    _inherited_slots: ClassVar[List[str]] = ["related_to", "interacts_with", "has_phenotype", "in_taxon"]

    type_uri: ClassVar[str] = "https://w3id.org/biolink/vocab/Case"
    type_curie: ClassVar[str] = "biolink:Case"
    type_name: ClassVar[str] = "case"

    id: Union[ElementIdentifier, CaseId] = None
    name: Union[str, LabelType] = None
    category: List[Union[str, IriType]] = empty_list()

    def __post_init__(self):
        if self.id is not None and not isinstance(self.id, CaseId):
            self.id = CaseId(self.id)
        super().__post_init__()


@dataclass
class PopulationOfIndividualOrganisms(OrganismalEntity):
    """
    A collection of individuals from the same taxonomic class distinguished by one or more characteristics.
    Characteristics can include, but are not limited to, shared geographic location, genetics, phenotypes [Alliance
    for Genome Resources]
    """
    _inherited_slots: ClassVar[List[str]] = ["related_to", "interacts_with", "has_phenotype", "in_taxon"]

    type_uri: ClassVar[str] = "http://semanticscience.org/resource/SIO_001061"
    type_curie: ClassVar[str] = "SIO:001061"
    type_name: ClassVar[str] = "population of individual organisms"

    id: Union[ElementIdentifier, PopulationOfIndividualOrganismsId] = None
    name: Union[str, LabelType] = None
    category: List[Union[str, IriType]] = empty_list()

    def __post_init__(self):
        if self.id is not None and not isinstance(self.id, PopulationOfIndividualOrganismsId):
            self.id = PopulationOfIndividualOrganismsId(self.id)
        super().__post_init__()


@dataclass
class Biosample(OrganismalEntity):
    _inherited_slots: ClassVar[List[str]] = ["related_to", "interacts_with", "has_phenotype", "in_taxon"]

    type_uri: ClassVar[str] = "http://semanticscience.org/resource/SIO_001050"
    type_curie: ClassVar[str] = "SIO:001050"
    type_name: ClassVar[str] = "biosample"

    id: Union[ElementIdentifier, BiosampleId] = None
    name: Union[str, LabelType] = None
    category: List[Union[str, IriType]] = empty_list()

    def __post_init__(self):
        if self.id is not None and not isinstance(self.id, BiosampleId):
            self.id = BiosampleId(self.id)
        super().__post_init__()


@dataclass
class DiseaseOrPhenotypicFeature(BiologicalEntity):
    """
    Either one of a disease or an individual phenotypic feature. Some knowledge resources such as Monarch treat these
    as distinct, others such as MESH conflate.
    """
    _inherited_slots: ClassVar[List[str]] = ["related_to", "interacts_with", "has_phenotype", "correlated_with", "has_biomarker", "treated_by", "in_taxon"]

    type_uri: ClassVar[str] = "https://w3id.org/biolink/vocab/DiseaseOrPhenotypicFeature"
    type_curie: ClassVar[str] = "biolink:DiseaseOrPhenotypicFeature"
    type_name: ClassVar[str] = "disease or phenotypic feature"

    id: Union[ElementIdentifier, DiseaseOrPhenotypicFeatureId] = None
    name: Union[str, LabelType] = None
    category: List[Union[str, IriType]] = empty_list()

    def __post_init__(self):
        if self.id is not None and not isinstance(self.id, DiseaseOrPhenotypicFeatureId):
            self.id = DiseaseOrPhenotypicFeatureId(self.id)
        super().__post_init__()


@dataclass
class Disease(DiseaseOrPhenotypicFeature):
    _inherited_slots: ClassVar[List[str]] = ["related_to", "interacts_with", "has_phenotype", "correlated_with", "has_biomarker", "treated_by", "in_taxon"]

    type_uri: ClassVar[str] = "http://purl.obolibrary.org/obo/MONDO_0000001"
    type_curie: ClassVar[str] = "MONDO:0000001"
    type_name: ClassVar[str] = "disease"

    id: Union[ElementIdentifier, DiseaseId] = None
    name: Union[str, LabelType] = None
    category: List[Union[str, IriType]] = empty_list()

    def __post_init__(self):
        if self.id is not None and not isinstance(self.id, DiseaseId):
            self.id = DiseaseId(self.id)
        super().__post_init__()


@dataclass
class PhenotypicFeature(DiseaseOrPhenotypicFeature):
    _inherited_slots: ClassVar[List[str]] = ["related_to", "interacts_with", "has_phenotype", "correlated_with", "has_biomarker", "treated_by", "in_taxon"]

    type_uri: ClassVar[str] = "http://purl.obolibrary.org/obo/UPHENO_0001001"
    type_curie: ClassVar[str] = "UPHENO:0001001"
    type_name: ClassVar[str] = "phenotypic feature"

    id: Union[ElementIdentifier, PhenotypicFeatureId] = None
    name: Union[str, LabelType] = None
    category: List[Union[str, IriType]] = empty_list()

    def __post_init__(self):
        if self.id is not None and not isinstance(self.id, PhenotypicFeatureId):
            self.id = PhenotypicFeatureId(self.id)
        super().__post_init__()


@dataclass
class Environment(BiologicalEntity):
    """
    A feature of the environment of an organism that influences one or more phenotypic features of that organism,
    potentially mediated by genes
    """
    _inherited_slots: ClassVar[List[str]] = ["related_to", "interacts_with", "has_phenotype"]

    type_uri: ClassVar[str] = "http://semanticscience.org/resource/SIO_000955"
    type_curie: ClassVar[str] = "SIO:000955"
    type_name: ClassVar[str] = "environment"

    id: Union[ElementIdentifier, EnvironmentId] = None
    name: Union[str, LabelType] = None
    category: List[Union[str, IriType]] = empty_list()

    def __post_init__(self):
        if self.id is not None and not isinstance(self.id, EnvironmentId):
            self.id = EnvironmentId(self.id)
        super().__post_init__()


@dataclass
class InformationContentEntity(NamedThing):
    """
    a piece of information that typically describes some piece of biology or is used as support.
    """
    _inherited_slots: ClassVar[List[str]] = ["related_to", "interacts_with"]

    type_uri: ClassVar[str] = "http://purl.obolibrary.org/obo/IAO_0000030"
    type_curie: ClassVar[str] = "IAO:0000030"
    type_name: ClassVar[str] = "information content entity"

    id: Union[ElementIdentifier, InformationContentEntityId] = None
    name: Union[str, LabelType] = None
    category: List[Union[str, IriType]] = empty_list()

@dataclass
class ConfidenceLevel(InformationContentEntity):
    """
    Level of confidence in a statement
    """
    _inherited_slots: ClassVar[List[str]] = ["related_to", "interacts_with"]

    type_uri: ClassVar[str] = "http://purl.obolibrary.org/obo/CIO_0000028"
    type_curie: ClassVar[str] = "CIO:0000028"
    type_name: ClassVar[str] = "confidence level"

    id: Union[ElementIdentifier, ConfidenceLevelId] = None
    name: Union[str, LabelType] = None
    category: List[Union[str, IriType]] = empty_list()

    def __post_init__(self):
        if self.id is not None and not isinstance(self.id, ConfidenceLevelId):
            self.id = ConfidenceLevelId(self.id)
        super().__post_init__()


@dataclass
class EvidenceType(InformationContentEntity):
    """
    Class of evidence that supports an association
    """
    _inherited_slots: ClassVar[List[str]] = ["related_to", "interacts_with"]

    type_uri: ClassVar[str] = "http://purl.obolibrary.org/obo/ECO_0000000"
    type_curie: ClassVar[str] = "ECO:0000000"
    type_name: ClassVar[str] = "evidence type"

    id: Union[ElementIdentifier, EvidenceTypeId] = None
    name: Union[str, LabelType] = None
    category: List[Union[str, IriType]] = empty_list()

    def __post_init__(self):
        if self.id is not None and not isinstance(self.id, EvidenceTypeId):
            self.id = EvidenceTypeId(self.id)
        super().__post_init__()


@dataclass
class Publication(InformationContentEntity):
    """
    Any published piece of information. Can refer to a whole publication, or to a part of it (e.g. a figure, figure
    legend, or section highlighted by NLP). The scope is intended to be general and include information published on
    the web as well as journals.
    """
    _inherited_slots: ClassVar[List[str]] = ["related_to", "interacts_with"]

    type_uri: ClassVar[str] = "http://purl.obolibrary.org/obo/IAO_0000311"
    type_curie: ClassVar[str] = "IAO:0000311"
    type_name: ClassVar[str] = "publication"

    id: Union[ElementIdentifier, PublicationId] = None
    name: Union[str, LabelType] = None
    category: List[Union[str, IriType]] = empty_list()

    def __post_init__(self):
        if self.id is not None and not isinstance(self.id, PublicationId):
            self.id = PublicationId(self.id)
        super().__post_init__()


@dataclass
class AdministrativeEntity(NamedThing):
    _inherited_slots: ClassVar[List[str]] = ["related_to", "interacts_with"]

    type_uri: ClassVar[str] = "https://w3id.org/biolink/vocab/AdministrativeEntity"
    type_curie: ClassVar[str] = "biolink:AdministrativeEntity"
    type_name: ClassVar[str] = "administrative entity"

    id: Union[ElementIdentifier, AdministrativeEntityId] = None
    name: Union[str, LabelType] = None
    category: List[Union[str, IriType]] = empty_list()

@dataclass
class Provider(AdministrativeEntity):
    """
    person, group, organization or project that provides a piece of information
    """
    _inherited_slots: ClassVar[List[str]] = ["related_to", "interacts_with"]

    type_uri: ClassVar[str] = "https://w3id.org/biolink/vocab/Provider"
    type_curie: ClassVar[str] = "biolink:Provider"
    type_name: ClassVar[str] = "provider"

    id: Union[ElementIdentifier, ProviderId] = None
    name: Union[str, LabelType] = None
    category: List[Union[str, IriType]] = empty_list()

    def __post_init__(self):
        if self.id is not None and not isinstance(self.id, ProviderId):
            self.id = ProviderId(self.id)
        super().__post_init__()


@dataclass
class MolecularEntity(BiologicalEntity):
    """
    A gene, gene product, small molecule or macromolecule (including protein complex)
    """
    _inherited_slots: ClassVar[List[str]] = ["related_to", "interacts_with", "has_phenotype", "molecularly_interacts_with", "affects_abundance_of", "increases_abundance_of", "decreases_abundance_of", "affects_activity_of", "increases_activity_of", "decreases_activity_of", "affects_expression_of", "increases_expression_of", "decreases_expression_of", "affects_folding_of", "increases_folding_of", "decreases_folding_of", "affects_localization_of", "increases_localization_of", "decreases_localization_of", "affects_metabolic_processing_of", "increases_metabolic_processing_of", "decreases_metabolic_processing_of", "affects_molecular_modification_of", "increases_molecular_modification_of", "decreases_molecular_modification_of", "affects_synthesis_of", "increases_synthesis_of", "decreases_synthesis_of", "affects_degradation_of", "increases_degradation_of", "decreases_degradation_of", "affects_mutation_rate_of", "increases_mutation_rate_of", "decreases_mutation_rate_of", "affects_response_to", "increases_response_to", "decreases_response_to", "affects_splicing_of", "increases_splicing_of", "decreases_splicing_of", "affects_stability_of", "increases_stability_of", "decreases_stability_of", "affects_transport_of", "increases_transport_of", "decreases_transport_of", "affects_secretion_of", "increases_secretion_of", "decreases_secretion_of", "affects_uptake_of", "increases_uptake_of", "decreases_uptake_of", "regulates_entity_to_entity", "biomarker_for", "in_taxon", "positively_regulates_entity_to_entity", "negatively_regulates_entity_to_entity"]

    type_uri: ClassVar[str] = "http://semanticscience.org/resource/SIO_010004"
    type_curie: ClassVar[str] = "SIO:010004"
    type_name: ClassVar[str] = "molecular entity"

    id: Union[ElementIdentifier, MolecularEntityId] = None
    name: Union[str, LabelType] = None
    category: List[Union[str, IriType]] = empty_list()

    def __post_init__(self):
        if self.id is not None and not isinstance(self.id, MolecularEntityId):
            self.id = MolecularEntityId(self.id)
        super().__post_init__()


@dataclass
class ChemicalSubstance(MolecularEntity):
    """
    May be a chemical entity or a formulation with a chemical entity as active ingredient, or a complex material with
    multiple chemical entities as part
    """
    _inherited_slots: ClassVar[List[str]] = ["related_to", "interacts_with", "has_phenotype", "molecularly_interacts_with", "affects_abundance_of", "increases_abundance_of", "decreases_abundance_of", "affects_activity_of", "increases_activity_of", "decreases_activity_of", "affects_expression_of", "increases_expression_of", "decreases_expression_of", "affects_folding_of", "increases_folding_of", "decreases_folding_of", "affects_localization_of", "increases_localization_of", "decreases_localization_of", "affects_metabolic_processing_of", "increases_metabolic_processing_of", "decreases_metabolic_processing_of", "affects_molecular_modification_of", "increases_molecular_modification_of", "decreases_molecular_modification_of", "affects_synthesis_of", "increases_synthesis_of", "decreases_synthesis_of", "affects_degradation_of", "increases_degradation_of", "decreases_degradation_of", "affects_mutation_rate_of", "increases_mutation_rate_of", "decreases_mutation_rate_of", "affects_response_to", "increases_response_to", "decreases_response_to", "affects_splicing_of", "increases_splicing_of", "decreases_splicing_of", "affects_stability_of", "increases_stability_of", "decreases_stability_of", "affects_transport_of", "increases_transport_of", "decreases_transport_of", "affects_secretion_of", "increases_secretion_of", "decreases_secretion_of", "affects_uptake_of", "increases_uptake_of", "decreases_uptake_of", "regulates_entity_to_entity", "biomarker_for", "in_taxon"]

    type_uri: ClassVar[str] = "http://semanticscience.org/resource/SIO_010004"
    type_curie: ClassVar[str] = "SIO:010004"
    type_name: ClassVar[str] = "chemical substance"

    id: Union[ElementIdentifier, ChemicalSubstanceId] = None
    name: Union[str, LabelType] = None
    category: List[Union[str, IriType]] = empty_list()

    def __post_init__(self):
        if self.id is not None and not isinstance(self.id, ChemicalSubstanceId):
            self.id = ChemicalSubstanceId(self.id)
        super().__post_init__()


@dataclass
class Carbohydrate(ChemicalSubstance):
    _inherited_slots: ClassVar[List[str]] = ["related_to", "interacts_with", "has_phenotype", "molecularly_interacts_with", "affects_abundance_of", "increases_abundance_of", "decreases_abundance_of", "affects_activity_of", "increases_activity_of", "decreases_activity_of", "affects_expression_of", "increases_expression_of", "decreases_expression_of", "affects_folding_of", "increases_folding_of", "decreases_folding_of", "affects_localization_of", "increases_localization_of", "decreases_localization_of", "affects_metabolic_processing_of", "increases_metabolic_processing_of", "decreases_metabolic_processing_of", "affects_molecular_modification_of", "increases_molecular_modification_of", "decreases_molecular_modification_of", "affects_synthesis_of", "increases_synthesis_of", "decreases_synthesis_of", "affects_degradation_of", "increases_degradation_of", "decreases_degradation_of", "affects_mutation_rate_of", "increases_mutation_rate_of", "decreases_mutation_rate_of", "affects_response_to", "increases_response_to", "decreases_response_to", "affects_splicing_of", "increases_splicing_of", "decreases_splicing_of", "affects_stability_of", "increases_stability_of", "decreases_stability_of", "affects_transport_of", "increases_transport_of", "decreases_transport_of", "affects_secretion_of", "increases_secretion_of", "decreases_secretion_of", "affects_uptake_of", "increases_uptake_of", "decreases_uptake_of", "regulates_entity_to_entity", "biomarker_for", "in_taxon"]

    type_uri: ClassVar[str] = "https://w3id.org/biolink/vocab/Carbohydrate"
    type_curie: ClassVar[str] = "biolink:Carbohydrate"
    type_name: ClassVar[str] = "carbohydrate"

    id: Union[ElementIdentifier, CarbohydrateId] = None
    name: Union[str, LabelType] = None
    category: List[Union[str, IriType]] = empty_list()

    def __post_init__(self):
        if self.id is not None and not isinstance(self.id, CarbohydrateId):
            self.id = CarbohydrateId(self.id)
        super().__post_init__()


@dataclass
class Drug(ChemicalSubstance):
    """
    A substance intended for use in the diagnosis, cure, mitigation, treatment, or prevention of disease
    """
    _inherited_slots: ClassVar[List[str]] = ["related_to", "interacts_with", "has_phenotype", "molecularly_interacts_with", "affects_abundance_of", "increases_abundance_of", "decreases_abundance_of", "affects_activity_of", "increases_activity_of", "decreases_activity_of", "affects_expression_of", "increases_expression_of", "decreases_expression_of", "affects_folding_of", "increases_folding_of", "decreases_folding_of", "affects_localization_of", "increases_localization_of", "decreases_localization_of", "affects_metabolic_processing_of", "increases_metabolic_processing_of", "decreases_metabolic_processing_of", "affects_molecular_modification_of", "increases_molecular_modification_of", "decreases_molecular_modification_of", "affects_synthesis_of", "increases_synthesis_of", "decreases_synthesis_of", "affects_degradation_of", "increases_degradation_of", "decreases_degradation_of", "affects_mutation_rate_of", "increases_mutation_rate_of", "decreases_mutation_rate_of", "affects_response_to", "increases_response_to", "decreases_response_to", "affects_splicing_of", "increases_splicing_of", "decreases_splicing_of", "affects_stability_of", "increases_stability_of", "decreases_stability_of", "affects_transport_of", "increases_transport_of", "decreases_transport_of", "affects_secretion_of", "increases_secretion_of", "decreases_secretion_of", "affects_uptake_of", "increases_uptake_of", "decreases_uptake_of", "regulates_entity_to_entity", "biomarker_for", "in_taxon"]

    type_uri: ClassVar[str] = "http://example.org/UNKNOWN/WD/Q12140"
    type_curie: ClassVar[str] = "WD:Q12140"
    type_name: ClassVar[str] = "drug"

    id: Union[ElementIdentifier, DrugId] = None
    name: Union[str, LabelType] = None
    category: List[Union[str, IriType]] = empty_list()

    def __post_init__(self):
        if self.id is not None and not isinstance(self.id, DrugId):
            self.id = DrugId(self.id)
        super().__post_init__()


@dataclass
class Metabolite(ChemicalSubstance):
    """
    Any intermediate or product resulting from metabolism. Includes primary and secondary metabolites.
    """
    _inherited_slots: ClassVar[List[str]] = ["related_to", "interacts_with", "has_phenotype", "molecularly_interacts_with", "affects_abundance_of", "increases_abundance_of", "decreases_abundance_of", "affects_activity_of", "increases_activity_of", "decreases_activity_of", "affects_expression_of", "increases_expression_of", "decreases_expression_of", "affects_folding_of", "increases_folding_of", "decreases_folding_of", "affects_localization_of", "increases_localization_of", "decreases_localization_of", "affects_metabolic_processing_of", "increases_metabolic_processing_of", "decreases_metabolic_processing_of", "affects_molecular_modification_of", "increases_molecular_modification_of", "decreases_molecular_modification_of", "affects_synthesis_of", "increases_synthesis_of", "decreases_synthesis_of", "affects_degradation_of", "increases_degradation_of", "decreases_degradation_of", "affects_mutation_rate_of", "increases_mutation_rate_of", "decreases_mutation_rate_of", "affects_response_to", "increases_response_to", "decreases_response_to", "affects_splicing_of", "increases_splicing_of", "decreases_splicing_of", "affects_stability_of", "increases_stability_of", "decreases_stability_of", "affects_transport_of", "increases_transport_of", "decreases_transport_of", "affects_secretion_of", "increases_secretion_of", "decreases_secretion_of", "affects_uptake_of", "increases_uptake_of", "decreases_uptake_of", "regulates_entity_to_entity", "biomarker_for", "in_taxon"]

    type_uri: ClassVar[str] = "http://purl.obolibrary.org/obo/CHEBI_25212"
    type_curie: ClassVar[str] = "CHEBI:25212"
    type_name: ClassVar[str] = "metabolite"

    id: Union[ElementIdentifier, MetaboliteId] = None
    name: Union[str, LabelType] = None
    category: List[Union[str, IriType]] = empty_list()

    def __post_init__(self):
        if self.id is not None and not isinstance(self.id, MetaboliteId):
            self.id = MetaboliteId(self.id)
        super().__post_init__()


@dataclass
class AnatomicalEntity(OrganismalEntity):
    """
    A subcellular location, cell type or gross anatomical part
    """
    _inherited_slots: ClassVar[List[str]] = ["related_to", "interacts_with", "has_phenotype", "expresses", "in_taxon"]

    type_uri: ClassVar[str] = "http://semanticscience.org/resource/SIO_010046"
    type_curie: ClassVar[str] = "SIO:010046"
    type_name: ClassVar[str] = "anatomical entity"

    id: Union[ElementIdentifier, AnatomicalEntityId] = None
    name: Union[str, LabelType] = None
    category: List[Union[str, IriType]] = empty_list()

    def __post_init__(self):
        if self.id is not None and not isinstance(self.id, AnatomicalEntityId):
            self.id = AnatomicalEntityId(self.id)
        super().__post_init__()


@dataclass
class LifeStage(OrganismalEntity):
    """
    A stage of development or growth of an organism, including post-natal adult stages
    """
    _inherited_slots: ClassVar[List[str]] = ["related_to", "interacts_with", "has_phenotype", "in_taxon"]

    type_uri: ClassVar[str] = "https://w3id.org/biolink/vocab/LifeStage"
    type_curie: ClassVar[str] = "biolink:LifeStage"
    type_name: ClassVar[str] = "life stage"

    id: Union[ElementIdentifier, LifeStageId] = None
    name: Union[str, LabelType] = None
    category: List[Union[str, IriType]] = empty_list()

    def __post_init__(self):
        if self.id is not None and not isinstance(self.id, LifeStageId):
            self.id = LifeStageId(self.id)
        super().__post_init__()


@dataclass
class PlanetaryEntity(NamedThing):
    """
    Any entity or process that exists at the level of the whole planet
    """
    _inherited_slots: ClassVar[List[str]] = ["related_to", "interacts_with"]

    type_uri: ClassVar[str] = "https://w3id.org/biolink/vocab/PlanetaryEntity"
    type_curie: ClassVar[str] = "biolink:PlanetaryEntity"
    type_name: ClassVar[str] = "planetary entity"

    id: Union[ElementIdentifier, PlanetaryEntityId] = None
    name: Union[str, LabelType] = None
    category: List[Union[str, IriType]] = empty_list()

    def __post_init__(self):
        if self.id is not None and not isinstance(self.id, PlanetaryEntityId):
            self.id = PlanetaryEntityId(self.id)
        super().__post_init__()


@dataclass
class EnvironmentalProcess(PlanetaryEntity):
    _inherited_slots: ClassVar[List[str]] = ["related_to", "interacts_with", "regulates_process_to_process", "has_participant", "has_input", "precedes"]

    type_uri: ClassVar[str] = "https://w3id.org/biolink/vocab/EnvironmentalProcess"
    type_curie: ClassVar[str] = "biolink:EnvironmentalProcess"
    type_name: ClassVar[str] = "environmental process"

    id: Union[ElementIdentifier, EnvironmentalProcessId] = None
    name: Union[str, LabelType] = None
    category: List[Union[str, IriType]] = empty_list()

    def __post_init__(self):
        if self.id is not None and not isinstance(self.id, EnvironmentalProcessId):
            self.id = EnvironmentalProcessId(self.id)
        super().__post_init__()


@dataclass
class EnvironmentalFeature(PlanetaryEntity):
    _inherited_slots: ClassVar[List[str]] = ["related_to", "interacts_with"]

    type_uri: ClassVar[str] = "https://w3id.org/biolink/vocab/EnvironmentalFeature"
    type_curie: ClassVar[str] = "biolink:EnvironmentalFeature"
    type_name: ClassVar[str] = "environmental feature"

    id: Union[ElementIdentifier, EnvironmentalFeatureId] = None
    name: Union[str, LabelType] = None
    category: List[Union[str, IriType]] = empty_list()

    def __post_init__(self):
        if self.id is not None and not isinstance(self.id, EnvironmentalFeatureId):
            self.id = EnvironmentalFeatureId(self.id)
        super().__post_init__()


@dataclass
class ClinicalEntity(NamedThing):
    """
    Any entity or process that exists in the clinical domain and outside the biological realm. Diseases are placed
    under biological entities
    """
    _inherited_slots: ClassVar[List[str]] = ["related_to", "interacts_with"]

    type_uri: ClassVar[str] = "https://w3id.org/biolink/vocab/ClinicalEntity"
    type_curie: ClassVar[str] = "biolink:ClinicalEntity"
    type_name: ClassVar[str] = "clinical entity"

    id: Union[ElementIdentifier, ClinicalEntityId] = None
    name: Union[str, LabelType] = None
    category: List[Union[str, IriType]] = empty_list()

    def __post_init__(self):
        if self.id is not None and not isinstance(self.id, ClinicalEntityId):
            self.id = ClinicalEntityId(self.id)
        super().__post_init__()


@dataclass
class ClinicalTrial(ClinicalEntity):
    _inherited_slots: ClassVar[List[str]] = ["related_to", "interacts_with"]

    type_uri: ClassVar[str] = "https://w3id.org/biolink/vocab/ClinicalTrial"
    type_curie: ClassVar[str] = "biolink:ClinicalTrial"
    type_name: ClassVar[str] = "clinical trial"

    id: Union[ElementIdentifier, ClinicalTrialId] = None
    name: Union[str, LabelType] = None
    category: List[Union[str, IriType]] = empty_list()

    def __post_init__(self):
        if self.id is not None and not isinstance(self.id, ClinicalTrialId):
            self.id = ClinicalTrialId(self.id)
        super().__post_init__()


@dataclass
class ClinicalIntervention(ClinicalEntity):
    _inherited_slots: ClassVar[List[str]] = ["related_to", "interacts_with"]

    type_uri: ClassVar[str] = "https://w3id.org/biolink/vocab/ClinicalIntervention"
    type_curie: ClassVar[str] = "biolink:ClinicalIntervention"
    type_name: ClassVar[str] = "clinical intervention"

    id: Union[ElementIdentifier, ClinicalInterventionId] = None
    name: Union[str, LabelType] = None
    category: List[Union[str, IriType]] = empty_list()

    def __post_init__(self):
        if self.id is not None and not isinstance(self.id, ClinicalInterventionId):
            self.id = ClinicalInterventionId(self.id)
        super().__post_init__()


@dataclass
class Device(NamedThing):
    """
    A thing made or adapted for a particular purpose, especially a piece of mechanical or electronic equipment
    """
    _inherited_slots: ClassVar[List[str]] = ["related_to", "interacts_with"]

    type_uri: ClassVar[str] = "https://w3id.org/biolink/vocab/Device"
    type_curie: ClassVar[str] = "biolink:Device"
    type_name: ClassVar[str] = "device"

    id: Union[ElementIdentifier, DeviceId] = None
    name: Union[str, LabelType] = None
    category: List[Union[str, IriType]] = empty_list()

    def __post_init__(self):
        if self.id is not None and not isinstance(self.id, DeviceId):
            self.id = DeviceId(self.id)
        super().__post_init__()


@dataclass
class GenomicEntity(MolecularEntity):
    """
    an entity that can either be directly located on a genome (gene, transcript, exon, regulatory region) or is
    encoded in a genome (protein)
    """
    _inherited_slots: ClassVar[List[str]] = ["related_to", "interacts_with", "has_phenotype", "molecularly_interacts_with", "affects_abundance_of", "increases_abundance_of", "decreases_abundance_of", "affects_activity_of", "increases_activity_of", "decreases_activity_of", "affects_expression_of", "increases_expression_of", "decreases_expression_of", "affects_folding_of", "increases_folding_of", "decreases_folding_of", "affects_localization_of", "increases_localization_of", "decreases_localization_of", "affects_metabolic_processing_of", "increases_metabolic_processing_of", "decreases_metabolic_processing_of", "affects_molecular_modification_of", "increases_molecular_modification_of", "decreases_molecular_modification_of", "affects_synthesis_of", "increases_synthesis_of", "decreases_synthesis_of", "affects_degradation_of", "increases_degradation_of", "decreases_degradation_of", "affects_mutation_rate_of", "increases_mutation_rate_of", "decreases_mutation_rate_of", "affects_response_to", "increases_response_to", "decreases_response_to", "affects_splicing_of", "increases_splicing_of", "decreases_splicing_of", "affects_stability_of", "increases_stability_of", "decreases_stability_of", "affects_transport_of", "increases_transport_of", "decreases_transport_of", "affects_secretion_of", "increases_secretion_of", "decreases_secretion_of", "affects_uptake_of", "increases_uptake_of", "decreases_uptake_of", "regulates_entity_to_entity", "biomarker_for", "in_taxon"]

    type_uri: ClassVar[str] = "http://purl.obolibrary.org/obo/SO_0000110"
    type_curie: ClassVar[str] = "SO:0000110"
    type_name: ClassVar[str] = "genomic entity"

    id: Union[ElementIdentifier, GenomicEntityId] = None
    name: Union[str, LabelType] = None
    category: List[Union[str, IriType]] = empty_list()
    has_biological_sequence: Optional[Union[str, BiologicalSequence]] = None

    def __post_init__(self):
        if self.id is not None and not isinstance(self.id, GenomicEntityId):
            self.id = GenomicEntityId(self.id)
        if self.has_biological_sequence is not None and not isinstance(self.has_biological_sequence, BiologicalSequence):
            self.has_biological_sequence = BiologicalSequence(self.has_biological_sequence)
        super().__post_init__()


@dataclass
class Genome(GenomicEntity):
    """
    A genome is the sum of genetic material within a cell or virion.
    """
    _inherited_slots: ClassVar[List[str]] = ["related_to", "interacts_with", "has_phenotype", "molecularly_interacts_with", "affects_abundance_of", "increases_abundance_of", "decreases_abundance_of", "affects_activity_of", "increases_activity_of", "decreases_activity_of", "affects_expression_of", "increases_expression_of", "decreases_expression_of", "affects_folding_of", "increases_folding_of", "decreases_folding_of", "affects_localization_of", "increases_localization_of", "decreases_localization_of", "affects_metabolic_processing_of", "increases_metabolic_processing_of", "decreases_metabolic_processing_of", "affects_molecular_modification_of", "increases_molecular_modification_of", "decreases_molecular_modification_of", "affects_synthesis_of", "increases_synthesis_of", "decreases_synthesis_of", "affects_degradation_of", "increases_degradation_of", "decreases_degradation_of", "affects_mutation_rate_of", "increases_mutation_rate_of", "decreases_mutation_rate_of", "affects_response_to", "increases_response_to", "decreases_response_to", "affects_splicing_of", "increases_splicing_of", "decreases_splicing_of", "affects_stability_of", "increases_stability_of", "decreases_stability_of", "affects_transport_of", "increases_transport_of", "decreases_transport_of", "affects_secretion_of", "increases_secretion_of", "decreases_secretion_of", "affects_uptake_of", "increases_uptake_of", "decreases_uptake_of", "regulates_entity_to_entity", "biomarker_for", "in_taxon"]

    type_uri: ClassVar[str] = "http://purl.obolibrary.org/obo/SO_0001026"
    type_curie: ClassVar[str] = "SO:0001026"
    type_name: ClassVar[str] = "genome"

    id: Union[ElementIdentifier, GenomeId] = None
    name: Union[str, LabelType] = None
    category: List[Union[str, IriType]] = empty_list()

    def __post_init__(self):
        if self.id is not None and not isinstance(self.id, GenomeId):
            self.id = GenomeId(self.id)
        super().__post_init__()


@dataclass
class Transcript(GenomicEntity):
    """
    An RNA synthesized on a DNA or RNA template by an RNA polymerase
    """
    _inherited_slots: ClassVar[List[str]] = ["related_to", "interacts_with", "has_phenotype", "molecularly_interacts_with", "affects_abundance_of", "increases_abundance_of", "decreases_abundance_of", "affects_activity_of", "increases_activity_of", "decreases_activity_of", "affects_expression_of", "increases_expression_of", "decreases_expression_of", "affects_folding_of", "increases_folding_of", "decreases_folding_of", "affects_localization_of", "increases_localization_of", "decreases_localization_of", "affects_metabolic_processing_of", "increases_metabolic_processing_of", "decreases_metabolic_processing_of", "affects_molecular_modification_of", "increases_molecular_modification_of", "decreases_molecular_modification_of", "affects_synthesis_of", "increases_synthesis_of", "decreases_synthesis_of", "affects_degradation_of", "increases_degradation_of", "decreases_degradation_of", "affects_mutation_rate_of", "increases_mutation_rate_of", "decreases_mutation_rate_of", "affects_response_to", "increases_response_to", "decreases_response_to", "affects_splicing_of", "increases_splicing_of", "decreases_splicing_of", "affects_stability_of", "increases_stability_of", "decreases_stability_of", "affects_transport_of", "increases_transport_of", "decreases_transport_of", "affects_secretion_of", "increases_secretion_of", "decreases_secretion_of", "affects_uptake_of", "increases_uptake_of", "decreases_uptake_of", "regulates_entity_to_entity", "biomarker_for", "in_taxon"]

    type_uri: ClassVar[str] = "http://purl.obolibrary.org/obo/SO_0000673"
    type_curie: ClassVar[str] = "SO:0000673"
    type_name: ClassVar[str] = "transcript"

    id: Union[ElementIdentifier, TranscriptId] = None
    name: Union[str, LabelType] = None
    category: List[Union[str, IriType]] = empty_list()

    def __post_init__(self):
        if self.id is not None and not isinstance(self.id, TranscriptId):
            self.id = TranscriptId(self.id)
        super().__post_init__()


@dataclass
class Exon(GenomicEntity):
    """
    A region of the transcript sequence within a gene which is not removed from the primary RNA transcript by RNA
    splicing
    """
    _inherited_slots: ClassVar[List[str]] = ["related_to", "interacts_with", "has_phenotype", "molecularly_interacts_with", "affects_abundance_of", "increases_abundance_of", "decreases_abundance_of", "affects_activity_of", "increases_activity_of", "decreases_activity_of", "affects_expression_of", "increases_expression_of", "decreases_expression_of", "affects_folding_of", "increases_folding_of", "decreases_folding_of", "affects_localization_of", "increases_localization_of", "decreases_localization_of", "affects_metabolic_processing_of", "increases_metabolic_processing_of", "decreases_metabolic_processing_of", "affects_molecular_modification_of", "increases_molecular_modification_of", "decreases_molecular_modification_of", "affects_synthesis_of", "increases_synthesis_of", "decreases_synthesis_of", "affects_degradation_of", "increases_degradation_of", "decreases_degradation_of", "affects_mutation_rate_of", "increases_mutation_rate_of", "decreases_mutation_rate_of", "affects_response_to", "increases_response_to", "decreases_response_to", "affects_splicing_of", "increases_splicing_of", "decreases_splicing_of", "affects_stability_of", "increases_stability_of", "decreases_stability_of", "affects_transport_of", "increases_transport_of", "decreases_transport_of", "affects_secretion_of", "increases_secretion_of", "decreases_secretion_of", "affects_uptake_of", "increases_uptake_of", "decreases_uptake_of", "regulates_entity_to_entity", "biomarker_for", "in_taxon"]

    type_uri: ClassVar[str] = "http://purl.obolibrary.org/obo/SO_0000147"
    type_curie: ClassVar[str] = "SO:0000147"
    type_name: ClassVar[str] = "exon"

    id: Union[ElementIdentifier, ExonId] = None
    name: Union[str, LabelType] = None
    category: List[Union[str, IriType]] = empty_list()

    def __post_init__(self):
        if self.id is not None and not isinstance(self.id, ExonId):
            self.id = ExonId(self.id)
        super().__post_init__()


@dataclass
class CodingSequence(GenomicEntity):
    _inherited_slots: ClassVar[List[str]] = ["related_to", "interacts_with", "has_phenotype", "molecularly_interacts_with", "affects_abundance_of", "increases_abundance_of", "decreases_abundance_of", "affects_activity_of", "increases_activity_of", "decreases_activity_of", "affects_expression_of", "increases_expression_of", "decreases_expression_of", "affects_folding_of", "increases_folding_of", "decreases_folding_of", "affects_localization_of", "increases_localization_of", "decreases_localization_of", "affects_metabolic_processing_of", "increases_metabolic_processing_of", "decreases_metabolic_processing_of", "affects_molecular_modification_of", "increases_molecular_modification_of", "decreases_molecular_modification_of", "affects_synthesis_of", "increases_synthesis_of", "decreases_synthesis_of", "affects_degradation_of", "increases_degradation_of", "decreases_degradation_of", "affects_mutation_rate_of", "increases_mutation_rate_of", "decreases_mutation_rate_of", "affects_response_to", "increases_response_to", "decreases_response_to", "affects_splicing_of", "increases_splicing_of", "decreases_splicing_of", "affects_stability_of", "increases_stability_of", "decreases_stability_of", "affects_transport_of", "increases_transport_of", "decreases_transport_of", "affects_secretion_of", "increases_secretion_of", "decreases_secretion_of", "affects_uptake_of", "increases_uptake_of", "decreases_uptake_of", "regulates_entity_to_entity", "biomarker_for", "in_taxon"]

    type_uri: ClassVar[str] = "http://purl.obolibrary.org/obo/SO_0000316"
    type_curie: ClassVar[str] = "SO:0000316"
    type_name: ClassVar[str] = "coding sequence"

    id: Union[ElementIdentifier, CodingSequenceId] = None
    name: Union[str, LabelType] = None
    category: List[Union[str, IriType]] = empty_list()

    def __post_init__(self):
        if self.id is not None and not isinstance(self.id, CodingSequenceId):
            self.id = CodingSequenceId(self.id)
        super().__post_init__()


@dataclass
class MacromolecularMachine(GenomicEntity):
    """
    A union of gene, gene product, and macromolecular complex. These are the basic units of function in a cell. They
    either carry out individual biological activities, or they encode molecules which do this.
    """
    _inherited_slots: ClassVar[List[str]] = ["related_to", "interacts_with", "has_phenotype", "molecularly_interacts_with", "affects_abundance_of", "increases_abundance_of", "decreases_abundance_of", "affects_activity_of", "increases_activity_of", "decreases_activity_of", "affects_expression_of", "increases_expression_of", "decreases_expression_of", "affects_folding_of", "increases_folding_of", "decreases_folding_of", "affects_localization_of", "increases_localization_of", "decreases_localization_of", "affects_metabolic_processing_of", "increases_metabolic_processing_of", "decreases_metabolic_processing_of", "affects_molecular_modification_of", "increases_molecular_modification_of", "decreases_molecular_modification_of", "affects_synthesis_of", "increases_synthesis_of", "decreases_synthesis_of", "affects_degradation_of", "increases_degradation_of", "decreases_degradation_of", "affects_mutation_rate_of", "increases_mutation_rate_of", "decreases_mutation_rate_of", "affects_response_to", "increases_response_to", "decreases_response_to", "affects_splicing_of", "increases_splicing_of", "decreases_splicing_of", "affects_stability_of", "increases_stability_of", "decreases_stability_of", "affects_transport_of", "increases_transport_of", "decreases_transport_of", "affects_secretion_of", "increases_secretion_of", "decreases_secretion_of", "affects_uptake_of", "increases_uptake_of", "decreases_uptake_of", "regulates_entity_to_entity", "biomarker_for", "in_taxon"]

    type_uri: ClassVar[str] = "https://w3id.org/biolink/vocab/MacromolecularMachine"
    type_curie: ClassVar[str] = "biolink:MacromolecularMachine"
    type_name: ClassVar[str] = "macromolecular machine"

    id: Union[ElementIdentifier, MacromolecularMachineId] = None
    name: Union[str, SymbolType] = None
    category: List[Union[str, IriType]] = empty_list()

    def __post_init__(self):
        if self.id is not None and not isinstance(self.id, MacromolecularMachineId):
            self.id = MacromolecularMachineId(self.id)
        if self.name is not None and not isinstance(self.name, SymbolType):
            self.name = SymbolType(self.name)
        super().__post_init__()


@dataclass
class GeneOrGeneProduct(MacromolecularMachine):
    """
    a union of genes or gene products. Frequently an identifier for one will be used as proxy for another
    """
    _inherited_slots: ClassVar[List[str]] = ["related_to", "interacts_with", "has_phenotype", "molecularly_interacts_with", "affects_abundance_of", "increases_abundance_of", "decreases_abundance_of", "affects_activity_of", "increases_activity_of", "decreases_activity_of", "affects_expression_of", "increases_expression_of", "decreases_expression_of", "affects_folding_of", "increases_folding_of", "decreases_folding_of", "affects_localization_of", "increases_localization_of", "decreases_localization_of", "affects_metabolic_processing_of", "increases_metabolic_processing_of", "decreases_metabolic_processing_of", "affects_molecular_modification_of", "increases_molecular_modification_of", "decreases_molecular_modification_of", "affects_synthesis_of", "increases_synthesis_of", "decreases_synthesis_of", "affects_degradation_of", "increases_degradation_of", "decreases_degradation_of", "affects_mutation_rate_of", "increases_mutation_rate_of", "decreases_mutation_rate_of", "affects_response_to", "increases_response_to", "decreases_response_to", "affects_splicing_of", "increases_splicing_of", "decreases_splicing_of", "affects_stability_of", "increases_stability_of", "decreases_stability_of", "affects_transport_of", "increases_transport_of", "decreases_transport_of", "affects_secretion_of", "increases_secretion_of", "decreases_secretion_of", "affects_uptake_of", "increases_uptake_of", "decreases_uptake_of", "regulates_entity_to_entity", "biomarker_for", "in_taxon", "in_pathway_with", "in_complex_with", "in_cell_population_with", "expressed_in"]

    type_uri: ClassVar[str] = "https://w3id.org/biolink/vocab/GeneOrGeneProduct"
    type_curie: ClassVar[str] = "biolink:GeneOrGeneProduct"
    type_name: ClassVar[str] = "gene or gene product"

    id: Union[ElementIdentifier, GeneOrGeneProductId] = None
    name: Union[str, SymbolType] = None
    category: List[Union[str, IriType]] = empty_list()

    def __post_init__(self):
        if self.id is not None and not isinstance(self.id, GeneOrGeneProductId):
            self.id = GeneOrGeneProductId(self.id)
        super().__post_init__()


@dataclass
class Gene(GeneOrGeneProduct):
    _inherited_slots: ClassVar[List[str]] = ["related_to", "interacts_with", "has_phenotype", "molecularly_interacts_with", "affects_abundance_of", "increases_abundance_of", "decreases_abundance_of", "affects_activity_of", "increases_activity_of", "decreases_activity_of", "affects_expression_of", "increases_expression_of", "decreases_expression_of", "affects_folding_of", "increases_folding_of", "decreases_folding_of", "affects_localization_of", "increases_localization_of", "decreases_localization_of", "affects_metabolic_processing_of", "increases_metabolic_processing_of", "decreases_metabolic_processing_of", "affects_molecular_modification_of", "increases_molecular_modification_of", "decreases_molecular_modification_of", "affects_synthesis_of", "increases_synthesis_of", "decreases_synthesis_of", "affects_degradation_of", "increases_degradation_of", "decreases_degradation_of", "affects_mutation_rate_of", "increases_mutation_rate_of", "decreases_mutation_rate_of", "affects_response_to", "increases_response_to", "decreases_response_to", "affects_splicing_of", "increases_splicing_of", "decreases_splicing_of", "affects_stability_of", "increases_stability_of", "decreases_stability_of", "affects_transport_of", "increases_transport_of", "decreases_transport_of", "affects_secretion_of", "increases_secretion_of", "decreases_secretion_of", "affects_uptake_of", "increases_uptake_of", "decreases_uptake_of", "regulates_entity_to_entity", "biomarker_for", "in_taxon", "in_pathway_with", "in_complex_with", "in_cell_population_with", "expressed_in", "genetically_interacts_with", "has_gene_product", "gene_associated_with_condition"]

    type_uri: ClassVar[str] = "http://purl.obolibrary.org/obo/SO_0000704"
    type_curie: ClassVar[str] = "SO:0000704"
    type_name: ClassVar[str] = "gene"

    id: Union[ElementIdentifier, GeneId] = None
    name: Union[str, SymbolType] = None
    category: List[Union[str, IriType]] = empty_list()

    def __post_init__(self):
        if self.id is not None and not isinstance(self.id, GeneId):
            self.id = GeneId(self.id)
        super().__post_init__()


@dataclass
class GeneProduct(GeneOrGeneProduct):
    """
    The functional molecular product of a single gene. Gene products are either proteins or functional RNA molecules
    """
    _inherited_slots: ClassVar[List[str]] = ["related_to", "interacts_with", "has_phenotype", "molecularly_interacts_with", "affects_abundance_of", "increases_abundance_of", "decreases_abundance_of", "affects_activity_of", "increases_activity_of", "decreases_activity_of", "affects_expression_of", "increases_expression_of", "decreases_expression_of", "affects_folding_of", "increases_folding_of", "decreases_folding_of", "affects_localization_of", "increases_localization_of", "decreases_localization_of", "affects_metabolic_processing_of", "increases_metabolic_processing_of", "decreases_metabolic_processing_of", "affects_molecular_modification_of", "increases_molecular_modification_of", "decreases_molecular_modification_of", "affects_synthesis_of", "increases_synthesis_of", "decreases_synthesis_of", "affects_degradation_of", "increases_degradation_of", "decreases_degradation_of", "affects_mutation_rate_of", "increases_mutation_rate_of", "decreases_mutation_rate_of", "affects_response_to", "increases_response_to", "decreases_response_to", "affects_splicing_of", "increases_splicing_of", "decreases_splicing_of", "affects_stability_of", "increases_stability_of", "decreases_stability_of", "affects_transport_of", "increases_transport_of", "decreases_transport_of", "affects_secretion_of", "increases_secretion_of", "decreases_secretion_of", "affects_uptake_of", "increases_uptake_of", "decreases_uptake_of", "regulates_entity_to_entity", "biomarker_for", "in_taxon", "in_pathway_with", "in_complex_with", "in_cell_population_with", "expressed_in"]

    type_uri: ClassVar[str] = "http://example.org/UNKNOWN/WD/Q424689"
    type_curie: ClassVar[str] = "WD:Q424689"
    type_name: ClassVar[str] = "gene product"

    id: Union[ElementIdentifier, GeneProductId] = None
    name: Union[str, SymbolType] = None
    category: List[Union[str, IriType]] = empty_list()

    def __post_init__(self):
        if self.id is not None and not isinstance(self.id, GeneProductId):
            self.id = GeneProductId(self.id)
        super().__post_init__()


@dataclass
class Protein(GeneProduct):
    """
    A gene product that is composed of a chain of amino acid sequences and is produced by ribosome-mediated
    translation of mRNA
    """
    _inherited_slots: ClassVar[List[str]] = ["related_to", "interacts_with", "has_phenotype", "molecularly_interacts_with", "affects_abundance_of", "increases_abundance_of", "decreases_abundance_of", "affects_activity_of", "increases_activity_of", "decreases_activity_of", "affects_expression_of", "increases_expression_of", "decreases_expression_of", "affects_folding_of", "increases_folding_of", "decreases_folding_of", "affects_localization_of", "increases_localization_of", "decreases_localization_of", "affects_metabolic_processing_of", "increases_metabolic_processing_of", "decreases_metabolic_processing_of", "affects_molecular_modification_of", "increases_molecular_modification_of", "decreases_molecular_modification_of", "affects_synthesis_of", "increases_synthesis_of", "decreases_synthesis_of", "affects_degradation_of", "increases_degradation_of", "decreases_degradation_of", "affects_mutation_rate_of", "increases_mutation_rate_of", "decreases_mutation_rate_of", "affects_response_to", "increases_response_to", "decreases_response_to", "affects_splicing_of", "increases_splicing_of", "decreases_splicing_of", "affects_stability_of", "increases_stability_of", "decreases_stability_of", "affects_transport_of", "increases_transport_of", "decreases_transport_of", "affects_secretion_of", "increases_secretion_of", "decreases_secretion_of", "affects_uptake_of", "increases_uptake_of", "decreases_uptake_of", "regulates_entity_to_entity", "biomarker_for", "in_taxon", "in_pathway_with", "in_complex_with", "in_cell_population_with", "expressed_in"]

    type_uri: ClassVar[str] = "http://purl.obolibrary.org/obo/PR_000000001"
    type_curie: ClassVar[str] = "PR:000000001"
    type_name: ClassVar[str] = "protein"

    id: Union[ElementIdentifier, ProteinId] = None
    name: Union[str, SymbolType] = None
    category: List[Union[str, IriType]] = empty_list()

    def __post_init__(self):
        if self.id is not None and not isinstance(self.id, ProteinId):
            self.id = ProteinId(self.id)
        super().__post_init__()


@dataclass
class GeneProductIsoform(GeneProduct):
    """
    This is an abstract class that can be mixed in with different kinds of gene products to indicate that the gene
    product is intended to represent a specific isoform rather than a canonical or reference or generic product. The
    designation of canonical or reference may be arbitrary, or it may represent the superclass of all isoforms.
    """
    _inherited_slots: ClassVar[List[str]] = ["related_to", "interacts_with", "has_phenotype", "molecularly_interacts_with", "affects_abundance_of", "increases_abundance_of", "decreases_abundance_of", "affects_activity_of", "increases_activity_of", "decreases_activity_of", "affects_expression_of", "increases_expression_of", "decreases_expression_of", "affects_folding_of", "increases_folding_of", "decreases_folding_of", "affects_localization_of", "increases_localization_of", "decreases_localization_of", "affects_metabolic_processing_of", "increases_metabolic_processing_of", "decreases_metabolic_processing_of", "affects_molecular_modification_of", "increases_molecular_modification_of", "decreases_molecular_modification_of", "affects_synthesis_of", "increases_synthesis_of", "decreases_synthesis_of", "affects_degradation_of", "increases_degradation_of", "decreases_degradation_of", "affects_mutation_rate_of", "increases_mutation_rate_of", "decreases_mutation_rate_of", "affects_response_to", "increases_response_to", "decreases_response_to", "affects_splicing_of", "increases_splicing_of", "decreases_splicing_of", "affects_stability_of", "increases_stability_of", "decreases_stability_of", "affects_transport_of", "increases_transport_of", "decreases_transport_of", "affects_secretion_of", "increases_secretion_of", "decreases_secretion_of", "affects_uptake_of", "increases_uptake_of", "decreases_uptake_of", "regulates_entity_to_entity", "biomarker_for", "in_taxon", "in_pathway_with", "in_complex_with", "in_cell_population_with", "expressed_in"]

    type_uri: ClassVar[str] = "https://w3id.org/biolink/vocab/GeneProductIsoform"
    type_curie: ClassVar[str] = "biolink:GeneProductIsoform"
    type_name: ClassVar[str] = "gene product isoform"

    id: Union[ElementIdentifier, GeneProductIsoformId] = None
    name: Union[str, SymbolType] = None
    category: List[Union[str, IriType]] = empty_list()

@dataclass
class ProteinIsoform(Protein):
    """
    Represents a protein that is a specific isoform of the canonical or reference protein. See
    https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4114032/
    """
    _inherited_slots: ClassVar[List[str]] = ["related_to", "interacts_with", "has_phenotype", "molecularly_interacts_with", "affects_abundance_of", "increases_abundance_of", "decreases_abundance_of", "affects_activity_of", "increases_activity_of", "decreases_activity_of", "affects_expression_of", "increases_expression_of", "decreases_expression_of", "affects_folding_of", "increases_folding_of", "decreases_folding_of", "affects_localization_of", "increases_localization_of", "decreases_localization_of", "affects_metabolic_processing_of", "increases_metabolic_processing_of", "decreases_metabolic_processing_of", "affects_molecular_modification_of", "increases_molecular_modification_of", "decreases_molecular_modification_of", "affects_synthesis_of", "increases_synthesis_of", "decreases_synthesis_of", "affects_degradation_of", "increases_degradation_of", "decreases_degradation_of", "affects_mutation_rate_of", "increases_mutation_rate_of", "decreases_mutation_rate_of", "affects_response_to", "increases_response_to", "decreases_response_to", "affects_splicing_of", "increases_splicing_of", "decreases_splicing_of", "affects_stability_of", "increases_stability_of", "decreases_stability_of", "affects_transport_of", "increases_transport_of", "decreases_transport_of", "affects_secretion_of", "increases_secretion_of", "decreases_secretion_of", "affects_uptake_of", "increases_uptake_of", "decreases_uptake_of", "regulates_entity_to_entity", "biomarker_for", "in_taxon", "in_pathway_with", "in_complex_with", "in_cell_population_with", "expressed_in"]

    type_uri: ClassVar[str] = "https://w3id.org/biolink/vocab/ProteinIsoform"
    type_curie: ClassVar[str] = "biolink:ProteinIsoform"
    type_name: ClassVar[str] = "protein isoform"

    id: Union[ElementIdentifier, ProteinIsoformId] = None
    name: Union[str, SymbolType] = None
    category: List[Union[str, IriType]] = empty_list()

    def __post_init__(self):
        if self.id is not None and not isinstance(self.id, ProteinIsoformId):
            self.id = ProteinIsoformId(self.id)
        super().__post_init__()


@dataclass
class RNAProduct(GeneProduct):
    _inherited_slots: ClassVar[List[str]] = ["related_to", "interacts_with", "has_phenotype", "molecularly_interacts_with", "affects_abundance_of", "increases_abundance_of", "decreases_abundance_of", "affects_activity_of", "increases_activity_of", "decreases_activity_of", "affects_expression_of", "increases_expression_of", "decreases_expression_of", "affects_folding_of", "increases_folding_of", "decreases_folding_of", "affects_localization_of", "increases_localization_of", "decreases_localization_of", "affects_metabolic_processing_of", "increases_metabolic_processing_of", "decreases_metabolic_processing_of", "affects_molecular_modification_of", "increases_molecular_modification_of", "decreases_molecular_modification_of", "affects_synthesis_of", "increases_synthesis_of", "decreases_synthesis_of", "affects_degradation_of", "increases_degradation_of", "decreases_degradation_of", "affects_mutation_rate_of", "increases_mutation_rate_of", "decreases_mutation_rate_of", "affects_response_to", "increases_response_to", "decreases_response_to", "affects_splicing_of", "increases_splicing_of", "decreases_splicing_of", "affects_stability_of", "increases_stability_of", "decreases_stability_of", "affects_transport_of", "increases_transport_of", "decreases_transport_of", "affects_secretion_of", "increases_secretion_of", "decreases_secretion_of", "affects_uptake_of", "increases_uptake_of", "decreases_uptake_of", "regulates_entity_to_entity", "biomarker_for", "in_taxon", "in_pathway_with", "in_complex_with", "in_cell_population_with", "expressed_in"]

    type_uri: ClassVar[str] = "http://purl.obolibrary.org/obo/CHEBI_33697"
    type_curie: ClassVar[str] = "CHEBI:33697"
    type_name: ClassVar[str] = "RNA product"

    id: Union[ElementIdentifier, RNAProductId] = None
    name: Union[str, SymbolType] = None
    category: List[Union[str, IriType]] = empty_list()

    def __post_init__(self):
        if self.id is not None and not isinstance(self.id, RNAProductId):
            self.id = RNAProductId(self.id)
        super().__post_init__()


@dataclass
class RNAProductIsoform(RNAProduct):
    """
    Represents a protein that is a specific isoform of the canonical or reference RNA
    """
    _inherited_slots: ClassVar[List[str]] = ["related_to", "interacts_with", "has_phenotype", "molecularly_interacts_with", "affects_abundance_of", "increases_abundance_of", "decreases_abundance_of", "affects_activity_of", "increases_activity_of", "decreases_activity_of", "affects_expression_of", "increases_expression_of", "decreases_expression_of", "affects_folding_of", "increases_folding_of", "decreases_folding_of", "affects_localization_of", "increases_localization_of", "decreases_localization_of", "affects_metabolic_processing_of", "increases_metabolic_processing_of", "decreases_metabolic_processing_of", "affects_molecular_modification_of", "increases_molecular_modification_of", "decreases_molecular_modification_of", "affects_synthesis_of", "increases_synthesis_of", "decreases_synthesis_of", "affects_degradation_of", "increases_degradation_of", "decreases_degradation_of", "affects_mutation_rate_of", "increases_mutation_rate_of", "decreases_mutation_rate_of", "affects_response_to", "increases_response_to", "decreases_response_to", "affects_splicing_of", "increases_splicing_of", "decreases_splicing_of", "affects_stability_of", "increases_stability_of", "decreases_stability_of", "affects_transport_of", "increases_transport_of", "decreases_transport_of", "affects_secretion_of", "increases_secretion_of", "decreases_secretion_of", "affects_uptake_of", "increases_uptake_of", "decreases_uptake_of", "regulates_entity_to_entity", "biomarker_for", "in_taxon", "in_pathway_with", "in_complex_with", "in_cell_population_with", "expressed_in"]

    type_uri: ClassVar[str] = "https://w3id.org/biolink/vocab/RNAProductIsoform"
    type_curie: ClassVar[str] = "biolink:RNAProductIsoform"
    type_name: ClassVar[str] = "RNA product isoform"

    id: Union[ElementIdentifier, RNAProductIsoformId] = None
    name: Union[str, SymbolType] = None
    category: List[Union[str, IriType]] = empty_list()

    def __post_init__(self):
        if self.id is not None and not isinstance(self.id, RNAProductIsoformId):
            self.id = RNAProductIsoformId(self.id)
        super().__post_init__()


@dataclass
class NoncodingRNAProduct(RNAProduct):
    _inherited_slots: ClassVar[List[str]] = ["related_to", "interacts_with", "has_phenotype", "molecularly_interacts_with", "affects_abundance_of", "increases_abundance_of", "decreases_abundance_of", "affects_activity_of", "increases_activity_of", "decreases_activity_of", "affects_expression_of", "increases_expression_of", "decreases_expression_of", "affects_folding_of", "increases_folding_of", "decreases_folding_of", "affects_localization_of", "increases_localization_of", "decreases_localization_of", "affects_metabolic_processing_of", "increases_metabolic_processing_of", "decreases_metabolic_processing_of", "affects_molecular_modification_of", "increases_molecular_modification_of", "decreases_molecular_modification_of", "affects_synthesis_of", "increases_synthesis_of", "decreases_synthesis_of", "affects_degradation_of", "increases_degradation_of", "decreases_degradation_of", "affects_mutation_rate_of", "increases_mutation_rate_of", "decreases_mutation_rate_of", "affects_response_to", "increases_response_to", "decreases_response_to", "affects_splicing_of", "increases_splicing_of", "decreases_splicing_of", "affects_stability_of", "increases_stability_of", "decreases_stability_of", "affects_transport_of", "increases_transport_of", "decreases_transport_of", "affects_secretion_of", "increases_secretion_of", "decreases_secretion_of", "affects_uptake_of", "increases_uptake_of", "decreases_uptake_of", "regulates_entity_to_entity", "biomarker_for", "in_taxon", "in_pathway_with", "in_complex_with", "in_cell_population_with", "expressed_in"]

    type_uri: ClassVar[str] = "http://semanticscience.org/resource/SIO_001235"
    type_curie: ClassVar[str] = "SIO:001235"
    type_name: ClassVar[str] = "noncoding RNA product"

    id: Union[ElementIdentifier, NoncodingRNAProductId] = None
    name: Union[str, SymbolType] = None
    category: List[Union[str, IriType]] = empty_list()

    def __post_init__(self):
        if self.id is not None and not isinstance(self.id, NoncodingRNAProductId):
            self.id = NoncodingRNAProductId(self.id)
        super().__post_init__()


@dataclass
class MicroRNA(NoncodingRNAProduct):
    _inherited_slots: ClassVar[List[str]] = ["related_to", "interacts_with", "has_phenotype", "molecularly_interacts_with", "affects_abundance_of", "increases_abundance_of", "decreases_abundance_of", "affects_activity_of", "increases_activity_of", "decreases_activity_of", "affects_expression_of", "increases_expression_of", "decreases_expression_of", "affects_folding_of", "increases_folding_of", "decreases_folding_of", "affects_localization_of", "increases_localization_of", "decreases_localization_of", "affects_metabolic_processing_of", "increases_metabolic_processing_of", "decreases_metabolic_processing_of", "affects_molecular_modification_of", "increases_molecular_modification_of", "decreases_molecular_modification_of", "affects_synthesis_of", "increases_synthesis_of", "decreases_synthesis_of", "affects_degradation_of", "increases_degradation_of", "decreases_degradation_of", "affects_mutation_rate_of", "increases_mutation_rate_of", "decreases_mutation_rate_of", "affects_response_to", "increases_response_to", "decreases_response_to", "affects_splicing_of", "increases_splicing_of", "decreases_splicing_of", "affects_stability_of", "increases_stability_of", "decreases_stability_of", "affects_transport_of", "increases_transport_of", "decreases_transport_of", "affects_secretion_of", "increases_secretion_of", "decreases_secretion_of", "affects_uptake_of", "increases_uptake_of", "decreases_uptake_of", "regulates_entity_to_entity", "biomarker_for", "in_taxon", "in_pathway_with", "in_complex_with", "in_cell_population_with", "expressed_in"]

    type_uri: ClassVar[str] = "http://semanticscience.org/resource/SIO_001397"
    type_curie: ClassVar[str] = "SIO:001397"
    type_name: ClassVar[str] = "microRNA"

    id: Union[ElementIdentifier, MicroRNAId] = None
    name: Union[str, SymbolType] = None
    category: List[Union[str, IriType]] = empty_list()

    def __post_init__(self):
        if self.id is not None and not isinstance(self.id, MicroRNAId):
            self.id = MicroRNAId(self.id)
        super().__post_init__()


@dataclass
class MacromolecularComplex(MacromolecularMachine):
    _inherited_slots: ClassVar[List[str]] = ["related_to", "interacts_with", "has_phenotype", "molecularly_interacts_with", "affects_abundance_of", "increases_abundance_of", "decreases_abundance_of", "affects_activity_of", "increases_activity_of", "decreases_activity_of", "affects_expression_of", "increases_expression_of", "decreases_expression_of", "affects_folding_of", "increases_folding_of", "decreases_folding_of", "affects_localization_of", "increases_localization_of", "decreases_localization_of", "affects_metabolic_processing_of", "increases_metabolic_processing_of", "decreases_metabolic_processing_of", "affects_molecular_modification_of", "increases_molecular_modification_of", "decreases_molecular_modification_of", "affects_synthesis_of", "increases_synthesis_of", "decreases_synthesis_of", "affects_degradation_of", "increases_degradation_of", "decreases_degradation_of", "affects_mutation_rate_of", "increases_mutation_rate_of", "decreases_mutation_rate_of", "affects_response_to", "increases_response_to", "decreases_response_to", "affects_splicing_of", "increases_splicing_of", "decreases_splicing_of", "affects_stability_of", "increases_stability_of", "decreases_stability_of", "affects_transport_of", "increases_transport_of", "decreases_transport_of", "affects_secretion_of", "increases_secretion_of", "decreases_secretion_of", "affects_uptake_of", "increases_uptake_of", "decreases_uptake_of", "regulates_entity_to_entity", "biomarker_for", "in_taxon"]

    type_uri: ClassVar[str] = "http://semanticscience.org/resource/SIO_010046"
    type_curie: ClassVar[str] = "SIO:010046"
    type_name: ClassVar[str] = "macromolecular complex"

    id: Union[ElementIdentifier, MacromolecularComplexId] = None
    name: Union[str, SymbolType] = None
    category: List[Union[str, IriType]] = empty_list()

    def __post_init__(self):
        if self.id is not None and not isinstance(self.id, MacromolecularComplexId):
            self.id = MacromolecularComplexId(self.id)
        super().__post_init__()


@dataclass
class GeneFamily(MolecularEntity):
    """
    any grouping of multiple genes or gene products related by common descent
    """
    _inherited_slots: ClassVar[List[str]] = ["related_to", "interacts_with", "has_phenotype", "molecularly_interacts_with", "affects_abundance_of", "increases_abundance_of", "decreases_abundance_of", "affects_activity_of", "increases_activity_of", "decreases_activity_of", "affects_expression_of", "increases_expression_of", "decreases_expression_of", "affects_folding_of", "increases_folding_of", "decreases_folding_of", "affects_localization_of", "increases_localization_of", "decreases_localization_of", "affects_metabolic_processing_of", "increases_metabolic_processing_of", "decreases_metabolic_processing_of", "affects_molecular_modification_of", "increases_molecular_modification_of", "decreases_molecular_modification_of", "affects_synthesis_of", "increases_synthesis_of", "decreases_synthesis_of", "affects_degradation_of", "increases_degradation_of", "decreases_degradation_of", "affects_mutation_rate_of", "increases_mutation_rate_of", "decreases_mutation_rate_of", "affects_response_to", "increases_response_to", "decreases_response_to", "affects_splicing_of", "increases_splicing_of", "decreases_splicing_of", "affects_stability_of", "increases_stability_of", "decreases_stability_of", "affects_transport_of", "increases_transport_of", "decreases_transport_of", "affects_secretion_of", "increases_secretion_of", "decreases_secretion_of", "affects_uptake_of", "increases_uptake_of", "decreases_uptake_of", "regulates_entity_to_entity", "biomarker_for", "in_taxon"]

    type_uri: ClassVar[str] = "http://semanticscience.org/resource/SIO_001380"
    type_curie: ClassVar[str] = "SIO:001380"
    type_name: ClassVar[str] = "gene family"

    id: Union[ElementIdentifier, GeneFamilyId] = None
    name: Union[str, LabelType] = None
    category: List[Union[str, IriType]] = empty_list()

    def __post_init__(self):
        if self.id is not None and not isinstance(self.id, GeneFamilyId):
            self.id = GeneFamilyId(self.id)
        super().__post_init__()


@dataclass
class Zygosity(Attribute):
    _inherited_slots: ClassVar[List[str]] = ["related_to", "interacts_with", "subclass_of"]

    type_uri: ClassVar[str] = "http://purl.obolibrary.org/obo/GENO_0000133"
    type_curie: ClassVar[str] = "GENO:0000133"
    type_name: ClassVar[str] = "zygosity"

    id: Union[ElementIdentifier, ZygosityId] = None
    name: Union[str, LabelType] = None
    category: List[Union[str, IriType]] = empty_list()

    def __post_init__(self):
        if self.id is not None and not isinstance(self.id, ZygosityId):
            self.id = ZygosityId(self.id)
        super().__post_init__()


@dataclass
class Genotype(GenomicEntity):
    """
    An information content entity that describes a genome by specifying the total variation in genomic sequence and/or
    gene expression, relative to some extablished background
    """
    _inherited_slots: ClassVar[List[str]] = ["related_to", "interacts_with", "has_phenotype", "molecularly_interacts_with", "affects_abundance_of", "increases_abundance_of", "decreases_abundance_of", "affects_activity_of", "increases_activity_of", "decreases_activity_of", "affects_expression_of", "increases_expression_of", "decreases_expression_of", "affects_folding_of", "increases_folding_of", "decreases_folding_of", "affects_localization_of", "increases_localization_of", "decreases_localization_of", "affects_metabolic_processing_of", "increases_metabolic_processing_of", "decreases_metabolic_processing_of", "affects_molecular_modification_of", "increases_molecular_modification_of", "decreases_molecular_modification_of", "affects_synthesis_of", "increases_synthesis_of", "decreases_synthesis_of", "affects_degradation_of", "increases_degradation_of", "decreases_degradation_of", "affects_mutation_rate_of", "increases_mutation_rate_of", "decreases_mutation_rate_of", "affects_response_to", "increases_response_to", "decreases_response_to", "affects_splicing_of", "increases_splicing_of", "decreases_splicing_of", "affects_stability_of", "increases_stability_of", "decreases_stability_of", "affects_transport_of", "increases_transport_of", "decreases_transport_of", "affects_secretion_of", "increases_secretion_of", "decreases_secretion_of", "affects_uptake_of", "increases_uptake_of", "decreases_uptake_of", "regulates_entity_to_entity", "biomarker_for", "in_taxon"]

    type_uri: ClassVar[str] = "http://purl.obolibrary.org/obo/GENO_0000536"
    type_curie: ClassVar[str] = "GENO:0000536"
    type_name: ClassVar[str] = "genotype"

    id: Union[ElementIdentifier, GenotypeId] = None
    name: Union[str, LabelType] = None
    category: List[Union[str, IriType]] = empty_list()
    has_zygosity: Optional[Union[ElementIdentifier, ZygosityId]] = None

    def __post_init__(self):
        if self.id is not None and not isinstance(self.id, GenotypeId):
            self.id = GenotypeId(self.id)
        if self.has_zygosity is not None and not isinstance(self.has_zygosity, ZygosityId):
            self.has_zygosity = ZygosityId(self.has_zygosity)
        super().__post_init__()


@dataclass
class Haplotype(GenomicEntity):
    """
    A set of zero or more Alleles on a single instance of a Sequence[VMC]
    """
    _inherited_slots: ClassVar[List[str]] = ["related_to", "interacts_with", "has_phenotype", "molecularly_interacts_with", "affects_abundance_of", "increases_abundance_of", "decreases_abundance_of", "affects_activity_of", "increases_activity_of", "decreases_activity_of", "affects_expression_of", "increases_expression_of", "decreases_expression_of", "affects_folding_of", "increases_folding_of", "decreases_folding_of", "affects_localization_of", "increases_localization_of", "decreases_localization_of", "affects_metabolic_processing_of", "increases_metabolic_processing_of", "decreases_metabolic_processing_of", "affects_molecular_modification_of", "increases_molecular_modification_of", "decreases_molecular_modification_of", "affects_synthesis_of", "increases_synthesis_of", "decreases_synthesis_of", "affects_degradation_of", "increases_degradation_of", "decreases_degradation_of", "affects_mutation_rate_of", "increases_mutation_rate_of", "decreases_mutation_rate_of", "affects_response_to", "increases_response_to", "decreases_response_to", "affects_splicing_of", "increases_splicing_of", "decreases_splicing_of", "affects_stability_of", "increases_stability_of", "decreases_stability_of", "affects_transport_of", "increases_transport_of", "decreases_transport_of", "affects_secretion_of", "increases_secretion_of", "decreases_secretion_of", "affects_uptake_of", "increases_uptake_of", "decreases_uptake_of", "regulates_entity_to_entity", "biomarker_for", "in_taxon"]

    type_uri: ClassVar[str] = "http://purl.obolibrary.org/obo/GENO_0000871"
    type_curie: ClassVar[str] = "GENO:0000871"
    type_name: ClassVar[str] = "haplotype"

    id: Union[ElementIdentifier, HaplotypeId] = None
    name: Union[str, LabelType] = None
    category: List[Union[str, IriType]] = empty_list()

    def __post_init__(self):
        if self.id is not None and not isinstance(self.id, HaplotypeId):
            self.id = HaplotypeId(self.id)
        super().__post_init__()


@dataclass
class SequenceVariant(GenomicEntity):
    """
    An allele that varies in its sequence from what is considered the reference allele at that locus.
    """
    _inherited_slots: ClassVar[List[str]] = ["related_to", "interacts_with", "has_phenotype", "molecularly_interacts_with", "affects_abundance_of", "increases_abundance_of", "decreases_abundance_of", "affects_activity_of", "increases_activity_of", "decreases_activity_of", "affects_expression_of", "increases_expression_of", "decreases_expression_of", "affects_folding_of", "increases_folding_of", "decreases_folding_of", "affects_localization_of", "increases_localization_of", "decreases_localization_of", "affects_metabolic_processing_of", "increases_metabolic_processing_of", "decreases_metabolic_processing_of", "affects_molecular_modification_of", "increases_molecular_modification_of", "decreases_molecular_modification_of", "affects_synthesis_of", "increases_synthesis_of", "decreases_synthesis_of", "affects_degradation_of", "increases_degradation_of", "decreases_degradation_of", "affects_mutation_rate_of", "increases_mutation_rate_of", "decreases_mutation_rate_of", "affects_response_to", "increases_response_to", "decreases_response_to", "affects_splicing_of", "increases_splicing_of", "decreases_splicing_of", "affects_stability_of", "increases_stability_of", "decreases_stability_of", "affects_transport_of", "increases_transport_of", "decreases_transport_of", "affects_secretion_of", "increases_secretion_of", "decreases_secretion_of", "affects_uptake_of", "increases_uptake_of", "decreases_uptake_of", "regulates_entity_to_entity", "biomarker_for", "in_taxon"]

    type_uri: ClassVar[str] = "http://purl.obolibrary.org/obo/GENO_0000002"
    type_curie: ClassVar[str] = "GENO:0000002"
    type_name: ClassVar[str] = "sequence variant"

    id: Union[ElementIdentifier, SequenceVariantId] = None
    name: Union[str, LabelType] = None
    category: List[Union[str, IriType]] = empty_list()
    has_biological_sequence: Optional[Union[str, BiologicalSequence]] = None
    has_gene: List[Union[ElementIdentifier, GeneId]] = empty_list()

    def __post_init__(self):
        if self.id is not None and not isinstance(self.id, SequenceVariantId):
            self.id = SequenceVariantId(self.id)
        if self.has_biological_sequence is not None and not isinstance(self.has_biological_sequence, BiologicalSequence):
            self.has_biological_sequence = BiologicalSequence(self.has_biological_sequence)
        self.has_gene = [v if isinstance(v, GeneId)
                         else GeneId(v) for v in self.has_gene]
        super().__post_init__()


@dataclass
class DrugExposure(Environment):
    """
    A drug exposure is an intake of a particular chemical substance
    """
    _inherited_slots: ClassVar[List[str]] = ["related_to", "interacts_with", "has_phenotype"]

    type_uri: ClassVar[str] = "http://example.org/UNKNOWN/ECTO/0000509"
    type_curie: ClassVar[str] = "ECTO:0000509"
    type_name: ClassVar[str] = "drug exposure"

    id: Union[ElementIdentifier, DrugExposureId] = None
    name: Union[str, LabelType] = None
    category: List[Union[str, IriType]] = empty_list()
    drug: List[Union[ElementIdentifier, ChemicalSubstanceId]] = empty_list()

    def __post_init__(self):
        if self.id is not None and not isinstance(self.id, DrugExposureId):
            self.id = DrugExposureId(self.id)
        super().__post_init__()


@dataclass
class Treatment(Environment):
    """
    A treatment is targeted at a disease or phenotype and may involve multiple drug 'exposures'
    """
    _inherited_slots: ClassVar[List[str]] = ["related_to", "interacts_with", "has_phenotype", "treats"]

    type_uri: ClassVar[str] = "http://purl.obolibrary.org/obo/OGMS_0000090"
    type_curie: ClassVar[str] = "OGMS:0000090"
    type_name: ClassVar[str] = "treatment"

    id: Union[ElementIdentifier, TreatmentId] = None
    name: Union[str, LabelType] = None
    category: List[Union[str, IriType]] = empty_list()
    treats: List[Union[ElementIdentifier, DiseaseOrPhenotypicFeatureId]] = empty_list()
    has_exposure_parts: List[Union[ElementIdentifier, DrugExposureId]] = empty_list()

    def __post_init__(self):
        if self.id is not None and not isinstance(self.id, TreatmentId):
            self.id = TreatmentId(self.id)
        super().__post_init__()


@dataclass
class GeographicLocation(PlanetaryEntity):
    """
    a location that can be described in lat/long coordinates
    """
    _inherited_slots: ClassVar[List[str]] = ["related_to", "interacts_with"]

    type_uri: ClassVar[str] = "https://w3id.org/biolink/vocab/GeographicLocation"
    type_curie: ClassVar[str] = "biolink:GeographicLocation"
    type_name: ClassVar[str] = "geographic location"

    id: Union[ElementIdentifier, GeographicLocationId] = None
    name: Union[str, LabelType] = None
    category: List[Union[str, IriType]] = empty_list()
    latitude: Optional[float] = None
    longitude: Optional[float] = None

    def __post_init__(self):
        if self.id is not None and not isinstance(self.id, GeographicLocationId):
            self.id = GeographicLocationId(self.id)
        super().__post_init__()


@dataclass
class GeographicLocationAtTime(GeographicLocation):
    """
    a location that can be described in lat/long coordinates, for a particular time
    """
    _inherited_slots: ClassVar[List[str]] = ["related_to", "interacts_with"]

    type_uri: ClassVar[str] = "https://w3id.org/biolink/vocab/GeographicLocationAtTime"
    type_curie: ClassVar[str] = "biolink:GeographicLocationAtTime"
    type_name: ClassVar[str] = "geographic location at time"

    id: Union[ElementIdentifier, GeographicLocationAtTimeId] = None
    name: Union[str, LabelType] = None
    category: List[Union[str, IriType]] = empty_list()
    timepoint: Optional[Union[str, TimeType]] = None

    def __post_init__(self):
        if self.id is not None and not isinstance(self.id, GeographicLocationAtTimeId):
            self.id = GeographicLocationAtTimeId(self.id)
        if self.timepoint is not None and not isinstance(self.timepoint, TimeType):
            self.timepoint = TimeType(self.timepoint)
        super().__post_init__()


@dataclass
class Association(YAMLRoot):
    """
    A typed association between two entities, supported by evidence
    """
    _inherited_slots: ClassVar[List[str]] = []

    type_uri: ClassVar[str] = "http://purl.org/oban/association"
    type_curie: ClassVar[str] = "OBAN:association"
    type_name: ClassVar[str] = "association"

    subject: Union[ElementIdentifier, NamedThingId]
    relation: Union[str, URIorCURIE]
    object: Union[ElementIdentifier, NamedThingId]
    edge_label: Union[str, LabelType]
    id: Union[ElementIdentifier, AssociationId] = bnode()
    negated: Optional[Bool] = None
    association_type: Optional[Union[ElementIdentifier, OntologyClassId]] = None
    qualifiers: List[Union[ElementIdentifier, OntologyClassId]] = empty_list()
    publications: List[Union[ElementIdentifier, PublicationId]] = empty_list()
    provided_by: Optional[Union[ElementIdentifier, ProviderId]] = None

    def __post_init__(self):
        if not isinstance(self.id, AssociationId):
            self.id = AssociationId(self.id)
        if not isinstance(self.subject, NamedThingId):
            self.subject = NamedThingId(self.subject)
        if not isinstance(self.relation, URIorCURIE):
            self.relation = URIorCURIE(self.relation)
        if not isinstance(self.object, NamedThingId):
            self.object = NamedThingId(self.object)
        if self.association_type is not None and not isinstance(self.association_type, OntologyClassId):
            self.association_type = OntologyClassId(self.association_type)
        self.qualifiers = [v if isinstance(v, OntologyClassId)
                           else OntologyClassId(v) for v in self.qualifiers]
        self.publications = [v if isinstance(v, PublicationId)
                             else PublicationId(v) for v in self.publications]
        if self.provided_by is not None and not isinstance(self.provided_by, ProviderId):
            self.provided_by = ProviderId(self.provided_by)
        super().__post_init__()


@dataclass
class GenotypeToGenotypePartAssociation(Association):
    """
    Any association between one genotype and a genotypic entity that is a sub-component of it
    """
    _inherited_slots: ClassVar[List[str]] = []

    type_uri: ClassVar[str] = "https://w3id.org/biolink/vocab/GenotypeToGenotypePartAssociation"
    type_curie: ClassVar[str] = "biolink:GenotypeToGenotypePartAssociation"
    type_name: ClassVar[str] = "genotype to genotype part association"

    subject: Union[ElementIdentifier, GenotypeId] = None
    relation: Union[str, URIorCURIE] = None
    object: Union[ElementIdentifier, GenotypeId] = None
    edge_label: Union[str, LabelType] = None
    id: Union[ElementIdentifier, GenotypeToGenotypePartAssociationId] = bnode()

    def __post_init__(self):
        if self.id is not None and not isinstance(self.id, GenotypeToGenotypePartAssociationId):
            self.id = GenotypeToGenotypePartAssociationId(self.id)
        if self.subject is not None and not isinstance(self.subject, GenotypeId):
            self.subject = GenotypeId(self.subject)
        if self.relation is not None and not isinstance(self.relation, URIorCURIE):
            self.relation = URIorCURIE(self.relation)
        if self.object is not None and not isinstance(self.object, GenotypeId):
            self.object = GenotypeId(self.object)
        super().__post_init__()


@dataclass
class GenotypeToGeneAssociation(Association):
    """
    Any association between a genotype and a gene. The genotype have have multiple variants in that gene or a single
    one. There is no assumption of cardinality
    """
    _inherited_slots: ClassVar[List[str]] = []

    type_uri: ClassVar[str] = "https://w3id.org/biolink/vocab/GenotypeToGeneAssociation"
    type_curie: ClassVar[str] = "biolink:GenotypeToGeneAssociation"
    type_name: ClassVar[str] = "genotype to gene association"

    subject: Union[ElementIdentifier, GenotypeId] = None
    relation: Union[str, URIorCURIE] = None
    object: Union[ElementIdentifier, GeneId] = None
    edge_label: Union[str, LabelType] = None
    id: Union[ElementIdentifier, GenotypeToGeneAssociationId] = bnode()

    def __post_init__(self):
        if self.id is not None and not isinstance(self.id, GenotypeToGeneAssociationId):
            self.id = GenotypeToGeneAssociationId(self.id)
        if self.subject is not None and not isinstance(self.subject, GenotypeId):
            self.subject = GenotypeId(self.subject)
        if self.relation is not None and not isinstance(self.relation, URIorCURIE):
            self.relation = URIorCURIE(self.relation)
        if self.object is not None and not isinstance(self.object, GeneId):
            self.object = GeneId(self.object)
        super().__post_init__()


@dataclass
class GenotypeToVariantAssociation(Association):
    """
    Any association between a genotype and a sequence variant.
    """
    _inherited_slots: ClassVar[List[str]] = []

    type_uri: ClassVar[str] = "https://w3id.org/biolink/vocab/GenotypeToVariantAssociation"
    type_curie: ClassVar[str] = "biolink:GenotypeToVariantAssociation"
    type_name: ClassVar[str] = "genotype to variant association"

    subject: Union[ElementIdentifier, GenotypeId] = None
    relation: Union[str, URIorCURIE] = None
    object: Union[ElementIdentifier, SequenceVariantId] = None
    edge_label: Union[str, LabelType] = None
    id: Union[ElementIdentifier, GenotypeToVariantAssociationId] = bnode()

    def __post_init__(self):
        if self.id is not None and not isinstance(self.id, GenotypeToVariantAssociationId):
            self.id = GenotypeToVariantAssociationId(self.id)
        if self.subject is not None and not isinstance(self.subject, GenotypeId):
            self.subject = GenotypeId(self.subject)
        if self.relation is not None and not isinstance(self.relation, URIorCURIE):
            self.relation = URIorCURIE(self.relation)
        if self.object is not None and not isinstance(self.object, SequenceVariantId):
            self.object = SequenceVariantId(self.object)
        super().__post_init__()


@dataclass
class GeneToGeneAssociation(Association):
    """
    abstract parent class for different kinds of gene-gene or gene product to gene product relationships. Includes
    homology and interaction.
    """
    _inherited_slots: ClassVar[List[str]] = []

    type_uri: ClassVar[str] = "https://w3id.org/biolink/vocab/GeneToGeneAssociation"
    type_curie: ClassVar[str] = "biolink:GeneToGeneAssociation"
    type_name: ClassVar[str] = "gene to gene association"

    subject: Union[ElementIdentifier, GeneOrGeneProductId] = None
    relation: Union[str, URIorCURIE] = None
    object: Union[ElementIdentifier, GeneOrGeneProductId] = None
    edge_label: Union[str, LabelType] = None
    id: Union[ElementIdentifier, GeneToGeneAssociationId] = bnode()

    def __post_init__(self):
        if self.subject is not None and not isinstance(self.subject, GeneOrGeneProductId):
            self.subject = GeneOrGeneProductId(self.subject)
        if self.object is not None and not isinstance(self.object, GeneOrGeneProductId):
            self.object = GeneOrGeneProductId(self.object)
        super().__post_init__()


@dataclass
class GeneToGeneHomologyAssociation(GeneToGeneAssociation):
    """
    A homology association between two genes. May be orthology (in which case the species of subject and object should
    differ) or paralogy (in which case the species may be the same)
    """
    _inherited_slots: ClassVar[List[str]] = []

    type_uri: ClassVar[str] = "https://w3id.org/biolink/vocab/GeneToGeneHomologyAssociation"
    type_curie: ClassVar[str] = "biolink:GeneToGeneHomologyAssociation"
    type_name: ClassVar[str] = "gene to gene homology association"

    subject: Union[ElementIdentifier, GeneOrGeneProductId] = None
    relation: Union[str, URIorCURIE] = None
    object: Union[ElementIdentifier, GeneOrGeneProductId] = None
    edge_label: Union[str, LabelType] = None
    id: Union[ElementIdentifier, GeneToGeneHomologyAssociationId] = bnode()

    def __post_init__(self):
        if self.id is not None and not isinstance(self.id, GeneToGeneHomologyAssociationId):
            self.id = GeneToGeneHomologyAssociationId(self.id)
        if self.relation is not None and not isinstance(self.relation, URIorCURIE):
            self.relation = URIorCURIE(self.relation)
        super().__post_init__()


@dataclass
class PairwiseGeneToGeneInteraction(GeneToGeneAssociation):
    """
    An interaction between two genes or two gene products. May be physical (e.g. protein binding) or genetic (between
    genes). May be symmetric (e.g. protein interaction) or directed (e.g. phosphorylation)
    """
    _inherited_slots: ClassVar[List[str]] = []

    type_uri: ClassVar[str] = "https://w3id.org/biolink/vocab/PairwiseGeneToGeneInteraction"
    type_curie: ClassVar[str] = "biolink:PairwiseGeneToGeneInteraction"
    type_name: ClassVar[str] = "pairwise gene to gene interaction"

    subject: Union[ElementIdentifier, GeneOrGeneProductId] = None
    relation: Union[str, URIorCURIE] = None
    object: Union[ElementIdentifier, GeneOrGeneProductId] = None
    edge_label: Union[str, LabelType] = None
    id: Union[ElementIdentifier, PairwiseGeneToGeneInteractionId] = bnode()

    def __post_init__(self):
        if self.id is not None and not isinstance(self.id, PairwiseGeneToGeneInteractionId):
            self.id = PairwiseGeneToGeneInteractionId(self.id)
        if self.relation is not None and not isinstance(self.relation, URIorCURIE):
            self.relation = URIorCURIE(self.relation)
        super().__post_init__()


@dataclass
class CellLineToThingAssociation(Association):
    """
    An relationship between a cell line and another entity
    """
    _inherited_slots: ClassVar[List[str]] = []

    type_uri: ClassVar[str] = "https://w3id.org/biolink/vocab/CellLineToThingAssociation"
    type_curie: ClassVar[str] = "biolink:CellLineToThingAssociation"
    type_name: ClassVar[str] = "cell line to thing association"

    subject: Union[ElementIdentifier, CellLineId] = None
    relation: Union[str, URIorCURIE] = None
    object: Union[ElementIdentifier, NamedThingId] = None
    edge_label: Union[str, LabelType] = None
    id: Union[ElementIdentifier, CellLineToThingAssociationId] = bnode()

    def __post_init__(self):
        if self.subject is not None and not isinstance(self.subject, CellLineId):
            self.subject = CellLineId(self.subject)
        super().__post_init__()


@dataclass
class CellLineToDiseaseOrPhenotypicFeatureAssociation(Association):
    """
    An relationship between a cell line and a disease or a phenotype, where the cell line is derived from an
    individual with that disease or phenotype
    """
    _inherited_slots: ClassVar[List[str]] = []

    type_uri: ClassVar[str] = "https://w3id.org/biolink/vocab/CellLineToDiseaseOrPhenotypicFeatureAssociation"
    type_curie: ClassVar[str] = "biolink:CellLineToDiseaseOrPhenotypicFeatureAssociation"
    type_name: ClassVar[str] = "cell line to disease or phenotypic feature association"

    subject: Union[ElementIdentifier, DiseaseOrPhenotypicFeatureId] = None
    relation: Union[str, URIorCURIE] = None
    object: Union[ElementIdentifier, NamedThingId] = None
    edge_label: Union[str, LabelType] = None
    id: Union[ElementIdentifier, CellLineToDiseaseOrPhenotypicFeatureAssociationId] = bnode()

    def __post_init__(self):
        if self.id is not None and not isinstance(self.id, CellLineToDiseaseOrPhenotypicFeatureAssociationId):
            self.id = CellLineToDiseaseOrPhenotypicFeatureAssociationId(self.id)
        if self.subject is not None and not isinstance(self.subject, DiseaseOrPhenotypicFeatureId):
            self.subject = DiseaseOrPhenotypicFeatureId(self.subject)
        super().__post_init__()


@dataclass
class ChemicalToThingAssociation(Association):
    """
    An interaction between a chemical entity and another entity
    """
    _inherited_slots: ClassVar[List[str]] = []

    type_uri: ClassVar[str] = "https://w3id.org/biolink/vocab/ChemicalToThingAssociation"
    type_curie: ClassVar[str] = "biolink:ChemicalToThingAssociation"
    type_name: ClassVar[str] = "chemical to thing association"

    subject: Union[ElementIdentifier, ChemicalSubstanceId] = None
    relation: Union[str, URIorCURIE] = None
    object: Union[ElementIdentifier, NamedThingId] = None
    edge_label: Union[str, LabelType] = None
    id: Union[ElementIdentifier, ChemicalToThingAssociationId] = bnode()

    def __post_init__(self):
        if self.subject is not None and not isinstance(self.subject, ChemicalSubstanceId):
            self.subject = ChemicalSubstanceId(self.subject)
        super().__post_init__()


@dataclass
class CaseToThingAssociation(Association):
    """
    An abstract association for use where the case is the subject
    """
    _inherited_slots: ClassVar[List[str]] = []

    type_uri: ClassVar[str] = "https://w3id.org/biolink/vocab/CaseToThingAssociation"
    type_curie: ClassVar[str] = "biolink:CaseToThingAssociation"
    type_name: ClassVar[str] = "case to thing association"

    subject: Union[ElementIdentifier, CaseId] = None
    relation: Union[str, URIorCURIE] = None
    object: Union[ElementIdentifier, NamedThingId] = None
    edge_label: Union[str, LabelType] = None
    id: Union[ElementIdentifier, CaseToThingAssociationId] = bnode()

    def __post_init__(self):
        if self.subject is not None and not isinstance(self.subject, CaseId):
            self.subject = CaseId(self.subject)
        super().__post_init__()


@dataclass
class ChemicalToDiseaseOrPhenotypicFeatureAssociation(Association):
    """
    An interaction between a chemical entity and a phenotype or disease, where the presence of the chemical gives rise
    to or exacerbates the phenotype
    """
    _inherited_slots: ClassVar[List[str]] = []

    type_uri: ClassVar[str] = "http://semanticscience.org/resource/SIO_000993"
    type_curie: ClassVar[str] = "SIO:000993"
    type_name: ClassVar[str] = "chemical to disease or phenotypic feature association"

    subject: Union[ElementIdentifier, NamedThingId] = None
    relation: Union[str, URIorCURIE] = None
    object: Union[ElementIdentifier, DiseaseOrPhenotypicFeatureId] = None
    edge_label: Union[str, LabelType] = None
    id: Union[ElementIdentifier, ChemicalToDiseaseOrPhenotypicFeatureAssociationId] = bnode()

    def __post_init__(self):
        if self.id is not None and not isinstance(self.id, ChemicalToDiseaseOrPhenotypicFeatureAssociationId):
            self.id = ChemicalToDiseaseOrPhenotypicFeatureAssociationId(self.id)
        if self.object is not None and not isinstance(self.object, DiseaseOrPhenotypicFeatureId):
            self.object = DiseaseOrPhenotypicFeatureId(self.object)
        super().__post_init__()


@dataclass
class ChemicalToPathwayAssociation(Association):
    """
    An interaction between a chemical entity and a biological process or pathway
    """
    _inherited_slots: ClassVar[List[str]] = []

    type_uri: ClassVar[str] = "http://semanticscience.org/resource/SIO_001250"
    type_curie: ClassVar[str] = "SIO:001250"
    type_name: ClassVar[str] = "chemical to pathway association"

    subject: Union[ElementIdentifier, NamedThingId] = None
    relation: Union[str, URIorCURIE] = None
    object: Union[ElementIdentifier, PathwayId] = None
    edge_label: Union[str, LabelType] = None
    id: Union[ElementIdentifier, ChemicalToPathwayAssociationId] = bnode()

    def __post_init__(self):
        if self.id is not None and not isinstance(self.id, ChemicalToPathwayAssociationId):
            self.id = ChemicalToPathwayAssociationId(self.id)
        if self.object is not None and not isinstance(self.object, PathwayId):
            self.object = PathwayId(self.object)
        super().__post_init__()


@dataclass
class ChemicalToGeneAssociation(Association):
    """
    An interaction between a chemical entity and a gene or gene product
    """
    _inherited_slots: ClassVar[List[str]] = []

    type_uri: ClassVar[str] = "http://semanticscience.org/resource/SIO_001257"
    type_curie: ClassVar[str] = "SIO:001257"
    type_name: ClassVar[str] = "chemical to gene association"

    subject: Union[ElementIdentifier, NamedThingId] = None
    relation: Union[str, URIorCURIE] = None
    object: Union[ElementIdentifier, GeneOrGeneProductId] = None
    edge_label: Union[str, LabelType] = None
    id: Union[ElementIdentifier, ChemicalToGeneAssociationId] = bnode()

    def __post_init__(self):
        if self.id is not None and not isinstance(self.id, ChemicalToGeneAssociationId):
            self.id = ChemicalToGeneAssociationId(self.id)
        if self.object is not None and not isinstance(self.object, GeneOrGeneProductId):
            self.object = GeneOrGeneProductId(self.object)
        super().__post_init__()


@dataclass
class BiosampleToThingAssociation(Association):
    """
    An association between a biosample and something
    """
    _inherited_slots: ClassVar[List[str]] = []

    type_uri: ClassVar[str] = "https://w3id.org/biolink/vocab/BiosampleToThingAssociation"
    type_curie: ClassVar[str] = "biolink:BiosampleToThingAssociation"
    type_name: ClassVar[str] = "biosample to thing association"

    subject: Union[ElementIdentifier, BiosampleId] = None
    relation: Union[str, URIorCURIE] = None
    object: Union[ElementIdentifier, NamedThingId] = None
    edge_label: Union[str, LabelType] = None
    id: Union[ElementIdentifier, BiosampleToThingAssociationId] = bnode()

    def __post_init__(self):
        if self.subject is not None and not isinstance(self.subject, BiosampleId):
            self.subject = BiosampleId(self.subject)
        super().__post_init__()


@dataclass
class BiosampleToDiseaseOrPhenotypicFeatureAssociation(Association):
    """
    An association between a biosample and a disease or phenotype
    """
    _inherited_slots: ClassVar[List[str]] = []

    type_uri: ClassVar[str] = "https://w3id.org/biolink/vocab/BiosampleToDiseaseOrPhenotypicFeatureAssociation"
    type_curie: ClassVar[str] = "biolink:BiosampleToDiseaseOrPhenotypicFeatureAssociation"
    type_name: ClassVar[str] = "biosample to disease or phenotypic feature association"

    subject: Union[ElementIdentifier, NamedThingId] = None
    relation: Union[str, URIorCURIE] = None
    object: Union[ElementIdentifier, NamedThingId] = None
    edge_label: Union[str, LabelType] = None
    id: Union[ElementIdentifier, BiosampleToDiseaseOrPhenotypicFeatureAssociationId] = bnode()

    def __post_init__(self):
        if self.id is not None and not isinstance(self.id, BiosampleToDiseaseOrPhenotypicFeatureAssociationId):
            self.id = BiosampleToDiseaseOrPhenotypicFeatureAssociationId(self.id)
        super().__post_init__()


@dataclass
class EntityToPhenotypicFeatureAssociation(Association):
    _inherited_slots: ClassVar[List[str]] = []

    type_uri: ClassVar[str] = "https://w3id.org/biolink/vocab/EntityToPhenotypicFeatureAssociation"
    type_curie: ClassVar[str] = "biolink:EntityToPhenotypicFeatureAssociation"
    type_name: ClassVar[str] = "entity to phenotypic feature association"

    subject: Union[ElementIdentifier, NamedThingId] = None
    relation: Union[str, URIorCURIE] = None
    object: Union[ElementIdentifier, PhenotypicFeatureId] = None
    edge_label: Union[str, LabelType] = None
    id: Union[ElementIdentifier, EntityToPhenotypicFeatureAssociationId] = bnode()
    sex_qualifier: Optional[Union[ElementIdentifier, BiologicalSexId]] = None

    def __post_init__(self):
        if self.object is not None and not isinstance(self.object, PhenotypicFeatureId):
            self.object = PhenotypicFeatureId(self.object)
        if self.sex_qualifier is not None and not isinstance(self.sex_qualifier, BiologicalSexId):
            self.sex_qualifier = BiologicalSexId(self.sex_qualifier)
        super().__post_init__()


@dataclass
class DiseaseOrPhenotypicFeatureAssociationToThingAssociation(Association):
    _inherited_slots: ClassVar[List[str]] = []

    type_uri: ClassVar[str] = "https://w3id.org/biolink/vocab/DiseaseOrPhenotypicFeatureAssociationToThingAssociation"
    type_curie: ClassVar[str] = "biolink:DiseaseOrPhenotypicFeatureAssociationToThingAssociation"
    type_name: ClassVar[str] = "disease or phenotypic feature association to thing association"

    subject: Union[ElementIdentifier, DiseaseOrPhenotypicFeatureId] = None
    relation: Union[str, URIorCURIE] = None
    object: Union[ElementIdentifier, NamedThingId] = None
    edge_label: Union[str, LabelType] = None
    id: Union[ElementIdentifier, DiseaseOrPhenotypicFeatureAssociationToThingAssociationId] = bnode()

    def __post_init__(self):
        if self.subject is not None and not isinstance(self.subject, DiseaseOrPhenotypicFeatureId):
            self.subject = DiseaseOrPhenotypicFeatureId(self.subject)
        super().__post_init__()


@dataclass
class DiseaseOrPhenotypicFeatureAssociationToLocationAssociation(DiseaseOrPhenotypicFeatureAssociationToThingAssociation):
    """
    An association between either a disease or a phenotypic feature and an anatomical entity, where the
    disease/feature manifests in that site.
    """
    _inherited_slots: ClassVar[List[str]] = []

    type_uri: ClassVar[str] = "http://purl.obolibrary.org/obo/NCIT_R100"
    type_curie: ClassVar[str] = "NCIT:R100"
    type_name: ClassVar[str] = "disease or phenotypic feature association to location association"

    subject: Union[ElementIdentifier, DiseaseOrPhenotypicFeatureId] = None
    relation: Union[str, URIorCURIE] = None
    object: Union[ElementIdentifier, AnatomicalEntityId] = None
    edge_label: Union[str, LabelType] = None
    id: Union[ElementIdentifier, DiseaseOrPhenotypicFeatureAssociationToLocationAssociationId] = bnode()

    def __post_init__(self):
        if self.id is not None and not isinstance(self.id, DiseaseOrPhenotypicFeatureAssociationToLocationAssociationId):
            self.id = DiseaseOrPhenotypicFeatureAssociationToLocationAssociationId(self.id)
        if self.object is not None and not isinstance(self.object, AnatomicalEntityId):
            self.object = AnatomicalEntityId(self.object)
        super().__post_init__()


@dataclass
class ThingToDiseaseOrPhenotypicFeatureAssociation(Association):
    _inherited_slots: ClassVar[List[str]] = []

    type_uri: ClassVar[str] = "https://w3id.org/biolink/vocab/ThingToDiseaseOrPhenotypicFeatureAssociation"
    type_curie: ClassVar[str] = "biolink:ThingToDiseaseOrPhenotypicFeatureAssociation"
    type_name: ClassVar[str] = "thing to disease or phenotypic feature association"

    subject: Union[ElementIdentifier, NamedThingId] = None
    relation: Union[str, URIorCURIE] = None
    object: Union[ElementIdentifier, DiseaseOrPhenotypicFeatureId] = None
    edge_label: Union[str, LabelType] = None
    id: Union[ElementIdentifier, ThingToDiseaseOrPhenotypicFeatureAssociationId] = bnode()

    def __post_init__(self):
        if self.object is not None and not isinstance(self.object, DiseaseOrPhenotypicFeatureId):
            self.object = DiseaseOrPhenotypicFeatureId(self.object)
        super().__post_init__()


@dataclass
class DiseaseToThingAssociation(Association):
    _inherited_slots: ClassVar[List[str]] = []

    type_uri: ClassVar[str] = "https://w3id.org/biolink/vocab/DiseaseToThingAssociation"
    type_curie: ClassVar[str] = "biolink:DiseaseToThingAssociation"
    type_name: ClassVar[str] = "disease to thing association"

    subject: Union[ElementIdentifier, DiseaseId] = None
    relation: Union[str, URIorCURIE] = None
    object: Union[ElementIdentifier, NamedThingId] = None
    edge_label: Union[str, LabelType] = None
    id: Union[ElementIdentifier, DiseaseToThingAssociationId] = bnode()

    def __post_init__(self):
        if self.subject is not None and not isinstance(self.subject, DiseaseId):
            self.subject = DiseaseId(self.subject)
        super().__post_init__()


@dataclass
class GenotypeToPhenotypicFeatureAssociation(Association):
    """
    Any association between one genotype and a phenotypic feature, where having the genotype confers the phenotype,
    either in isolation or through environment
    """
    _inherited_slots: ClassVar[List[str]] = []

    type_uri: ClassVar[str] = "https://w3id.org/biolink/vocab/GenotypeToPhenotypicFeatureAssociation"
    type_curie: ClassVar[str] = "biolink:GenotypeToPhenotypicFeatureAssociation"
    type_name: ClassVar[str] = "genotype to phenotypic feature association"

    subject: Union[ElementIdentifier, GenotypeId] = None
    relation: Union[str, URIorCURIE] = None
    object: Union[ElementIdentifier, NamedThingId] = None
    edge_label: Union[str, LabelType] = None
    id: Union[ElementIdentifier, GenotypeToPhenotypicFeatureAssociationId] = bnode()

    def __post_init__(self):
        if self.id is not None and not isinstance(self.id, GenotypeToPhenotypicFeatureAssociationId):
            self.id = GenotypeToPhenotypicFeatureAssociationId(self.id)
        if self.subject is not None and not isinstance(self.subject, GenotypeId):
            self.subject = GenotypeId(self.subject)
        if self.relation is not None and not isinstance(self.relation, URIorCURIE):
            self.relation = URIorCURIE(self.relation)
        super().__post_init__()


@dataclass
class EnvironmentToPhenotypicFeatureAssociation(Association):
    """
    Any association between an environment and a phenotypic feature, where being in the environment influences the
    phenotype
    """
    _inherited_slots: ClassVar[List[str]] = []

    type_uri: ClassVar[str] = "https://w3id.org/biolink/vocab/EnvironmentToPhenotypicFeatureAssociation"
    type_curie: ClassVar[str] = "biolink:EnvironmentToPhenotypicFeatureAssociation"
    type_name: ClassVar[str] = "environment to phenotypic feature association"

    subject: Union[ElementIdentifier, EnvironmentId] = None
    relation: Union[str, URIorCURIE] = None
    object: Union[ElementIdentifier, NamedThingId] = None
    edge_label: Union[str, LabelType] = None
    id: Union[ElementIdentifier, EnvironmentToPhenotypicFeatureAssociationId] = bnode()

    def __post_init__(self):
        if self.id is not None and not isinstance(self.id, EnvironmentToPhenotypicFeatureAssociationId):
            self.id = EnvironmentToPhenotypicFeatureAssociationId(self.id)
        if self.subject is not None and not isinstance(self.subject, EnvironmentId):
            self.subject = EnvironmentId(self.subject)
        super().__post_init__()


@dataclass
class DiseaseToPhenotypicFeatureAssociation(Association):
    """
    An association between a disease and a phenotypic feature in which the phenotypic feature is associated with the
    disease in some way
    """
    _inherited_slots: ClassVar[List[str]] = []

    type_uri: ClassVar[str] = "https://w3id.org/biolink/vocab/DiseaseToPhenotypicFeatureAssociation"
    type_curie: ClassVar[str] = "biolink:DiseaseToPhenotypicFeatureAssociation"
    type_name: ClassVar[str] = "disease to phenotypic feature association"

    subject: Union[ElementIdentifier, NamedThingId] = None
    relation: Union[str, URIorCURIE] = None
    object: Union[ElementIdentifier, NamedThingId] = None
    edge_label: Union[str, LabelType] = None
    id: Union[ElementIdentifier, DiseaseToPhenotypicFeatureAssociationId] = bnode()

    def __post_init__(self):
        if self.id is not None and not isinstance(self.id, DiseaseToPhenotypicFeatureAssociationId):
            self.id = DiseaseToPhenotypicFeatureAssociationId(self.id)
        super().__post_init__()


@dataclass
class CaseToPhenotypicFeatureAssociation(Association):
    """
    An association between a case (e.g. individual patient) and a phenotypic feature in which the individual has or
    has had the phenotype
    """
    _inherited_slots: ClassVar[List[str]] = []

    type_uri: ClassVar[str] = "https://w3id.org/biolink/vocab/CaseToPhenotypicFeatureAssociation"
    type_curie: ClassVar[str] = "biolink:CaseToPhenotypicFeatureAssociation"
    type_name: ClassVar[str] = "case to phenotypic feature association"

    subject: Union[ElementIdentifier, NamedThingId] = None
    relation: Union[str, URIorCURIE] = None
    object: Union[ElementIdentifier, NamedThingId] = None
    edge_label: Union[str, LabelType] = None
    id: Union[ElementIdentifier, CaseToPhenotypicFeatureAssociationId] = bnode()

    def __post_init__(self):
        if self.id is not None and not isinstance(self.id, CaseToPhenotypicFeatureAssociationId):
            self.id = CaseToPhenotypicFeatureAssociationId(self.id)
        super().__post_init__()


@dataclass
class GeneToThingAssociation(Association):
    _inherited_slots: ClassVar[List[str]] = []

    type_uri: ClassVar[str] = "https://w3id.org/biolink/vocab/GeneToThingAssociation"
    type_curie: ClassVar[str] = "biolink:GeneToThingAssociation"
    type_name: ClassVar[str] = "gene to thing association"

    subject: Union[ElementIdentifier, GeneOrGeneProductId] = None
    relation: Union[str, URIorCURIE] = None
    object: Union[ElementIdentifier, NamedThingId] = None
    edge_label: Union[str, LabelType] = None
    id: Union[ElementIdentifier, GeneToThingAssociationId] = bnode()

    def __post_init__(self):
        if self.subject is not None and not isinstance(self.subject, GeneOrGeneProductId):
            self.subject = GeneOrGeneProductId(self.subject)
        super().__post_init__()


@dataclass
class GeneToPhenotypicFeatureAssociation(Association):
    _inherited_slots: ClassVar[List[str]] = []

    type_uri: ClassVar[str] = "http://bio2rdf.org/wormbase_vocabulary:Gene-Phenotype-Association"
    type_curie: ClassVar[str] = None
    type_name: ClassVar[str] = "gene to phenotypic feature association"

    subject: Union[ElementIdentifier, GeneOrGeneProductId] = None
    relation: Union[str, URIorCURIE] = None
    object: Union[ElementIdentifier, NamedThingId] = None
    edge_label: Union[str, LabelType] = None
    id: Union[ElementIdentifier, GeneToPhenotypicFeatureAssociationId] = bnode()

    def __post_init__(self):
        if self.id is not None and not isinstance(self.id, GeneToPhenotypicFeatureAssociationId):
            self.id = GeneToPhenotypicFeatureAssociationId(self.id)
        if self.subject is not None and not isinstance(self.subject, GeneOrGeneProductId):
            self.subject = GeneOrGeneProductId(self.subject)
        super().__post_init__()


@dataclass
class GeneToDiseaseAssociation(Association):
    _inherited_slots: ClassVar[List[str]] = []

    type_uri: ClassVar[str] = "http://semanticscience.org/resource/SIO_000983"
    type_curie: ClassVar[str] = "SIO:000983"
    type_name: ClassVar[str] = "gene to disease association"

    subject: Union[ElementIdentifier, GeneOrGeneProductId] = None
    relation: Union[str, URIorCURIE] = None
    object: Union[ElementIdentifier, NamedThingId] = None
    edge_label: Union[str, LabelType] = None
    id: Union[ElementIdentifier, GeneToDiseaseAssociationId] = bnode()

    def __post_init__(self):
        if self.id is not None and not isinstance(self.id, GeneToDiseaseAssociationId):
            self.id = GeneToDiseaseAssociationId(self.id)
        if self.subject is not None and not isinstance(self.subject, GeneOrGeneProductId):
            self.subject = GeneOrGeneProductId(self.subject)
        super().__post_init__()


@dataclass
class VariantToPopulationAssociation(Association):
    """
    An association between a variant and a population, where the variant has particular frequency in the population
    """
    _inherited_slots: ClassVar[List[str]] = []

    type_uri: ClassVar[str] = "https://w3id.org/biolink/vocab/VariantToPopulationAssociation"
    type_curie: ClassVar[str] = "biolink:VariantToPopulationAssociation"
    type_name: ClassVar[str] = "variant to population association"

    subject: Union[ElementIdentifier, SequenceVariantId] = None
    relation: Union[str, URIorCURIE] = None
    object: Union[ElementIdentifier, PopulationOfIndividualOrganismsId] = None
    edge_label: Union[str, LabelType] = None
    id: Union[ElementIdentifier, VariantToPopulationAssociationId] = bnode()
    has_count: Optional[int] = None
    has_total: Optional[int] = None
    has_quotient: Optional[float] = None

    def __post_init__(self):
        if self.id is not None and not isinstance(self.id, VariantToPopulationAssociationId):
            self.id = VariantToPopulationAssociationId(self.id)
        if self.subject is not None and not isinstance(self.subject, SequenceVariantId):
            self.subject = SequenceVariantId(self.subject)
        if self.object is not None and not isinstance(self.object, PopulationOfIndividualOrganismsId):
            self.object = PopulationOfIndividualOrganismsId(self.object)
        super().__post_init__()


@dataclass
class PopulationToPopulationAssociation(Association):
    """
    An association between a two populations
    """
    _inherited_slots: ClassVar[List[str]] = []

    type_uri: ClassVar[str] = "https://w3id.org/biolink/vocab/PopulationToPopulationAssociation"
    type_curie: ClassVar[str] = "biolink:PopulationToPopulationAssociation"
    type_name: ClassVar[str] = "population to population association"

    subject: Union[ElementIdentifier, PopulationOfIndividualOrganismsId] = None
    relation: Union[str, URIorCURIE] = None
    object: Union[ElementIdentifier, PopulationOfIndividualOrganismsId] = None
    edge_label: Union[str, LabelType] = None
    id: Union[ElementIdentifier, PopulationToPopulationAssociationId] = bnode()

    def __post_init__(self):
        if self.id is not None and not isinstance(self.id, PopulationToPopulationAssociationId):
            self.id = PopulationToPopulationAssociationId(self.id)
        if self.subject is not None and not isinstance(self.subject, PopulationOfIndividualOrganismsId):
            self.subject = PopulationOfIndividualOrganismsId(self.subject)
        if self.relation is not None and not isinstance(self.relation, URIorCURIE):
            self.relation = URIorCURIE(self.relation)
        if self.object is not None and not isinstance(self.object, PopulationOfIndividualOrganismsId):
            self.object = PopulationOfIndividualOrganismsId(self.object)
        super().__post_init__()


@dataclass
class VariantToPhenotypicFeatureAssociation(Association):
    _inherited_slots: ClassVar[List[str]] = []

    type_uri: ClassVar[str] = "https://w3id.org/biolink/vocab/VariantToPhenotypicFeatureAssociation"
    type_curie: ClassVar[str] = "biolink:VariantToPhenotypicFeatureAssociation"
    type_name: ClassVar[str] = "variant to phenotypic feature association"

    subject: Union[ElementIdentifier, SequenceVariantId] = None
    relation: Union[str, URIorCURIE] = None
    object: Union[ElementIdentifier, NamedThingId] = None
    edge_label: Union[str, LabelType] = None
    id: Union[ElementIdentifier, VariantToPhenotypicFeatureAssociationId] = bnode()

    def __post_init__(self):
        if self.id is not None and not isinstance(self.id, VariantToPhenotypicFeatureAssociationId):
            self.id = VariantToPhenotypicFeatureAssociationId(self.id)
        if self.subject is not None and not isinstance(self.subject, SequenceVariantId):
            self.subject = SequenceVariantId(self.subject)
        super().__post_init__()


@dataclass
class VariantToDiseaseAssociation(Association):
    _inherited_slots: ClassVar[List[str]] = []

    type_uri: ClassVar[str] = "https://w3id.org/biolink/vocab/VariantToDiseaseAssociation"
    type_curie: ClassVar[str] = "biolink:VariantToDiseaseAssociation"
    type_name: ClassVar[str] = "variant to disease association"

    subject: Union[ElementIdentifier, NamedThingId] = None
    relation: Union[str, URIorCURIE] = None
    object: Union[ElementIdentifier, NamedThingId] = None
    edge_label: Union[str, LabelType] = None
    id: Union[ElementIdentifier, VariantToDiseaseAssociationId] = bnode()

    def __post_init__(self):
        if self.id is not None and not isinstance(self.id, VariantToDiseaseAssociationId):
            self.id = VariantToDiseaseAssociationId(self.id)
        if self.subject is not None and not isinstance(self.subject, NamedThingId):
            self.subject = NamedThingId(self.subject)
        if self.relation is not None and not isinstance(self.relation, URIorCURIE):
            self.relation = URIorCURIE(self.relation)
        if self.object is not None and not isinstance(self.object, NamedThingId):
            self.object = NamedThingId(self.object)
        super().__post_init__()


@dataclass
class GeneAsAModelOfDiseaseAssociation(GeneToDiseaseAssociation):
    _inherited_slots: ClassVar[List[str]] = []

    type_uri: ClassVar[str] = "https://w3id.org/biolink/vocab/GeneAsAModelOfDiseaseAssociation"
    type_curie: ClassVar[str] = "biolink:GeneAsAModelOfDiseaseAssociation"
    type_name: ClassVar[str] = "gene as a model of disease association"

    subject: Union[ElementIdentifier, GeneOrGeneProductId] = None
    relation: Union[str, URIorCURIE] = None
    object: Union[ElementIdentifier, NamedThingId] = None
    edge_label: Union[str, LabelType] = None
    id: Union[ElementIdentifier, GeneAsAModelOfDiseaseAssociationId] = bnode()

    def __post_init__(self):
        if self.id is not None and not isinstance(self.id, GeneAsAModelOfDiseaseAssociationId):
            self.id = GeneAsAModelOfDiseaseAssociationId(self.id)
        if self.subject is not None and not isinstance(self.subject, GeneOrGeneProductId):
            self.subject = GeneOrGeneProductId(self.subject)
        super().__post_init__()


@dataclass
class GeneHasVariantThatContributesToDiseaseAssociation(GeneToDiseaseAssociation):
    _inherited_slots: ClassVar[List[str]] = []

    type_uri: ClassVar[str] = "https://w3id.org/biolink/vocab/GeneHasVariantThatContributesToDiseaseAssociation"
    type_curie: ClassVar[str] = "biolink:GeneHasVariantThatContributesToDiseaseAssociation"
    type_name: ClassVar[str] = "gene has variant that contributes to disease association"

    subject: Union[ElementIdentifier, GeneOrGeneProductId] = None
    relation: Union[str, URIorCURIE] = None
    object: Union[ElementIdentifier, NamedThingId] = None
    edge_label: Union[str, LabelType] = None
    id: Union[ElementIdentifier, GeneHasVariantThatContributesToDiseaseAssociationId] = bnode()
    sequence_variant_qualifier: Optional[Union[ElementIdentifier, SequenceVariantId]] = None

    def __post_init__(self):
        if self.id is not None and not isinstance(self.id, GeneHasVariantThatContributesToDiseaseAssociationId):
            self.id = GeneHasVariantThatContributesToDiseaseAssociationId(self.id)
        if self.subject is not None and not isinstance(self.subject, GeneOrGeneProductId):
            self.subject = GeneOrGeneProductId(self.subject)
        if self.sequence_variant_qualifier is not None and not isinstance(self.sequence_variant_qualifier, SequenceVariantId):
            self.sequence_variant_qualifier = SequenceVariantId(self.sequence_variant_qualifier)
        super().__post_init__()


@dataclass
class GenotypeToThingAssociation(Association):
    _inherited_slots: ClassVar[List[str]] = []

    type_uri: ClassVar[str] = "https://w3id.org/biolink/vocab/GenotypeToThingAssociation"
    type_curie: ClassVar[str] = "biolink:GenotypeToThingAssociation"
    type_name: ClassVar[str] = "genotype to thing association"

    subject: Union[ElementIdentifier, GenotypeId] = None
    relation: Union[str, URIorCURIE] = None
    object: Union[ElementIdentifier, NamedThingId] = None
    edge_label: Union[str, LabelType] = None
    id: Union[ElementIdentifier, GenotypeToThingAssociationId] = bnode()

    def __post_init__(self):
        if self.subject is not None and not isinstance(self.subject, GenotypeId):
            self.subject = GenotypeId(self.subject)
        super().__post_init__()


@dataclass
class GeneToExpressionSiteAssociation(Association):
    """
    An association between a gene and an expression site, possibly qualified by stage/timing info.
    """
    _inherited_slots: ClassVar[List[str]] = []

    type_uri: ClassVar[str] = "https://w3id.org/biolink/vocab/GeneToExpressionSiteAssociation"
    type_curie: ClassVar[str] = "biolink:GeneToExpressionSiteAssociation"
    type_name: ClassVar[str] = "gene to expression site association"

    subject: Union[ElementIdentifier, GeneOrGeneProductId] = None
    relation: Union[str, URIorCURIE] = None
    object: Union[ElementIdentifier, AnatomicalEntityId] = None
    edge_label: Union[str, LabelType] = None
    id: Union[ElementIdentifier, GeneToExpressionSiteAssociationId] = bnode()
    stage_qualifier: Optional[Union[ElementIdentifier, LifeStageId]] = None
    quantifier_qualifier: Optional[Union[ElementIdentifier, OntologyClassId]] = None

    def __post_init__(self):
        if self.id is not None and not isinstance(self.id, GeneToExpressionSiteAssociationId):
            self.id = GeneToExpressionSiteAssociationId(self.id)
        if self.subject is not None and not isinstance(self.subject, GeneOrGeneProductId):
            self.subject = GeneOrGeneProductId(self.subject)
        if self.relation is not None and not isinstance(self.relation, URIorCURIE):
            self.relation = URIorCURIE(self.relation)
        if self.object is not None and not isinstance(self.object, AnatomicalEntityId):
            self.object = AnatomicalEntityId(self.object)
        if self.stage_qualifier is not None and not isinstance(self.stage_qualifier, LifeStageId):
            self.stage_qualifier = LifeStageId(self.stage_qualifier)
        if self.quantifier_qualifier is not None and not isinstance(self.quantifier_qualifier, OntologyClassId):
            self.quantifier_qualifier = OntologyClassId(self.quantifier_qualifier)
        super().__post_init__()


@dataclass
class SequenceVariantModulatesTreatmentAssociation(Association):
    """
    An association between a sequence variant and a treatment or health intervention. The treatment object itself
    encompasses both the disease and the drug used.
    """
    _inherited_slots: ClassVar[List[str]] = []

    type_uri: ClassVar[str] = "https://w3id.org/biolink/vocab/SequenceVariantModulatesTreatmentAssociation"
    type_curie: ClassVar[str] = "biolink:SequenceVariantModulatesTreatmentAssociation"
    type_name: ClassVar[str] = "sequence variant modulates treatment association"

    subject: Union[ElementIdentifier, SequenceVariantId] = None
    relation: Union[str, URIorCURIE] = None
    object: Union[ElementIdentifier, TreatmentId] = None
    edge_label: Union[str, LabelType] = None
    id: Union[ElementIdentifier, SequenceVariantModulatesTreatmentAssociationId] = bnode()

    def __post_init__(self):
        if self.subject is not None and not isinstance(self.subject, SequenceVariantId):
            self.subject = SequenceVariantId(self.subject)
        if self.object is not None and not isinstance(self.object, TreatmentId):
            self.object = TreatmentId(self.object)
        super().__post_init__()


@dataclass
class FunctionalAssociation(Association):
    """
    An association between a macromolecular machine (gene, gene product or complex of gene products) and either a
    molecular activity, a biological process or a cellular location in which a function is executed
    """
    _inherited_slots: ClassVar[List[str]] = []

    type_uri: ClassVar[str] = "https://w3id.org/biolink/vocab/FunctionalAssociation"
    type_curie: ClassVar[str] = "biolink:FunctionalAssociation"
    type_name: ClassVar[str] = "functional association"

    subject: Union[ElementIdentifier, MacromolecularMachineId] = None
    relation: Union[str, URIorCURIE] = None
    object: Union[ElementIdentifier, GeneOntologyClassId] = None
    edge_label: Union[str, LabelType] = None
    id: Union[ElementIdentifier, FunctionalAssociationId] = bnode()

    def __post_init__(self):
        if self.id is not None and not isinstance(self.id, FunctionalAssociationId):
            self.id = FunctionalAssociationId(self.id)
        if self.subject is not None and not isinstance(self.subject, MacromolecularMachineId):
            self.subject = MacromolecularMachineId(self.subject)
        if self.object is not None and not isinstance(self.object, GeneOntologyClassId):
            self.object = GeneOntologyClassId(self.object)
        super().__post_init__()


@dataclass
class MacromolecularMachineToMolecularActivityAssociation(FunctionalAssociation):
    """
    A functional association between a macromolecular machine (gene, gene product or complex) and a molecular activity
    (as represented in the GO molecular function branch), where the entity carries out the activity, or contributes to
    its execution
    """
    _inherited_slots: ClassVar[List[str]] = []

    type_uri: ClassVar[str] = "https://w3id.org/biolink/vocab/MacromolecularMachineToMolecularActivityAssociation"
    type_curie: ClassVar[str] = "biolink:MacromolecularMachineToMolecularActivityAssociation"
    type_name: ClassVar[str] = "macromolecular machine to molecular activity association"

    subject: Union[ElementIdentifier, MacromolecularMachineId] = None
    relation: Union[str, URIorCURIE] = None
    object: Union[ElementIdentifier, MolecularActivityId] = None
    edge_label: Union[str, LabelType] = None
    id: Union[ElementIdentifier, MacromolecularMachineToMolecularActivityAssociationId] = bnode()

    def __post_init__(self):
        if self.id is not None and not isinstance(self.id, MacromolecularMachineToMolecularActivityAssociationId):
            self.id = MacromolecularMachineToMolecularActivityAssociationId(self.id)
        if self.object is not None and not isinstance(self.object, MolecularActivityId):
            self.object = MolecularActivityId(self.object)
        super().__post_init__()


@dataclass
class MacromolecularMachineToBiologicalProcessAssociation(FunctionalAssociation):
    """
    A functional association between a macromolecular machine (gene, gene product or complex) and a biological process
    or pathway (as represented in the GO biological process branch), where the entity carries out some part of the
    process, regulates it, or acts upstream of it
    """
    _inherited_slots: ClassVar[List[str]] = []

    type_uri: ClassVar[str] = "https://w3id.org/biolink/vocab/MacromolecularMachineToBiologicalProcessAssociation"
    type_curie: ClassVar[str] = "biolink:MacromolecularMachineToBiologicalProcessAssociation"
    type_name: ClassVar[str] = "macromolecular machine to biological process association"

    subject: Union[ElementIdentifier, MacromolecularMachineId] = None
    relation: Union[str, URIorCURIE] = None
    object: Union[ElementIdentifier, BiologicalProcessId] = None
    edge_label: Union[str, LabelType] = None
    id: Union[ElementIdentifier, MacromolecularMachineToBiologicalProcessAssociationId] = bnode()

    def __post_init__(self):
        if self.id is not None and not isinstance(self.id, MacromolecularMachineToBiologicalProcessAssociationId):
            self.id = MacromolecularMachineToBiologicalProcessAssociationId(self.id)
        if self.object is not None and not isinstance(self.object, BiologicalProcessId):
            self.object = BiologicalProcessId(self.object)
        super().__post_init__()


@dataclass
class MacromolecularMachineToCellularComponentAssociation(FunctionalAssociation):
    """
    A functional association between a macromolecular machine (gene, gene product or complex) and a cellular component
    (as represented in the GO cellular component branch), where the entity carries out its function in the cellular
    component
    """
    _inherited_slots: ClassVar[List[str]] = []

    type_uri: ClassVar[str] = "https://w3id.org/biolink/vocab/MacromolecularMachineToCellularComponentAssociation"
    type_curie: ClassVar[str] = "biolink:MacromolecularMachineToCellularComponentAssociation"
    type_name: ClassVar[str] = "macromolecular machine to cellular component association"

    subject: Union[ElementIdentifier, MacromolecularMachineId] = None
    relation: Union[str, URIorCURIE] = None
    object: Union[ElementIdentifier, CellularComponentId] = None
    edge_label: Union[str, LabelType] = None
    id: Union[ElementIdentifier, MacromolecularMachineToCellularComponentAssociationId] = bnode()

    def __post_init__(self):
        if self.id is not None and not isinstance(self.id, MacromolecularMachineToCellularComponentAssociationId):
            self.id = MacromolecularMachineToCellularComponentAssociationId(self.id)
        if self.object is not None and not isinstance(self.object, CellularComponentId):
            self.object = CellularComponentId(self.object)
        super().__post_init__()


@dataclass
class GeneToGoTermAssociation(FunctionalAssociation):
    _inherited_slots: ClassVar[List[str]] = []

    type_uri: ClassVar[str] = "http://bio2rdf.org/wormbase_vocabulary:Gene-GO-Association"
    type_curie: ClassVar[str] = None
    type_name: ClassVar[str] = "gene to go term association"

    subject: Union[ElementIdentifier, MolecularEntityId] = None
    relation: Union[str, URIorCURIE] = None
    object: Union[ElementIdentifier, GeneOntologyClassId] = None
    edge_label: Union[str, LabelType] = None
    id: Union[ElementIdentifier, GeneToGoTermAssociationId] = bnode()

    def __post_init__(self):
        if self.id is not None and not isinstance(self.id, GeneToGoTermAssociationId):
            self.id = GeneToGoTermAssociationId(self.id)
        if self.subject is not None and not isinstance(self.subject, MolecularEntityId):
            self.subject = MolecularEntityId(self.subject)
        if self.object is not None and not isinstance(self.object, GeneOntologyClassId):
            self.object = GeneOntologyClassId(self.object)
        super().__post_init__()


@dataclass
class GenomicSequenceLocalization(Association):
    """
    A relationship between a sequence feature and an entity it is localized to. The reference entity may be a
    chromosome, chromosome region or information entity such as a contig
    """
    _inherited_slots: ClassVar[List[str]] = []

    type_uri: ClassVar[str] = "http://biohackathon.org/resource/faldo#location"
    type_curie: ClassVar[str] = "faldo:location"
    type_name: ClassVar[str] = "genomic sequence localization"

    subject: Union[ElementIdentifier, GenomicEntityId] = None
    relation: Union[str, URIorCURIE] = None
    object: Union[ElementIdentifier, GenomicEntityId] = None
    edge_label: Union[str, LabelType] = None
    id: Union[ElementIdentifier, GenomicSequenceLocalizationId] = bnode()
    start_interbase_coordinate: Optional[str] = None
    end_interbase_coordinate: Optional[str] = None
    genome_build: Optional[str] = None
    phase: Optional[str] = None

    def __post_init__(self):
        if self.id is not None and not isinstance(self.id, GenomicSequenceLocalizationId):
            self.id = GenomicSequenceLocalizationId(self.id)
        if self.subject is not None and not isinstance(self.subject, GenomicEntityId):
            self.subject = GenomicEntityId(self.subject)
        if self.object is not None and not isinstance(self.object, GenomicEntityId):
            self.object = GenomicEntityId(self.object)
        super().__post_init__()


@dataclass
class SequenceFeatureRelationship(Association):
    """
    For example, a particular exon is part of a particular transcript or gene
    """
    _inherited_slots: ClassVar[List[str]] = []

    type_uri: ClassVar[str] = "https://w3id.org/biolink/vocab/SequenceFeatureRelationship"
    type_curie: ClassVar[str] = "biolink:SequenceFeatureRelationship"
    type_name: ClassVar[str] = "sequence feature relationship"

    subject: Union[ElementIdentifier, GenomicEntityId] = None
    relation: Union[str, URIorCURIE] = None
    object: Union[ElementIdentifier, GenomicEntityId] = None
    edge_label: Union[str, LabelType] = None
    id: Union[ElementIdentifier, SequenceFeatureRelationshipId] = bnode()

    def __post_init__(self):
        if self.id is not None and not isinstance(self.id, SequenceFeatureRelationshipId):
            self.id = SequenceFeatureRelationshipId(self.id)
        if self.subject is not None and not isinstance(self.subject, GenomicEntityId):
            self.subject = GenomicEntityId(self.subject)
        if self.object is not None and not isinstance(self.object, GenomicEntityId):
            self.object = GenomicEntityId(self.object)
        super().__post_init__()


@dataclass
class TranscriptToGeneRelationship(SequenceFeatureRelationship):
    """
    A gene is a collection of transcripts
    """
    _inherited_slots: ClassVar[List[str]] = []

    type_uri: ClassVar[str] = "https://w3id.org/biolink/vocab/TranscriptToGeneRelationship"
    type_curie: ClassVar[str] = "biolink:TranscriptToGeneRelationship"
    type_name: ClassVar[str] = "transcript to gene relationship"

    subject: Union[ElementIdentifier, TranscriptId] = None
    relation: Union[str, URIorCURIE] = None
    object: Union[ElementIdentifier, GeneId] = None
    edge_label: Union[str, LabelType] = None
    id: Union[ElementIdentifier, TranscriptToGeneRelationshipId] = bnode()

    def __post_init__(self):
        if self.id is not None and not isinstance(self.id, TranscriptToGeneRelationshipId):
            self.id = TranscriptToGeneRelationshipId(self.id)
        if self.subject is not None and not isinstance(self.subject, TranscriptId):
            self.subject = TranscriptId(self.subject)
        if self.object is not None and not isinstance(self.object, GeneId):
            self.object = GeneId(self.object)
        super().__post_init__()


@dataclass
class GeneToGeneProductRelationship(SequenceFeatureRelationship):
    """
    A gene is transcribed and potentially translated to a gene product
    """
    _inherited_slots: ClassVar[List[str]] = []

    type_uri: ClassVar[str] = "https://w3id.org/biolink/vocab/GeneToGeneProductRelationship"
    type_curie: ClassVar[str] = "biolink:GeneToGeneProductRelationship"
    type_name: ClassVar[str] = "gene to gene product relationship"

    subject: Union[ElementIdentifier, GeneId] = None
    relation: Union[str, URIorCURIE] = None
    object: Union[ElementIdentifier, GeneProductId] = None
    edge_label: Union[str, LabelType] = None
    id: Union[ElementIdentifier, GeneToGeneProductRelationshipId] = bnode()

    def __post_init__(self):
        if self.id is not None and not isinstance(self.id, GeneToGeneProductRelationshipId):
            self.id = GeneToGeneProductRelationshipId(self.id)
        if self.subject is not None and not isinstance(self.subject, GeneId):
            self.subject = GeneId(self.subject)
        if self.relation is not None and not isinstance(self.relation, URIorCURIE):
            self.relation = URIorCURIE(self.relation)
        if self.object is not None and not isinstance(self.object, GeneProductId):
            self.object = GeneProductId(self.object)
        super().__post_init__()


@dataclass
class ExonToTranscriptRelationship(SequenceFeatureRelationship):
    """
    A transcript is formed from multiple exons
    """
    _inherited_slots: ClassVar[List[str]] = []

    type_uri: ClassVar[str] = "https://w3id.org/biolink/vocab/ExonToTranscriptRelationship"
    type_curie: ClassVar[str] = "biolink:ExonToTranscriptRelationship"
    type_name: ClassVar[str] = "exon to transcript relationship"

    subject: Union[ElementIdentifier, ExonId] = None
    relation: Union[str, URIorCURIE] = None
    object: Union[ElementIdentifier, TranscriptId] = None
    edge_label: Union[str, LabelType] = None
    id: Union[ElementIdentifier, ExonToTranscriptRelationshipId] = bnode()

    def __post_init__(self):
        if self.id is not None and not isinstance(self.id, ExonToTranscriptRelationshipId):
            self.id = ExonToTranscriptRelationshipId(self.id)
        if self.subject is not None and not isinstance(self.subject, ExonId):
            self.subject = ExonId(self.subject)
        if self.object is not None and not isinstance(self.object, TranscriptId):
            self.object = TranscriptId(self.object)
        super().__post_init__()


@dataclass
class GeneRegulatoryRelationship(Association):
    """
    A regulatory relationship between two genes
    """
    _inherited_slots: ClassVar[List[str]] = []

    type_uri: ClassVar[str] = "https://w3id.org/biolink/vocab/GeneRegulatoryRelationship"
    type_curie: ClassVar[str] = "biolink:GeneRegulatoryRelationship"
    type_name: ClassVar[str] = "gene regulatory relationship"

    subject: Union[ElementIdentifier, GeneOrGeneProductId] = None
    relation: Union[str, URIorCURIE] = None
    object: Union[ElementIdentifier, GeneOrGeneProductId] = None
    edge_label: Union[str, LabelType] = None
    id: Union[ElementIdentifier, GeneRegulatoryRelationshipId] = bnode()

    def __post_init__(self):
        if self.id is not None and not isinstance(self.id, GeneRegulatoryRelationshipId):
            self.id = GeneRegulatoryRelationshipId(self.id)
        if self.subject is not None and not isinstance(self.subject, GeneOrGeneProductId):
            self.subject = GeneOrGeneProductId(self.subject)
        if self.relation is not None and not isinstance(self.relation, URIorCURIE):
            self.relation = URIorCURIE(self.relation)
        if self.object is not None and not isinstance(self.object, GeneOrGeneProductId):
            self.object = GeneOrGeneProductId(self.object)
        super().__post_init__()


@dataclass
class AnatomicalEntityToAnatomicalEntityAssociation(Association):
    _inherited_slots: ClassVar[List[str]] = []

    type_uri: ClassVar[str] = "https://w3id.org/biolink/vocab/AnatomicalEntityToAnatomicalEntityAssociation"
    type_curie: ClassVar[str] = "biolink:AnatomicalEntityToAnatomicalEntityAssociation"
    type_name: ClassVar[str] = "anatomical entity to anatomical entity association"

    subject: Union[ElementIdentifier, AnatomicalEntityId] = None
    relation: Union[str, URIorCURIE] = None
    object: Union[ElementIdentifier, AnatomicalEntityId] = None
    edge_label: Union[str, LabelType] = None
    id: Union[ElementIdentifier, AnatomicalEntityToAnatomicalEntityAssociationId] = bnode()

    def __post_init__(self):
        if self.id is not None and not isinstance(self.id, AnatomicalEntityToAnatomicalEntityAssociationId):
            self.id = AnatomicalEntityToAnatomicalEntityAssociationId(self.id)
        if self.subject is not None and not isinstance(self.subject, AnatomicalEntityId):
            self.subject = AnatomicalEntityId(self.subject)
        if self.object is not None and not isinstance(self.object, AnatomicalEntityId):
            self.object = AnatomicalEntityId(self.object)
        super().__post_init__()


@dataclass
class AnatomicalEntityToAnatomicalEntityPartOfAssociation(AnatomicalEntityToAnatomicalEntityAssociation):
    """
    A relationship between two anatomical entities where the relationship is mereological, i.e the two entities are
    related by parthood. This includes relationships between cellular components and cells, between cells and tissues,
    tissues and whole organisms
    """
    _inherited_slots: ClassVar[List[str]] = []

    type_uri: ClassVar[str] = "https://w3id.org/biolink/vocab/AnatomicalEntityToAnatomicalEntityPartOfAssociation"
    type_curie: ClassVar[str] = "biolink:AnatomicalEntityToAnatomicalEntityPartOfAssociation"
    type_name: ClassVar[str] = "anatomical entity to anatomical entity part of association"

    subject: Union[ElementIdentifier, AnatomicalEntityId] = None
    relation: Union[str, URIorCURIE] = None
    object: Union[ElementIdentifier, AnatomicalEntityId] = None
    edge_label: Union[str, LabelType] = None
    id: Union[ElementIdentifier, AnatomicalEntityToAnatomicalEntityPartOfAssociationId] = bnode()

    def __post_init__(self):
        if self.id is not None and not isinstance(self.id, AnatomicalEntityToAnatomicalEntityPartOfAssociationId):
            self.id = AnatomicalEntityToAnatomicalEntityPartOfAssociationId(self.id)
        if self.subject is not None and not isinstance(self.subject, AnatomicalEntityId):
            self.subject = AnatomicalEntityId(self.subject)
        if self.relation is not None and not isinstance(self.relation, URIorCURIE):
            self.relation = URIorCURIE(self.relation)
        if self.object is not None and not isinstance(self.object, AnatomicalEntityId):
            self.object = AnatomicalEntityId(self.object)
        super().__post_init__()


@dataclass
class AnatomicalEntityToAnatomicalEntityOntogenicAssociation(AnatomicalEntityToAnatomicalEntityAssociation):
    """
    A relationship between two anatomical entities where the relationship is ontogenic, i.e the two entities are
    related by development. A number of different relationship types can be used to specify the precise nature of the
    relationship
    """
    _inherited_slots: ClassVar[List[str]] = []

    type_uri: ClassVar[str] = "https://w3id.org/biolink/vocab/AnatomicalEntityToAnatomicalEntityOntogenicAssociation"
    type_curie: ClassVar[str] = "biolink:AnatomicalEntityToAnatomicalEntityOntogenicAssociation"
    type_name: ClassVar[str] = "anatomical entity to anatomical entity ontogenic association"

    subject: Union[ElementIdentifier, AnatomicalEntityId] = None
    relation: Union[str, URIorCURIE] = None
    object: Union[ElementIdentifier, AnatomicalEntityId] = None
    edge_label: Union[str, LabelType] = None
    id: Union[ElementIdentifier, AnatomicalEntityToAnatomicalEntityOntogenicAssociationId] = bnode()

    def __post_init__(self):
        if self.id is not None and not isinstance(self.id, AnatomicalEntityToAnatomicalEntityOntogenicAssociationId):
            self.id = AnatomicalEntityToAnatomicalEntityOntogenicAssociationId(self.id)
        if self.subject is not None and not isinstance(self.subject, AnatomicalEntityId):
            self.subject = AnatomicalEntityId(self.subject)
        if self.relation is not None and not isinstance(self.relation, URIorCURIE):
            self.relation = URIorCURIE(self.relation)
        if self.object is not None and not isinstance(self.object, AnatomicalEntityId):
            self.object = AnatomicalEntityId(self.object)
        super().__post_init__()


@dataclass
class Occurrent(NamedThing):
    """
    A processual entity
    """
    _inherited_slots: ClassVar[List[str]] = ["related_to", "interacts_with", "regulates_process_to_process", "has_participant", "has_input", "precedes", "positively_regulates_process_to_process", "negatively_regulates_process_to_process"]

    type_uri: ClassVar[str] = "http://purl.obolibrary.org/obo/BFO_0000003"
    type_curie: ClassVar[str] = "BFO:0000003"
    type_name: ClassVar[str] = "occurrent"

    id: Union[ElementIdentifier, OccurrentId] = None
    name: Union[str, LabelType] = None
    category: List[Union[str, IriType]] = empty_list()

    def __post_init__(self):
        if self.id is not None and not isinstance(self.id, OccurrentId):
            self.id = OccurrentId(self.id)
        super().__post_init__()


@dataclass
class BiologicalProcessOrActivity(BiologicalEntity):
    """
    Either an individual molecular activity, or a collection of causally connected molecular activities
    """
    _inherited_slots: ClassVar[List[str]] = ["related_to", "interacts_with", "has_phenotype"]

    type_uri: ClassVar[str] = "https://w3id.org/biolink/vocab/BiologicalProcessOrActivity"
    type_curie: ClassVar[str] = "biolink:BiologicalProcessOrActivity"
    type_name: ClassVar[str] = "biological process or activity"

    id: Union[ElementIdentifier, BiologicalProcessOrActivityId] = None
    name: Union[str, LabelType] = None
    category: List[Union[str, IriType]] = empty_list()

    def __post_init__(self):
        if self.id is not None and not isinstance(self.id, BiologicalProcessOrActivityId):
            self.id = BiologicalProcessOrActivityId(self.id)
        super().__post_init__()


@dataclass
class MolecularActivity(BiologicalProcessOrActivity):
    """
    An execution of a molecular function carried out by a gene product or macromolecular complex.
    """
    _inherited_slots: ClassVar[List[str]] = ["related_to", "interacts_with", "has_phenotype", "regulates_process_to_process", "has_participant", "has_input", "precedes"]

    type_uri: ClassVar[str] = "http://purl.obolibrary.org/obo/GO_0003674"
    type_curie: ClassVar[str] = "GO:0003674"
    type_name: ClassVar[str] = "molecular activity"

    id: Union[ElementIdentifier, MolecularActivityId] = None
    name: Union[str, LabelType] = None
    category: List[Union[str, IriType]] = empty_list()

    def __post_init__(self):
        if self.id is not None and not isinstance(self.id, MolecularActivityId):
            self.id = MolecularActivityId(self.id)
        super().__post_init__()


@dataclass
class ActivityAndBehavior(Occurrent):
    """
    Activity or behavior of any independent integral living, organization or mechanical actor in the world
    """
    _inherited_slots: ClassVar[List[str]] = ["related_to", "interacts_with", "regulates_process_to_process", "has_participant", "has_input", "precedes"]

    type_uri: ClassVar[str] = "https://w3id.org/biolink/vocab/ActivityAndBehavior"
    type_curie: ClassVar[str] = "biolink:ActivityAndBehavior"
    type_name: ClassVar[str] = "activity and behavior"

    id: Union[ElementIdentifier, ActivityAndBehaviorId] = None
    name: Union[str, LabelType] = None
    category: List[Union[str, IriType]] = empty_list()

    def __post_init__(self):
        if self.id is not None and not isinstance(self.id, ActivityAndBehaviorId):
            self.id = ActivityAndBehaviorId(self.id)
        super().__post_init__()


@dataclass
class Procedure(Occurrent):
    """
    A series of actions conducted in a certain order or manner
    """
    _inherited_slots: ClassVar[List[str]] = ["related_to", "interacts_with", "regulates_process_to_process", "has_participant", "has_input", "precedes"]

    type_uri: ClassVar[str] = "https://w3id.org/biolink/vocab/Procedure"
    type_curie: ClassVar[str] = "biolink:Procedure"
    type_name: ClassVar[str] = "procedure"

    id: Union[ElementIdentifier, ProcedureId] = None
    name: Union[str, LabelType] = None
    category: List[Union[str, IriType]] = empty_list()

    def __post_init__(self):
        if self.id is not None and not isinstance(self.id, ProcedureId):
            self.id = ProcedureId(self.id)
        super().__post_init__()


@dataclass
class Phenomenon(Occurrent):
    """
    a fact or situation that is observed to exist or happen, especially one whose cause or explanation is in question
    """
    _inherited_slots: ClassVar[List[str]] = ["related_to", "interacts_with", "regulates_process_to_process", "has_participant", "has_input", "precedes"]

    type_uri: ClassVar[str] = "https://w3id.org/biolink/vocab/Phenomenon"
    type_curie: ClassVar[str] = "biolink:Phenomenon"
    type_name: ClassVar[str] = "phenomenon"

    id: Union[ElementIdentifier, PhenomenonId] = None
    name: Union[str, LabelType] = None
    category: List[Union[str, IriType]] = empty_list()

    def __post_init__(self):
        if self.id is not None and not isinstance(self.id, PhenomenonId):
            self.id = PhenomenonId(self.id)
        super().__post_init__()


@dataclass
class BiologicalProcess(BiologicalProcessOrActivity):
    """
    One or more causally connected executions of molecular functions
    """
    _inherited_slots: ClassVar[List[str]] = ["related_to", "interacts_with", "has_phenotype", "regulates_process_to_process", "has_participant", "has_input", "precedes"]

    type_uri: ClassVar[str] = "http://purl.obolibrary.org/obo/GO_0008150"
    type_curie: ClassVar[str] = "GO:0008150"
    type_name: ClassVar[str] = "biological process"

    id: Union[ElementIdentifier, BiologicalProcessId] = None
    name: Union[str, LabelType] = None
    category: List[Union[str, IriType]] = empty_list()

    def __post_init__(self):
        if self.id is not None and not isinstance(self.id, BiologicalProcessId):
            self.id = BiologicalProcessId(self.id)
        super().__post_init__()


@dataclass
class Pathway(BiologicalProcess):
    _inherited_slots: ClassVar[List[str]] = ["related_to", "interacts_with", "has_phenotype", "regulates_process_to_process", "has_participant", "has_input", "precedes"]

    type_uri: ClassVar[str] = "http://purl.obolibrary.org/obo/GO_0007165"
    type_curie: ClassVar[str] = "GO:0007165"
    type_name: ClassVar[str] = "pathway"

    id: Union[ElementIdentifier, PathwayId] = None
    name: Union[str, LabelType] = None
    category: List[Union[str, IriType]] = empty_list()

    def __post_init__(self):
        if self.id is not None and not isinstance(self.id, PathwayId):
            self.id = PathwayId(self.id)
        super().__post_init__()


@dataclass
class PhysiologicalProcess(BiologicalProcess):
    _inherited_slots: ClassVar[List[str]] = ["related_to", "interacts_with", "has_phenotype", "regulates_process_to_process", "has_participant", "has_input", "precedes"]

    type_uri: ClassVar[str] = "https://w3id.org/biolink/vocab/PhysiologicalProcess"
    type_curie: ClassVar[str] = "biolink:PhysiologicalProcess"
    type_name: ClassVar[str] = "physiological process"

    id: Union[ElementIdentifier, PhysiologicalProcessId] = None
    name: Union[str, LabelType] = None
    category: List[Union[str, IriType]] = empty_list()

    def __post_init__(self):
        if self.id is not None and not isinstance(self.id, PhysiologicalProcessId):
            self.id = PhysiologicalProcessId(self.id)
        super().__post_init__()


@dataclass
class CellularComponent(AnatomicalEntity):
    """
    A location in or around a cell
    """
    _inherited_slots: ClassVar[List[str]] = ["related_to", "interacts_with", "has_phenotype", "expresses", "in_taxon"]

    type_uri: ClassVar[str] = "http://purl.obolibrary.org/obo/GO_0005575"
    type_curie: ClassVar[str] = "GO:0005575"
    type_name: ClassVar[str] = "cellular component"

    id: Union[ElementIdentifier, CellularComponentId] = None
    name: Union[str, LabelType] = None
    category: List[Union[str, IriType]] = empty_list()

    def __post_init__(self):
        if self.id is not None and not isinstance(self.id, CellularComponentId):
            self.id = CellularComponentId(self.id)
        super().__post_init__()


@dataclass
class Cell(AnatomicalEntity):
    _inherited_slots: ClassVar[List[str]] = ["related_to", "interacts_with", "has_phenotype", "expresses", "in_taxon"]

    type_uri: ClassVar[str] = "http://purl.obolibrary.org/obo/GO_0005623"
    type_curie: ClassVar[str] = "GO:0005623"
    type_name: ClassVar[str] = "cell"

    id: Union[ElementIdentifier, CellId] = None
    name: Union[str, LabelType] = None
    category: List[Union[str, IriType]] = empty_list()

    def __post_init__(self):
        if self.id is not None and not isinstance(self.id, CellId):
            self.id = CellId(self.id)
        super().__post_init__()


@dataclass
class CellLine(Biosample):
    _inherited_slots: ClassVar[List[str]] = ["related_to", "interacts_with", "has_phenotype", "in_taxon"]

    type_uri: ClassVar[str] = "http://purl.obolibrary.org/obo/CLO_0000031"
    type_curie: ClassVar[str] = "CLO:0000031"
    type_name: ClassVar[str] = "cell line"

    id: Union[ElementIdentifier, CellLineId] = None
    name: Union[str, LabelType] = None
    category: List[Union[str, IriType]] = empty_list()

    def __post_init__(self):
        if self.id is not None and not isinstance(self.id, CellLineId):
            self.id = CellLineId(self.id)
        super().__post_init__()


@dataclass
class GrossAnatomicalStructure(AnatomicalEntity):
    _inherited_slots: ClassVar[List[str]] = ["related_to", "interacts_with", "has_phenotype", "expresses", "in_taxon"]

    type_uri: ClassVar[str] = "http://purl.obolibrary.org/obo/UBERON_0010000"
    type_curie: ClassVar[str] = "UBERON:0010000"
    type_name: ClassVar[str] = "gross anatomical structure"

    id: Union[ElementIdentifier, GrossAnatomicalStructureId] = None
    name: Union[str, LabelType] = None
    category: List[Union[str, IriType]] = empty_list()

    def __post_init__(self):
        if self.id is not None and not isinstance(self.id, GrossAnatomicalStructureId):
            self.id = GrossAnatomicalStructureId(self.id)
        super().__post_init__()

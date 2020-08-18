# Auto generated from .yaml by pythongen.py version:
# Generation date:
# Schema: Biolink-Model
#
# id: https://w3id.org/biolink/biolink-model
# description: Entity and association taxonomy and datamodel for life-sciences data
# license: https://creativecommons.org/publicdomain/zero/1.0/

import dataclasses
import sys
from typing import Optional, List, Union, Dict, ClassVar, Any
from dataclasses import dataclass
from biolinkml.utils.slot import Slot
from biolinkml.utils.metamodelcore import empty_list, empty_dict, bnode
from biolinkml.utils.yamlutils import YAMLRoot, extended_str, extended_float, extended_int
if sys.version_info < (3, 7, 6):
    from biolinkml.utils.dataclass_extensions_375 import dataclasses_init_fn_with_kwargs
else:
    from biolinkml.utils.dataclass_extensions_376 import dataclasses_init_fn_with_kwargs
from biolinkml.utils.formatutils import camelcase, underscore, sfx
from rdflib import Namespace, URIRef
from biolinkml.utils.curienamespace import CurieNamespace
from biolinkml.utils.metamodelcore import Bool, URIorCURIE, XSDDate, XSDTime
from includes.types import Boolean, Date, Double, Float, Integer, String, Time, Uriorcurie

metamodel_version = "1.5.3"

# Overwrite dataclasses _init_fn to add **kwargs in __init__
dataclasses._init_fn = dataclasses_init_fn_with_kwargs

# Namespaces
BFO = CurieNamespace('BFO', 'http://purl.obolibrary.org/obo/BFO_')
BIOGRID = CurieNamespace('BIOGRID', 'http://thebiogrid.org/')
BIOSAMPLE = CurieNamespace('BioSample', 'http://example.org/UNKNOWN/BioSample/')
CAID = CurieNamespace('CAID', 'http://example.org/UNKNOWN/CAID/')
CHEBI = CurieNamespace('CHEBI', 'http://purl.obolibrary.org/obo/CHEBI_')
CHEMBL_COMPOUND = CurieNamespace('CHEMBL_COMPOUND', 'http://identifiers.org/chembl.compound/')
CHEMBL_TARGET = CurieNamespace('CHEMBL_TARGET', 'http://identifiers.org/chembl.target/')
CIO = CurieNamespace('CIO', 'http://purl.obolibrary.org/obo/CIO_')
CIVIC = CurieNamespace('CIViC', 'http://example.org/UNKNOWN/CIViC/')
CL = CurieNamespace('CL', 'http://purl.obolibrary.org/obo/CL_')
CLO = CurieNamespace('CLO', 'http://purl.obolibrary.org/obo/CLO_')
CLINVAR = CurieNamespace('ClinVar', 'http://www.ncbi.nlm.nih.gov/clinvar/')
DBSNP = CurieNamespace('DBSNP', 'http://identifiers.org/dbsnp/')
DOID = CurieNamespace('DOID', 'http://purl.obolibrary.org/obo/DOID_')
DRUGBANK = CurieNamespace('DRUGBANK', 'http://identifiers.org/drugbank/')
ECO = CurieNamespace('ECO', 'http://purl.obolibrary.org/obo/ECO_')
ECTO = CurieNamespace('ECTO', 'http://example.org/UNKNOWN/ECTO/')
EFO = CurieNamespace('EFO', 'http://purl.obolibrary.org/obo/EFO_')
ENSEMBL = CurieNamespace('ENSEMBL', 'http://ensembl.org/id/')
EXO = CurieNamespace('ExO', 'http://example.org/UNKNOWN/ExO/')
FAO = CurieNamespace('FAO', 'http://purl.obolibrary.org/obo/FAO_')
GENO = CurieNamespace('GENO', 'http://purl.obolibrary.org/obo/GENO_')
GO = CurieNamespace('GO', 'http://purl.obolibrary.org/obo/GO_')
GOLD_META = CurieNamespace('GOLD_META', 'http://identifiers.org/gold.meta/')
GTOPDB = CurieNamespace('GTOPDB', 'http://example.org/UNKNOWN/GTOPDB/')
HANCESTRO = CurieNamespace('HANCESTRO', 'http://example.org/UNKNOWN/HANCESTRO/')
HGNC = CurieNamespace('HGNC', 'http://www.genenames.org/cgi-bin/gene_symbol_report?hgnc_id=')
HGVS = CurieNamespace('HGVS', 'http://example.org/UNKNOWN/HGVS/')
HMDB = CurieNamespace('HMDB', 'http://www.hmdb.ca/metabolites/')
HP = CurieNamespace('HP', 'http://purl.obolibrary.org/obo/HP_')
IAO = CurieNamespace('IAO', 'http://purl.obolibrary.org/obo/IAO_')
INCHI = CurieNamespace('INCHI', 'http://identifiers.org/inchi/')
INCHIKEY = CurieNamespace('INCHIKEY', 'http://identifiers.org/inchikey/')
IUPHAR = CurieNamespace('IUPHAR', 'http://example.org/UNKNOWN/IUPHAR/')
INTACT = CurieNamespace('IntAct', 'http://example.org/UNKNOWN/IntAct/')
KEGG = CurieNamespace('KEGG', 'http://identifiers.org/kegg/')
MEDDRA = CurieNamespace('MEDDRA', 'http://purl.bioontology.org/ontology/MEDDRA/')
MESH = CurieNamespace('MESH', 'http://purl.obolibrary.org/obo/MESH_')
MGI = CurieNamespace('MGI', 'http://www.informatics.jax.org/accession/MGI:')
MIR = CurieNamespace('MIR', 'http://identifiers.org/mir/')
MONDO = CurieNamespace('MONDO', 'http://purl.obolibrary.org/obo/MONDO_')
MYVARIANT_HG19 = CurieNamespace('MYVARIANT_HG19', 'http://example.org/UNKNOWN/MYVARIANT_HG19/')
MYVARIANT_HG38 = CurieNamespace('MYVARIANT_HG38', 'http://example.org/UNKNOWN/MYVARIANT_HG38/')
NCBIGENE = CurieNamespace('NCBIGene', 'http://www.ncbi.nlm.nih.gov/gene/')
NCIT = CurieNamespace('NCIT', 'http://purl.obolibrary.org/obo/NCIT_')
OBAN = CurieNamespace('OBAN', 'http://purl.org/oban/')
OBI = CurieNamespace('OBI', 'http://purl.obolibrary.org/obo/OBI_')
OGMS = CurieNamespace('OGMS', 'http://purl.obolibrary.org/obo/OGMS_')
OIO = CurieNamespace('OIO', 'http://www.geneontology.org/formats/oboInOwl#')
OMIM = CurieNamespace('OMIM', 'http://purl.obolibrary.org/obo/OMIM_')
ORPHANET = CurieNamespace('ORPHANET', 'http://identifiers.org/orphanet/')
PANTHER = CurieNamespace('PANTHER', 'http://www.pantherdb.org/panther/family.do?clsAccession=')
PHARMGKB = CurieNamespace('PHARMGKB', 'http://example.org/UNKNOWN/PHARMGKB/')
PMID = CurieNamespace('PMID', 'http://www.ncbi.nlm.nih.gov/pubmed/')
PO = CurieNamespace('PO', 'http://purl.obolibrary.org/obo/PO_')
PR = CurieNamespace('PR', 'http://purl.obolibrary.org/obo/PR_')
PUBCHEM = CurieNamespace('PUBCHEM', 'http://example.org/UNKNOWN/PUBCHEM/')
PW = CurieNamespace('PW', 'http://purl.obolibrary.org/obo/PW_')
POMBASE = CurieNamespace('PomBase', 'https://www.pombase.org/spombe/result/')
RHEA = CurieNamespace('RHEA', 'http://identifiers.org/rhea/')
RNACENTRAL = CurieNamespace('RNAcentral', 'http://example.org/UNKNOWN/RNAcentral/')
RO = CurieNamespace('RO', 'http://purl.obolibrary.org/obo/RO_')
REACTOME = CurieNamespace('Reactome', 'http://example.org/UNKNOWN/Reactome/')
SEMMEDDB = CurieNamespace('SEMMEDDB', 'http://example.org/UNKNOWN/SEMMEDDB/')
SGD = CurieNamespace('SGD', 'https://www.yeastgenome.org/locus/')
SIO = CurieNamespace('SIO', 'http://semanticscience.org/resource/SIO_')
SMPDB = CurieNamespace('SMPDB', 'http://smpdb.ca/view/')
SO = CurieNamespace('SO', 'http://purl.obolibrary.org/obo/SO_')
STATO = CurieNamespace('STATO', 'http://purl.obolibrary.org/obo/STATO_')
UBERON = CurieNamespace('UBERON', 'http://purl.obolibrary.org/obo/UBERON_')
UMLS = CurieNamespace('UMLS', 'http://linkedlifedata.com/resource/umls/id/')
UMLSSC = CurieNamespace('UMLSSC', 'https://uts-ws.nlm.nih.gov/rest/semantic-network/semantic-network/current/TUI/')
UMLSSG = CurieNamespace('UMLSSG', 'https://uts-ws.nlm.nih.gov/rest/semantic-network/semantic-network/current/GROUP/')
UMLSST = CurieNamespace('UMLSST', 'https://uts-ws.nlm.nih.gov/rest/semantic-network/semantic-network/current/STY/')
UNII = CurieNamespace('UNII', 'http://fdasis.nlm.nih.gov/srs/unii/')
UO = CurieNamespace('UO', 'http://purl.obolibrary.org/obo/UO_')
UPHENO = CurieNamespace('UPHENO', 'http://purl.obolibrary.org/obo/UPHENO_')
UNIPROTKB = CurieNamespace('UniProtKB', 'http://identifiers.org/uniprot/')
VMC = CurieNamespace('VMC', 'http://example.org/UNKNOWN/VMC/')
WB = CurieNamespace('WB', 'http://identifiers.org/wb/')
WD = CurieNamespace('WD', 'http://example.org/UNKNOWN/WD/')
WIKIPATHWAYS = CurieNamespace('WIKIPATHWAYS', 'http://identifiers.org/wikipathways/')
ZFIN = CurieNamespace('ZFIN', 'http://zfin.org/')
BIOLINK = CurieNamespace('biolink', 'https://w3id.org/biolink/vocab/')
BIOLINKML = CurieNamespace('biolinkml', 'https://w3id.org/biolink/biolinkml/')
DCT = CurieNamespace('dct', 'http://example.org/UNKNOWN/dct/')
DCTERMS = CurieNamespace('dcterms', 'http://purl.org/dc/terms/')
DICTYBASE = CurieNamespace('dictyBase', 'http://dictybase.org/gene/')
FALDO = CurieNamespace('faldo', 'http://biohackathon.org/resource/faldo#')
OWL = CurieNamespace('owl', 'http://www.w3.org/2002/07/owl#')
PAV = CurieNamespace('pav', 'http://purl.org/pav/')
QUD = CurieNamespace('qud', 'http://qudt.org/1.1/schema/qudt#')
RDF = CurieNamespace('rdf', 'http://www.w3.org/1999/02/22-rdf-syntax-ns#')
RDFS = CurieNamespace('rdfs', 'http://www.w3.org/2000/01/rdf-schema#')
SKOS = CurieNamespace('skos', 'https://www.w3.org/TR/skos-reference/#')
VOID = CurieNamespace('void', 'http://rdfs.org/ns/void#')
WGS = CurieNamespace('wgs', 'http://www.w3.org/2003/01/geo/wgs84_pos')
XSD = CurieNamespace('xsd', 'http://www.w3.org/2001/XMLSchema#')
DEFAULT_ = BIOLINK


# Types
class ChemicalFormulaValue(str):
    """ A chemical formula """
    type_class_uri = XSD.string
    type_class_curie = "xsd:string"
    type_name = "chemical formula value"
    type_model_uri = BIOLINK.ChemicalFormulaValue


class IriType(Uriorcurie):
    """ An IRI """
    type_class_uri = XSD.anyURI
    type_class_curie = "xsd:anyURI"
    type_name = "iri type"
    type_model_uri = BIOLINK.IriType


class LabelType(String):
    """ A string that provides a human-readable name for a thing """
    type_class_uri = XSD.string
    type_class_curie = "xsd:string"
    type_name = "label type"
    type_model_uri = BIOLINK.LabelType


class NarrativeText(String):
    """ A string that provides a human-readable description of something """
    type_class_uri = XSD.string
    type_class_curie = "xsd:string"
    type_name = "narrative text"
    type_model_uri = BIOLINK.NarrativeText


class SymbolType(String):
    type_class_uri = XSD.string
    type_class_curie = "xsd:string"
    type_name = "symbol type"
    type_model_uri = BIOLINK.SymbolType


class Frequency(String):
    type_class_uri = UO["0000105"]
    type_class_curie = "UO:0000105"
    type_name = "frequency"
    type_model_uri = BIOLINK.Frequency


class PercentageFrequencyValue(Double):
    type_class_uri = UO["0000187"]
    type_class_curie = "UO:0000187"
    type_name = "percentage frequency value"
    type_model_uri = BIOLINK.PercentageFrequencyValue


class Quotient(Double):
    type_class_uri = UO["0010006"]
    type_class_curie = "UO:0010006"
    type_name = "quotient"
    type_model_uri = BIOLINK.Quotient


class Unit(String):
    type_class_uri = UO["0000000"]
    type_class_curie = "UO:0000000"
    type_name = "unit"
    type_model_uri = BIOLINK.Unit


class TimeType(Time):
    type_class_uri = XSD.dateTime
    type_class_curie = "xsd:dateTime"
    type_name = "time type"
    type_model_uri = BIOLINK.TimeType


class BiologicalSequence(String):
    type_class_uri = XSD.string
    type_class_curie = "xsd:string"
    type_name = "biological sequence"
    type_model_uri = BIOLINK.BiologicalSequence


# Class references
class AttributeId(extended_str):
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


class NamedThingId(extended_str):
    pass


class DataFileId(NamedThingId):
    pass


class SourceFileId(DataFileId):
    pass


class DataSetId(NamedThingId):
    pass


class DataSetVersionId(DataSetId):
    pass


class DistributionLevelId(DataSetVersionId):
    pass


class DataSetSummaryId(DataSetVersionId):
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


class MaterialSampleId(NamedThingId):
    pass


class DiseaseOrPhenotypicFeatureId(BiologicalEntityId):
    pass


class DiseaseId(DiseaseOrPhenotypicFeatureId):
    pass


class PhenotypicFeatureId(DiseaseOrPhenotypicFeatureId):
    pass


class ExposureEventId(BiologicalEntityId):
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


class ChemicalExposureId(ExposureEventId):
    pass


class DrugExposureId(ChemicalExposureId):
    pass


class TreatmentId(ExposureEventId):
    pass


class GeographicLocationId(PlanetaryEntityId):
    pass


class GeographicLocationAtTimeId(GeographicLocationId):
    pass


class AssociationId(extended_str):
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


class ChemicalToChemicalAssociationId(AssociationId):
    pass


class ChemicalToChemicalDerivationAssociationId(ChemicalToChemicalAssociationId):
    pass


class ChemicalToDiseaseOrPhenotypicFeatureAssociationId(AssociationId):
    pass


class ChemicalToPathwayAssociationId(AssociationId):
    pass


class ChemicalToGeneAssociationId(AssociationId):
    pass


class MaterialSampleToThingAssociationId(AssociationId):
    pass


class MaterialSampleDerivationAssociationId(AssociationId):
    pass


class MaterialSampleToDiseaseOrPhenotypicFeatureAssociationId(AssociationId):
    pass


class DiseaseToThingAssociationId(AssociationId):
    pass


class DiseaseToExposureAssociationId(DiseaseToThingAssociationId):
    pass


class EntityToPhenotypicFeatureAssociationId(AssociationId):
    pass


class DiseaseOrPhenotypicFeatureAssociationToThingAssociationId(AssociationId):
    pass


class DiseaseOrPhenotypicFeatureAssociationToLocationAssociationId(DiseaseOrPhenotypicFeatureAssociationToThingAssociationId):
    pass


class ThingToDiseaseOrPhenotypicFeatureAssociationId(AssociationId):
    pass


class GenotypeToPhenotypicFeatureAssociationId(AssociationId):
    pass


class ExposureEventToPhenotypicFeatureAssociationId(AssociationId):
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


class PhysicalEntityId(NamedThingId):
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


class CellLineId(OrganismalEntityId):
    pass


class GrossAnatomicalStructureId(AnatomicalEntityId):
    pass


class AbstractEntity(YAMLRoot):
    """
    Any thing that is not a process or a physical mass-bearing entity
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = BIOLINK.AbstractEntity
    class_class_curie: ClassVar[str] = "biolink:AbstractEntity"
    class_name: ClassVar[str] = "abstract entity"
    class_model_uri: ClassVar[URIRef] = BIOLINK.AbstractEntity


@dataclass
class Attribute(AbstractEntity):
    """
    A property or characteristic of an entity. For example, an apple may have properties such as color, shape, age,
    crispiness. An environmental sample may have attributes such as depth, lat, long, material.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = BIOLINK.Attribute
    class_class_curie: ClassVar[str] = "biolink:Attribute"
    class_name: ClassVar[str] = "attribute"
    class_model_uri: ClassVar[URIRef] = BIOLINK.Attribute

    id: Union[str, AttributeId] = None
    name: Union[str, LabelType] = None
    category: List[Union[str, IriType]] = empty_list()
    has_attribute_type: Optional[Union[str, OntologyClassId]] = None
    has_quantitative_value: List[Union[dict, "QuantityValue"]] = empty_list()
    has_qualitative_value: Optional[Union[str, NamedThingId]] = None

    def __post_init__(self, **kwargs: Dict[str, Any]):
        if self.id is None:
            raise ValueError(f"id must be supplied")
        if not isinstance(self.id, AttributeId):
            self.id = AttributeId(self.id)
        if self.has_attribute_type is not None and not isinstance(self.has_attribute_type, OntologyClassId):
            self.has_attribute_type = OntologyClassId(self.has_attribute_type)
        self.has_quantitative_value = [QuantityValue(*e) for e in self.has_quantitative_value.items()] if isinstance(self.has_quantitative_value, dict) \
                                       else [v if isinstance(v, QuantityValue) else QuantityValue(**v)
                                             for v in ([self.has_quantitative_value] if isinstance(self.has_quantitative_value, str) else self.has_quantitative_value)]
        if self.has_qualitative_value is not None and not isinstance(self.has_qualitative_value, NamedThingId):
            self.has_qualitative_value = NamedThingId(self.has_qualitative_value)
        super().__post_init__(**kwargs)


@dataclass
class QuantityValue(AbstractEntity):
    """
    A value of an attribute that is quantitative and measurable, expressed as a combination of a unit and a numeric
    value
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = BIOLINK.QuantityValue
    class_class_curie: ClassVar[str] = "biolink:QuantityValue"
    class_name: ClassVar[str] = "quantity value"
    class_model_uri: ClassVar[URIRef] = BIOLINK.QuantityValue

    has_unit: Optional[Union[str, Unit]] = None
    has_numeric_value: Optional[float] = None

    def __post_init__(self, **kwargs: Dict[str, Any]):
        if self.has_unit is not None and not isinstance(self.has_unit, Unit):
            self.has_unit = Unit(self.has_unit)
        super().__post_init__(**kwargs)


@dataclass
class BiologicalSex(Attribute):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = BIOLINK.BiologicalSex
    class_class_curie: ClassVar[str] = "biolink:BiologicalSex"
    class_name: ClassVar[str] = "biological sex"
    class_model_uri: ClassVar[URIRef] = BIOLINK.BiologicalSex

    id: Union[str, BiologicalSexId] = None
    name: Union[str, LabelType] = None
    category: List[Union[str, IriType]] = empty_list()

    def __post_init__(self, **kwargs: Dict[str, Any]):
        if self.id is None:
            raise ValueError(f"id must be supplied")
        if not isinstance(self.id, BiologicalSexId):
            self.id = BiologicalSexId(self.id)
        super().__post_init__(**kwargs)


@dataclass
class PhenotypicSex(BiologicalSex):
    """
    An attribute corresponding to the phenotypic sex of the individual, based upon the reproductive organs present.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = BIOLINK.PhenotypicSex
    class_class_curie: ClassVar[str] = "biolink:PhenotypicSex"
    class_name: ClassVar[str] = "phenotypic sex"
    class_model_uri: ClassVar[URIRef] = BIOLINK.PhenotypicSex

    id: Union[str, PhenotypicSexId] = None
    name: Union[str, LabelType] = None
    category: List[Union[str, IriType]] = empty_list()

    def __post_init__(self, **kwargs: Dict[str, Any]):
        if self.id is None:
            raise ValueError(f"id must be supplied")
        if not isinstance(self.id, PhenotypicSexId):
            self.id = PhenotypicSexId(self.id)
        super().__post_init__(**kwargs)


@dataclass
class GenotypicSex(BiologicalSex):
    """
    An attribute corresponding to the genotypic sex of the individual, based upon genotypic composition of sex
    chromosomes.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = BIOLINK.GenotypicSex
    class_class_curie: ClassVar[str] = "biolink:GenotypicSex"
    class_name: ClassVar[str] = "genotypic sex"
    class_model_uri: ClassVar[URIRef] = BIOLINK.GenotypicSex

    id: Union[str, GenotypicSexId] = None
    name: Union[str, LabelType] = None
    category: List[Union[str, IriType]] = empty_list()

    def __post_init__(self, **kwargs: Dict[str, Any]):
        if self.id is None:
            raise ValueError(f"id must be supplied")
        if not isinstance(self.id, GenotypicSexId):
            self.id = GenotypicSexId(self.id)
        super().__post_init__(**kwargs)


@dataclass
class SeverityValue(Attribute):
    """
    describes the severity of a phenotypic feature or disease
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = BIOLINK.SeverityValue
    class_class_curie: ClassVar[str] = "biolink:SeverityValue"
    class_name: ClassVar[str] = "severity value"
    class_model_uri: ClassVar[URIRef] = BIOLINK.SeverityValue

    id: Union[str, SeverityValueId] = None
    name: Union[str, LabelType] = None
    category: List[Union[str, IriType]] = empty_list()

    def __post_init__(self, **kwargs: Dict[str, Any]):
        if self.id is None:
            raise ValueError(f"id must be supplied")
        if not isinstance(self.id, SeverityValueId):
            self.id = SeverityValueId(self.id)
        super().__post_init__(**kwargs)


@dataclass
class FrequencyValue(Attribute):
    """
    describes the frequency of occurrence of an event or condition
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = BIOLINK.FrequencyValue
    class_class_curie: ClassVar[str] = "biolink:FrequencyValue"
    class_name: ClassVar[str] = "frequency value"
    class_model_uri: ClassVar[URIRef] = BIOLINK.FrequencyValue

    id: Union[str, FrequencyValueId] = None
    name: Union[str, LabelType] = None
    category: List[Union[str, IriType]] = empty_list()

    def __post_init__(self, **kwargs: Dict[str, Any]):
        if self.id is None:
            raise ValueError(f"id must be supplied")
        if not isinstance(self.id, FrequencyValueId):
            self.id = FrequencyValueId(self.id)
        super().__post_init__(**kwargs)


@dataclass
class ClinicalModifier(Attribute):
    """
    Used to characterize and specify the phenotypic abnormalities defined in the Phenotypic abnormality subontology,
    with respect to severity, laterality, age of onset, and other aspects
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = BIOLINK.ClinicalModifier
    class_class_curie: ClassVar[str] = "biolink:ClinicalModifier"
    class_name: ClassVar[str] = "clinical modifier"
    class_model_uri: ClassVar[URIRef] = BIOLINK.ClinicalModifier

    id: Union[str, ClinicalModifierId] = None
    name: Union[str, LabelType] = None
    category: List[Union[str, IriType]] = empty_list()

    def __post_init__(self, **kwargs: Dict[str, Any]):
        if self.id is None:
            raise ValueError(f"id must be supplied")
        if not isinstance(self.id, ClinicalModifierId):
            self.id = ClinicalModifierId(self.id)
        super().__post_init__(**kwargs)


@dataclass
class Onset(Attribute):
    """
    The age group in which manifestations appear
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = BIOLINK.Onset
    class_class_curie: ClassVar[str] = "biolink:Onset"
    class_name: ClassVar[str] = "onset"
    class_model_uri: ClassVar[URIRef] = BIOLINK.Onset

    id: Union[str, OnsetId] = None
    name: Union[str, LabelType] = None
    category: List[Union[str, IriType]] = empty_list()

    def __post_init__(self, **kwargs: Dict[str, Any]):
        if self.id is None:
            raise ValueError(f"id must be supplied")
        if not isinstance(self.id, OnsetId):
            self.id = OnsetId(self.id)
        super().__post_init__(**kwargs)


@dataclass
class NamedThing(YAMLRoot):
    """
    a databased entity or concept/class
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = BIOLINK.NamedThing
    class_class_curie: ClassVar[str] = "biolink:NamedThing"
    class_name: ClassVar[str] = "named thing"
    class_model_uri: ClassVar[URIRef] = BIOLINK.NamedThing

    id: Union[str, NamedThingId]
    name: Union[str, LabelType]
    category: List[Union[str, IriType]] = empty_list()

    def __post_init__(self, **kwargs: Dict[str, Any]):
        if self.id is None:
            raise ValueError(f"id must be supplied")
        if not isinstance(self.id, NamedThingId):
            self.id = NamedThingId(self.id)
        if self.name is None:
            raise ValueError(f"name must be supplied")
        if not isinstance(self.name, LabelType):
            self.name = LabelType(self.name)
        if not isinstance(self.category, list) or len(self.category) == 0:
            raise ValueError(f"category must be a non-empty list")
        self.category = [v if isinstance(v, IriType)
                         else IriType(v) for v in ([self.category] if isinstance(self.category, str) else self.category)]
        super().__post_init__(**kwargs)


@dataclass
class DataFile(NamedThing):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = BIOLINK.DataFile
    class_class_curie: ClassVar[str] = "biolink:DataFile"
    class_name: ClassVar[str] = "data file"
    class_model_uri: ClassVar[URIRef] = BIOLINK.DataFile

    id: Union[str, DataFileId] = None
    name: Union[str, LabelType] = None
    category: List[Union[str, IriType]] = empty_list()

    def __post_init__(self, **kwargs: Dict[str, Any]):
        if self.id is None:
            raise ValueError(f"id must be supplied")
        if not isinstance(self.id, DataFileId):
            self.id = DataFileId(self.id)
        super().__post_init__(**kwargs)


@dataclass
class SourceFile(DataFile):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = BIOLINK.SourceFile
    class_class_curie: ClassVar[str] = "biolink:SourceFile"
    class_name: ClassVar[str] = "source file"
    class_model_uri: ClassVar[URIRef] = BIOLINK.SourceFile

    id: Union[str, SourceFileId] = None
    name: Union[str, LabelType] = None
    category: List[Union[str, IriType]] = empty_list()
    source_version: Optional[str] = None
    retrievedOn: Optional[Union[str, XSDDate]] = None

    def __post_init__(self, **kwargs: Dict[str, Any]):
        if self.id is None:
            raise ValueError(f"id must be supplied")
        if not isinstance(self.id, SourceFileId):
            self.id = SourceFileId(self.id)
        if self.retrievedOn is not None and not isinstance(self.retrievedOn, XSDDate):
            self.retrievedOn = XSDDate(self.retrievedOn)
        super().__post_init__(**kwargs)


@dataclass
class DataSet(NamedThing):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = BIOLINK.DataSet
    class_class_curie: ClassVar[str] = "biolink:DataSet"
    class_name: ClassVar[str] = "data set"
    class_model_uri: ClassVar[URIRef] = BIOLINK.DataSet

    id: Union[str, DataSetId] = None
    name: Union[str, LabelType] = None
    category: List[Union[str, IriType]] = empty_list()

    def __post_init__(self, **kwargs: Dict[str, Any]):
        if self.id is None:
            raise ValueError(f"id must be supplied")
        if not isinstance(self.id, DataSetId):
            self.id = DataSetId(self.id)
        super().__post_init__(**kwargs)


@dataclass
class DataSetVersion(DataSet):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = BIOLINK.DataSetVersion
    class_class_curie: ClassVar[str] = "biolink:DataSetVersion"
    class_name: ClassVar[str] = "data set version"
    class_model_uri: ClassVar[URIRef] = BIOLINK.DataSetVersion

    id: Union[str, DataSetVersionId] = None
    name: Union[str, LabelType] = None
    category: List[Union[str, IriType]] = empty_list()
    title: Optional[str] = None
    source_data_file: Optional[Union[str, DataFileId]] = None
    versionOf: Optional[Union[str, DataSetId]] = None
    type: Optional[str] = None
    distribution: Optional[Union[str, DistributionLevelId]] = None

    def __post_init__(self, **kwargs: Dict[str, Any]):
        if self.id is None:
            raise ValueError(f"id must be supplied")
        if not isinstance(self.id, DataSetVersionId):
            self.id = DataSetVersionId(self.id)
        if self.source_data_file is not None and not isinstance(self.source_data_file, DataFileId):
            self.source_data_file = DataFileId(self.source_data_file)
        if self.versionOf is not None and not isinstance(self.versionOf, DataSetId):
            self.versionOf = DataSetId(self.versionOf)
        if self.distribution is not None and not isinstance(self.distribution, DistributionLevelId):
            self.distribution = DistributionLevelId(self.distribution)
        super().__post_init__(**kwargs)


@dataclass
class BiologicalEntity(NamedThing):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = BIOLINK.BiologicalEntity
    class_class_curie: ClassVar[str] = "biolink:BiologicalEntity"
    class_name: ClassVar[str] = "biological entity"
    class_model_uri: ClassVar[URIRef] = BIOLINK.BiologicalEntity

    id: Union[str, BiologicalEntityId] = None
    name: Union[str, LabelType] = None
    category: List[Union[str, IriType]] = empty_list()

@dataclass
class OntologyClass(NamedThing):
    """
    a concept or class in an ontology, vocabulary or thesaurus
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = BIOLINK.OntologyClass
    class_class_curie: ClassVar[str] = "biolink:OntologyClass"
    class_name: ClassVar[str] = "ontology class"
    class_model_uri: ClassVar[URIRef] = BIOLINK.OntologyClass

    id: Union[str, OntologyClassId] = None
    name: Union[str, LabelType] = None
    category: List[Union[str, IriType]] = empty_list()

    def __post_init__(self, **kwargs: Dict[str, Any]):
        if self.id is None:
            raise ValueError(f"id must be supplied")
        if not isinstance(self.id, OntologyClassId):
            self.id = OntologyClassId(self.id)
        super().__post_init__(**kwargs)


@dataclass
class RelationshipType(OntologyClass):
    """
    An OWL property used as an edge label
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = BIOLINK.RelationshipType
    class_class_curie: ClassVar[str] = "biolink:RelationshipType"
    class_name: ClassVar[str] = "relationship type"
    class_model_uri: ClassVar[URIRef] = BIOLINK.RelationshipType

    id: Union[str, RelationshipTypeId] = None
    name: Union[str, LabelType] = None
    category: List[Union[str, IriType]] = empty_list()

    def __post_init__(self, **kwargs: Dict[str, Any]):
        if self.id is None:
            raise ValueError(f"id must be supplied")
        if not isinstance(self.id, RelationshipTypeId):
            self.id = RelationshipTypeId(self.id)
        super().__post_init__(**kwargs)


@dataclass
class GeneOntologyClass(OntologyClass):
    """
    an ontology class that describes a functional aspect of a gene, gene prodoct or complex
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = BIOLINK.GeneOntologyClass
    class_class_curie: ClassVar[str] = "biolink:GeneOntologyClass"
    class_name: ClassVar[str] = "gene ontology class"
    class_model_uri: ClassVar[URIRef] = BIOLINK.GeneOntologyClass

    id: Union[str, GeneOntologyClassId] = None
    name: Union[str, LabelType] = None
    category: List[Union[str, IriType]] = empty_list()

    def __post_init__(self, **kwargs: Dict[str, Any]):
        if self.id is None:
            raise ValueError(f"id must be supplied")
        if not isinstance(self.id, GeneOntologyClassId):
            self.id = GeneOntologyClassId(self.id)
        super().__post_init__(**kwargs)


@dataclass
class OrganismTaxon(OntologyClass):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = BIOLINK.OrganismTaxon
    class_class_curie: ClassVar[str] = "biolink:OrganismTaxon"
    class_name: ClassVar[str] = "organism taxon"
    class_model_uri: ClassVar[URIRef] = BIOLINK.OrganismTaxon

    id: Union[str, OrganismTaxonId] = None
    name: Union[str, LabelType] = None
    category: List[Union[str, IriType]] = empty_list()

    def __post_init__(self, **kwargs: Dict[str, Any]):
        if self.id is None:
            raise ValueError(f"id must be supplied")
        if not isinstance(self.id, OrganismTaxonId):
            self.id = OrganismTaxonId(self.id)
        super().__post_init__(**kwargs)


@dataclass
class OrganismalEntity(BiologicalEntity):
    """
    A named entity that is either a part of an organism, a whole organism, population or clade of organisms, excluding
    molecular entities
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = BIOLINK.OrganismalEntity
    class_class_curie: ClassVar[str] = "biolink:OrganismalEntity"
    class_name: ClassVar[str] = "organismal entity"
    class_model_uri: ClassVar[URIRef] = BIOLINK.OrganismalEntity

    id: Union[str, OrganismalEntityId] = None
    name: Union[str, LabelType] = None
    category: List[Union[str, IriType]] = empty_list()

@dataclass
class IndividualOrganism(OrganismalEntity):
    _inherited_slots: ClassVar[List[str]] = ["in_taxon"]

    class_class_uri: ClassVar[URIRef] = BIOLINK.IndividualOrganism
    class_class_curie: ClassVar[str] = "biolink:IndividualOrganism"
    class_name: ClassVar[str] = "individual organism"
    class_model_uri: ClassVar[URIRef] = BIOLINK.IndividualOrganism

    id: Union[str, IndividualOrganismId] = None
    name: Union[str, LabelType] = None
    category: List[Union[str, IriType]] = empty_list()
    in_taxon: List[Union[str, OrganismTaxonId]] = empty_list()

    def __post_init__(self, **kwargs: Dict[str, Any]):
        if self.id is None:
            raise ValueError(f"id must be supplied")
        if not isinstance(self.id, IndividualOrganismId):
            self.id = IndividualOrganismId(self.id)
        self.in_taxon = [v if isinstance(v, OrganismTaxonId)
                         else OrganismTaxonId(v) for v in ([self.in_taxon] if isinstance(self.in_taxon, str) else self.in_taxon)]
        super().__post_init__(**kwargs)


@dataclass
class Case(IndividualOrganism):
    """
    An individual organism that has a patient role in some clinical context.
    """
    _inherited_slots: ClassVar[List[str]] = ["in_taxon"]

    class_class_uri: ClassVar[URIRef] = BIOLINK.Case
    class_class_curie: ClassVar[str] = "biolink:Case"
    class_name: ClassVar[str] = "case"
    class_model_uri: ClassVar[URIRef] = BIOLINK.Case

    id: Union[str, CaseId] = None
    name: Union[str, LabelType] = None
    category: List[Union[str, IriType]] = empty_list()

    def __post_init__(self, **kwargs: Dict[str, Any]):
        if self.id is None:
            raise ValueError(f"id must be supplied")
        if not isinstance(self.id, CaseId):
            self.id = CaseId(self.id)
        super().__post_init__(**kwargs)


@dataclass
class PopulationOfIndividualOrganisms(OrganismalEntity):
    """
    A collection of individuals from the same taxonomic class distinguished by one or more characteristics.
    Characteristics can include, but are not limited to, shared geographic location, genetics, phenotypes [Alliance
    for Genome Resources]
    """
    _inherited_slots: ClassVar[List[str]] = ["in_taxon"]

    class_class_uri: ClassVar[URIRef] = BIOLINK.PopulationOfIndividualOrganisms
    class_class_curie: ClassVar[str] = "biolink:PopulationOfIndividualOrganisms"
    class_name: ClassVar[str] = "population of individual organisms"
    class_model_uri: ClassVar[URIRef] = BIOLINK.PopulationOfIndividualOrganisms

    id: Union[str, PopulationOfIndividualOrganismsId] = None
    name: Union[str, LabelType] = None
    category: List[Union[str, IriType]] = empty_list()
    in_taxon: List[Union[str, OrganismTaxonId]] = empty_list()

    def __post_init__(self, **kwargs: Dict[str, Any]):
        if self.id is None:
            raise ValueError(f"id must be supplied")
        if not isinstance(self.id, PopulationOfIndividualOrganismsId):
            self.id = PopulationOfIndividualOrganismsId(self.id)
        self.in_taxon = [v if isinstance(v, OrganismTaxonId)
                         else OrganismTaxonId(v) for v in ([self.in_taxon] if isinstance(self.in_taxon, str) else self.in_taxon)]
        super().__post_init__(**kwargs)


@dataclass
class MaterialSample(NamedThing):
    """
    A sample is a limited quantity of something (e.g. an individual or set of individuals from a population, or a
    portion of a substance) to be used for testing, analysis, inspection, investigation, demonstration, or trial use.
    [SIO]
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = BIOLINK.MaterialSample
    class_class_curie: ClassVar[str] = "biolink:MaterialSample"
    class_name: ClassVar[str] = "material sample"
    class_model_uri: ClassVar[URIRef] = BIOLINK.MaterialSample

    id: Union[str, MaterialSampleId] = None
    name: Union[str, LabelType] = None
    category: List[Union[str, IriType]] = empty_list()
    has_attribute: List[Union[str, AttributeId]] = empty_list()

    def __post_init__(self, **kwargs: Dict[str, Any]):
        if self.id is None:
            raise ValueError(f"id must be supplied")
        if not isinstance(self.id, MaterialSampleId):
            self.id = MaterialSampleId(self.id)
        self.has_attribute = [v if isinstance(v, AttributeId)
                              else AttributeId(v) for v in ([self.has_attribute] if isinstance(self.has_attribute, str) else self.has_attribute)]
        super().__post_init__(**kwargs)


@dataclass
class DiseaseOrPhenotypicFeature(BiologicalEntity):
    """
    Either one of a disease or an individual phenotypic feature. Some knowledge resources such as Monarch treat these
    as distinct, others such as MESH conflate.
    """
    _inherited_slots: ClassVar[List[str]] = ["in_taxon"]

    class_class_uri: ClassVar[URIRef] = BIOLINK.DiseaseOrPhenotypicFeature
    class_class_curie: ClassVar[str] = "biolink:DiseaseOrPhenotypicFeature"
    class_name: ClassVar[str] = "disease or phenotypic feature"
    class_model_uri: ClassVar[URIRef] = BIOLINK.DiseaseOrPhenotypicFeature

    id: Union[str, DiseaseOrPhenotypicFeatureId] = None
    name: Union[str, LabelType] = None
    category: List[Union[str, IriType]] = empty_list()
    in_taxon: List[Union[str, OrganismTaxonId]] = empty_list()

    def __post_init__(self, **kwargs: Dict[str, Any]):
        if self.id is None:
            raise ValueError(f"id must be supplied")
        if not isinstance(self.id, DiseaseOrPhenotypicFeatureId):
            self.id = DiseaseOrPhenotypicFeatureId(self.id)
        self.in_taxon = [v if isinstance(v, OrganismTaxonId)
                         else OrganismTaxonId(v) for v in ([self.in_taxon] if isinstance(self.in_taxon, str) else self.in_taxon)]
        super().__post_init__(**kwargs)


@dataclass
class Disease(DiseaseOrPhenotypicFeature):
    _inherited_slots: ClassVar[List[str]] = ["in_taxon"]

    class_class_uri: ClassVar[URIRef] = BIOLINK.Disease
    class_class_curie: ClassVar[str] = "biolink:Disease"
    class_name: ClassVar[str] = "disease"
    class_model_uri: ClassVar[URIRef] = BIOLINK.Disease

    id: Union[str, DiseaseId] = None
    name: Union[str, LabelType] = None
    category: List[Union[str, IriType]] = empty_list()

    def __post_init__(self, **kwargs: Dict[str, Any]):
        if self.id is None:
            raise ValueError(f"id must be supplied")
        if not isinstance(self.id, DiseaseId):
            self.id = DiseaseId(self.id)
        super().__post_init__(**kwargs)


@dataclass
class PhenotypicFeature(DiseaseOrPhenotypicFeature):
    _inherited_slots: ClassVar[List[str]] = ["in_taxon"]

    class_class_uri: ClassVar[URIRef] = BIOLINK.PhenotypicFeature
    class_class_curie: ClassVar[str] = "biolink:PhenotypicFeature"
    class_name: ClassVar[str] = "phenotypic feature"
    class_model_uri: ClassVar[URIRef] = BIOLINK.PhenotypicFeature

    id: Union[str, PhenotypicFeatureId] = None
    name: Union[str, LabelType] = None
    category: List[Union[str, IriType]] = empty_list()

    def __post_init__(self, **kwargs: Dict[str, Any]):
        if self.id is None:
            raise ValueError(f"id must be supplied")
        if not isinstance(self.id, PhenotypicFeatureId):
            self.id = PhenotypicFeatureId(self.id)
        super().__post_init__(**kwargs)


@dataclass
class ExposureEvent(BiologicalEntity):
    """
    A feature of the environment of an organism that influences one or more phenotypic features of that organism,
    potentially mediated by genes
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = BIOLINK.ExposureEvent
    class_class_curie: ClassVar[str] = "biolink:ExposureEvent"
    class_name: ClassVar[str] = "exposure event"
    class_model_uri: ClassVar[URIRef] = BIOLINK.ExposureEvent

    id: Union[str, ExposureEventId] = None
    name: Union[str, LabelType] = None
    category: List[Union[str, IriType]] = empty_list()

    def __post_init__(self, **kwargs: Dict[str, Any]):
        if self.id is None:
            raise ValueError(f"id must be supplied")
        if not isinstance(self.id, ExposureEventId):
            self.id = ExposureEventId(self.id)
        super().__post_init__(**kwargs)


@dataclass
class InformationContentEntity(NamedThing):
    """
    a piece of information that typically describes some piece of biology or is used as support.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = BIOLINK.InformationContentEntity
    class_class_curie: ClassVar[str] = "biolink:InformationContentEntity"
    class_name: ClassVar[str] = "information content entity"
    class_model_uri: ClassVar[URIRef] = BIOLINK.InformationContentEntity

    id: Union[str, InformationContentEntityId] = None
    name: Union[str, LabelType] = None
    category: List[Union[str, IriType]] = empty_list()

@dataclass
class ConfidenceLevel(InformationContentEntity):
    """
    Level of confidence in a statement
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = BIOLINK.ConfidenceLevel
    class_class_curie: ClassVar[str] = "biolink:ConfidenceLevel"
    class_name: ClassVar[str] = "confidence level"
    class_model_uri: ClassVar[URIRef] = BIOLINK.ConfidenceLevel

    id: Union[str, ConfidenceLevelId] = None
    name: Union[str, LabelType] = None
    category: List[Union[str, IriType]] = empty_list()

    def __post_init__(self, **kwargs: Dict[str, Any]):
        if self.id is None:
            raise ValueError(f"id must be supplied")
        if not isinstance(self.id, ConfidenceLevelId):
            self.id = ConfidenceLevelId(self.id)
        super().__post_init__(**kwargs)


@dataclass
class EvidenceType(InformationContentEntity):
    """
    Class of evidence that supports an association
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = BIOLINK.EvidenceType
    class_class_curie: ClassVar[str] = "biolink:EvidenceType"
    class_name: ClassVar[str] = "evidence type"
    class_model_uri: ClassVar[URIRef] = BIOLINK.EvidenceType

    id: Union[str, EvidenceTypeId] = None
    name: Union[str, LabelType] = None
    category: List[Union[str, IriType]] = empty_list()

    def __post_init__(self, **kwargs: Dict[str, Any]):
        if self.id is None:
            raise ValueError(f"id must be supplied")
        if not isinstance(self.id, EvidenceTypeId):
            self.id = EvidenceTypeId(self.id)
        super().__post_init__(**kwargs)


@dataclass
class Publication(InformationContentEntity):
    """
    Any published piece of information. Can refer to a whole publication, or to a part of it (e.g. a figure, figure
    legend, or section highlighted by NLP). The scope is intended to be general and include information published on
    the web as well as journals.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = BIOLINK.Publication
    class_class_curie: ClassVar[str] = "biolink:Publication"
    class_name: ClassVar[str] = "publication"
    class_model_uri: ClassVar[URIRef] = BIOLINK.Publication

    id: Union[str, PublicationId] = None
    name: Union[str, LabelType] = None
    category: List[Union[str, IriType]] = empty_list()

    def __post_init__(self, **kwargs: Dict[str, Any]):
        if self.id is None:
            raise ValueError(f"id must be supplied")
        if not isinstance(self.id, PublicationId):
            self.id = PublicationId(self.id)
        super().__post_init__(**kwargs)


@dataclass
class AdministrativeEntity(NamedThing):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = BIOLINK.AdministrativeEntity
    class_class_curie: ClassVar[str] = "biolink:AdministrativeEntity"
    class_name: ClassVar[str] = "administrative entity"
    class_model_uri: ClassVar[URIRef] = BIOLINK.AdministrativeEntity

    id: Union[str, AdministrativeEntityId] = None
    name: Union[str, LabelType] = None
    category: List[Union[str, IriType]] = empty_list()

@dataclass
class Provider(AdministrativeEntity):
    """
    person, group, organization or project that provides a piece of information
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = BIOLINK.Provider
    class_class_curie: ClassVar[str] = "biolink:Provider"
    class_name: ClassVar[str] = "provider"
    class_model_uri: ClassVar[URIRef] = BIOLINK.Provider

    id: Union[str, ProviderId] = None
    name: Union[str, LabelType] = None
    category: List[Union[str, IriType]] = empty_list()

    def __post_init__(self, **kwargs: Dict[str, Any]):
        if self.id is None:
            raise ValueError(f"id must be supplied")
        if not isinstance(self.id, ProviderId):
            self.id = ProviderId(self.id)
        super().__post_init__(**kwargs)


@dataclass
class MolecularEntity(BiologicalEntity):
    """
    A gene, gene product, small molecule or macromolecule (including protein complex)
    """
    _inherited_slots: ClassVar[List[str]] = ["in_taxon"]

    class_class_uri: ClassVar[URIRef] = BIOLINK.MolecularEntity
    class_class_curie: ClassVar[str] = "biolink:MolecularEntity"
    class_name: ClassVar[str] = "molecular entity"
    class_model_uri: ClassVar[URIRef] = BIOLINK.MolecularEntity

    id: Union[str, MolecularEntityId] = None
    name: Union[str, LabelType] = None
    category: List[Union[str, IriType]] = empty_list()
    in_taxon: List[Union[str, OrganismTaxonId]] = empty_list()

    def __post_init__(self, **kwargs: Dict[str, Any]):
        if self.id is None:
            raise ValueError(f"id must be supplied")
        if not isinstance(self.id, MolecularEntityId):
            self.id = MolecularEntityId(self.id)
        self.in_taxon = [v if isinstance(v, OrganismTaxonId)
                         else OrganismTaxonId(v) for v in ([self.in_taxon] if isinstance(self.in_taxon, str) else self.in_taxon)]
        super().__post_init__(**kwargs)


@dataclass
class ChemicalSubstance(MolecularEntity):
    """
    May be a chemical entity or a formulation with a chemical entity as active ingredient, or a complex material with
    multiple chemical entities as part
    """
    _inherited_slots: ClassVar[List[str]] = ["in_taxon"]

    class_class_uri: ClassVar[URIRef] = BIOLINK.ChemicalSubstance
    class_class_curie: ClassVar[str] = "biolink:ChemicalSubstance"
    class_name: ClassVar[str] = "chemical substance"
    class_model_uri: ClassVar[URIRef] = BIOLINK.ChemicalSubstance

    id: Union[str, ChemicalSubstanceId] = None
    name: Union[str, LabelType] = None
    category: List[Union[str, IriType]] = empty_list()

    def __post_init__(self, **kwargs: Dict[str, Any]):
        if self.id is None:
            raise ValueError(f"id must be supplied")
        if not isinstance(self.id, ChemicalSubstanceId):
            self.id = ChemicalSubstanceId(self.id)
        super().__post_init__(**kwargs)


@dataclass
class Carbohydrate(ChemicalSubstance):
    _inherited_slots: ClassVar[List[str]] = ["in_taxon"]

    class_class_uri: ClassVar[URIRef] = BIOLINK.Carbohydrate
    class_class_curie: ClassVar[str] = "biolink:Carbohydrate"
    class_name: ClassVar[str] = "carbohydrate"
    class_model_uri: ClassVar[URIRef] = BIOLINK.Carbohydrate

    id: Union[str, CarbohydrateId] = None
    name: Union[str, LabelType] = None
    category: List[Union[str, IriType]] = empty_list()

    def __post_init__(self, **kwargs: Dict[str, Any]):
        if self.id is None:
            raise ValueError(f"id must be supplied")
        if not isinstance(self.id, CarbohydrateId):
            self.id = CarbohydrateId(self.id)
        super().__post_init__(**kwargs)


@dataclass
class Drug(ChemicalSubstance):
    """
    A substance intended for use in the diagnosis, cure, mitigation, treatment, or prevention of disease
    """
    _inherited_slots: ClassVar[List[str]] = ["in_taxon"]

    class_class_uri: ClassVar[URIRef] = BIOLINK.Drug
    class_class_curie: ClassVar[str] = "biolink:Drug"
    class_name: ClassVar[str] = "drug"
    class_model_uri: ClassVar[URIRef] = BIOLINK.Drug

    id: Union[str, DrugId] = None
    name: Union[str, LabelType] = None
    category: List[Union[str, IriType]] = empty_list()

    def __post_init__(self, **kwargs: Dict[str, Any]):
        if self.id is None:
            raise ValueError(f"id must be supplied")
        if not isinstance(self.id, DrugId):
            self.id = DrugId(self.id)
        super().__post_init__(**kwargs)


@dataclass
class Metabolite(ChemicalSubstance):
    """
    Any intermediate or product resulting from metabolism. Includes primary and secondary metabolites.
    """
    _inherited_slots: ClassVar[List[str]] = ["in_taxon"]

    class_class_uri: ClassVar[URIRef] = BIOLINK.Metabolite
    class_class_curie: ClassVar[str] = "biolink:Metabolite"
    class_name: ClassVar[str] = "metabolite"
    class_model_uri: ClassVar[URIRef] = BIOLINK.Metabolite

    id: Union[str, MetaboliteId] = None
    name: Union[str, LabelType] = None
    category: List[Union[str, IriType]] = empty_list()

    def __post_init__(self, **kwargs: Dict[str, Any]):
        if self.id is None:
            raise ValueError(f"id must be supplied")
        if not isinstance(self.id, MetaboliteId):
            self.id = MetaboliteId(self.id)
        super().__post_init__(**kwargs)


@dataclass
class AnatomicalEntity(OrganismalEntity):
    """
    A subcellular location, cell type or gross anatomical part
    """
    _inherited_slots: ClassVar[List[str]] = ["in_taxon"]

    class_class_uri: ClassVar[URIRef] = BIOLINK.AnatomicalEntity
    class_class_curie: ClassVar[str] = "biolink:AnatomicalEntity"
    class_name: ClassVar[str] = "anatomical entity"
    class_model_uri: ClassVar[URIRef] = BIOLINK.AnatomicalEntity

    id: Union[str, AnatomicalEntityId] = None
    name: Union[str, LabelType] = None
    category: List[Union[str, IriType]] = empty_list()
    in_taxon: List[Union[str, OrganismTaxonId]] = empty_list()

    def __post_init__(self, **kwargs: Dict[str, Any]):
        if self.id is None:
            raise ValueError(f"id must be supplied")
        if not isinstance(self.id, AnatomicalEntityId):
            self.id = AnatomicalEntityId(self.id)
        self.in_taxon = [v if isinstance(v, OrganismTaxonId)
                         else OrganismTaxonId(v) for v in ([self.in_taxon] if isinstance(self.in_taxon, str) else self.in_taxon)]
        super().__post_init__(**kwargs)


@dataclass
class LifeStage(OrganismalEntity):
    """
    A stage of development or growth of an organism, including post-natal adult stages
    """
    _inherited_slots: ClassVar[List[str]] = ["in_taxon"]

    class_class_uri: ClassVar[URIRef] = BIOLINK.LifeStage
    class_class_curie: ClassVar[str] = "biolink:LifeStage"
    class_name: ClassVar[str] = "life stage"
    class_model_uri: ClassVar[URIRef] = BIOLINK.LifeStage

    id: Union[str, LifeStageId] = None
    name: Union[str, LabelType] = None
    category: List[Union[str, IriType]] = empty_list()
    in_taxon: List[Union[str, OrganismTaxonId]] = empty_list()

    def __post_init__(self, **kwargs: Dict[str, Any]):
        if self.id is None:
            raise ValueError(f"id must be supplied")
        if not isinstance(self.id, LifeStageId):
            self.id = LifeStageId(self.id)
        self.in_taxon = [v if isinstance(v, OrganismTaxonId)
                         else OrganismTaxonId(v) for v in ([self.in_taxon] if isinstance(self.in_taxon, str) else self.in_taxon)]
        super().__post_init__(**kwargs)


@dataclass
class PlanetaryEntity(NamedThing):
    """
    Any entity or process that exists at the level of the whole planet
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = BIOLINK.PlanetaryEntity
    class_class_curie: ClassVar[str] = "biolink:PlanetaryEntity"
    class_name: ClassVar[str] = "planetary entity"
    class_model_uri: ClassVar[URIRef] = BIOLINK.PlanetaryEntity

    id: Union[str, PlanetaryEntityId] = None
    name: Union[str, LabelType] = None
    category: List[Union[str, IriType]] = empty_list()

    def __post_init__(self, **kwargs: Dict[str, Any]):
        if self.id is None:
            raise ValueError(f"id must be supplied")
        if not isinstance(self.id, PlanetaryEntityId):
            self.id = PlanetaryEntityId(self.id)
        super().__post_init__(**kwargs)


@dataclass
class EnvironmentalProcess(PlanetaryEntity):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = BIOLINK.EnvironmentalProcess
    class_class_curie: ClassVar[str] = "biolink:EnvironmentalProcess"
    class_name: ClassVar[str] = "environmental process"
    class_model_uri: ClassVar[URIRef] = BIOLINK.EnvironmentalProcess

    id: Union[str, EnvironmentalProcessId] = None
    name: Union[str, LabelType] = None
    category: List[Union[str, IriType]] = empty_list()

    def __post_init__(self, **kwargs: Dict[str, Any]):
        if self.id is None:
            raise ValueError(f"id must be supplied")
        if not isinstance(self.id, EnvironmentalProcessId):
            self.id = EnvironmentalProcessId(self.id)
        super().__post_init__(**kwargs)


@dataclass
class EnvironmentalFeature(PlanetaryEntity):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = BIOLINK.EnvironmentalFeature
    class_class_curie: ClassVar[str] = "biolink:EnvironmentalFeature"
    class_name: ClassVar[str] = "environmental feature"
    class_model_uri: ClassVar[URIRef] = BIOLINK.EnvironmentalFeature

    id: Union[str, EnvironmentalFeatureId] = None
    name: Union[str, LabelType] = None
    category: List[Union[str, IriType]] = empty_list()

    def __post_init__(self, **kwargs: Dict[str, Any]):
        if self.id is None:
            raise ValueError(f"id must be supplied")
        if not isinstance(self.id, EnvironmentalFeatureId):
            self.id = EnvironmentalFeatureId(self.id)
        super().__post_init__(**kwargs)


@dataclass
class ClinicalEntity(NamedThing):
    """
    Any entity or process that exists in the clinical domain and outside the biological realm. Diseases are placed
    under biological entities
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = BIOLINK.ClinicalEntity
    class_class_curie: ClassVar[str] = "biolink:ClinicalEntity"
    class_name: ClassVar[str] = "clinical entity"
    class_model_uri: ClassVar[URIRef] = BIOLINK.ClinicalEntity

    id: Union[str, ClinicalEntityId] = None
    name: Union[str, LabelType] = None
    category: List[Union[str, IriType]] = empty_list()

    def __post_init__(self, **kwargs: Dict[str, Any]):
        if self.id is None:
            raise ValueError(f"id must be supplied")
        if not isinstance(self.id, ClinicalEntityId):
            self.id = ClinicalEntityId(self.id)
        super().__post_init__(**kwargs)


@dataclass
class ClinicalTrial(ClinicalEntity):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = BIOLINK.ClinicalTrial
    class_class_curie: ClassVar[str] = "biolink:ClinicalTrial"
    class_name: ClassVar[str] = "clinical trial"
    class_model_uri: ClassVar[URIRef] = BIOLINK.ClinicalTrial

    id: Union[str, ClinicalTrialId] = None
    name: Union[str, LabelType] = None
    category: List[Union[str, IriType]] = empty_list()

    def __post_init__(self, **kwargs: Dict[str, Any]):
        if self.id is None:
            raise ValueError(f"id must be supplied")
        if not isinstance(self.id, ClinicalTrialId):
            self.id = ClinicalTrialId(self.id)
        super().__post_init__(**kwargs)


@dataclass
class ClinicalIntervention(ClinicalEntity):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = BIOLINK.ClinicalIntervention
    class_class_curie: ClassVar[str] = "biolink:ClinicalIntervention"
    class_name: ClassVar[str] = "clinical intervention"
    class_model_uri: ClassVar[URIRef] = BIOLINK.ClinicalIntervention

    id: Union[str, ClinicalInterventionId] = None
    name: Union[str, LabelType] = None
    category: List[Union[str, IriType]] = empty_list()

    def __post_init__(self, **kwargs: Dict[str, Any]):
        if self.id is None:
            raise ValueError(f"id must be supplied")
        if not isinstance(self.id, ClinicalInterventionId):
            self.id = ClinicalInterventionId(self.id)
        super().__post_init__(**kwargs)


@dataclass
class Device(NamedThing):
    """
    A thing made or adapted for a particular purpose, especially a piece of mechanical or electronic equipment
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = BIOLINK.Device
    class_class_curie: ClassVar[str] = "biolink:Device"
    class_name: ClassVar[str] = "device"
    class_model_uri: ClassVar[URIRef] = BIOLINK.Device

    id: Union[str, DeviceId] = None
    name: Union[str, LabelType] = None
    category: List[Union[str, IriType]] = empty_list()

    def __post_init__(self, **kwargs: Dict[str, Any]):
        if self.id is None:
            raise ValueError(f"id must be supplied")
        if not isinstance(self.id, DeviceId):
            self.id = DeviceId(self.id)
        super().__post_init__(**kwargs)


@dataclass
class GenomicEntity(MolecularEntity):
    """
    an entity that can either be directly located on a genome (gene, transcript, exon, regulatory region) or is
    encoded in a genome (protein)
    """
    _inherited_slots: ClassVar[List[str]] = ["in_taxon"]

    class_class_uri: ClassVar[URIRef] = BIOLINK.GenomicEntity
    class_class_curie: ClassVar[str] = "biolink:GenomicEntity"
    class_name: ClassVar[str] = "genomic entity"
    class_model_uri: ClassVar[URIRef] = BIOLINK.GenomicEntity

    id: Union[str, GenomicEntityId] = None
    name: Union[str, LabelType] = None
    category: List[Union[str, IriType]] = empty_list()
    has_biological_sequence: Optional[Union[str, BiologicalSequence]] = None

    def __post_init__(self, **kwargs: Dict[str, Any]):
        if self.id is None:
            raise ValueError(f"id must be supplied")
        if not isinstance(self.id, GenomicEntityId):
            self.id = GenomicEntityId(self.id)
        if self.has_biological_sequence is not None and not isinstance(self.has_biological_sequence, BiologicalSequence):
            self.has_biological_sequence = BiologicalSequence(self.has_biological_sequence)
        super().__post_init__(**kwargs)


@dataclass
class Genome(GenomicEntity):
    """
    A genome is the sum of genetic material within a cell or virion.
    """
    _inherited_slots: ClassVar[List[str]] = ["in_taxon"]

    class_class_uri: ClassVar[URIRef] = BIOLINK.Genome
    class_class_curie: ClassVar[str] = "biolink:Genome"
    class_name: ClassVar[str] = "genome"
    class_model_uri: ClassVar[URIRef] = BIOLINK.Genome

    id: Union[str, GenomeId] = None
    name: Union[str, LabelType] = None
    category: List[Union[str, IriType]] = empty_list()

    def __post_init__(self, **kwargs: Dict[str, Any]):
        if self.id is None:
            raise ValueError(f"id must be supplied")
        if not isinstance(self.id, GenomeId):
            self.id = GenomeId(self.id)
        super().__post_init__(**kwargs)


@dataclass
class Transcript(GenomicEntity):
    """
    An RNA synthesized on a DNA or RNA template by an RNA polymerase
    """
    _inherited_slots: ClassVar[List[str]] = ["in_taxon"]

    class_class_uri: ClassVar[URIRef] = BIOLINK.Transcript
    class_class_curie: ClassVar[str] = "biolink:Transcript"
    class_name: ClassVar[str] = "transcript"
    class_model_uri: ClassVar[URIRef] = BIOLINK.Transcript

    id: Union[str, TranscriptId] = None
    name: Union[str, LabelType] = None
    category: List[Union[str, IriType]] = empty_list()

    def __post_init__(self, **kwargs: Dict[str, Any]):
        if self.id is None:
            raise ValueError(f"id must be supplied")
        if not isinstance(self.id, TranscriptId):
            self.id = TranscriptId(self.id)
        super().__post_init__(**kwargs)


@dataclass
class Exon(GenomicEntity):
    """
    A region of the transcript sequence within a gene which is not removed from the primary RNA transcript by RNA
    splicing
    """
    _inherited_slots: ClassVar[List[str]] = ["in_taxon"]

    class_class_uri: ClassVar[URIRef] = BIOLINK.Exon
    class_class_curie: ClassVar[str] = "biolink:Exon"
    class_name: ClassVar[str] = "exon"
    class_model_uri: ClassVar[URIRef] = BIOLINK.Exon

    id: Union[str, ExonId] = None
    name: Union[str, LabelType] = None
    category: List[Union[str, IriType]] = empty_list()

    def __post_init__(self, **kwargs: Dict[str, Any]):
        if self.id is None:
            raise ValueError(f"id must be supplied")
        if not isinstance(self.id, ExonId):
            self.id = ExonId(self.id)
        super().__post_init__(**kwargs)


@dataclass
class CodingSequence(GenomicEntity):
    _inherited_slots: ClassVar[List[str]] = ["in_taxon"]

    class_class_uri: ClassVar[URIRef] = BIOLINK.CodingSequence
    class_class_curie: ClassVar[str] = "biolink:CodingSequence"
    class_name: ClassVar[str] = "coding sequence"
    class_model_uri: ClassVar[URIRef] = BIOLINK.CodingSequence

    id: Union[str, CodingSequenceId] = None
    name: Union[str, LabelType] = None
    category: List[Union[str, IriType]] = empty_list()

    def __post_init__(self, **kwargs: Dict[str, Any]):
        if self.id is None:
            raise ValueError(f"id must be supplied")
        if not isinstance(self.id, CodingSequenceId):
            self.id = CodingSequenceId(self.id)
        super().__post_init__(**kwargs)


@dataclass
class MacromolecularMachine(GenomicEntity):
    """
    A union of gene, gene product, and macromolecular complex. These are the basic units of function in a cell. They
    either carry out individual biological activities, or they encode molecules which do this.
    """
    _inherited_slots: ClassVar[List[str]] = ["in_taxon"]

    class_class_uri: ClassVar[URIRef] = BIOLINK.MacromolecularMachine
    class_class_curie: ClassVar[str] = "biolink:MacromolecularMachine"
    class_name: ClassVar[str] = "macromolecular machine"
    class_model_uri: ClassVar[URIRef] = BIOLINK.MacromolecularMachine

    id: Union[str, MacromolecularMachineId] = None
    category: List[Union[str, IriType]] = empty_list()
    name: Union[str, SymbolType] = None

    def __post_init__(self, **kwargs: Dict[str, Any]):
        if self.id is None:
            raise ValueError(f"id must be supplied")
        if not isinstance(self.id, MacromolecularMachineId):
            self.id = MacromolecularMachineId(self.id)
        if self.name is None:
            raise ValueError(f"name must be supplied")
        if not isinstance(self.name, SymbolType):
            self.name = SymbolType(self.name)
        super().__post_init__(**kwargs)


@dataclass
class GeneOrGeneProduct(MacromolecularMachine):
    """
    a union of genes or gene products. Frequently an identifier for one will be used as proxy for another
    """
    _inherited_slots: ClassVar[List[str]] = ["in_taxon"]

    class_class_uri: ClassVar[URIRef] = BIOLINK.GeneOrGeneProduct
    class_class_curie: ClassVar[str] = "biolink:GeneOrGeneProduct"
    class_name: ClassVar[str] = "gene or gene product"
    class_model_uri: ClassVar[URIRef] = BIOLINK.GeneOrGeneProduct

    id: Union[str, GeneOrGeneProductId] = None
    category: List[Union[str, IriType]] = empty_list()
    name: Union[str, SymbolType] = None

    def __post_init__(self, **kwargs: Dict[str, Any]):
        if self.id is None:
            raise ValueError(f"id must be supplied")
        if not isinstance(self.id, GeneOrGeneProductId):
            self.id = GeneOrGeneProductId(self.id)
        super().__post_init__(**kwargs)


@dataclass
class Gene(GeneOrGeneProduct):
    _inherited_slots: ClassVar[List[str]] = ["in_taxon"]

    class_class_uri: ClassVar[URIRef] = BIOLINK.Gene
    class_class_curie: ClassVar[str] = "biolink:Gene"
    class_name: ClassVar[str] = "gene"
    class_model_uri: ClassVar[URIRef] = BIOLINK.Gene

    id: Union[str, GeneId] = None
    category: List[Union[str, IriType]] = empty_list()
    name: Union[str, SymbolType] = None

    def __post_init__(self, **kwargs: Dict[str, Any]):
        if self.id is None:
            raise ValueError(f"id must be supplied")
        if not isinstance(self.id, GeneId):
            self.id = GeneId(self.id)
        super().__post_init__(**kwargs)


@dataclass
class GeneProduct(GeneOrGeneProduct):
    """
    The functional molecular product of a single gene. Gene products are either proteins or functional RNA molecules
    """
    _inherited_slots: ClassVar[List[str]] = ["in_taxon"]

    class_class_uri: ClassVar[URIRef] = BIOLINK.GeneProduct
    class_class_curie: ClassVar[str] = "biolink:GeneProduct"
    class_name: ClassVar[str] = "gene product"
    class_model_uri: ClassVar[URIRef] = BIOLINK.GeneProduct

    id: Union[str, GeneProductId] = None
    category: List[Union[str, IriType]] = empty_list()
    name: Union[str, SymbolType] = None

    def __post_init__(self, **kwargs: Dict[str, Any]):
        if self.id is None:
            raise ValueError(f"id must be supplied")
        if not isinstance(self.id, GeneProductId):
            self.id = GeneProductId(self.id)
        super().__post_init__(**kwargs)


@dataclass
class Protein(GeneProduct):
    """
    A gene product that is composed of a chain of amino acid sequences and is produced by ribosome-mediated
    translation of mRNA
    """
    _inherited_slots: ClassVar[List[str]] = ["in_taxon"]

    class_class_uri: ClassVar[URIRef] = BIOLINK.Protein
    class_class_curie: ClassVar[str] = "biolink:Protein"
    class_name: ClassVar[str] = "protein"
    class_model_uri: ClassVar[URIRef] = BIOLINK.Protein

    id: Union[str, ProteinId] = None
    category: List[Union[str, IriType]] = empty_list()
    name: Union[str, SymbolType] = None

    def __post_init__(self, **kwargs: Dict[str, Any]):
        if self.id is None:
            raise ValueError(f"id must be supplied")
        if not isinstance(self.id, ProteinId):
            self.id = ProteinId(self.id)
        super().__post_init__(**kwargs)


@dataclass
class GeneProductIsoform(GeneProduct):
    """
    This is an abstract class that can be mixed in with different kinds of gene products to indicate that the gene
    product is intended to represent a specific isoform rather than a canonical or reference or generic product. The
    designation of canonical or reference may be arbitrary, or it may represent the superclass of all isoforms.
    """
    _inherited_slots: ClassVar[List[str]] = ["in_taxon"]

    class_class_uri: ClassVar[URIRef] = BIOLINK.GeneProductIsoform
    class_class_curie: ClassVar[str] = "biolink:GeneProductIsoform"
    class_name: ClassVar[str] = "gene product isoform"
    class_model_uri: ClassVar[URIRef] = BIOLINK.GeneProductIsoform

    id: Union[str, GeneProductIsoformId] = None
    category: List[Union[str, IriType]] = empty_list()
    name: Union[str, SymbolType] = None

@dataclass
class ProteinIsoform(Protein):
    """
    Represents a protein that is a specific isoform of the canonical or reference protein. See
    https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4114032/
    """
    _inherited_slots: ClassVar[List[str]] = ["in_taxon"]

    class_class_uri: ClassVar[URIRef] = BIOLINK.ProteinIsoform
    class_class_curie: ClassVar[str] = "biolink:ProteinIsoform"
    class_name: ClassVar[str] = "protein isoform"
    class_model_uri: ClassVar[URIRef] = BIOLINK.ProteinIsoform

    id: Union[str, ProteinIsoformId] = None
    category: List[Union[str, IriType]] = empty_list()
    name: Union[str, SymbolType] = None

    def __post_init__(self, **kwargs: Dict[str, Any]):
        if self.id is None:
            raise ValueError(f"id must be supplied")
        if not isinstance(self.id, ProteinIsoformId):
            self.id = ProteinIsoformId(self.id)
        super().__post_init__(**kwargs)


@dataclass
class RNAProduct(GeneProduct):
    _inherited_slots: ClassVar[List[str]] = ["in_taxon"]

    class_class_uri: ClassVar[URIRef] = BIOLINK.RNAProduct
    class_class_curie: ClassVar[str] = "biolink:RNAProduct"
    class_name: ClassVar[str] = "RNA product"
    class_model_uri: ClassVar[URIRef] = BIOLINK.RNAProduct

    id: Union[str, RNAProductId] = None
    category: List[Union[str, IriType]] = empty_list()
    name: Union[str, SymbolType] = None

    def __post_init__(self, **kwargs: Dict[str, Any]):
        if self.id is None:
            raise ValueError(f"id must be supplied")
        if not isinstance(self.id, RNAProductId):
            self.id = RNAProductId(self.id)
        super().__post_init__(**kwargs)


@dataclass
class RNAProductIsoform(RNAProduct):
    """
    Represents a protein that is a specific isoform of the canonical or reference RNA
    """
    _inherited_slots: ClassVar[List[str]] = ["in_taxon"]

    class_class_uri: ClassVar[URIRef] = BIOLINK.RNAProductIsoform
    class_class_curie: ClassVar[str] = "biolink:RNAProductIsoform"
    class_name: ClassVar[str] = "RNA product isoform"
    class_model_uri: ClassVar[URIRef] = BIOLINK.RNAProductIsoform

    id: Union[str, RNAProductIsoformId] = None
    category: List[Union[str, IriType]] = empty_list()
    name: Union[str, SymbolType] = None

    def __post_init__(self, **kwargs: Dict[str, Any]):
        if self.id is None:
            raise ValueError(f"id must be supplied")
        if not isinstance(self.id, RNAProductIsoformId):
            self.id = RNAProductIsoformId(self.id)
        super().__post_init__(**kwargs)


@dataclass
class NoncodingRNAProduct(RNAProduct):
    _inherited_slots: ClassVar[List[str]] = ["in_taxon"]

    class_class_uri: ClassVar[URIRef] = BIOLINK.NoncodingRNAProduct
    class_class_curie: ClassVar[str] = "biolink:NoncodingRNAProduct"
    class_name: ClassVar[str] = "noncoding RNA product"
    class_model_uri: ClassVar[URIRef] = BIOLINK.NoncodingRNAProduct

    id: Union[str, NoncodingRNAProductId] = None
    category: List[Union[str, IriType]] = empty_list()
    name: Union[str, SymbolType] = None

    def __post_init__(self, **kwargs: Dict[str, Any]):
        if self.id is None:
            raise ValueError(f"id must be supplied")
        if not isinstance(self.id, NoncodingRNAProductId):
            self.id = NoncodingRNAProductId(self.id)
        super().__post_init__(**kwargs)


@dataclass
class MicroRNA(NoncodingRNAProduct):
    _inherited_slots: ClassVar[List[str]] = ["in_taxon"]

    class_class_uri: ClassVar[URIRef] = BIOLINK.MicroRNA
    class_class_curie: ClassVar[str] = "biolink:MicroRNA"
    class_name: ClassVar[str] = "microRNA"
    class_model_uri: ClassVar[URIRef] = BIOLINK.MicroRNA

    id: Union[str, MicroRNAId] = None
    category: List[Union[str, IriType]] = empty_list()
    name: Union[str, SymbolType] = None

    def __post_init__(self, **kwargs: Dict[str, Any]):
        if self.id is None:
            raise ValueError(f"id must be supplied")
        if not isinstance(self.id, MicroRNAId):
            self.id = MicroRNAId(self.id)
        super().__post_init__(**kwargs)


@dataclass
class MacromolecularComplex(MacromolecularMachine):
    _inherited_slots: ClassVar[List[str]] = ["in_taxon"]

    class_class_uri: ClassVar[URIRef] = BIOLINK.MacromolecularComplex
    class_class_curie: ClassVar[str] = "biolink:MacromolecularComplex"
    class_name: ClassVar[str] = "macromolecular complex"
    class_model_uri: ClassVar[URIRef] = BIOLINK.MacromolecularComplex

    id: Union[str, MacromolecularComplexId] = None
    category: List[Union[str, IriType]] = empty_list()
    name: Union[str, SymbolType] = None

    def __post_init__(self, **kwargs: Dict[str, Any]):
        if self.id is None:
            raise ValueError(f"id must be supplied")
        if not isinstance(self.id, MacromolecularComplexId):
            self.id = MacromolecularComplexId(self.id)
        super().__post_init__(**kwargs)


@dataclass
class GeneFamily(MolecularEntity):
    """
    any grouping of multiple genes or gene products related by common descent
    """
    _inherited_slots: ClassVar[List[str]] = ["in_taxon"]

    class_class_uri: ClassVar[URIRef] = BIOLINK.GeneFamily
    class_class_curie: ClassVar[str] = "biolink:GeneFamily"
    class_name: ClassVar[str] = "gene family"
    class_model_uri: ClassVar[URIRef] = BIOLINK.GeneFamily

    id: Union[str, GeneFamilyId] = None
    name: Union[str, LabelType] = None
    category: List[Union[str, IriType]] = empty_list()

    def __post_init__(self, **kwargs: Dict[str, Any]):
        if self.id is None:
            raise ValueError(f"id must be supplied")
        if not isinstance(self.id, GeneFamilyId):
            self.id = GeneFamilyId(self.id)
        super().__post_init__(**kwargs)


@dataclass
class Zygosity(Attribute):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = BIOLINK.Zygosity
    class_class_curie: ClassVar[str] = "biolink:Zygosity"
    class_name: ClassVar[str] = "zygosity"
    class_model_uri: ClassVar[URIRef] = BIOLINK.Zygosity

    id: Union[str, ZygosityId] = None
    name: Union[str, LabelType] = None
    category: List[Union[str, IriType]] = empty_list()

    def __post_init__(self, **kwargs: Dict[str, Any]):
        if self.id is None:
            raise ValueError(f"id must be supplied")
        if not isinstance(self.id, ZygosityId):
            self.id = ZygosityId(self.id)
        super().__post_init__(**kwargs)


@dataclass
class Genotype(GenomicEntity):
    """
    An information content entity that describes a genome by specifying the total variation in genomic sequence and/or
    gene expression, relative to some extablished background
    """
    _inherited_slots: ClassVar[List[str]] = ["in_taxon"]

    class_class_uri: ClassVar[URIRef] = BIOLINK.Genotype
    class_class_curie: ClassVar[str] = "biolink:Genotype"
    class_name: ClassVar[str] = "genotype"
    class_model_uri: ClassVar[URIRef] = BIOLINK.Genotype

    id: Union[str, GenotypeId] = None
    name: Union[str, LabelType] = None
    category: List[Union[str, IriType]] = empty_list()
    has_zygosity: Optional[Union[str, ZygosityId]] = None

    def __post_init__(self, **kwargs: Dict[str, Any]):
        if self.id is None:
            raise ValueError(f"id must be supplied")
        if not isinstance(self.id, GenotypeId):
            self.id = GenotypeId(self.id)
        if self.has_zygosity is not None and not isinstance(self.has_zygosity, ZygosityId):
            self.has_zygosity = ZygosityId(self.has_zygosity)
        super().__post_init__(**kwargs)


@dataclass
class Haplotype(GenomicEntity):
    """
    A set of zero or more Alleles on a single instance of a Sequence[VMC]
    """
    _inherited_slots: ClassVar[List[str]] = ["in_taxon"]

    class_class_uri: ClassVar[URIRef] = BIOLINK.Haplotype
    class_class_curie: ClassVar[str] = "biolink:Haplotype"
    class_name: ClassVar[str] = "haplotype"
    class_model_uri: ClassVar[URIRef] = BIOLINK.Haplotype

    id: Union[str, HaplotypeId] = None
    name: Union[str, LabelType] = None
    category: List[Union[str, IriType]] = empty_list()

    def __post_init__(self, **kwargs: Dict[str, Any]):
        if self.id is None:
            raise ValueError(f"id must be supplied")
        if not isinstance(self.id, HaplotypeId):
            self.id = HaplotypeId(self.id)
        super().__post_init__(**kwargs)


@dataclass
class SequenceVariant(GenomicEntity):
    """
    An allele that varies in its sequence from what is considered the reference allele at that locus.
    """
    _inherited_slots: ClassVar[List[str]] = ["in_taxon"]

    class_class_uri: ClassVar[URIRef] = BIOLINK.SequenceVariant
    class_class_curie: ClassVar[str] = "biolink:SequenceVariant"
    class_name: ClassVar[str] = "sequence variant"
    class_model_uri: ClassVar[URIRef] = BIOLINK.SequenceVariant

    id: Union[str, SequenceVariantId] = None
    name: Union[str, LabelType] = None
    category: List[Union[str, IriType]] = empty_list()
    has_gene: List[Union[str, GeneId]] = empty_list()
    has_biological_sequence: Optional[Union[str, BiologicalSequence]] = None

    def __post_init__(self, **kwargs: Dict[str, Any]):
        if self.id is None:
            raise ValueError(f"id must be supplied")
        if not isinstance(self.id, SequenceVariantId):
            self.id = SequenceVariantId(self.id)
        self.has_gene = [v if isinstance(v, GeneId)
                         else GeneId(v) for v in ([self.has_gene] if isinstance(self.has_gene, str) else self.has_gene)]
        if self.has_biological_sequence is not None and not isinstance(self.has_biological_sequence, BiologicalSequence):
            self.has_biological_sequence = BiologicalSequence(self.has_biological_sequence)
        super().__post_init__(**kwargs)


@dataclass
class ChemicalExposure(ExposureEvent):
    """
    A chemical exposure is an intake of a particular chemical substance
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = BIOLINK.ChemicalExposure
    class_class_curie: ClassVar[str] = "biolink:ChemicalExposure"
    class_name: ClassVar[str] = "chemical exposure"
    class_model_uri: ClassVar[URIRef] = BIOLINK.ChemicalExposure

    id: Union[str, ChemicalExposureId] = None
    name: Union[str, LabelType] = None
    category: List[Union[str, IriType]] = empty_list()

    def __post_init__(self, **kwargs: Dict[str, Any]):
        if self.id is None:
            raise ValueError(f"id must be supplied")
        if not isinstance(self.id, ChemicalExposureId):
            self.id = ChemicalExposureId(self.id)
        super().__post_init__(**kwargs)


@dataclass
class DrugExposure(ChemicalExposure):
    """
    A drug exposure is an intake of a particular chemical substance
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = BIOLINK.DrugExposure
    class_class_curie: ClassVar[str] = "biolink:DrugExposure"
    class_name: ClassVar[str] = "drug exposure"
    class_model_uri: ClassVar[URIRef] = BIOLINK.DrugExposure

    id: Union[str, DrugExposureId] = None
    name: Union[str, LabelType] = None
    category: List[Union[str, IriType]] = empty_list()
    has_drug: List[Union[str, ChemicalSubstanceId]] = empty_list()

    def __post_init__(self, **kwargs: Dict[str, Any]):
        if self.id is None:
            raise ValueError(f"id must be supplied")
        if not isinstance(self.id, DrugExposureId):
            self.id = DrugExposureId(self.id)
        if not isinstance(self.has_drug, list) or len(self.has_drug) == 0:
            raise ValueError(f"has_drug must be a non-empty list")
        self.has_drug = [v if isinstance(v, ChemicalSubstanceId)
                         else ChemicalSubstanceId(v) for v in ([self.has_drug] if isinstance(self.has_drug, str) else self.has_drug)]
        super().__post_init__(**kwargs)


@dataclass
class Treatment(ExposureEvent):
    """
    A treatment is targeted at a disease or phenotype and may involve multiple drug 'exposures'
    """
    _inherited_slots: ClassVar[List[str]] = ["has_part"]

    class_class_uri: ClassVar[URIRef] = BIOLINK.Treatment
    class_class_curie: ClassVar[str] = "biolink:Treatment"
    class_name: ClassVar[str] = "treatment"
    class_model_uri: ClassVar[URIRef] = BIOLINK.Treatment

    id: Union[str, TreatmentId] = None
    name: Union[str, LabelType] = None
    category: List[Union[str, IriType]] = empty_list()
    has_part: List[Union[str, DrugExposureId]] = empty_list()

    def __post_init__(self, **kwargs: Dict[str, Any]):
        if self.id is None:
            raise ValueError(f"id must be supplied")
        if not isinstance(self.id, TreatmentId):
            self.id = TreatmentId(self.id)
        if not isinstance(self.has_part, list) or len(self.has_part) == 0:
            raise ValueError(f"has_part must be a non-empty list")
        self.has_part = [v if isinstance(v, DrugExposureId)
                         else DrugExposureId(v) for v in ([self.has_part] if isinstance(self.has_part, str) else self.has_part)]
        super().__post_init__(**kwargs)


@dataclass
class GeographicLocation(PlanetaryEntity):
    """
    a location that can be described in lat/long coordinates
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = BIOLINK.GeographicLocation
    class_class_curie: ClassVar[str] = "biolink:GeographicLocation"
    class_name: ClassVar[str] = "geographic location"
    class_model_uri: ClassVar[URIRef] = BIOLINK.GeographicLocation

    id: Union[str, GeographicLocationId] = None
    name: Union[str, LabelType] = None
    category: List[Union[str, IriType]] = empty_list()
    latitude: Optional[float] = None
    longitude: Optional[float] = None

    def __post_init__(self, **kwargs: Dict[str, Any]):
        if self.id is None:
            raise ValueError(f"id must be supplied")
        if not isinstance(self.id, GeographicLocationId):
            self.id = GeographicLocationId(self.id)
        super().__post_init__(**kwargs)


@dataclass
class GeographicLocationAtTime(GeographicLocation):
    """
    a location that can be described in lat/long coordinates, for a particular time
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = BIOLINK.GeographicLocationAtTime
    class_class_curie: ClassVar[str] = "biolink:GeographicLocationAtTime"
    class_name: ClassVar[str] = "geographic location at time"
    class_model_uri: ClassVar[URIRef] = BIOLINK.GeographicLocationAtTime

    id: Union[str, GeographicLocationAtTimeId] = None
    name: Union[str, LabelType] = None
    category: List[Union[str, IriType]] = empty_list()
    timepoint: Optional[Union[str, TimeType]] = None

    def __post_init__(self, **kwargs: Dict[str, Any]):
        if self.id is None:
            raise ValueError(f"id must be supplied")
        if not isinstance(self.id, GeographicLocationAtTimeId):
            self.id = GeographicLocationAtTimeId(self.id)
        if self.timepoint is not None and not isinstance(self.timepoint, TimeType):
            self.timepoint = TimeType(self.timepoint)
        super().__post_init__(**kwargs)


@dataclass
class Association(YAMLRoot):
    """
    A typed association between two entities, supported by evidence
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = BIOLINK.Association
    class_class_curie: ClassVar[str] = "biolink:Association"
    class_name: ClassVar[str] = "association"
    class_model_uri: ClassVar[URIRef] = BIOLINK.Association

    id: Union[str, AssociationId]
    subject: Union[str, NamedThingId]
    relation: Union[str, URIorCURIE]
    object: Union[str, NamedThingId]
    negated: Optional[Bool] = None
    association_type: Optional[Union[str, OntologyClassId]] = None
    qualifiers: List[Union[str, OntologyClassId]] = empty_list()
    publications: List[Union[str, PublicationId]] = empty_list()
    provided_by: List[Union[str, ProviderId]] = empty_list()

    def __post_init__(self, **kwargs: Dict[str, Any]):
        if self.id is None:
            raise ValueError(f"id must be supplied")
        if not isinstance(self.id, AssociationId):
            self.id = AssociationId(self.id)
        if self.subject is None:
            raise ValueError(f"subject must be supplied")
        if not isinstance(self.subject, NamedThingId):
            self.subject = NamedThingId(self.subject)
        if self.relation is None:
            raise ValueError(f"relation must be supplied")
        if not isinstance(self.relation, URIorCURIE):
            self.relation = URIorCURIE(self.relation)
        if self.object is None:
            raise ValueError(f"object must be supplied")
        if not isinstance(self.object, NamedThingId):
            self.object = NamedThingId(self.object)
        if self.association_type is not None and not isinstance(self.association_type, OntologyClassId):
            self.association_type = OntologyClassId(self.association_type)
        self.qualifiers = [v if isinstance(v, OntologyClassId)
                           else OntologyClassId(v) for v in ([self.qualifiers] if isinstance(self.qualifiers, str) else self.qualifiers)]
        self.publications = [v if isinstance(v, PublicationId)
                             else PublicationId(v) for v in ([self.publications] if isinstance(self.publications, str) else self.publications)]
        self.provided_by = [v if isinstance(v, ProviderId)
                            else ProviderId(v) for v in ([self.provided_by] if isinstance(self.provided_by, str) else self.provided_by)]
        super().__post_init__(**kwargs)


@dataclass
class GenotypeToGenotypePartAssociation(Association):
    """
    Any association between one genotype and a genotypic entity that is a sub-component of it
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = BIOLINK.GenotypeToGenotypePartAssociation
    class_class_curie: ClassVar[str] = "biolink:GenotypeToGenotypePartAssociation"
    class_name: ClassVar[str] = "genotype to genotype part association"
    class_model_uri: ClassVar[URIRef] = BIOLINK.GenotypeToGenotypePartAssociation

    id: Union[str, GenotypeToGenotypePartAssociationId] = None
    relation: Union[str, URIorCURIE] = None
    subject: Union[str, GenotypeId] = None
    object: Union[str, GenotypeId] = None

    def __post_init__(self, **kwargs: Dict[str, Any]):
        if self.id is None:
            raise ValueError(f"id must be supplied")
        if not isinstance(self.id, GenotypeToGenotypePartAssociationId):
            self.id = GenotypeToGenotypePartAssociationId(self.id)
        if self.relation is None:
            raise ValueError(f"relation must be supplied")
        if not isinstance(self.relation, URIorCURIE):
            self.relation = URIorCURIE(self.relation)
        if self.subject is None:
            raise ValueError(f"subject must be supplied")
        if not isinstance(self.subject, GenotypeId):
            self.subject = GenotypeId(self.subject)
        if self.object is None:
            raise ValueError(f"object must be supplied")
        if not isinstance(self.object, GenotypeId):
            self.object = GenotypeId(self.object)
        super().__post_init__(**kwargs)


@dataclass
class GenotypeToGeneAssociation(Association):
    """
    Any association between a genotype and a gene. The genotype have have multiple variants in that gene or a single
    one. There is no assumption of cardinality
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = BIOLINK.GenotypeToGeneAssociation
    class_class_curie: ClassVar[str] = "biolink:GenotypeToGeneAssociation"
    class_name: ClassVar[str] = "genotype to gene association"
    class_model_uri: ClassVar[URIRef] = BIOLINK.GenotypeToGeneAssociation

    id: Union[str, GenotypeToGeneAssociationId] = None
    relation: Union[str, URIorCURIE] = None
    subject: Union[str, GenotypeId] = None
    object: Union[str, GeneId] = None

    def __post_init__(self, **kwargs: Dict[str, Any]):
        if self.id is None:
            raise ValueError(f"id must be supplied")
        if not isinstance(self.id, GenotypeToGeneAssociationId):
            self.id = GenotypeToGeneAssociationId(self.id)
        if self.relation is None:
            raise ValueError(f"relation must be supplied")
        if not isinstance(self.relation, URIorCURIE):
            self.relation = URIorCURIE(self.relation)
        if self.subject is None:
            raise ValueError(f"subject must be supplied")
        if not isinstance(self.subject, GenotypeId):
            self.subject = GenotypeId(self.subject)
        if self.object is None:
            raise ValueError(f"object must be supplied")
        if not isinstance(self.object, GeneId):
            self.object = GeneId(self.object)
        super().__post_init__(**kwargs)


@dataclass
class GenotypeToVariantAssociation(Association):
    """
    Any association between a genotype and a sequence variant.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = BIOLINK.GenotypeToVariantAssociation
    class_class_curie: ClassVar[str] = "biolink:GenotypeToVariantAssociation"
    class_name: ClassVar[str] = "genotype to variant association"
    class_model_uri: ClassVar[URIRef] = BIOLINK.GenotypeToVariantAssociation

    id: Union[str, GenotypeToVariantAssociationId] = None
    relation: Union[str, URIorCURIE] = None
    subject: Union[str, GenotypeId] = None
    object: Union[str, SequenceVariantId] = None

    def __post_init__(self, **kwargs: Dict[str, Any]):
        if self.id is None:
            raise ValueError(f"id must be supplied")
        if not isinstance(self.id, GenotypeToVariantAssociationId):
            self.id = GenotypeToVariantAssociationId(self.id)
        if self.relation is None:
            raise ValueError(f"relation must be supplied")
        if not isinstance(self.relation, URIorCURIE):
            self.relation = URIorCURIE(self.relation)
        if self.subject is None:
            raise ValueError(f"subject must be supplied")
        if not isinstance(self.subject, GenotypeId):
            self.subject = GenotypeId(self.subject)
        if self.object is None:
            raise ValueError(f"object must be supplied")
        if not isinstance(self.object, SequenceVariantId):
            self.object = SequenceVariantId(self.object)
        super().__post_init__(**kwargs)


@dataclass
class GeneToGeneAssociation(Association):
    """
    abstract parent class for different kinds of gene-gene or gene product to gene product relationships. Includes
    homology and interaction.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = BIOLINK.GeneToGeneAssociation
    class_class_curie: ClassVar[str] = "biolink:GeneToGeneAssociation"
    class_name: ClassVar[str] = "gene to gene association"
    class_model_uri: ClassVar[URIRef] = BIOLINK.GeneToGeneAssociation

    id: Union[str, GeneToGeneAssociationId] = None
    relation: Union[str, URIorCURIE] = None
    subject: Union[str, GeneOrGeneProductId] = None
    object: Union[str, GeneOrGeneProductId] = None

    def __post_init__(self, **kwargs: Dict[str, Any]):
        if self.subject is None:
            raise ValueError(f"subject must be supplied")
        if not isinstance(self.subject, GeneOrGeneProductId):
            self.subject = GeneOrGeneProductId(self.subject)
        if self.object is None:
            raise ValueError(f"object must be supplied")
        if not isinstance(self.object, GeneOrGeneProductId):
            self.object = GeneOrGeneProductId(self.object)
        super().__post_init__(**kwargs)


@dataclass
class GeneToGeneHomologyAssociation(GeneToGeneAssociation):
    """
    A homology association between two genes. May be orthology (in which case the species of subject and object should
    differ) or paralogy (in which case the species may be the same)
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = BIOLINK.GeneToGeneHomologyAssociation
    class_class_curie: ClassVar[str] = "biolink:GeneToGeneHomologyAssociation"
    class_name: ClassVar[str] = "gene to gene homology association"
    class_model_uri: ClassVar[URIRef] = BIOLINK.GeneToGeneHomologyAssociation

    id: Union[str, GeneToGeneHomologyAssociationId] = None
    subject: Union[str, GeneOrGeneProductId] = None
    object: Union[str, GeneOrGeneProductId] = None
    relation: Union[str, URIorCURIE] = None

    def __post_init__(self, **kwargs: Dict[str, Any]):
        if self.id is None:
            raise ValueError(f"id must be supplied")
        if not isinstance(self.id, GeneToGeneHomologyAssociationId):
            self.id = GeneToGeneHomologyAssociationId(self.id)
        if self.relation is None:
            raise ValueError(f"relation must be supplied")
        if not isinstance(self.relation, URIorCURIE):
            self.relation = URIorCURIE(self.relation)
        super().__post_init__(**kwargs)


@dataclass
class PairwiseGeneToGeneInteraction(GeneToGeneAssociation):
    """
    An interaction between two genes or two gene products. May be physical (e.g. protein binding) or genetic (between
    genes). May be symmetric (e.g. protein interaction) or directed (e.g. phosphorylation)
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = BIOLINK.PairwiseGeneToGeneInteraction
    class_class_curie: ClassVar[str] = "biolink:PairwiseGeneToGeneInteraction"
    class_name: ClassVar[str] = "pairwise gene to gene interaction"
    class_model_uri: ClassVar[URIRef] = BIOLINK.PairwiseGeneToGeneInteraction

    id: Union[str, PairwiseGeneToGeneInteractionId] = None
    subject: Union[str, GeneOrGeneProductId] = None
    object: Union[str, GeneOrGeneProductId] = None
    relation: Union[str, URIorCURIE] = None
    interacting_molecules_category: Optional[Union[str, OntologyClassId]] = None

    def __post_init__(self, **kwargs: Dict[str, Any]):
        if self.id is None:
            raise ValueError(f"id must be supplied")
        if not isinstance(self.id, PairwiseGeneToGeneInteractionId):
            self.id = PairwiseGeneToGeneInteractionId(self.id)
        if self.relation is None:
            raise ValueError(f"relation must be supplied")
        if not isinstance(self.relation, URIorCURIE):
            self.relation = URIorCURIE(self.relation)
        if self.interacting_molecules_category is not None and not isinstance(self.interacting_molecules_category, OntologyClassId):
            self.interacting_molecules_category = OntologyClassId(self.interacting_molecules_category)
        super().__post_init__(**kwargs)


@dataclass
class CellLineToThingAssociation(Association):
    """
    An relationship between a cell line and another entity
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = BIOLINK.CellLineToThingAssociation
    class_class_curie: ClassVar[str] = "biolink:CellLineToThingAssociation"
    class_name: ClassVar[str] = "cell line to thing association"
    class_model_uri: ClassVar[URIRef] = BIOLINK.CellLineToThingAssociation

    id: Union[str, CellLineToThingAssociationId] = None
    relation: Union[str, URIorCURIE] = None
    object: Union[str, NamedThingId] = None
    subject: Union[str, CellLineId] = None

    def __post_init__(self, **kwargs: Dict[str, Any]):
        if self.subject is None:
            raise ValueError(f"subject must be supplied")
        if not isinstance(self.subject, CellLineId):
            self.subject = CellLineId(self.subject)
        super().__post_init__(**kwargs)


@dataclass
class CellLineToDiseaseOrPhenotypicFeatureAssociation(Association):
    """
    An relationship between a cell line and a disease or a phenotype, where the cell line is derived from an
    individual with that disease or phenotype
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = BIOLINK.CellLineToDiseaseOrPhenotypicFeatureAssociation
    class_class_curie: ClassVar[str] = "biolink:CellLineToDiseaseOrPhenotypicFeatureAssociation"
    class_name: ClassVar[str] = "cell line to disease or phenotypic feature association"
    class_model_uri: ClassVar[URIRef] = BIOLINK.CellLineToDiseaseOrPhenotypicFeatureAssociation

    id: Union[str, CellLineToDiseaseOrPhenotypicFeatureAssociationId] = None
    relation: Union[str, URIorCURIE] = None
    object: Union[str, NamedThingId] = None
    subject: Union[str, DiseaseOrPhenotypicFeatureId] = None

    def __post_init__(self, **kwargs: Dict[str, Any]):
        if self.id is None:
            raise ValueError(f"id must be supplied")
        if not isinstance(self.id, CellLineToDiseaseOrPhenotypicFeatureAssociationId):
            self.id = CellLineToDiseaseOrPhenotypicFeatureAssociationId(self.id)
        if self.subject is None:
            raise ValueError(f"subject must be supplied")
        if not isinstance(self.subject, DiseaseOrPhenotypicFeatureId):
            self.subject = DiseaseOrPhenotypicFeatureId(self.subject)
        super().__post_init__(**kwargs)


@dataclass
class ChemicalToThingAssociation(Association):
    """
    An interaction between a chemical entity and another entity
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = BIOLINK.ChemicalToThingAssociation
    class_class_curie: ClassVar[str] = "biolink:ChemicalToThingAssociation"
    class_name: ClassVar[str] = "chemical to thing association"
    class_model_uri: ClassVar[URIRef] = BIOLINK.ChemicalToThingAssociation

    id: Union[str, ChemicalToThingAssociationId] = None
    relation: Union[str, URIorCURIE] = None
    object: Union[str, NamedThingId] = None
    subject: Union[str, ChemicalSubstanceId] = None

    def __post_init__(self, **kwargs: Dict[str, Any]):
        if self.subject is None:
            raise ValueError(f"subject must be supplied")
        if not isinstance(self.subject, ChemicalSubstanceId):
            self.subject = ChemicalSubstanceId(self.subject)
        super().__post_init__(**kwargs)


@dataclass
class CaseToThingAssociation(Association):
    """
    An abstract association for use where the case is the subject
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = BIOLINK.CaseToThingAssociation
    class_class_curie: ClassVar[str] = "biolink:CaseToThingAssociation"
    class_name: ClassVar[str] = "case to thing association"
    class_model_uri: ClassVar[URIRef] = BIOLINK.CaseToThingAssociation

    id: Union[str, CaseToThingAssociationId] = None
    relation: Union[str, URIorCURIE] = None
    object: Union[str, NamedThingId] = None
    subject: Union[str, CaseId] = None

    def __post_init__(self, **kwargs: Dict[str, Any]):
        if self.subject is None:
            raise ValueError(f"subject must be supplied")
        if not isinstance(self.subject, CaseId):
            self.subject = CaseId(self.subject)
        super().__post_init__(**kwargs)


@dataclass
class ChemicalToChemicalAssociation(Association):
    """
    A relationship between two chemical entities. This can encompass actual interactions as well as temporal causal
    edges, e.g. one chemical converted to another.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = BIOLINK.ChemicalToChemicalAssociation
    class_class_curie: ClassVar[str] = "biolink:ChemicalToChemicalAssociation"
    class_name: ClassVar[str] = "chemical to chemical association"
    class_model_uri: ClassVar[URIRef] = BIOLINK.ChemicalToChemicalAssociation

    id: Union[str, ChemicalToChemicalAssociationId] = None
    subject: Union[str, NamedThingId] = None
    relation: Union[str, URIorCURIE] = None
    object: Union[str, ChemicalSubstanceId] = None

    def __post_init__(self, **kwargs: Dict[str, Any]):
        if self.id is None:
            raise ValueError(f"id must be supplied")
        if not isinstance(self.id, ChemicalToChemicalAssociationId):
            self.id = ChemicalToChemicalAssociationId(self.id)
        if self.object is None:
            raise ValueError(f"object must be supplied")
        if not isinstance(self.object, ChemicalSubstanceId):
            self.object = ChemicalSubstanceId(self.object)
        super().__post_init__(**kwargs)


@dataclass
class ChemicalToChemicalDerivationAssociation(ChemicalToChemicalAssociation):
    """
    A causal relationship between two chemical entities, where the subject represents the upstream entity and the
    object represents the downstream. For any such association there is an implicit reaction:
    IF
    R has-input C1 AND
    R has-output C2 AND
    R enabled-by P AND
    R type Reaction
    THEN
    C1 derives-into C2 <<change is catalyzed by P>>
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = BIOLINK.ChemicalToChemicalDerivationAssociation
    class_class_curie: ClassVar[str] = "biolink:ChemicalToChemicalDerivationAssociation"
    class_name: ClassVar[str] = "chemical to chemical derivation association"
    class_model_uri: ClassVar[URIRef] = BIOLINK.ChemicalToChemicalDerivationAssociation

    id: Union[str, ChemicalToChemicalDerivationAssociationId] = None
    subject: Union[str, ChemicalSubstanceId] = None
    object: Union[str, ChemicalSubstanceId] = None
    relation: Union[str, URIorCURIE] = None
    change_is_catalyzed_by: List[Union[str, MacromolecularMachineId]] = empty_list()

    def __post_init__(self, **kwargs: Dict[str, Any]):
        if self.id is None:
            raise ValueError(f"id must be supplied")
        if not isinstance(self.id, ChemicalToChemicalDerivationAssociationId):
            self.id = ChemicalToChemicalDerivationAssociationId(self.id)
        self.change_is_catalyzed_by = [v if isinstance(v, MacromolecularMachineId)
                                       else MacromolecularMachineId(v) for v in ([self.change_is_catalyzed_by] if isinstance(self.change_is_catalyzed_by, str) else self.change_is_catalyzed_by)]
        if self.subject is None:
            raise ValueError(f"subject must be supplied")
        if not isinstance(self.subject, ChemicalSubstanceId):
            self.subject = ChemicalSubstanceId(self.subject)
        if self.object is None:
            raise ValueError(f"object must be supplied")
        if not isinstance(self.object, ChemicalSubstanceId):
            self.object = ChemicalSubstanceId(self.object)
        if self.relation is None:
            raise ValueError(f"relation must be supplied")
        if not isinstance(self.relation, URIorCURIE):
            self.relation = URIorCURIE(self.relation)
        super().__post_init__(**kwargs)


@dataclass
class ChemicalToDiseaseOrPhenotypicFeatureAssociation(Association):
    """
    An interaction between a chemical entity and a phenotype or disease, where the presence of the chemical gives rise
    to or exacerbates the phenotype
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = BIOLINK.ChemicalToDiseaseOrPhenotypicFeatureAssociation
    class_class_curie: ClassVar[str] = "biolink:ChemicalToDiseaseOrPhenotypicFeatureAssociation"
    class_name: ClassVar[str] = "chemical to disease or phenotypic feature association"
    class_model_uri: ClassVar[URIRef] = BIOLINK.ChemicalToDiseaseOrPhenotypicFeatureAssociation

    id: Union[str, ChemicalToDiseaseOrPhenotypicFeatureAssociationId] = None
    subject: Union[str, NamedThingId] = None
    relation: Union[str, URIorCURIE] = None
    object: Union[str, DiseaseOrPhenotypicFeatureId] = None

    def __post_init__(self, **kwargs: Dict[str, Any]):
        if self.id is None:
            raise ValueError(f"id must be supplied")
        if not isinstance(self.id, ChemicalToDiseaseOrPhenotypicFeatureAssociationId):
            self.id = ChemicalToDiseaseOrPhenotypicFeatureAssociationId(self.id)
        if self.object is None:
            raise ValueError(f"object must be supplied")
        if not isinstance(self.object, DiseaseOrPhenotypicFeatureId):
            self.object = DiseaseOrPhenotypicFeatureId(self.object)
        super().__post_init__(**kwargs)


@dataclass
class ChemicalToPathwayAssociation(Association):
    """
    An interaction between a chemical entity and a biological process or pathway
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = BIOLINK.ChemicalToPathwayAssociation
    class_class_curie: ClassVar[str] = "biolink:ChemicalToPathwayAssociation"
    class_name: ClassVar[str] = "chemical to pathway association"
    class_model_uri: ClassVar[URIRef] = BIOLINK.ChemicalToPathwayAssociation

    id: Union[str, ChemicalToPathwayAssociationId] = None
    subject: Union[str, NamedThingId] = None
    relation: Union[str, URIorCURIE] = None
    object: Union[str, PathwayId] = None

    def __post_init__(self, **kwargs: Dict[str, Any]):
        if self.id is None:
            raise ValueError(f"id must be supplied")
        if not isinstance(self.id, ChemicalToPathwayAssociationId):
            self.id = ChemicalToPathwayAssociationId(self.id)
        if self.object is None:
            raise ValueError(f"object must be supplied")
        if not isinstance(self.object, PathwayId):
            self.object = PathwayId(self.object)
        super().__post_init__(**kwargs)


@dataclass
class ChemicalToGeneAssociation(Association):
    """
    An interaction between a chemical entity and a gene or gene product
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = BIOLINK.ChemicalToGeneAssociation
    class_class_curie: ClassVar[str] = "biolink:ChemicalToGeneAssociation"
    class_name: ClassVar[str] = "chemical to gene association"
    class_model_uri: ClassVar[URIRef] = BIOLINK.ChemicalToGeneAssociation

    id: Union[str, ChemicalToGeneAssociationId] = None
    subject: Union[str, NamedThingId] = None
    relation: Union[str, URIorCURIE] = None
    object: Union[str, GeneOrGeneProductId] = None

    def __post_init__(self, **kwargs: Dict[str, Any]):
        if self.id is None:
            raise ValueError(f"id must be supplied")
        if not isinstance(self.id, ChemicalToGeneAssociationId):
            self.id = ChemicalToGeneAssociationId(self.id)
        if self.object is None:
            raise ValueError(f"object must be supplied")
        if not isinstance(self.object, GeneOrGeneProductId):
            self.object = GeneOrGeneProductId(self.object)
        super().__post_init__(**kwargs)


@dataclass
class MaterialSampleToThingAssociation(Association):
    """
    An association between a material sample and something
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = BIOLINK.MaterialSampleToThingAssociation
    class_class_curie: ClassVar[str] = "biolink:MaterialSampleToThingAssociation"
    class_name: ClassVar[str] = "material sample to thing association"
    class_model_uri: ClassVar[URIRef] = BIOLINK.MaterialSampleToThingAssociation

    id: Union[str, MaterialSampleToThingAssociationId] = None
    relation: Union[str, URIorCURIE] = None
    object: Union[str, NamedThingId] = None
    subject: Union[str, MaterialSampleId] = None

    def __post_init__(self, **kwargs: Dict[str, Any]):
        if self.subject is None:
            raise ValueError(f"subject must be supplied")
        if not isinstance(self.subject, MaterialSampleId):
            self.subject = MaterialSampleId(self.subject)
        super().__post_init__(**kwargs)


@dataclass
class MaterialSampleDerivationAssociation(Association):
    """
    An association between a material sample and the material entity it is derived from
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = BIOLINK.MaterialSampleDerivationAssociation
    class_class_curie: ClassVar[str] = "biolink:MaterialSampleDerivationAssociation"
    class_name: ClassVar[str] = "material sample derivation association"
    class_model_uri: ClassVar[URIRef] = BIOLINK.MaterialSampleDerivationAssociation

    id: Union[str, MaterialSampleDerivationAssociationId] = None
    subject: Union[str, MaterialSampleId] = None
    object: Union[str, NamedThingId] = None
    relation: Union[str, URIorCURIE] = None

    def __post_init__(self, **kwargs: Dict[str, Any]):
        if self.id is None:
            raise ValueError(f"id must be supplied")
        if not isinstance(self.id, MaterialSampleDerivationAssociationId):
            self.id = MaterialSampleDerivationAssociationId(self.id)
        if self.subject is None:
            raise ValueError(f"subject must be supplied")
        if not isinstance(self.subject, MaterialSampleId):
            self.subject = MaterialSampleId(self.subject)
        if self.object is None:
            raise ValueError(f"object must be supplied")
        if not isinstance(self.object, NamedThingId):
            self.object = NamedThingId(self.object)
        if self.relation is None:
            raise ValueError(f"relation must be supplied")
        if not isinstance(self.relation, URIorCURIE):
            self.relation = URIorCURIE(self.relation)
        super().__post_init__(**kwargs)


@dataclass
class MaterialSampleToDiseaseOrPhenotypicFeatureAssociation(Association):
    """
    An association between a material sample and a disease or phenotype
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = BIOLINK.MaterialSampleToDiseaseOrPhenotypicFeatureAssociation
    class_class_curie: ClassVar[str] = "biolink:MaterialSampleToDiseaseOrPhenotypicFeatureAssociation"
    class_name: ClassVar[str] = "material sample to disease or phenotypic feature association"
    class_model_uri: ClassVar[URIRef] = BIOLINK.MaterialSampleToDiseaseOrPhenotypicFeatureAssociation

    id: Union[str, MaterialSampleToDiseaseOrPhenotypicFeatureAssociationId] = None
    subject: Union[str, NamedThingId] = None
    relation: Union[str, URIorCURIE] = None
    object: Union[str, NamedThingId] = None

    def __post_init__(self, **kwargs: Dict[str, Any]):
        if self.id is None:
            raise ValueError(f"id must be supplied")
        if not isinstance(self.id, MaterialSampleToDiseaseOrPhenotypicFeatureAssociationId):
            self.id = MaterialSampleToDiseaseOrPhenotypicFeatureAssociationId(self.id)
        super().__post_init__(**kwargs)


@dataclass
class DiseaseToThingAssociation(Association):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = BIOLINK.DiseaseToThingAssociation
    class_class_curie: ClassVar[str] = "biolink:DiseaseToThingAssociation"
    class_name: ClassVar[str] = "disease to thing association"
    class_model_uri: ClassVar[URIRef] = BIOLINK.DiseaseToThingAssociation

    id: Union[str, DiseaseToThingAssociationId] = None
    relation: Union[str, URIorCURIE] = None
    object: Union[str, NamedThingId] = None
    subject: Union[str, DiseaseId] = None

    def __post_init__(self, **kwargs: Dict[str, Any]):
        if self.subject is None:
            raise ValueError(f"subject must be supplied")
        if not isinstance(self.subject, DiseaseId):
            self.subject = DiseaseId(self.subject)
        super().__post_init__(**kwargs)


@dataclass
class DiseaseToExposureAssociation(DiseaseToThingAssociation):
    """
    An association between an exposure event and a disease
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = BIOLINK.DiseaseToExposureAssociation
    class_class_curie: ClassVar[str] = "biolink:DiseaseToExposureAssociation"
    class_name: ClassVar[str] = "disease to exposure association"
    class_model_uri: ClassVar[URIRef] = BIOLINK.DiseaseToExposureAssociation

    id: Union[str, DiseaseToExposureAssociationId] = None
    relation: Union[str, URIorCURIE] = None
    subject: Union[str, DiseaseId] = None
    object: Union[str, ExposureEventId] = None

    def __post_init__(self, **kwargs: Dict[str, Any]):
        if self.id is None:
            raise ValueError(f"id must be supplied")
        if not isinstance(self.id, DiseaseToExposureAssociationId):
            self.id = DiseaseToExposureAssociationId(self.id)
        if self.subject is None:
            raise ValueError(f"subject must be supplied")
        if not isinstance(self.subject, DiseaseId):
            self.subject = DiseaseId(self.subject)
        if self.object is None:
            raise ValueError(f"object must be supplied")
        if not isinstance(self.object, ExposureEventId):
            self.object = ExposureEventId(self.object)
        super().__post_init__(**kwargs)


@dataclass
class EntityToPhenotypicFeatureAssociation(Association):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = BIOLINK.EntityToPhenotypicFeatureAssociation
    class_class_curie: ClassVar[str] = "biolink:EntityToPhenotypicFeatureAssociation"
    class_name: ClassVar[str] = "entity to phenotypic feature association"
    class_model_uri: ClassVar[URIRef] = BIOLINK.EntityToPhenotypicFeatureAssociation

    id: Union[str, EntityToPhenotypicFeatureAssociationId] = None
    subject: Union[str, NamedThingId] = None
    relation: Union[str, URIorCURIE] = None
    object: Union[str, PhenotypicFeatureId] = None
    sex_qualifier: Optional[Union[str, BiologicalSexId]] = None
    description: Optional[Union[str, NarrativeText]] = None
    severity_qualifier: Optional[Union[str, SeverityValueId]] = None
    onset_qualifier: Optional[Union[str, OnsetId]] = None

    def __post_init__(self, **kwargs: Dict[str, Any]):
        if self.sex_qualifier is not None and not isinstance(self.sex_qualifier, BiologicalSexId):
            self.sex_qualifier = BiologicalSexId(self.sex_qualifier)
        if self.description is not None and not isinstance(self.description, NarrativeText):
            self.description = NarrativeText(self.description)
        if self.object is None:
            raise ValueError(f"object must be supplied")
        if not isinstance(self.object, PhenotypicFeatureId):
            self.object = PhenotypicFeatureId(self.object)
        if self.severity_qualifier is not None and not isinstance(self.severity_qualifier, SeverityValueId):
            self.severity_qualifier = SeverityValueId(self.severity_qualifier)
        if self.onset_qualifier is not None and not isinstance(self.onset_qualifier, OnsetId):
            self.onset_qualifier = OnsetId(self.onset_qualifier)
        super().__post_init__(**kwargs)


@dataclass
class DiseaseOrPhenotypicFeatureAssociationToThingAssociation(Association):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = BIOLINK.DiseaseOrPhenotypicFeatureAssociationToThingAssociation
    class_class_curie: ClassVar[str] = "biolink:DiseaseOrPhenotypicFeatureAssociationToThingAssociation"
    class_name: ClassVar[str] = "disease or phenotypic feature association to thing association"
    class_model_uri: ClassVar[URIRef] = BIOLINK.DiseaseOrPhenotypicFeatureAssociationToThingAssociation

    id: Union[str, DiseaseOrPhenotypicFeatureAssociationToThingAssociationId] = None
    relation: Union[str, URIorCURIE] = None
    object: Union[str, NamedThingId] = None
    subject: Union[str, DiseaseOrPhenotypicFeatureId] = None

    def __post_init__(self, **kwargs: Dict[str, Any]):
        if self.subject is None:
            raise ValueError(f"subject must be supplied")
        if not isinstance(self.subject, DiseaseOrPhenotypicFeatureId):
            self.subject = DiseaseOrPhenotypicFeatureId(self.subject)
        super().__post_init__(**kwargs)


@dataclass
class DiseaseOrPhenotypicFeatureAssociationToLocationAssociation(DiseaseOrPhenotypicFeatureAssociationToThingAssociation):
    """
    An association between either a disease or a phenotypic feature and an anatomical entity, where the
    disease/feature manifests in that site.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = BIOLINK.DiseaseOrPhenotypicFeatureAssociationToLocationAssociation
    class_class_curie: ClassVar[str] = "biolink:DiseaseOrPhenotypicFeatureAssociationToLocationAssociation"
    class_name: ClassVar[str] = "disease or phenotypic feature association to location association"
    class_model_uri: ClassVar[URIRef] = BIOLINK.DiseaseOrPhenotypicFeatureAssociationToLocationAssociation

    id: Union[str, DiseaseOrPhenotypicFeatureAssociationToLocationAssociationId] = None
    relation: Union[str, URIorCURIE] = None
    subject: Union[str, DiseaseOrPhenotypicFeatureId] = None
    object: Union[str, AnatomicalEntityId] = None

    def __post_init__(self, **kwargs: Dict[str, Any]):
        if self.id is None:
            raise ValueError(f"id must be supplied")
        if not isinstance(self.id, DiseaseOrPhenotypicFeatureAssociationToLocationAssociationId):
            self.id = DiseaseOrPhenotypicFeatureAssociationToLocationAssociationId(self.id)
        if self.object is None:
            raise ValueError(f"object must be supplied")
        if not isinstance(self.object, AnatomicalEntityId):
            self.object = AnatomicalEntityId(self.object)
        super().__post_init__(**kwargs)


@dataclass
class ThingToDiseaseOrPhenotypicFeatureAssociation(Association):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = BIOLINK.ThingToDiseaseOrPhenotypicFeatureAssociation
    class_class_curie: ClassVar[str] = "biolink:ThingToDiseaseOrPhenotypicFeatureAssociation"
    class_name: ClassVar[str] = "thing to disease or phenotypic feature association"
    class_model_uri: ClassVar[URIRef] = BIOLINK.ThingToDiseaseOrPhenotypicFeatureAssociation

    id: Union[str, ThingToDiseaseOrPhenotypicFeatureAssociationId] = None
    subject: Union[str, NamedThingId] = None
    relation: Union[str, URIorCURIE] = None
    object: Union[str, DiseaseOrPhenotypicFeatureId] = None

    def __post_init__(self, **kwargs: Dict[str, Any]):
        if self.object is None:
            raise ValueError(f"object must be supplied")
        if not isinstance(self.object, DiseaseOrPhenotypicFeatureId):
            self.object = DiseaseOrPhenotypicFeatureId(self.object)
        super().__post_init__(**kwargs)


@dataclass
class GenotypeToPhenotypicFeatureAssociation(Association):
    """
    Any association between one genotype and a phenotypic feature, where having the genotype confers the phenotype,
    either in isolation or through environment
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = BIOLINK.GenotypeToPhenotypicFeatureAssociation
    class_class_curie: ClassVar[str] = "biolink:GenotypeToPhenotypicFeatureAssociation"
    class_name: ClassVar[str] = "genotype to phenotypic feature association"
    class_model_uri: ClassVar[URIRef] = BIOLINK.GenotypeToPhenotypicFeatureAssociation

    id: Union[str, GenotypeToPhenotypicFeatureAssociationId] = None
    object: Union[str, NamedThingId] = None
    relation: Union[str, URIorCURIE] = None
    subject: Union[str, GenotypeId] = None
    sex_qualifier: Optional[Union[str, BiologicalSexId]] = None
    description: Optional[Union[str, NarrativeText]] = None

    def __post_init__(self, **kwargs: Dict[str, Any]):
        if self.id is None:
            raise ValueError(f"id must be supplied")
        if not isinstance(self.id, GenotypeToPhenotypicFeatureAssociationId):
            self.id = GenotypeToPhenotypicFeatureAssociationId(self.id)
        if self.relation is None:
            raise ValueError(f"relation must be supplied")
        if not isinstance(self.relation, URIorCURIE):
            self.relation = URIorCURIE(self.relation)
        if self.subject is None:
            raise ValueError(f"subject must be supplied")
        if not isinstance(self.subject, GenotypeId):
            self.subject = GenotypeId(self.subject)
        if self.sex_qualifier is not None and not isinstance(self.sex_qualifier, BiologicalSexId):
            self.sex_qualifier = BiologicalSexId(self.sex_qualifier)
        if self.description is not None and not isinstance(self.description, NarrativeText):
            self.description = NarrativeText(self.description)
        super().__post_init__(**kwargs)


@dataclass
class ExposureEventToPhenotypicFeatureAssociation(Association):
    """
    Any association between an environment and a phenotypic feature, where being in the environment influences the
    phenotype
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = BIOLINK.ExposureEventToPhenotypicFeatureAssociation
    class_class_curie: ClassVar[str] = "biolink:ExposureEventToPhenotypicFeatureAssociation"
    class_name: ClassVar[str] = "exposure event to phenotypic feature association"
    class_model_uri: ClassVar[URIRef] = BIOLINK.ExposureEventToPhenotypicFeatureAssociation

    id: Union[str, ExposureEventToPhenotypicFeatureAssociationId] = None
    relation: Union[str, URIorCURIE] = None
    object: Union[str, NamedThingId] = None
    subject: Union[str, ExposureEventId] = None
    sex_qualifier: Optional[Union[str, BiologicalSexId]] = None
    description: Optional[Union[str, NarrativeText]] = None

    def __post_init__(self, **kwargs: Dict[str, Any]):
        if self.id is None:
            raise ValueError(f"id must be supplied")
        if not isinstance(self.id, ExposureEventToPhenotypicFeatureAssociationId):
            self.id = ExposureEventToPhenotypicFeatureAssociationId(self.id)
        if self.subject is None:
            raise ValueError(f"subject must be supplied")
        if not isinstance(self.subject, ExposureEventId):
            self.subject = ExposureEventId(self.subject)
        if self.sex_qualifier is not None and not isinstance(self.sex_qualifier, BiologicalSexId):
            self.sex_qualifier = BiologicalSexId(self.sex_qualifier)
        if self.description is not None and not isinstance(self.description, NarrativeText):
            self.description = NarrativeText(self.description)
        super().__post_init__(**kwargs)


@dataclass
class DiseaseToPhenotypicFeatureAssociation(Association):
    """
    An association between a disease and a phenotypic feature in which the phenotypic feature is associated with the
    disease in some way
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = BIOLINK.DiseaseToPhenotypicFeatureAssociation
    class_class_curie: ClassVar[str] = "biolink:DiseaseToPhenotypicFeatureAssociation"
    class_name: ClassVar[str] = "disease to phenotypic feature association"
    class_model_uri: ClassVar[URIRef] = BIOLINK.DiseaseToPhenotypicFeatureAssociation

    id: Union[str, DiseaseToPhenotypicFeatureAssociationId] = None
    subject: Union[str, NamedThingId] = None
    relation: Union[str, URIorCURIE] = None
    object: Union[str, NamedThingId] = None
    sex_qualifier: Optional[Union[str, BiologicalSexId]] = None
    description: Optional[Union[str, NarrativeText]] = None

    def __post_init__(self, **kwargs: Dict[str, Any]):
        if self.id is None:
            raise ValueError(f"id must be supplied")
        if not isinstance(self.id, DiseaseToPhenotypicFeatureAssociationId):
            self.id = DiseaseToPhenotypicFeatureAssociationId(self.id)
        if self.sex_qualifier is not None and not isinstance(self.sex_qualifier, BiologicalSexId):
            self.sex_qualifier = BiologicalSexId(self.sex_qualifier)
        if self.description is not None and not isinstance(self.description, NarrativeText):
            self.description = NarrativeText(self.description)
        super().__post_init__(**kwargs)


@dataclass
class CaseToPhenotypicFeatureAssociation(Association):
    """
    An association between a case (e.g. individual patient) and a phenotypic feature in which the individual has or
    has had the phenotype
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = BIOLINK.CaseToPhenotypicFeatureAssociation
    class_class_curie: ClassVar[str] = "biolink:CaseToPhenotypicFeatureAssociation"
    class_name: ClassVar[str] = "case to phenotypic feature association"
    class_model_uri: ClassVar[URIRef] = BIOLINK.CaseToPhenotypicFeatureAssociation

    id: Union[str, CaseToPhenotypicFeatureAssociationId] = None
    subject: Union[str, NamedThingId] = None
    relation: Union[str, URIorCURIE] = None
    object: Union[str, NamedThingId] = None
    sex_qualifier: Optional[Union[str, BiologicalSexId]] = None
    description: Optional[Union[str, NarrativeText]] = None

    def __post_init__(self, **kwargs: Dict[str, Any]):
        if self.id is None:
            raise ValueError(f"id must be supplied")
        if not isinstance(self.id, CaseToPhenotypicFeatureAssociationId):
            self.id = CaseToPhenotypicFeatureAssociationId(self.id)
        if self.sex_qualifier is not None and not isinstance(self.sex_qualifier, BiologicalSexId):
            self.sex_qualifier = BiologicalSexId(self.sex_qualifier)
        if self.description is not None and not isinstance(self.description, NarrativeText):
            self.description = NarrativeText(self.description)
        super().__post_init__(**kwargs)


@dataclass
class GeneToThingAssociation(Association):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = BIOLINK.GeneToThingAssociation
    class_class_curie: ClassVar[str] = "biolink:GeneToThingAssociation"
    class_name: ClassVar[str] = "gene to thing association"
    class_model_uri: ClassVar[URIRef] = BIOLINK.GeneToThingAssociation

    id: Union[str, GeneToThingAssociationId] = None
    relation: Union[str, URIorCURIE] = None
    object: Union[str, NamedThingId] = None
    subject: Union[str, GeneOrGeneProductId] = None

    def __post_init__(self, **kwargs: Dict[str, Any]):
        if self.subject is None:
            raise ValueError(f"subject must be supplied")
        if not isinstance(self.subject, GeneOrGeneProductId):
            self.subject = GeneOrGeneProductId(self.subject)
        super().__post_init__(**kwargs)


@dataclass
class GeneToPhenotypicFeatureAssociation(Association):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = BIOLINK.GeneToPhenotypicFeatureAssociation
    class_class_curie: ClassVar[str] = "biolink:GeneToPhenotypicFeatureAssociation"
    class_name: ClassVar[str] = "gene to phenotypic feature association"
    class_model_uri: ClassVar[URIRef] = BIOLINK.GeneToPhenotypicFeatureAssociation

    id: Union[str, GeneToPhenotypicFeatureAssociationId] = None
    relation: Union[str, URIorCURIE] = None
    object: Union[str, NamedThingId] = None
    subject: Union[str, GeneOrGeneProductId] = None
    sex_qualifier: Optional[Union[str, BiologicalSexId]] = None
    description: Optional[Union[str, NarrativeText]] = None

    def __post_init__(self, **kwargs: Dict[str, Any]):
        if self.id is None:
            raise ValueError(f"id must be supplied")
        if not isinstance(self.id, GeneToPhenotypicFeatureAssociationId):
            self.id = GeneToPhenotypicFeatureAssociationId(self.id)
        if self.subject is None:
            raise ValueError(f"subject must be supplied")
        if not isinstance(self.subject, GeneOrGeneProductId):
            self.subject = GeneOrGeneProductId(self.subject)
        if self.sex_qualifier is not None and not isinstance(self.sex_qualifier, BiologicalSexId):
            self.sex_qualifier = BiologicalSexId(self.sex_qualifier)
        if self.description is not None and not isinstance(self.description, NarrativeText):
            self.description = NarrativeText(self.description)
        super().__post_init__(**kwargs)


@dataclass
class GeneToDiseaseAssociation(Association):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = BIOLINK.GeneToDiseaseAssociation
    class_class_curie: ClassVar[str] = "biolink:GeneToDiseaseAssociation"
    class_name: ClassVar[str] = "gene to disease association"
    class_model_uri: ClassVar[URIRef] = BIOLINK.GeneToDiseaseAssociation

    id: Union[str, GeneToDiseaseAssociationId] = None
    relation: Union[str, URIorCURIE] = None
    object: Union[str, NamedThingId] = None
    subject: Union[str, GeneOrGeneProductId] = None

    def __post_init__(self, **kwargs: Dict[str, Any]):
        if self.id is None:
            raise ValueError(f"id must be supplied")
        if not isinstance(self.id, GeneToDiseaseAssociationId):
            self.id = GeneToDiseaseAssociationId(self.id)
        if self.subject is None:
            raise ValueError(f"subject must be supplied")
        if not isinstance(self.subject, GeneOrGeneProductId):
            self.subject = GeneOrGeneProductId(self.subject)
        super().__post_init__(**kwargs)


@dataclass
class VariantToPopulationAssociation(Association):
    """
    An association between a variant and a population, where the variant has particular frequency in the population
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = BIOLINK.VariantToPopulationAssociation
    class_class_curie: ClassVar[str] = "biolink:VariantToPopulationAssociation"
    class_name: ClassVar[str] = "variant to population association"
    class_model_uri: ClassVar[URIRef] = BIOLINK.VariantToPopulationAssociation

    id: Union[str, VariantToPopulationAssociationId] = None
    relation: Union[str, URIorCURIE] = None
    subject: Union[str, SequenceVariantId] = None
    object: Union[str, PopulationOfIndividualOrganismsId] = None
    has_quotient: Optional[float] = None
    has_count: Optional[int] = None
    has_total: Optional[int] = None
    has_percentage: Optional[float] = None
    frequency_qualifier: Optional[Union[str, FrequencyValueId]] = None

    def __post_init__(self, **kwargs: Dict[str, Any]):
        if self.id is None:
            raise ValueError(f"id must be supplied")
        if not isinstance(self.id, VariantToPopulationAssociationId):
            self.id = VariantToPopulationAssociationId(self.id)
        if self.subject is None:
            raise ValueError(f"subject must be supplied")
        if not isinstance(self.subject, SequenceVariantId):
            self.subject = SequenceVariantId(self.subject)
        if self.object is None:
            raise ValueError(f"object must be supplied")
        if not isinstance(self.object, PopulationOfIndividualOrganismsId):
            self.object = PopulationOfIndividualOrganismsId(self.object)
        if self.frequency_qualifier is not None and not isinstance(self.frequency_qualifier, FrequencyValueId):
            self.frequency_qualifier = FrequencyValueId(self.frequency_qualifier)
        super().__post_init__(**kwargs)


@dataclass
class PopulationToPopulationAssociation(Association):
    """
    An association between a two populations
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = BIOLINK.PopulationToPopulationAssociation
    class_class_curie: ClassVar[str] = "biolink:PopulationToPopulationAssociation"
    class_name: ClassVar[str] = "population to population association"
    class_model_uri: ClassVar[URIRef] = BIOLINK.PopulationToPopulationAssociation

    id: Union[str, PopulationToPopulationAssociationId] = None
    subject: Union[str, PopulationOfIndividualOrganismsId] = None
    object: Union[str, PopulationOfIndividualOrganismsId] = None
    relation: Union[str, URIorCURIE] = None

    def __post_init__(self, **kwargs: Dict[str, Any]):
        if self.id is None:
            raise ValueError(f"id must be supplied")
        if not isinstance(self.id, PopulationToPopulationAssociationId):
            self.id = PopulationToPopulationAssociationId(self.id)
        if self.subject is None:
            raise ValueError(f"subject must be supplied")
        if not isinstance(self.subject, PopulationOfIndividualOrganismsId):
            self.subject = PopulationOfIndividualOrganismsId(self.subject)
        if self.object is None:
            raise ValueError(f"object must be supplied")
        if not isinstance(self.object, PopulationOfIndividualOrganismsId):
            self.object = PopulationOfIndividualOrganismsId(self.object)
        if self.relation is None:
            raise ValueError(f"relation must be supplied")
        if not isinstance(self.relation, URIorCURIE):
            self.relation = URIorCURIE(self.relation)
        super().__post_init__(**kwargs)


@dataclass
class VariantToPhenotypicFeatureAssociation(Association):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = BIOLINK.VariantToPhenotypicFeatureAssociation
    class_class_curie: ClassVar[str] = "biolink:VariantToPhenotypicFeatureAssociation"
    class_name: ClassVar[str] = "variant to phenotypic feature association"
    class_model_uri: ClassVar[URIRef] = BIOLINK.VariantToPhenotypicFeatureAssociation

    id: Union[str, VariantToPhenotypicFeatureAssociationId] = None
    relation: Union[str, URIorCURIE] = None
    object: Union[str, NamedThingId] = None
    subject: Union[str, SequenceVariantId] = None
    sex_qualifier: Optional[Union[str, BiologicalSexId]] = None
    description: Optional[Union[str, NarrativeText]] = None

    def __post_init__(self, **kwargs: Dict[str, Any]):
        if self.id is None:
            raise ValueError(f"id must be supplied")
        if not isinstance(self.id, VariantToPhenotypicFeatureAssociationId):
            self.id = VariantToPhenotypicFeatureAssociationId(self.id)
        if self.subject is None:
            raise ValueError(f"subject must be supplied")
        if not isinstance(self.subject, SequenceVariantId):
            self.subject = SequenceVariantId(self.subject)
        if self.sex_qualifier is not None and not isinstance(self.sex_qualifier, BiologicalSexId):
            self.sex_qualifier = BiologicalSexId(self.sex_qualifier)
        if self.description is not None and not isinstance(self.description, NarrativeText):
            self.description = NarrativeText(self.description)
        super().__post_init__(**kwargs)


@dataclass
class VariantToDiseaseAssociation(Association):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = BIOLINK.VariantToDiseaseAssociation
    class_class_curie: ClassVar[str] = "biolink:VariantToDiseaseAssociation"
    class_name: ClassVar[str] = "variant to disease association"
    class_model_uri: ClassVar[URIRef] = BIOLINK.VariantToDiseaseAssociation

    id: Union[str, VariantToDiseaseAssociationId] = None
    subject: Union[str, NamedThingId] = None
    relation: Union[str, URIorCURIE] = None
    object: Union[str, NamedThingId] = None

    def __post_init__(self, **kwargs: Dict[str, Any]):
        if self.id is None:
            raise ValueError(f"id must be supplied")
        if not isinstance(self.id, VariantToDiseaseAssociationId):
            self.id = VariantToDiseaseAssociationId(self.id)
        if self.subject is None:
            raise ValueError(f"subject must be supplied")
        if not isinstance(self.subject, NamedThingId):
            self.subject = NamedThingId(self.subject)
        if self.relation is None:
            raise ValueError(f"relation must be supplied")
        if not isinstance(self.relation, URIorCURIE):
            self.relation = URIorCURIE(self.relation)
        if self.object is None:
            raise ValueError(f"object must be supplied")
        if not isinstance(self.object, NamedThingId):
            self.object = NamedThingId(self.object)
        super().__post_init__(**kwargs)


@dataclass
class GeneAsAModelOfDiseaseAssociation(GeneToDiseaseAssociation):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = BIOLINK.GeneAsAModelOfDiseaseAssociation
    class_class_curie: ClassVar[str] = "biolink:GeneAsAModelOfDiseaseAssociation"
    class_name: ClassVar[str] = "gene as a model of disease association"
    class_model_uri: ClassVar[URIRef] = BIOLINK.GeneAsAModelOfDiseaseAssociation

    id: Union[str, GeneAsAModelOfDiseaseAssociationId] = None
    relation: Union[str, URIorCURIE] = None
    object: Union[str, NamedThingId] = None
    subject: Union[str, GeneOrGeneProductId] = None

    def __post_init__(self, **kwargs: Dict[str, Any]):
        if self.id is None:
            raise ValueError(f"id must be supplied")
        if not isinstance(self.id, GeneAsAModelOfDiseaseAssociationId):
            self.id = GeneAsAModelOfDiseaseAssociationId(self.id)
        if self.subject is None:
            raise ValueError(f"subject must be supplied")
        if not isinstance(self.subject, GeneOrGeneProductId):
            self.subject = GeneOrGeneProductId(self.subject)
        super().__post_init__(**kwargs)


@dataclass
class GeneHasVariantThatContributesToDiseaseAssociation(GeneToDiseaseAssociation):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = BIOLINK.GeneHasVariantThatContributesToDiseaseAssociation
    class_class_curie: ClassVar[str] = "biolink:GeneHasVariantThatContributesToDiseaseAssociation"
    class_name: ClassVar[str] = "gene has variant that contributes to disease association"
    class_model_uri: ClassVar[URIRef] = BIOLINK.GeneHasVariantThatContributesToDiseaseAssociation

    id: Union[str, GeneHasVariantThatContributesToDiseaseAssociationId] = None
    relation: Union[str, URIorCURIE] = None
    object: Union[str, NamedThingId] = None
    subject: Union[str, GeneOrGeneProductId] = None
    sequence_variant_qualifier: Optional[Union[str, SequenceVariantId]] = None

    def __post_init__(self, **kwargs: Dict[str, Any]):
        if self.id is None:
            raise ValueError(f"id must be supplied")
        if not isinstance(self.id, GeneHasVariantThatContributesToDiseaseAssociationId):
            self.id = GeneHasVariantThatContributesToDiseaseAssociationId(self.id)
        if self.sequence_variant_qualifier is not None and not isinstance(self.sequence_variant_qualifier, SequenceVariantId):
            self.sequence_variant_qualifier = SequenceVariantId(self.sequence_variant_qualifier)
        if self.subject is None:
            raise ValueError(f"subject must be supplied")
        if not isinstance(self.subject, GeneOrGeneProductId):
            self.subject = GeneOrGeneProductId(self.subject)
        super().__post_init__(**kwargs)


@dataclass
class GenotypeToThingAssociation(Association):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = BIOLINK.GenotypeToThingAssociation
    class_class_curie: ClassVar[str] = "biolink:GenotypeToThingAssociation"
    class_name: ClassVar[str] = "genotype to thing association"
    class_model_uri: ClassVar[URIRef] = BIOLINK.GenotypeToThingAssociation

    id: Union[str, GenotypeToThingAssociationId] = None
    relation: Union[str, URIorCURIE] = None
    object: Union[str, NamedThingId] = None
    subject: Union[str, GenotypeId] = None

    def __post_init__(self, **kwargs: Dict[str, Any]):
        if self.subject is None:
            raise ValueError(f"subject must be supplied")
        if not isinstance(self.subject, GenotypeId):
            self.subject = GenotypeId(self.subject)
        super().__post_init__(**kwargs)


@dataclass
class GeneToExpressionSiteAssociation(Association):
    """
    An association between a gene and an expression site, possibly qualified by stage/timing info.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = BIOLINK.GeneToExpressionSiteAssociation
    class_class_curie: ClassVar[str] = "biolink:GeneToExpressionSiteAssociation"
    class_name: ClassVar[str] = "gene to expression site association"
    class_model_uri: ClassVar[URIRef] = BIOLINK.GeneToExpressionSiteAssociation

    id: Union[str, GeneToExpressionSiteAssociationId] = None
    subject: Union[str, GeneOrGeneProductId] = None
    object: Union[str, AnatomicalEntityId] = None
    relation: Union[str, URIorCURIE] = None
    stage_qualifier: Optional[Union[str, LifeStageId]] = None
    quantifier_qualifier: Optional[Union[str, OntologyClassId]] = None

    def __post_init__(self, **kwargs: Dict[str, Any]):
        if self.id is None:
            raise ValueError(f"id must be supplied")
        if not isinstance(self.id, GeneToExpressionSiteAssociationId):
            self.id = GeneToExpressionSiteAssociationId(self.id)
        if self.stage_qualifier is not None and not isinstance(self.stage_qualifier, LifeStageId):
            self.stage_qualifier = LifeStageId(self.stage_qualifier)
        if self.quantifier_qualifier is not None and not isinstance(self.quantifier_qualifier, OntologyClassId):
            self.quantifier_qualifier = OntologyClassId(self.quantifier_qualifier)
        if self.subject is None:
            raise ValueError(f"subject must be supplied")
        if not isinstance(self.subject, GeneOrGeneProductId):
            self.subject = GeneOrGeneProductId(self.subject)
        if self.object is None:
            raise ValueError(f"object must be supplied")
        if not isinstance(self.object, AnatomicalEntityId):
            self.object = AnatomicalEntityId(self.object)
        if self.relation is None:
            raise ValueError(f"relation must be supplied")
        if not isinstance(self.relation, URIorCURIE):
            self.relation = URIorCURIE(self.relation)
        super().__post_init__(**kwargs)


@dataclass
class SequenceVariantModulatesTreatmentAssociation(Association):
    """
    An association between a sequence variant and a treatment or health intervention. The treatment object itself
    encompasses both the disease and the drug used.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = BIOLINK.SequenceVariantModulatesTreatmentAssociation
    class_class_curie: ClassVar[str] = "biolink:SequenceVariantModulatesTreatmentAssociation"
    class_name: ClassVar[str] = "sequence variant modulates treatment association"
    class_model_uri: ClassVar[URIRef] = BIOLINK.SequenceVariantModulatesTreatmentAssociation

    id: Union[str, SequenceVariantModulatesTreatmentAssociationId] = None
    relation: Union[str, URIorCURIE] = None
    subject: Union[str, SequenceVariantId] = None
    object: Union[str, TreatmentId] = None

    def __post_init__(self, **kwargs: Dict[str, Any]):
        if self.subject is None:
            raise ValueError(f"subject must be supplied")
        if not isinstance(self.subject, SequenceVariantId):
            self.subject = SequenceVariantId(self.subject)
        if self.object is None:
            raise ValueError(f"object must be supplied")
        if not isinstance(self.object, TreatmentId):
            self.object = TreatmentId(self.object)
        super().__post_init__(**kwargs)


@dataclass
class FunctionalAssociation(Association):
    """
    An association between a macromolecular machine (gene, gene product or complex of gene products) and either a
    molecular activity, a biological process or a cellular location in which a function is executed
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = BIOLINK.FunctionalAssociation
    class_class_curie: ClassVar[str] = "biolink:FunctionalAssociation"
    class_name: ClassVar[str] = "functional association"
    class_model_uri: ClassVar[URIRef] = BIOLINK.FunctionalAssociation

    id: Union[str, FunctionalAssociationId] = None
    relation: Union[str, URIorCURIE] = None
    subject: Union[str, MacromolecularMachineId] = None
    object: Union[str, GeneOntologyClassId] = None

    def __post_init__(self, **kwargs: Dict[str, Any]):
        if self.id is None:
            raise ValueError(f"id must be supplied")
        if not isinstance(self.id, FunctionalAssociationId):
            self.id = FunctionalAssociationId(self.id)
        if self.subject is None:
            raise ValueError(f"subject must be supplied")
        if not isinstance(self.subject, MacromolecularMachineId):
            self.subject = MacromolecularMachineId(self.subject)
        if self.object is None:
            raise ValueError(f"object must be supplied")
        if not isinstance(self.object, GeneOntologyClassId):
            self.object = GeneOntologyClassId(self.object)
        super().__post_init__(**kwargs)


@dataclass
class MacromolecularMachineToMolecularActivityAssociation(FunctionalAssociation):
    """
    A functional association between a macromolecular machine (gene, gene product or complex) and a molecular activity
    (as represented in the GO molecular function branch), where the entity carries out the activity, or contributes to
    its execution
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = BIOLINK.MacromolecularMachineToMolecularActivityAssociation
    class_class_curie: ClassVar[str] = "biolink:MacromolecularMachineToMolecularActivityAssociation"
    class_name: ClassVar[str] = "macromolecular machine to molecular activity association"
    class_model_uri: ClassVar[URIRef] = BIOLINK.MacromolecularMachineToMolecularActivityAssociation

    id: Union[str, MacromolecularMachineToMolecularActivityAssociationId] = None
    relation: Union[str, URIorCURIE] = None
    subject: Union[str, MacromolecularMachineId] = None
    object: Union[str, MolecularActivityId] = None

    def __post_init__(self, **kwargs: Dict[str, Any]):
        if self.id is None:
            raise ValueError(f"id must be supplied")
        if not isinstance(self.id, MacromolecularMachineToMolecularActivityAssociationId):
            self.id = MacromolecularMachineToMolecularActivityAssociationId(self.id)
        if self.object is None:
            raise ValueError(f"object must be supplied")
        if not isinstance(self.object, MolecularActivityId):
            self.object = MolecularActivityId(self.object)
        super().__post_init__(**kwargs)


@dataclass
class MacromolecularMachineToBiologicalProcessAssociation(FunctionalAssociation):
    """
    A functional association between a macromolecular machine (gene, gene product or complex) and a biological process
    or pathway (as represented in the GO biological process branch), where the entity carries out some part of the
    process, regulates it, or acts upstream of it
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = BIOLINK.MacromolecularMachineToBiologicalProcessAssociation
    class_class_curie: ClassVar[str] = "biolink:MacromolecularMachineToBiologicalProcessAssociation"
    class_name: ClassVar[str] = "macromolecular machine to biological process association"
    class_model_uri: ClassVar[URIRef] = BIOLINK.MacromolecularMachineToBiologicalProcessAssociation

    id: Union[str, MacromolecularMachineToBiologicalProcessAssociationId] = None
    relation: Union[str, URIorCURIE] = None
    subject: Union[str, MacromolecularMachineId] = None
    object: Union[str, BiologicalProcessId] = None

    def __post_init__(self, **kwargs: Dict[str, Any]):
        if self.id is None:
            raise ValueError(f"id must be supplied")
        if not isinstance(self.id, MacromolecularMachineToBiologicalProcessAssociationId):
            self.id = MacromolecularMachineToBiologicalProcessAssociationId(self.id)
        if self.object is None:
            raise ValueError(f"object must be supplied")
        if not isinstance(self.object, BiologicalProcessId):
            self.object = BiologicalProcessId(self.object)
        super().__post_init__(**kwargs)


@dataclass
class MacromolecularMachineToCellularComponentAssociation(FunctionalAssociation):
    """
    A functional association between a macromolecular machine (gene, gene product or complex) and a cellular component
    (as represented in the GO cellular component branch), where the entity carries out its function in the cellular
    component
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = BIOLINK.MacromolecularMachineToCellularComponentAssociation
    class_class_curie: ClassVar[str] = "biolink:MacromolecularMachineToCellularComponentAssociation"
    class_name: ClassVar[str] = "macromolecular machine to cellular component association"
    class_model_uri: ClassVar[URIRef] = BIOLINK.MacromolecularMachineToCellularComponentAssociation

    id: Union[str, MacromolecularMachineToCellularComponentAssociationId] = None
    relation: Union[str, URIorCURIE] = None
    subject: Union[str, MacromolecularMachineId] = None
    object: Union[str, CellularComponentId] = None

    def __post_init__(self, **kwargs: Dict[str, Any]):
        if self.id is None:
            raise ValueError(f"id must be supplied")
        if not isinstance(self.id, MacromolecularMachineToCellularComponentAssociationId):
            self.id = MacromolecularMachineToCellularComponentAssociationId(self.id)
        if self.object is None:
            raise ValueError(f"object must be supplied")
        if not isinstance(self.object, CellularComponentId):
            self.object = CellularComponentId(self.object)
        super().__post_init__(**kwargs)


@dataclass
class GeneToGoTermAssociation(FunctionalAssociation):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = BIOLINK.GeneToGoTermAssociation
    class_class_curie: ClassVar[str] = "biolink:GeneToGoTermAssociation"
    class_name: ClassVar[str] = "gene to go term association"
    class_model_uri: ClassVar[URIRef] = BIOLINK.GeneToGoTermAssociation

    id: Union[str, GeneToGoTermAssociationId] = None
    relation: Union[str, URIorCURIE] = None
    subject: Union[str, MolecularEntityId] = None
    object: Union[str, GeneOntologyClassId] = None

    def __post_init__(self, **kwargs: Dict[str, Any]):
        if self.id is None:
            raise ValueError(f"id must be supplied")
        if not isinstance(self.id, GeneToGoTermAssociationId):
            self.id = GeneToGoTermAssociationId(self.id)
        if self.subject is None:
            raise ValueError(f"subject must be supplied")
        if not isinstance(self.subject, MolecularEntityId):
            self.subject = MolecularEntityId(self.subject)
        if self.object is None:
            raise ValueError(f"object must be supplied")
        if not isinstance(self.object, GeneOntologyClassId):
            self.object = GeneOntologyClassId(self.object)
        super().__post_init__(**kwargs)


@dataclass
class GenomicSequenceLocalization(Association):
    """
    A relationship between a sequence feature and an entity it is localized to. The reference entity may be a
    chromosome, chromosome region or information entity such as a contig
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = BIOLINK.GenomicSequenceLocalization
    class_class_curie: ClassVar[str] = "biolink:GenomicSequenceLocalization"
    class_name: ClassVar[str] = "genomic sequence localization"
    class_model_uri: ClassVar[URIRef] = BIOLINK.GenomicSequenceLocalization

    id: Union[str, GenomicSequenceLocalizationId] = None
    relation: Union[str, URIorCURIE] = None
    subject: Union[str, GenomicEntityId] = None
    object: Union[str, GenomicEntityId] = None
    start_interbase_coordinate: Optional[str] = None
    end_interbase_coordinate: Optional[str] = None
    genome_build: Optional[str] = None
    phase: Optional[str] = None

    def __post_init__(self, **kwargs: Dict[str, Any]):
        if self.id is None:
            raise ValueError(f"id must be supplied")
        if not isinstance(self.id, GenomicSequenceLocalizationId):
            self.id = GenomicSequenceLocalizationId(self.id)
        if self.subject is None:
            raise ValueError(f"subject must be supplied")
        if not isinstance(self.subject, GenomicEntityId):
            self.subject = GenomicEntityId(self.subject)
        if self.object is None:
            raise ValueError(f"object must be supplied")
        if not isinstance(self.object, GenomicEntityId):
            self.object = GenomicEntityId(self.object)
        super().__post_init__(**kwargs)


@dataclass
class SequenceFeatureRelationship(Association):
    """
    For example, a particular exon is part of a particular transcript or gene
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = BIOLINK.SequenceFeatureRelationship
    class_class_curie: ClassVar[str] = "biolink:SequenceFeatureRelationship"
    class_name: ClassVar[str] = "sequence feature relationship"
    class_model_uri: ClassVar[URIRef] = BIOLINK.SequenceFeatureRelationship

    id: Union[str, SequenceFeatureRelationshipId] = None
    relation: Union[str, URIorCURIE] = None
    subject: Union[str, GenomicEntityId] = None
    object: Union[str, GenomicEntityId] = None

    def __post_init__(self, **kwargs: Dict[str, Any]):
        if self.id is None:
            raise ValueError(f"id must be supplied")
        if not isinstance(self.id, SequenceFeatureRelationshipId):
            self.id = SequenceFeatureRelationshipId(self.id)
        if self.subject is None:
            raise ValueError(f"subject must be supplied")
        if not isinstance(self.subject, GenomicEntityId):
            self.subject = GenomicEntityId(self.subject)
        if self.object is None:
            raise ValueError(f"object must be supplied")
        if not isinstance(self.object, GenomicEntityId):
            self.object = GenomicEntityId(self.object)
        super().__post_init__(**kwargs)


@dataclass
class TranscriptToGeneRelationship(SequenceFeatureRelationship):
    """
    A gene is a collection of transcripts
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = BIOLINK.TranscriptToGeneRelationship
    class_class_curie: ClassVar[str] = "biolink:TranscriptToGeneRelationship"
    class_name: ClassVar[str] = "transcript to gene relationship"
    class_model_uri: ClassVar[URIRef] = BIOLINK.TranscriptToGeneRelationship

    id: Union[str, TranscriptToGeneRelationshipId] = None
    relation: Union[str, URIorCURIE] = None
    subject: Union[str, TranscriptId] = None
    object: Union[str, GeneId] = None

    def __post_init__(self, **kwargs: Dict[str, Any]):
        if self.id is None:
            raise ValueError(f"id must be supplied")
        if not isinstance(self.id, TranscriptToGeneRelationshipId):
            self.id = TranscriptToGeneRelationshipId(self.id)
        if self.subject is None:
            raise ValueError(f"subject must be supplied")
        if not isinstance(self.subject, TranscriptId):
            self.subject = TranscriptId(self.subject)
        if self.object is None:
            raise ValueError(f"object must be supplied")
        if not isinstance(self.object, GeneId):
            self.object = GeneId(self.object)
        super().__post_init__(**kwargs)


@dataclass
class GeneToGeneProductRelationship(SequenceFeatureRelationship):
    """
    A gene is transcribed and potentially translated to a gene product
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = BIOLINK.GeneToGeneProductRelationship
    class_class_curie: ClassVar[str] = "biolink:GeneToGeneProductRelationship"
    class_name: ClassVar[str] = "gene to gene product relationship"
    class_model_uri: ClassVar[URIRef] = BIOLINK.GeneToGeneProductRelationship

    id: Union[str, GeneToGeneProductRelationshipId] = None
    subject: Union[str, GeneId] = None
    object: Union[str, GeneProductId] = None
    relation: Union[str, URIorCURIE] = None

    def __post_init__(self, **kwargs: Dict[str, Any]):
        if self.id is None:
            raise ValueError(f"id must be supplied")
        if not isinstance(self.id, GeneToGeneProductRelationshipId):
            self.id = GeneToGeneProductRelationshipId(self.id)
        if self.subject is None:
            raise ValueError(f"subject must be supplied")
        if not isinstance(self.subject, GeneId):
            self.subject = GeneId(self.subject)
        if self.object is None:
            raise ValueError(f"object must be supplied")
        if not isinstance(self.object, GeneProductId):
            self.object = GeneProductId(self.object)
        if self.relation is None:
            raise ValueError(f"relation must be supplied")
        if not isinstance(self.relation, URIorCURIE):
            self.relation = URIorCURIE(self.relation)
        super().__post_init__(**kwargs)


@dataclass
class ExonToTranscriptRelationship(SequenceFeatureRelationship):
    """
    A transcript is formed from multiple exons
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = BIOLINK.ExonToTranscriptRelationship
    class_class_curie: ClassVar[str] = "biolink:ExonToTranscriptRelationship"
    class_name: ClassVar[str] = "exon to transcript relationship"
    class_model_uri: ClassVar[URIRef] = BIOLINK.ExonToTranscriptRelationship

    id: Union[str, ExonToTranscriptRelationshipId] = None
    relation: Union[str, URIorCURIE] = None
    subject: Union[str, ExonId] = None
    object: Union[str, TranscriptId] = None

    def __post_init__(self, **kwargs: Dict[str, Any]):
        if self.id is None:
            raise ValueError(f"id must be supplied")
        if not isinstance(self.id, ExonToTranscriptRelationshipId):
            self.id = ExonToTranscriptRelationshipId(self.id)
        if self.subject is None:
            raise ValueError(f"subject must be supplied")
        if not isinstance(self.subject, ExonId):
            self.subject = ExonId(self.subject)
        if self.object is None:
            raise ValueError(f"object must be supplied")
        if not isinstance(self.object, TranscriptId):
            self.object = TranscriptId(self.object)
        super().__post_init__(**kwargs)


@dataclass
class GeneRegulatoryRelationship(Association):
    """
    A regulatory relationship between two genes
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = BIOLINK.GeneRegulatoryRelationship
    class_class_curie: ClassVar[str] = "biolink:GeneRegulatoryRelationship"
    class_name: ClassVar[str] = "gene regulatory relationship"
    class_model_uri: ClassVar[URIRef] = BIOLINK.GeneRegulatoryRelationship

    id: Union[str, GeneRegulatoryRelationshipId] = None
    relation: Union[str, URIorCURIE] = None
    subject: Union[str, GeneOrGeneProductId] = None
    object: Union[str, GeneOrGeneProductId] = None

    def __post_init__(self, **kwargs: Dict[str, Any]):
        if self.id is None:
            raise ValueError(f"id must be supplied")
        if not isinstance(self.id, GeneRegulatoryRelationshipId):
            self.id = GeneRegulatoryRelationshipId(self.id)
        if self.relation is None:
            raise ValueError(f"relation must be supplied")
        if not isinstance(self.relation, URIorCURIE):
            self.relation = URIorCURIE(self.relation)
        if self.subject is None:
            raise ValueError(f"subject must be supplied")
        if not isinstance(self.subject, GeneOrGeneProductId):
            self.subject = GeneOrGeneProductId(self.subject)
        if self.object is None:
            raise ValueError(f"object must be supplied")
        if not isinstance(self.object, GeneOrGeneProductId):
            self.object = GeneOrGeneProductId(self.object)
        super().__post_init__(**kwargs)


@dataclass
class AnatomicalEntityToAnatomicalEntityAssociation(Association):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = BIOLINK.AnatomicalEntityToAnatomicalEntityAssociation
    class_class_curie: ClassVar[str] = "biolink:AnatomicalEntityToAnatomicalEntityAssociation"
    class_name: ClassVar[str] = "anatomical entity to anatomical entity association"
    class_model_uri: ClassVar[URIRef] = BIOLINK.AnatomicalEntityToAnatomicalEntityAssociation

    id: Union[str, AnatomicalEntityToAnatomicalEntityAssociationId] = None
    relation: Union[str, URIorCURIE] = None
    subject: Union[str, AnatomicalEntityId] = None
    object: Union[str, AnatomicalEntityId] = None

    def __post_init__(self, **kwargs: Dict[str, Any]):
        if self.id is None:
            raise ValueError(f"id must be supplied")
        if not isinstance(self.id, AnatomicalEntityToAnatomicalEntityAssociationId):
            self.id = AnatomicalEntityToAnatomicalEntityAssociationId(self.id)
        if self.subject is None:
            raise ValueError(f"subject must be supplied")
        if not isinstance(self.subject, AnatomicalEntityId):
            self.subject = AnatomicalEntityId(self.subject)
        if self.object is None:
            raise ValueError(f"object must be supplied")
        if not isinstance(self.object, AnatomicalEntityId):
            self.object = AnatomicalEntityId(self.object)
        super().__post_init__(**kwargs)


@dataclass
class AnatomicalEntityToAnatomicalEntityPartOfAssociation(AnatomicalEntityToAnatomicalEntityAssociation):
    """
    A relationship between two anatomical entities where the relationship is mereological, i.e the two entities are
    related by parthood. This includes relationships between cellular components and cells, between cells and tissues,
    tissues and whole organisms
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = BIOLINK.AnatomicalEntityToAnatomicalEntityPartOfAssociation
    class_class_curie: ClassVar[str] = "biolink:AnatomicalEntityToAnatomicalEntityPartOfAssociation"
    class_name: ClassVar[str] = "anatomical entity to anatomical entity part of association"
    class_model_uri: ClassVar[URIRef] = BIOLINK.AnatomicalEntityToAnatomicalEntityPartOfAssociation

    id: Union[str, AnatomicalEntityToAnatomicalEntityPartOfAssociationId] = None
    subject: Union[str, AnatomicalEntityId] = None
    object: Union[str, AnatomicalEntityId] = None
    relation: Union[str, URIorCURIE] = None

    def __post_init__(self, **kwargs: Dict[str, Any]):
        if self.id is None:
            raise ValueError(f"id must be supplied")
        if not isinstance(self.id, AnatomicalEntityToAnatomicalEntityPartOfAssociationId):
            self.id = AnatomicalEntityToAnatomicalEntityPartOfAssociationId(self.id)
        if self.subject is None:
            raise ValueError(f"subject must be supplied")
        if not isinstance(self.subject, AnatomicalEntityId):
            self.subject = AnatomicalEntityId(self.subject)
        if self.object is None:
            raise ValueError(f"object must be supplied")
        if not isinstance(self.object, AnatomicalEntityId):
            self.object = AnatomicalEntityId(self.object)
        if self.relation is None:
            raise ValueError(f"relation must be supplied")
        if not isinstance(self.relation, URIorCURIE):
            self.relation = URIorCURIE(self.relation)
        super().__post_init__(**kwargs)


@dataclass
class AnatomicalEntityToAnatomicalEntityOntogenicAssociation(AnatomicalEntityToAnatomicalEntityAssociation):
    """
    A relationship between two anatomical entities where the relationship is ontogenic, i.e the two entities are
    related by development. A number of different relationship types can be used to specify the precise nature of the
    relationship
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = BIOLINK.AnatomicalEntityToAnatomicalEntityOntogenicAssociation
    class_class_curie: ClassVar[str] = "biolink:AnatomicalEntityToAnatomicalEntityOntogenicAssociation"
    class_name: ClassVar[str] = "anatomical entity to anatomical entity ontogenic association"
    class_model_uri: ClassVar[URIRef] = BIOLINK.AnatomicalEntityToAnatomicalEntityOntogenicAssociation

    id: Union[str, AnatomicalEntityToAnatomicalEntityOntogenicAssociationId] = None
    subject: Union[str, AnatomicalEntityId] = None
    object: Union[str, AnatomicalEntityId] = None
    relation: Union[str, URIorCURIE] = None

    def __post_init__(self, **kwargs: Dict[str, Any]):
        if self.id is None:
            raise ValueError(f"id must be supplied")
        if not isinstance(self.id, AnatomicalEntityToAnatomicalEntityOntogenicAssociationId):
            self.id = AnatomicalEntityToAnatomicalEntityOntogenicAssociationId(self.id)
        if self.subject is None:
            raise ValueError(f"subject must be supplied")
        if not isinstance(self.subject, AnatomicalEntityId):
            self.subject = AnatomicalEntityId(self.subject)
        if self.object is None:
            raise ValueError(f"object must be supplied")
        if not isinstance(self.object, AnatomicalEntityId):
            self.object = AnatomicalEntityId(self.object)
        if self.relation is None:
            raise ValueError(f"relation must be supplied")
        if not isinstance(self.relation, URIorCURIE):
            self.relation = URIorCURIE(self.relation)
        super().__post_init__(**kwargs)


@dataclass
class Occurrent(NamedThing):
    """
    A processual entity
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = BIOLINK.Occurrent
    class_class_curie: ClassVar[str] = "biolink:Occurrent"
    class_name: ClassVar[str] = "occurrent"
    class_model_uri: ClassVar[URIRef] = BIOLINK.Occurrent

    id: Union[str, OccurrentId] = None
    name: Union[str, LabelType] = None
    category: List[Union[str, IriType]] = empty_list()

    def __post_init__(self, **kwargs: Dict[str, Any]):
        if self.id is None:
            raise ValueError(f"id must be supplied")
        if not isinstance(self.id, OccurrentId):
            self.id = OccurrentId(self.id)
        super().__post_init__(**kwargs)


@dataclass
class PhysicalEntity(NamedThing):
    """
    An entity that has physical properties such as mass, volume, or charge
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = BIOLINK.PhysicalEntity
    class_class_curie: ClassVar[str] = "biolink:PhysicalEntity"
    class_name: ClassVar[str] = "physical entity"
    class_model_uri: ClassVar[URIRef] = BIOLINK.PhysicalEntity

    id: Union[str, PhysicalEntityId] = None
    name: Union[str, LabelType] = None
    category: List[Union[str, IriType]] = empty_list()

    def __post_init__(self, **kwargs: Dict[str, Any]):
        if self.id is None:
            raise ValueError(f"id must be supplied")
        if not isinstance(self.id, PhysicalEntityId):
            self.id = PhysicalEntityId(self.id)
        super().__post_init__(**kwargs)


@dataclass
class BiologicalProcessOrActivity(BiologicalEntity):
    """
    Either an individual molecular activity, or a collection of causally connected molecular activities
    """
    _inherited_slots: ClassVar[List[str]] = ["has_input", "has_output", "enabled_by"]

    class_class_uri: ClassVar[URIRef] = BIOLINK.BiologicalProcessOrActivity
    class_class_curie: ClassVar[str] = "biolink:BiologicalProcessOrActivity"
    class_name: ClassVar[str] = "biological process or activity"
    class_model_uri: ClassVar[URIRef] = BIOLINK.BiologicalProcessOrActivity

    id: Union[str, BiologicalProcessOrActivityId] = None
    name: Union[str, LabelType] = None
    category: List[Union[str, IriType]] = empty_list()
    has_input: List[Union[str, NamedThingId]] = empty_list()
    has_output: List[Union[str, NamedThingId]] = empty_list()
    enabled_by: List[Union[str, BiologicalProcessOrActivityId]] = empty_list()

    def __post_init__(self, **kwargs: Dict[str, Any]):
        if self.id is None:
            raise ValueError(f"id must be supplied")
        if not isinstance(self.id, BiologicalProcessOrActivityId):
            self.id = BiologicalProcessOrActivityId(self.id)
        self.has_input = [v if isinstance(v, NamedThingId)
                          else NamedThingId(v) for v in ([self.has_input] if isinstance(self.has_input, str) else self.has_input)]
        self.has_output = [v if isinstance(v, NamedThingId)
                           else NamedThingId(v) for v in ([self.has_output] if isinstance(self.has_output, str) else self.has_output)]
        self.enabled_by = [v if isinstance(v, BiologicalProcessOrActivityId)
                           else BiologicalProcessOrActivityId(v) for v in ([self.enabled_by] if isinstance(self.enabled_by, str) else self.enabled_by)]
        super().__post_init__(**kwargs)


@dataclass
class MolecularActivity(BiologicalProcessOrActivity):
    """
    An execution of a molecular function carried out by a gene product or macromolecular complex.
    """
    _inherited_slots: ClassVar[List[str]] = ["has_input", "has_output", "enabled_by"]

    class_class_uri: ClassVar[URIRef] = BIOLINK.MolecularActivity
    class_class_curie: ClassVar[str] = "biolink:MolecularActivity"
    class_name: ClassVar[str] = "molecular activity"
    class_model_uri: ClassVar[URIRef] = BIOLINK.MolecularActivity

    id: Union[str, MolecularActivityId] = None
    name: Union[str, LabelType] = None
    category: List[Union[str, IriType]] = empty_list()
    has_input: List[Union[str, ChemicalSubstanceId]] = empty_list()
    has_output: List[Union[str, ChemicalSubstanceId]] = empty_list()
    enabled_by: List[Union[str, MacromolecularMachineId]] = empty_list()

    def __post_init__(self, **kwargs: Dict[str, Any]):
        if self.id is None:
            raise ValueError(f"id must be supplied")
        if not isinstance(self.id, MolecularActivityId):
            self.id = MolecularActivityId(self.id)
        self.has_input = [v if isinstance(v, ChemicalSubstanceId)
                          else ChemicalSubstanceId(v) for v in ([self.has_input] if isinstance(self.has_input, str) else self.has_input)]
        self.has_output = [v if isinstance(v, ChemicalSubstanceId)
                           else ChemicalSubstanceId(v) for v in ([self.has_output] if isinstance(self.has_output, str) else self.has_output)]
        self.enabled_by = [v if isinstance(v, MacromolecularMachineId)
                           else MacromolecularMachineId(v) for v in ([self.enabled_by] if isinstance(self.enabled_by, str) else self.enabled_by)]
        super().__post_init__(**kwargs)


@dataclass
class ActivityAndBehavior(Occurrent):
    """
    Activity or behavior of any independent integral living, organization or mechanical actor in the world
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = BIOLINK.ActivityAndBehavior
    class_class_curie: ClassVar[str] = "biolink:ActivityAndBehavior"
    class_name: ClassVar[str] = "activity and behavior"
    class_model_uri: ClassVar[URIRef] = BIOLINK.ActivityAndBehavior

    id: Union[str, ActivityAndBehaviorId] = None
    name: Union[str, LabelType] = None
    category: List[Union[str, IriType]] = empty_list()

    def __post_init__(self, **kwargs: Dict[str, Any]):
        if self.id is None:
            raise ValueError(f"id must be supplied")
        if not isinstance(self.id, ActivityAndBehaviorId):
            self.id = ActivityAndBehaviorId(self.id)
        super().__post_init__(**kwargs)


@dataclass
class Procedure(Occurrent):
    """
    A series of actions conducted in a certain order or manner
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = BIOLINK.Procedure
    class_class_curie: ClassVar[str] = "biolink:Procedure"
    class_name: ClassVar[str] = "procedure"
    class_model_uri: ClassVar[URIRef] = BIOLINK.Procedure

    id: Union[str, ProcedureId] = None
    name: Union[str, LabelType] = None
    category: List[Union[str, IriType]] = empty_list()

    def __post_init__(self, **kwargs: Dict[str, Any]):
        if self.id is None:
            raise ValueError(f"id must be supplied")
        if not isinstance(self.id, ProcedureId):
            self.id = ProcedureId(self.id)
        super().__post_init__(**kwargs)


@dataclass
class Phenomenon(Occurrent):
    """
    a fact or situation that is observed to exist or happen, especially one whose cause or explanation is in question
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = BIOLINK.Phenomenon
    class_class_curie: ClassVar[str] = "biolink:Phenomenon"
    class_name: ClassVar[str] = "phenomenon"
    class_model_uri: ClassVar[URIRef] = BIOLINK.Phenomenon

    id: Union[str, PhenomenonId] = None
    name: Union[str, LabelType] = None
    category: List[Union[str, IriType]] = empty_list()

    def __post_init__(self, **kwargs: Dict[str, Any]):
        if self.id is None:
            raise ValueError(f"id must be supplied")
        if not isinstance(self.id, PhenomenonId):
            self.id = PhenomenonId(self.id)
        super().__post_init__(**kwargs)


@dataclass
class BiologicalProcess(BiologicalProcessOrActivity):
    """
    One or more causally connected executions of molecular functions
    """
    _inherited_slots: ClassVar[List[str]] = ["has_input", "has_output", "enabled_by"]

    class_class_uri: ClassVar[URIRef] = BIOLINK.BiologicalProcess
    class_class_curie: ClassVar[str] = "biolink:BiologicalProcess"
    class_name: ClassVar[str] = "biological process"
    class_model_uri: ClassVar[URIRef] = BIOLINK.BiologicalProcess

    id: Union[str, BiologicalProcessId] = None
    name: Union[str, LabelType] = None
    category: List[Union[str, IriType]] = empty_list()

    def __post_init__(self, **kwargs: Dict[str, Any]):
        if self.id is None:
            raise ValueError(f"id must be supplied")
        if not isinstance(self.id, BiologicalProcessId):
            self.id = BiologicalProcessId(self.id)
        super().__post_init__(**kwargs)


@dataclass
class Pathway(BiologicalProcess):
    _inherited_slots: ClassVar[List[str]] = ["has_input", "has_output", "enabled_by"]

    class_class_uri: ClassVar[URIRef] = BIOLINK.Pathway
    class_class_curie: ClassVar[str] = "biolink:Pathway"
    class_name: ClassVar[str] = "pathway"
    class_model_uri: ClassVar[URIRef] = BIOLINK.Pathway

    id: Union[str, PathwayId] = None
    name: Union[str, LabelType] = None
    category: List[Union[str, IriType]] = empty_list()

    def __post_init__(self, **kwargs: Dict[str, Any]):
        if self.id is None:
            raise ValueError(f"id must be supplied")
        if not isinstance(self.id, PathwayId):
            self.id = PathwayId(self.id)
        super().__post_init__(**kwargs)


@dataclass
class PhysiologicalProcess(BiologicalProcess):
    _inherited_slots: ClassVar[List[str]] = ["has_input", "has_output", "enabled_by"]

    class_class_uri: ClassVar[URIRef] = BIOLINK.PhysiologicalProcess
    class_class_curie: ClassVar[str] = "biolink:PhysiologicalProcess"
    class_name: ClassVar[str] = "physiological process"
    class_model_uri: ClassVar[URIRef] = BIOLINK.PhysiologicalProcess

    id: Union[str, PhysiologicalProcessId] = None
    name: Union[str, LabelType] = None
    category: List[Union[str, IriType]] = empty_list()

    def __post_init__(self, **kwargs: Dict[str, Any]):
        if self.id is None:
            raise ValueError(f"id must be supplied")
        if not isinstance(self.id, PhysiologicalProcessId):
            self.id = PhysiologicalProcessId(self.id)
        super().__post_init__(**kwargs)


@dataclass
class CellularComponent(AnatomicalEntity):
    """
    A location in or around a cell
    """
    _inherited_slots: ClassVar[List[str]] = ["in_taxon"]

    class_class_uri: ClassVar[URIRef] = BIOLINK.CellularComponent
    class_class_curie: ClassVar[str] = "biolink:CellularComponent"
    class_name: ClassVar[str] = "cellular component"
    class_model_uri: ClassVar[URIRef] = BIOLINK.CellularComponent

    id: Union[str, CellularComponentId] = None
    name: Union[str, LabelType] = None
    category: List[Union[str, IriType]] = empty_list()

    def __post_init__(self, **kwargs: Dict[str, Any]):
        if self.id is None:
            raise ValueError(f"id must be supplied")
        if not isinstance(self.id, CellularComponentId):
            self.id = CellularComponentId(self.id)
        super().__post_init__(**kwargs)


@dataclass
class Cell(AnatomicalEntity):
    _inherited_slots: ClassVar[List[str]] = ["in_taxon"]

    class_class_uri: ClassVar[URIRef] = BIOLINK.Cell
    class_class_curie: ClassVar[str] = "biolink:Cell"
    class_name: ClassVar[str] = "cell"
    class_model_uri: ClassVar[URIRef] = BIOLINK.Cell

    id: Union[str, CellId] = None
    name: Union[str, LabelType] = None
    category: List[Union[str, IriType]] = empty_list()

    def __post_init__(self, **kwargs: Dict[str, Any]):
        if self.id is None:
            raise ValueError(f"id must be supplied")
        if not isinstance(self.id, CellId):
            self.id = CellId(self.id)
        super().__post_init__(**kwargs)


@dataclass
class CellLine(OrganismalEntity):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = BIOLINK.CellLine
    class_class_curie: ClassVar[str] = "biolink:CellLine"
    class_name: ClassVar[str] = "cell line"
    class_model_uri: ClassVar[URIRef] = BIOLINK.CellLine

    id: Union[str, CellLineId] = None
    name: Union[str, LabelType] = None
    category: List[Union[str, IriType]] = empty_list()

    def __post_init__(self, **kwargs: Dict[str, Any]):
        if self.id is None:
            raise ValueError(f"id must be supplied")
        if not isinstance(self.id, CellLineId):
            self.id = CellLineId(self.id)
        super().__post_init__(**kwargs)


@dataclass
class GrossAnatomicalStructure(AnatomicalEntity):
    _inherited_slots: ClassVar[List[str]] = ["in_taxon"]

    class_class_uri: ClassVar[URIRef] = BIOLINK.GrossAnatomicalStructure
    class_class_curie: ClassVar[str] = "biolink:GrossAnatomicalStructure"
    class_name: ClassVar[str] = "gross anatomical structure"
    class_model_uri: ClassVar[URIRef] = BIOLINK.GrossAnatomicalStructure

    id: Union[str, GrossAnatomicalStructureId] = None
    name: Union[str, LabelType] = None
    category: List[Union[str, IriType]] = empty_list()

    def __post_init__(self, **kwargs: Dict[str, Any]):
        if self.id is None:
            raise ValueError(f"id must be supplied")
        if not isinstance(self.id, GrossAnatomicalStructureId):
            self.id = GrossAnatomicalStructureId(self.id)
        super().__post_init__(**kwargs)



# Slots
class slots:
    pass

slots.related_to = Slot(uri=BIOLINK.related_to, name="related to", curie=BIOLINK.curie('related_to'),
                      model_uri=BIOLINK.related_to, domain=NamedThing, range=List[Union[str, NamedThingId]], mappings = [OWL.topObjectProperty, SEMMEDDB.ASSOCIATED_WITH])

slots.interacts_with = Slot(uri=BIOLINK.interacts_with, name="interacts with", curie=BIOLINK.curie('interacts_with'),
                      model_uri=BIOLINK.interacts_with, domain=NamedThing, range=List[Union[str, NamedThingId]], mappings = [RO["0002434"]])

slots.physically_interacts_with = Slot(uri=BIOLINK.physically_interacts_with, name="physically interacts with", curie=BIOLINK.curie('physically_interacts_with'),
                      model_uri=BIOLINK.physically_interacts_with, domain=NamedThing, range=List[Union[str, NamedThingId]], mappings = [WD.P129, SEMMEDDB.INTERACTS_WITH])

slots.molecularly_interacts_with = Slot(uri=BIOLINK.molecularly_interacts_with, name="molecularly interacts with", curie=BIOLINK.curie('molecularly_interacts_with'),
                      model_uri=BIOLINK.molecularly_interacts_with, domain=MolecularEntity, range=List[Union[str, MolecularEntityId]], mappings = [RO["0002436"]])

slots.genetically_interacts_with = Slot(uri=BIOLINK.genetically_interacts_with, name="genetically interacts with", curie=BIOLINK.curie('genetically_interacts_with'),
                      model_uri=BIOLINK.genetically_interacts_with, domain=Gene, range=List[Union[str, GeneId]], mappings = [RO["0002435"]])

slots.affects = Slot(uri=BIOLINK.affects, name="affects", curie=BIOLINK.curie('affects'),
                      model_uri=BIOLINK.affects, domain=NamedThing, range=List[Union[str, NamedThingId]], mappings = [SEMMEDDB.AFFECTS])

slots.affects_abundance_of = Slot(uri=BIOLINK.affects_abundance_of, name="affects abundance of", curie=BIOLINK.curie('affects_abundance_of'),
                      model_uri=BIOLINK.affects_abundance_of, domain=MolecularEntity, range=List[Union[str, MolecularEntityId]])

slots.increases_abundance_of = Slot(uri=BIOLINK.increases_abundance_of, name="increases abundance of", curie=BIOLINK.curie('increases_abundance_of'),
                      model_uri=BIOLINK.increases_abundance_of, domain=MolecularEntity, range=List[Union[str, MolecularEntityId]])

slots.decreases_abundance_of = Slot(uri=BIOLINK.decreases_abundance_of, name="decreases abundance of", curie=BIOLINK.curie('decreases_abundance_of'),
                      model_uri=BIOLINK.decreases_abundance_of, domain=MolecularEntity, range=List[Union[str, MolecularEntityId]])

slots.affects_activity_of = Slot(uri=BIOLINK.affects_activity_of, name="affects activity of", curie=BIOLINK.curie('affects_activity_of'),
                      model_uri=BIOLINK.affects_activity_of, domain=MolecularEntity, range=List[Union[str, MolecularEntityId]])

slots.increases_activity_of = Slot(uri=BIOLINK.increases_activity_of, name="increases activity of", curie=BIOLINK.curie('increases_activity_of'),
                      model_uri=BIOLINK.increases_activity_of, domain=MolecularEntity, range=List[Union[str, MolecularEntityId]])

slots.decreases_activity_of = Slot(uri=BIOLINK.decreases_activity_of, name="decreases activity of", curie=BIOLINK.curie('decreases_activity_of'),
                      model_uri=BIOLINK.decreases_activity_of, domain=MolecularEntity, range=List[Union[str, MolecularEntityId]])

slots.affects_expression_of = Slot(uri=BIOLINK.affects_expression_of, name="affects expression of", curie=BIOLINK.curie('affects_expression_of'),
                      model_uri=BIOLINK.affects_expression_of, domain=MolecularEntity, range=List[Union[str, GenomicEntityId]])

slots.increases_expression_of = Slot(uri=BIOLINK.increases_expression_of, name="increases expression of", curie=BIOLINK.curie('increases_expression_of'),
                      model_uri=BIOLINK.increases_expression_of, domain=MolecularEntity, range=List[Union[str, GenomicEntityId]])

slots.decreases_expression_of = Slot(uri=BIOLINK.decreases_expression_of, name="decreases expression of", curie=BIOLINK.curie('decreases_expression_of'),
                      model_uri=BIOLINK.decreases_expression_of, domain=MolecularEntity, range=List[Union[str, GenomicEntityId]])

slots.affects_folding_of = Slot(uri=BIOLINK.affects_folding_of, name="affects folding of", curie=BIOLINK.curie('affects_folding_of'),
                      model_uri=BIOLINK.affects_folding_of, domain=MolecularEntity, range=List[Union[str, MolecularEntityId]])

slots.increases_folding_of = Slot(uri=BIOLINK.increases_folding_of, name="increases folding of", curie=BIOLINK.curie('increases_folding_of'),
                      model_uri=BIOLINK.increases_folding_of, domain=MolecularEntity, range=List[Union[str, MolecularEntityId]])

slots.decreases_folding_of = Slot(uri=BIOLINK.decreases_folding_of, name="decreases folding of", curie=BIOLINK.curie('decreases_folding_of'),
                      model_uri=BIOLINK.decreases_folding_of, domain=MolecularEntity, range=List[Union[str, MolecularEntityId]])

slots.affects_localization_of = Slot(uri=BIOLINK.affects_localization_of, name="affects localization of", curie=BIOLINK.curie('affects_localization_of'),
                      model_uri=BIOLINK.affects_localization_of, domain=MolecularEntity, range=List[Union[str, MolecularEntityId]])

slots.increases_localization_of = Slot(uri=BIOLINK.increases_localization_of, name="increases localization of", curie=BIOLINK.curie('increases_localization_of'),
                      model_uri=BIOLINK.increases_localization_of, domain=MolecularEntity, range=List[Union[str, MolecularEntityId]])

slots.decreases_localization_of = Slot(uri=BIOLINK.decreases_localization_of, name="decreases localization of", curie=BIOLINK.curie('decreases_localization_of'),
                      model_uri=BIOLINK.decreases_localization_of, domain=MolecularEntity, range=List[Union[str, MolecularEntityId]])

slots.affects_metabolic_processing_of = Slot(uri=BIOLINK.affects_metabolic_processing_of, name="affects metabolic processing of", curie=BIOLINK.curie('affects_metabolic_processing_of'),
                      model_uri=BIOLINK.affects_metabolic_processing_of, domain=MolecularEntity, range=List[Union[str, MolecularEntityId]])

slots.increases_metabolic_processing_of = Slot(uri=BIOLINK.increases_metabolic_processing_of, name="increases metabolic processing of", curie=BIOLINK.curie('increases_metabolic_processing_of'),
                      model_uri=BIOLINK.increases_metabolic_processing_of, domain=MolecularEntity, range=List[Union[str, MolecularEntityId]])

slots.decreases_metabolic_processing_of = Slot(uri=BIOLINK.decreases_metabolic_processing_of, name="decreases metabolic processing of", curie=BIOLINK.curie('decreases_metabolic_processing_of'),
                      model_uri=BIOLINK.decreases_metabolic_processing_of, domain=MolecularEntity, range=List[Union[str, MolecularEntityId]])

slots.affects_molecular_modification_of = Slot(uri=BIOLINK.affects_molecular_modification_of, name="affects molecular modification of", curie=BIOLINK.curie('affects_molecular_modification_of'),
                      model_uri=BIOLINK.affects_molecular_modification_of, domain=MolecularEntity, range=List[Union[str, MolecularEntityId]])

slots.increases_molecular_modification_of = Slot(uri=BIOLINK.increases_molecular_modification_of, name="increases molecular modification of", curie=BIOLINK.curie('increases_molecular_modification_of'),
                      model_uri=BIOLINK.increases_molecular_modification_of, domain=MolecularEntity, range=List[Union[str, MolecularEntityId]])

slots.decreases_molecular_modification_of = Slot(uri=BIOLINK.decreases_molecular_modification_of, name="decreases molecular modification of", curie=BIOLINK.curie('decreases_molecular_modification_of'),
                      model_uri=BIOLINK.decreases_molecular_modification_of, domain=MolecularEntity, range=List[Union[str, MolecularEntityId]])

slots.affects_synthesis_of = Slot(uri=BIOLINK.affects_synthesis_of, name="affects synthesis of", curie=BIOLINK.curie('affects_synthesis_of'),
                      model_uri=BIOLINK.affects_synthesis_of, domain=MolecularEntity, range=List[Union[str, MolecularEntityId]])

slots.increases_synthesis_of = Slot(uri=BIOLINK.increases_synthesis_of, name="increases synthesis of", curie=BIOLINK.curie('increases_synthesis_of'),
                      model_uri=BIOLINK.increases_synthesis_of, domain=MolecularEntity, range=List[Union[str, MolecularEntityId]])

slots.decreases_synthesis_of = Slot(uri=BIOLINK.decreases_synthesis_of, name="decreases synthesis of", curie=BIOLINK.curie('decreases_synthesis_of'),
                      model_uri=BIOLINK.decreases_synthesis_of, domain=MolecularEntity, range=List[Union[str, MolecularEntityId]])

slots.affects_degradation_of = Slot(uri=BIOLINK.affects_degradation_of, name="affects degradation of", curie=BIOLINK.curie('affects_degradation_of'),
                      model_uri=BIOLINK.affects_degradation_of, domain=MolecularEntity, range=List[Union[str, MolecularEntityId]])

slots.increases_degradation_of = Slot(uri=BIOLINK.increases_degradation_of, name="increases degradation of", curie=BIOLINK.curie('increases_degradation_of'),
                      model_uri=BIOLINK.increases_degradation_of, domain=MolecularEntity, range=List[Union[str, MolecularEntityId]])

slots.decreases_degradation_of = Slot(uri=BIOLINK.decreases_degradation_of, name="decreases degradation of", curie=BIOLINK.curie('decreases_degradation_of'),
                      model_uri=BIOLINK.decreases_degradation_of, domain=MolecularEntity, range=List[Union[str, MolecularEntityId]])

slots.affects_mutation_rate_of = Slot(uri=BIOLINK.affects_mutation_rate_of, name="affects mutation rate of", curie=BIOLINK.curie('affects_mutation_rate_of'),
                      model_uri=BIOLINK.affects_mutation_rate_of, domain=MolecularEntity, range=List[Union[str, GenomicEntityId]])

slots.increases_mutation_rate_of = Slot(uri=BIOLINK.increases_mutation_rate_of, name="increases mutation rate of", curie=BIOLINK.curie('increases_mutation_rate_of'),
                      model_uri=BIOLINK.increases_mutation_rate_of, domain=MolecularEntity, range=List[Union[str, GenomicEntityId]])

slots.decreases_mutation_rate_of = Slot(uri=BIOLINK.decreases_mutation_rate_of, name="decreases mutation rate of", curie=BIOLINK.curie('decreases_mutation_rate_of'),
                      model_uri=BIOLINK.decreases_mutation_rate_of, domain=MolecularEntity, range=List[Union[str, GenomicEntityId]])

slots.affects_response_to = Slot(uri=BIOLINK.affects_response_to, name="affects response to", curie=BIOLINK.curie('affects_response_to'),
                      model_uri=BIOLINK.affects_response_to, domain=MolecularEntity, range=List[Union[str, MolecularEntityId]])

slots.increases_response_to = Slot(uri=BIOLINK.increases_response_to, name="increases response to", curie=BIOLINK.curie('increases_response_to'),
                      model_uri=BIOLINK.increases_response_to, domain=MolecularEntity, range=List[Union[str, MolecularEntityId]])

slots.decreases_response_to = Slot(uri=BIOLINK.decreases_response_to, name="decreases response to", curie=BIOLINK.curie('decreases_response_to'),
                      model_uri=BIOLINK.decreases_response_to, domain=MolecularEntity, range=List[Union[str, MolecularEntityId]])

slots.affects_splicing_of = Slot(uri=BIOLINK.affects_splicing_of, name="affects splicing of", curie=BIOLINK.curie('affects_splicing_of'),
                      model_uri=BIOLINK.affects_splicing_of, domain=MolecularEntity, range=List[Union[str, TranscriptId]])

slots.increases_splicing_of = Slot(uri=BIOLINK.increases_splicing_of, name="increases splicing of", curie=BIOLINK.curie('increases_splicing_of'),
                      model_uri=BIOLINK.increases_splicing_of, domain=MolecularEntity, range=List[Union[str, TranscriptId]])

slots.decreases_splicing_of = Slot(uri=BIOLINK.decreases_splicing_of, name="decreases splicing of", curie=BIOLINK.curie('decreases_splicing_of'),
                      model_uri=BIOLINK.decreases_splicing_of, domain=MolecularEntity, range=List[Union[str, TranscriptId]])

slots.affects_stability_of = Slot(uri=BIOLINK.affects_stability_of, name="affects stability of", curie=BIOLINK.curie('affects_stability_of'),
                      model_uri=BIOLINK.affects_stability_of, domain=MolecularEntity, range=List[Union[str, MolecularEntityId]])

slots.increases_stability_of = Slot(uri=BIOLINK.increases_stability_of, name="increases stability of", curie=BIOLINK.curie('increases_stability_of'),
                      model_uri=BIOLINK.increases_stability_of, domain=MolecularEntity, range=List[Union[str, MolecularEntityId]])

slots.decreases_stability_of = Slot(uri=BIOLINK.decreases_stability_of, name="decreases stability of", curie=BIOLINK.curie('decreases_stability_of'),
                      model_uri=BIOLINK.decreases_stability_of, domain=MolecularEntity, range=List[Union[str, MolecularEntityId]])

slots.affects_transport_of = Slot(uri=BIOLINK.affects_transport_of, name="affects transport of", curie=BIOLINK.curie('affects_transport_of'),
                      model_uri=BIOLINK.affects_transport_of, domain=MolecularEntity, range=List[Union[str, MolecularEntityId]])

slots.increases_transport_of = Slot(uri=BIOLINK.increases_transport_of, name="increases transport of", curie=BIOLINK.curie('increases_transport_of'),
                      model_uri=BIOLINK.increases_transport_of, domain=MolecularEntity, range=List[Union[str, MolecularEntityId]])

slots.decreases_transport_of = Slot(uri=BIOLINK.decreases_transport_of, name="decreases transport of", curie=BIOLINK.curie('decreases_transport_of'),
                      model_uri=BIOLINK.decreases_transport_of, domain=MolecularEntity, range=List[Union[str, MolecularEntityId]])

slots.affects_secretion_of = Slot(uri=BIOLINK.affects_secretion_of, name="affects secretion of", curie=BIOLINK.curie('affects_secretion_of'),
                      model_uri=BIOLINK.affects_secretion_of, domain=MolecularEntity, range=List[Union[str, MolecularEntityId]])

slots.increases_secretion_of = Slot(uri=BIOLINK.increases_secretion_of, name="increases secretion of", curie=BIOLINK.curie('increases_secretion_of'),
                      model_uri=BIOLINK.increases_secretion_of, domain=MolecularEntity, range=List[Union[str, MolecularEntityId]])

slots.decreases_secretion_of = Slot(uri=BIOLINK.decreases_secretion_of, name="decreases secretion of", curie=BIOLINK.curie('decreases_secretion_of'),
                      model_uri=BIOLINK.decreases_secretion_of, domain=MolecularEntity, range=List[Union[str, MolecularEntityId]])

slots.affects_uptake_of = Slot(uri=BIOLINK.affects_uptake_of, name="affects uptake of", curie=BIOLINK.curie('affects_uptake_of'),
                      model_uri=BIOLINK.affects_uptake_of, domain=MolecularEntity, range=List[Union[str, MolecularEntityId]])

slots.increases_uptake_of = Slot(uri=BIOLINK.increases_uptake_of, name="increases uptake of", curie=BIOLINK.curie('increases_uptake_of'),
                      model_uri=BIOLINK.increases_uptake_of, domain=MolecularEntity, range=List[Union[str, MolecularEntityId]])

slots.decreases_uptake_of = Slot(uri=BIOLINK.decreases_uptake_of, name="decreases uptake of", curie=BIOLINK.curie('decreases_uptake_of'),
                      model_uri=BIOLINK.decreases_uptake_of, domain=MolecularEntity, range=List[Union[str, MolecularEntityId]])

slots.regulates = Slot(uri=BIOLINK.regulates, name="regulates", curie=BIOLINK.curie('regulates'),
                      model_uri=BIOLINK.regulates, domain=NamedThing, range=List[Union[str, NamedThingId]], mappings = [WD.P128])

slots.positively_regulates = Slot(uri=BIOLINK.positively_regulates, name="positively regulates", curie=BIOLINK.curie('positively_regulates'),
                      model_uri=BIOLINK.positively_regulates, domain=NamedThing, range=List[Union[str, NamedThingId]])

slots.negatively_regulates = Slot(uri=BIOLINK.negatively_regulates, name="negatively regulates", curie=BIOLINK.curie('negatively_regulates'),
                      model_uri=BIOLINK.negatively_regulates, domain=NamedThing, range=List[Union[str, NamedThingId]])

slots.regulates_process_to_process = Slot(uri=BIOLINK.regulates_process_to_process, name="regulates, process to process", curie=BIOLINK.curie('regulates_process_to_process'),
                      model_uri=BIOLINK.regulates_process_to_process, domain=Occurrent, range=List[Union[str, OccurrentId]], mappings = [RO["0002211"]])

slots.positively_regulates_process_to_process = Slot(uri=BIOLINK.positively_regulates_process_to_process, name="positively regulates, process to process", curie=BIOLINK.curie('positively_regulates_process_to_process'),
                      model_uri=BIOLINK.positively_regulates_process_to_process, domain=Occurrent, range=List[Union[str, OccurrentId]], mappings = [RO["0002213"]])

slots.negatively_regulates_process_to_process = Slot(uri=BIOLINK.negatively_regulates_process_to_process, name="negatively regulates, process to process", curie=BIOLINK.curie('negatively_regulates_process_to_process'),
                      model_uri=BIOLINK.negatively_regulates_process_to_process, domain=Occurrent, range=List[Union[str, OccurrentId]], mappings = [RO["0002212"]])

slots.regulates_entity_to_entity = Slot(uri=BIOLINK.regulates_entity_to_entity, name="regulates, entity to entity", curie=BIOLINK.curie('regulates_entity_to_entity'),
                      model_uri=BIOLINK.regulates_entity_to_entity, domain=MolecularEntity, range=List[Union[str, MolecularEntityId]], mappings = [RO["0002448"]])

slots.positively_regulates_entity_to_entity = Slot(uri=BIOLINK.positively_regulates_entity_to_entity, name="positively regulates, entity to entity", curie=BIOLINK.curie('positively_regulates_entity_to_entity'),
                      model_uri=BIOLINK.positively_regulates_entity_to_entity, domain=MolecularEntity, range=List[Union[str, MolecularEntityId]], mappings = [RO["0002450"], SEMMEDDB.STIMULATES])

slots.negatively_regulates_entity_to_entity = Slot(uri=BIOLINK.negatively_regulates_entity_to_entity, name="negatively regulates, entity to entity", curie=BIOLINK.curie('negatively_regulates_entity_to_entity'),
                      model_uri=BIOLINK.negatively_regulates_entity_to_entity, domain=MolecularEntity, range=List[Union[str, MolecularEntityId]], mappings = [RO["0002449"], SEMMEDDB.INHIBITS])

slots.disrupts = Slot(uri=BIOLINK.disrupts, name="disrupts", curie=BIOLINK.curie('disrupts'),
                      model_uri=BIOLINK.disrupts, domain=NamedThing, range=List[Union[str, NamedThingId]], mappings = [SEMMEDDB.DISRUPTS])

slots.has_gene_product = Slot(uri=BIOLINK.has_gene_product, name="has gene product", curie=BIOLINK.curie('has_gene_product'),
                      model_uri=BIOLINK.has_gene_product, domain=Gene, range=List[Union[str, GeneProductId]], mappings = [RO["0002205"], WD.P688])

slots.homologous_to = Slot(uri=BIOLINK.homologous_to, name="homologous to", curie=BIOLINK.curie('homologous_to'),
                      model_uri=BIOLINK.homologous_to, domain=NamedThing, range=List[Union[str, NamedThingId]], mappings = [RO.HOM0000001, SIO["010302"]])

slots.paralogous_to = Slot(uri=BIOLINK.paralogous_to, name="paralogous to", curie=BIOLINK.curie('paralogous_to'),
                      model_uri=BIOLINK.paralogous_to, domain=NamedThing, range=List[Union[str, NamedThingId]], mappings = [RO.HOM0000011])

slots.orthologous_to = Slot(uri=BIOLINK.orthologous_to, name="orthologous to", curie=BIOLINK.curie('orthologous_to'),
                      model_uri=BIOLINK.orthologous_to, domain=NamedThing, range=List[Union[str, NamedThingId]], mappings = [RO.HOM0000017, WD.P684])

slots.xenologous_to = Slot(uri=BIOLINK.xenologous_to, name="xenologous to", curie=BIOLINK.curie('xenologous_to'),
                      model_uri=BIOLINK.xenologous_to, domain=NamedThing, range=List[Union[str, NamedThingId]], mappings = [RO.HOM0000018])

slots.coexists_with = Slot(uri=BIOLINK.coexists_with, name="coexists with", curie=BIOLINK.curie('coexists_with'),
                      model_uri=BIOLINK.coexists_with, domain=NamedThing, range=List[Union[str, NamedThingId]], mappings = [SEMMEDDB.COEXISTS_WITH])

slots.in_pathway_with = Slot(uri=BIOLINK.in_pathway_with, name="in pathway with", curie=BIOLINK.curie('in_pathway_with'),
                      model_uri=BIOLINK.in_pathway_with, domain=GeneOrGeneProduct, range=List[Union[str, GeneOrGeneProductId]])

slots.in_complex_with = Slot(uri=BIOLINK.in_complex_with, name="in complex with", curie=BIOLINK.curie('in_complex_with'),
                      model_uri=BIOLINK.in_complex_with, domain=GeneOrGeneProduct, range=List[Union[str, GeneOrGeneProductId]])

slots.in_cell_population_with = Slot(uri=BIOLINK.in_cell_population_with, name="in cell population with", curie=BIOLINK.curie('in_cell_population_with'),
                      model_uri=BIOLINK.in_cell_population_with, domain=GeneOrGeneProduct, range=List[Union[str, GeneOrGeneProductId]])

slots.colocalizes_with = Slot(uri=BIOLINK.colocalizes_with, name="colocalizes with", curie=BIOLINK.curie('colocalizes_with'),
                      model_uri=BIOLINK.colocalizes_with, domain=NamedThing, range=List[Union[str, NamedThingId]], mappings = [RO["00002325"]])

slots.gene_associated_with_condition = Slot(uri=BIOLINK.gene_associated_with_condition, name="gene associated with condition", curie=BIOLINK.curie('gene_associated_with_condition'),
                      model_uri=BIOLINK.gene_associated_with_condition, domain=Gene, range=List[Union[str, DiseaseOrPhenotypicFeatureId]], mappings = [WD.P2293])

slots.affects_risk_for = Slot(uri=BIOLINK.affects_risk_for, name="affects risk for", curie=BIOLINK.curie('affects_risk_for'),
                      model_uri=BIOLINK.affects_risk_for, domain=NamedThing, range=List[Union[str, NamedThingId]])

slots.predisposes = Slot(uri=BIOLINK.predisposes, name="predisposes", curie=BIOLINK.curie('predisposes'),
                      model_uri=BIOLINK.predisposes, domain=NamedThing, range=List[Union[str, NamedThingId]], mappings = [SEMMEDDB.PREDISPOSES])

slots.contributes_to = Slot(uri=BIOLINK.contributes_to, name="contributes to", curie=BIOLINK.curie('contributes_to'),
                      model_uri=BIOLINK.contributes_to, domain=NamedThing, range=List[Union[str, NamedThingId]], mappings = [RO["0002326"]])

slots.causes = Slot(uri=BIOLINK.causes, name="causes", curie=BIOLINK.curie('causes'),
                      model_uri=BIOLINK.causes, domain=NamedThing, range=List[Union[str, NamedThingId]], mappings = [RO["0002410"], SEMMEDDB.CAUSES, WD.P1542])

slots.caused_by = Slot(uri=BIOLINK.caused_by, name="caused by", curie=BIOLINK.curie('caused_by'),
                      model_uri=BIOLINK.caused_by, domain=NamedThing, range=List[Union[str, NamedThingId]], mappings = [WD.P828])

slots.treats = Slot(uri=BIOLINK.treats, name="treats", curie=BIOLINK.curie('treats'),
                      model_uri=BIOLINK.treats, domain=Treatment, range=List[Union[str, DiseaseOrPhenotypicFeatureId]], mappings = [RO["0002606"], RO["0003307"], SEMMEDDB.TREATS, WD.P2175])

slots.prevents = Slot(uri=BIOLINK.prevents, name="prevents", curie=BIOLINK.curie('prevents'),
                      model_uri=BIOLINK.prevents, domain=NamedThing, range=List[Union[str, NamedThingId]], mappings = [RO["0002599"], SEMMEDDB.PREVENTS])

slots.correlated_with = Slot(uri=BIOLINK.correlated_with, name="correlated with", curie=BIOLINK.curie('correlated_with'),
                      model_uri=BIOLINK.correlated_with, domain=NamedThing, range=List[Union[str, NamedThingId]], mappings = [RO["0002610"]])

slots.has_biomarker = Slot(uri=BIOLINK.has_biomarker, name="has biomarker", curie=BIOLINK.curie('has_biomarker'),
                      model_uri=BIOLINK.has_biomarker, domain=DiseaseOrPhenotypicFeature, range=List[Union[str, MolecularEntityId]])

slots.biomarker_for = Slot(uri=BIOLINK.biomarker_for, name="biomarker for", curie=BIOLINK.curie('biomarker_for'),
                      model_uri=BIOLINK.biomarker_for, domain=MolecularEntity, range=List[Union[str, DiseaseOrPhenotypicFeatureId]], mappings = [RO["0002607"]])

slots.treated_by = Slot(uri=BIOLINK.treated_by, name="treated by", curie=BIOLINK.curie('treated_by'),
                      model_uri=BIOLINK.treated_by, domain=DiseaseOrPhenotypicFeature, range=List[Union[str, NamedThingId]], mappings = [RO["0002302"], WD.P2176])

slots.expressed_in = Slot(uri=BIOLINK.expressed_in, name="expressed in", curie=BIOLINK.curie('expressed_in'),
                      model_uri=BIOLINK.expressed_in, domain=GeneOrGeneProduct, range=List[Union[str, AnatomicalEntityId]], mappings = [RO["0002206"]])

slots.expresses = Slot(uri=BIOLINK.expresses, name="expresses", curie=BIOLINK.curie('expresses'),
                      model_uri=BIOLINK.expresses, domain=AnatomicalEntity, range=List[Union[str, GeneOrGeneProductId]], mappings = [RO["0002292"]])

slots.has_phenotype = Slot(uri=BIOLINK.has_phenotype, name="has phenotype", curie=BIOLINK.curie('has_phenotype'),
                      model_uri=BIOLINK.has_phenotype, domain=BiologicalEntity, range=List[Union[str, PhenotypicFeatureId]], mappings = [RO["0002200"]])

slots.occurs_in = Slot(uri=BIOLINK.occurs_in, name="occurs in", curie=BIOLINK.curie('occurs_in'),
                      model_uri=BIOLINK.occurs_in, domain=NamedThing, range=List[Union[str, NamedThingId]], mappings = [BFO["0000066"], SEMMEDDB.OCCURS_IN, SEMMEDDB.PROCESS_OF])

slots.located_in = Slot(uri=BIOLINK.located_in, name="located in", curie=BIOLINK.curie('located_in'),
                      model_uri=BIOLINK.located_in, domain=NamedThing, range=List[Union[str, NamedThingId]], mappings = [RO["0001025"]])

slots.location_of = Slot(uri=BIOLINK.location_of, name="location of", curie=BIOLINK.curie('location_of'),
                      model_uri=BIOLINK.location_of, domain=NamedThing, range=List[Union[str, NamedThingId]], mappings = [RO["0001015"], SEMMEDDB.LOCATION_OF, WD["276"]])

slots.model_of = Slot(uri=BIOLINK.model_of, name="model of", curie=BIOLINK.curie('model_of'),
                      model_uri=BIOLINK.model_of, domain=NamedThing, range=List[Union[str, NamedThingId]], mappings = [RO["0003301"]])

slots.overlaps = Slot(uri=BIOLINK.overlaps, name="overlaps", curie=BIOLINK.curie('overlaps'),
                      model_uri=BIOLINK.overlaps, domain=NamedThing, range=List[Union[str, NamedThingId]], mappings = [RO["0002131"]])

slots.has_part = Slot(uri=BIOLINK.has_part, name="has part", curie=BIOLINK.curie('has_part'),
                      model_uri=BIOLINK.has_part, domain=NamedThing, range=List[Union[str, NamedThingId]], mappings = [BFO["0000051"], WD.P527])

slots.part_of = Slot(uri=BIOLINK.part_of, name="part of", curie=BIOLINK.curie('part_of'),
                      model_uri=BIOLINK.part_of, domain=NamedThing, range=List[Union[str, NamedThingId]], mappings = [BFO["0000050"], SEMMEDDB.PART_OF, WD.P361])

slots.has_participant = Slot(uri=BIOLINK.has_participant, name="has participant", curie=BIOLINK.curie('has_participant'),
                      model_uri=BIOLINK.has_participant, domain=Occurrent, range=List[Union[str, NamedThingId]], mappings = [RO["0000057"], WD.P2283])

slots.has_input = Slot(uri=BIOLINK.has_input, name="has input", curie=BIOLINK.curie('has_input'),
                      model_uri=BIOLINK.has_input, domain=Occurrent, range=List[Union[str, NamedThingId]], mappings = [RO["0002233"], SEMMEDDB.USES])

slots.has_output = Slot(uri=BIOLINK.has_output, name="has output", curie=BIOLINK.curie('has_output'),
                      model_uri=BIOLINK.has_output, domain=Occurrent, range=List[Union[str, NamedThingId]], mappings = [RO["0002234"]])

slots.participates_in = Slot(uri=BIOLINK.participates_in, name="participates in", curie=BIOLINK.curie('participates_in'),
                      model_uri=BIOLINK.participates_in, domain=NamedThing, range=List[Union[str, OccurrentId]], mappings = [RO["0000056"]])

slots.actively_involved_in = Slot(uri=BIOLINK.actively_involved_in, name="actively involved in", curie=BIOLINK.curie('actively_involved_in'),
                      model_uri=BIOLINK.actively_involved_in, domain=NamedThing, range=List[Union[str, OccurrentId]], mappings = [RO["0002331"]])

slots.capable_of = Slot(uri=BIOLINK.capable_of, name="capable of", curie=BIOLINK.curie('capable_of'),
                      model_uri=BIOLINK.capable_of, domain=NamedThing, range=List[Union[str, OccurrentId]], mappings = [RO["0002215"]])

slots.enabled_by = Slot(uri=BIOLINK.enabled_by, name="enabled by", curie=BIOLINK.curie('enabled_by'),
                      model_uri=BIOLINK.enabled_by, domain=Occurrent, range=List[Union[str, BiologicalProcessOrActivityId]], mappings = [RO["0002333"]])

slots.derives_into = Slot(uri=BIOLINK.derives_into, name="derives into", curie=BIOLINK.curie('derives_into'),
                      model_uri=BIOLINK.derives_into, domain=NamedThing, range=List[Union[str, NamedThingId]], mappings = [RO["0001001"], SEMMEDDB.CONVERTS_TO])

slots.derives_from = Slot(uri=BIOLINK.derives_from, name="derives from", curie=BIOLINK.curie('derives_from'),
                      model_uri=BIOLINK.derives_from, domain=NamedThing, range=List[Union[str, NamedThingId]], mappings = [RO["0001000"]])

slots.manifestation_of = Slot(uri=BIOLINK.manifestation_of, name="manifestation of", curie=BIOLINK.curie('manifestation_of'),
                      model_uri=BIOLINK.manifestation_of, domain=NamedThing, range=List[Union[str, DiseaseId]], mappings = [SEMMEDDB.MANIFESTATION_OF, WD.P1557])

slots.produces = Slot(uri=BIOLINK.produces, name="produces", curie=BIOLINK.curie('produces'),
                      model_uri=BIOLINK.produces, domain=NamedThing, range=List[Union[str, NamedThingId]], mappings = [RO["0003000"], WD.P1056, SEMMEDDB.PRODUCES])

slots.precedes = Slot(uri=BIOLINK.precedes, name="precedes", curie=BIOLINK.curie('precedes'),
                      model_uri=BIOLINK.precedes, domain=Occurrent, range=List[Union[str, OccurrentId]], mappings = [BFO["0000063"], SEMMEDDB.PRECEDES, WD.P156])

slots.same_as = Slot(uri=BIOLINK.same_as, name="same as", curie=BIOLINK.curie('same_as'),
                      model_uri=BIOLINK.same_as, domain=NamedThing, range=List[Union[str, NamedThingId]], mappings = [OWL.equivalentClass, OWL.sameAs, SKOS.exactMatch, WD.P2888])

slots.subclass_of = Slot(uri=BIOLINK.subclass_of, name="subclass of", curie=BIOLINK.curie('subclass_of'),
                      model_uri=BIOLINK.subclass_of, domain=OntologyClass, range=List[Union[str, IriType]], mappings = [RDFS.subClassOf, SEMMEDDB.IS_A, WD.P279])

slots.node_property = Slot(uri=BIOLINK.node_property, name="node property", curie=BIOLINK.curie('node_property'),
                      model_uri=BIOLINK.node_property, domain=NamedThing, range=Optional[str])

slots.title = Slot(uri=BIOLINK.title, name="title", curie=BIOLINK.curie('title'),
                      model_uri=BIOLINK.title, domain=DataSetVersion, range=Optional[str], mappings = [DCT.title])

slots.source_data_file = Slot(uri=BIOLINK.source_data_file, name="source data file", curie=BIOLINK.curie('source_data_file'),
                      model_uri=BIOLINK.source_data_file, domain=DataSetVersion, range=Optional[Union[str, DataFileId]], mappings = [DCTERMS.source])

slots.source_web_page = Slot(uri=BIOLINK.source_web_page, name="source web page", curie=BIOLINK.curie('source_web_page'),
                      model_uri=BIOLINK.source_web_page, domain=None, range=Optional[str], mappings = [DCTERMS.source])

slots.retrievedOn = Slot(uri=BIOLINK.retrievedOn, name="retrievedOn", curie=BIOLINK.curie('retrievedOn'),
                      model_uri=BIOLINK.retrievedOn, domain=SourceFile, range=Optional[Union[str, XSDDate]], mappings = [PAV.retrievedOn])

slots.versionOf = Slot(uri=BIOLINK.versionOf, name="versionOf", curie=BIOLINK.curie('versionOf'),
                      model_uri=BIOLINK.versionOf, domain=DataSetVersion, range=Optional[Union[str, DataSetId]], mappings = [DCT.isVersionOf])

slots.source_version = Slot(uri=BIOLINK.source_version, name="source version", curie=BIOLINK.curie('source_version'),
                      model_uri=BIOLINK.source_version, domain=SourceFile, range=Optional[str], mappings = [PAV.version])

slots.downloadURL = Slot(uri=BIOLINK.downloadURL, name="downloadURL", curie=BIOLINK.curie('downloadURL'),
                      model_uri=BIOLINK.downloadURL, domain=None, range=Optional[str], mappings = [DCT.downloadURL])

slots.distribution = Slot(uri=BIOLINK.distribution, name="distribution", curie=BIOLINK.curie('distribution'),
                      model_uri=BIOLINK.distribution, domain=DataSetVersion, range=Optional[Union[str, DistributionLevelId]], mappings = [VOID.Dataset])

slots.type = Slot(uri=BIOLINK.type, name="type", curie=BIOLINK.curie('type'),
                      model_uri=BIOLINK.type, domain=NamedThing, range=Optional[str], mappings = [RDF.type])

slots.id = Slot(uri=BIOLINK.id, name="id", curie=BIOLINK.curie('id'),
                      model_uri=BIOLINK.id, domain=NamedThing, range=Union[str, NamedThingId])

slots.iri = Slot(uri=BIOLINK.iri, name="iri", curie=BIOLINK.curie('iri'),
                      model_uri=BIOLINK.iri, domain=NamedThing, range=Optional[Union[str, IriType]])

slots.name = Slot(uri=RDFS.label, name="name", curie=RDFS.curie('label'),
                      model_uri=BIOLINK.name, domain=NamedThing, range=Union[str, LabelType])

slots.synonym = Slot(uri=BIOLINK.synonym, name="synonym", curie=BIOLINK.curie('synonym'),
                      model_uri=BIOLINK.synonym, domain=NamedThing, range=List[Union[str, LabelType]])

slots.category = Slot(uri=RDF.type, name="category", curie=RDF.curie('type'),
                      model_uri=BIOLINK.category, domain=NamedThing, range=List[Union[str, IriType]])

slots.full_name = Slot(uri=BIOLINK.full_name, name="full name", curie=BIOLINK.curie('full_name'),
                      model_uri=BIOLINK.full_name, domain=NamedThing, range=Optional[Union[str, LabelType]])

slots.description = Slot(uri=DCTERMS.description, name="description", curie=DCTERMS.curie('description'),
                      model_uri=BIOLINK.description, domain=NamedThing, range=Optional[Union[str, NarrativeText]])

slots.systematic_synonym = Slot(uri=BIOLINK.systematic_synonym, name="systematic synonym", curie=BIOLINK.curie('systematic_synonym'),
                      model_uri=BIOLINK.systematic_synonym, domain=NamedThing, range=List[Union[str, LabelType]])

slots.association_slot = Slot(uri=BIOLINK.association_slot, name="association slot", curie=BIOLINK.curie('association_slot'),
                      model_uri=BIOLINK.association_slot, domain=Association, range=Optional[str])

slots.association_id = Slot(uri=BIOLINK.id, name="association_id", curie=BIOLINK.curie('id'),
                      model_uri=BIOLINK.association_id, domain=Association, range=Union[str, AssociationId])

slots.subject = Slot(uri=RDF.subject, name="subject", curie=RDF.curie('subject'),
                      model_uri=BIOLINK.subject, domain=Association, range=Union[str, NamedThingId], mappings = [OWL.annotatedSource, OBAN.association_has_subject])

slots.object = Slot(uri=RDF.object, name="object", curie=RDF.curie('object'),
                      model_uri=BIOLINK.object, domain=Association, range=Union[str, NamedThingId], mappings = [OWL.annotatedTarget, OBAN.association_has_object])

slots.edge_label = Slot(uri=BIOLINK.edge_label, name="edge label", curie=BIOLINK.curie('edge_label'),
                      model_uri=BIOLINK.edge_label, domain=Association, range=Union[str, LabelType])

slots.relation = Slot(uri=RDF.predicate, name="relation", curie=RDF.curie('predicate'),
                      model_uri=BIOLINK.relation, domain=Association, range=Union[str, URIorCURIE], mappings = [OWL.annotatedProperty, OBAN.association_has_predicate])

slots.negated = Slot(uri=BIOLINK.negated, name="negated", curie=BIOLINK.curie('negated'),
                      model_uri=BIOLINK.negated, domain=Association, range=Optional[Bool])

slots.has_confidence_level = Slot(uri=BIOLINK.has_confidence_level, name="has confidence level", curie=BIOLINK.curie('has_confidence_level'),
                      model_uri=BIOLINK.has_confidence_level, domain=Association, range=Optional[Union[str, ConfidenceLevelId]])

slots.has_evidence = Slot(uri=BIOLINK.has_evidence, name="has evidence", curie=BIOLINK.curie('has_evidence'),
                      model_uri=BIOLINK.has_evidence, domain=Association, range=Optional[Union[str, EvidenceTypeId]], mappings = [RO["0002558"]])

slots.provided_by = Slot(uri=PAV.providedBy, name="provided by", curie=PAV.curie('providedBy'),
                      model_uri=BIOLINK.provided_by, domain=Association, range=List[Union[str, ProviderId]])

slots.association_type = Slot(uri=BIOLINK.association_type, name="association type", curie=BIOLINK.curie('association_type'),
                      model_uri=BIOLINK.association_type, domain=Association, range=Optional[Union[str, OntologyClassId]], mappings = [RDF.type])

slots.chi_squared_statistic = Slot(uri=STATO['0000030'], name="chi squared statistic", curie=STATO.curie('0000030'),
                      model_uri=BIOLINK.chi_squared_statistic, domain=Association, range=Optional[float])

slots.p_value = Slot(uri=OBI['0000175'], name="p value", curie=OBI.curie('0000175'),
                      model_uri=BIOLINK.p_value, domain=Association, range=Optional[float])

slots.creation_date = Slot(uri=BIOLINK.creation_date, name="creation date", curie=BIOLINK.curie('creation_date'),
                      model_uri=BIOLINK.creation_date, domain=NamedThing, range=Optional[Union[str, XSDDate]], mappings = [DCTERMS.created])

slots.has_receptor = Slot(uri=BIOLINK.has_receptor, name="has receptor", curie=BIOLINK.curie('has_receptor'),
                      model_uri=BIOLINK.has_receptor, domain=ExposureEvent, range=Optional[Union[str, OrganismalEntityId]], mappings = [EXO["0000001"]])

slots.has_stressor = Slot(uri=BIOLINK.has_stressor, name="has stressor", curie=BIOLINK.curie('has_stressor'),
                      model_uri=BIOLINK.has_stressor, domain=ExposureEvent, range=Optional[str], mappings = [EXO["0000000"]])

slots.has_route = Slot(uri=BIOLINK.has_route, name="has route", curie=BIOLINK.curie('has_route'),
                      model_uri=BIOLINK.has_route, domain=ExposureEvent, range=Optional[str], mappings = [EXO["0000055"]])

slots.update_date = Slot(uri=BIOLINK.update_date, name="update date", curie=BIOLINK.curie('update_date'),
                      model_uri=BIOLINK.update_date, domain=NamedThing, range=Optional[Union[str, XSDDate]])

slots.in_taxon = Slot(uri=BIOLINK.in_taxon, name="in taxon", curie=BIOLINK.curie('in_taxon'),
                      model_uri=BIOLINK.in_taxon, domain=None, range=List[Union[str, OrganismTaxonId]], mappings = [RO["0002162"], WD.P703])

slots.latitude = Slot(uri=BIOLINK.latitude, name="latitude", curie=BIOLINK.curie('latitude'),
                      model_uri=BIOLINK.latitude, domain=NamedThing, range=Optional[float], mappings = [WGS.lat])

slots.longitude = Slot(uri=BIOLINK.longitude, name="longitude", curie=BIOLINK.curie('longitude'),
                      model_uri=BIOLINK.longitude, domain=NamedThing, range=Optional[float], mappings = [WGS.long])

slots.has_chemical_formula = Slot(uri=BIOLINK.has_chemical_formula, name="has chemical formula", curie=BIOLINK.curie('has_chemical_formula'),
                      model_uri=BIOLINK.has_chemical_formula, domain=NamedThing, range=Optional[str], mappings = [WD.P274])

slots.aggregate_statistic = Slot(uri=BIOLINK.aggregate_statistic, name="aggregate statistic", curie=BIOLINK.curie('aggregate_statistic'),
                      model_uri=BIOLINK.aggregate_statistic, domain=NamedThing, range=Optional[str])

slots.has_count = Slot(uri=BIOLINK.has_count, name="has count", curie=BIOLINK.curie('has_count'),
                      model_uri=BIOLINK.has_count, domain=NamedThing, range=Optional[int])

slots.has_total = Slot(uri=BIOLINK.has_total, name="has total", curie=BIOLINK.curie('has_total'),
                      model_uri=BIOLINK.has_total, domain=NamedThing, range=Optional[int])

slots.has_quotient = Slot(uri=BIOLINK.has_quotient, name="has quotient", curie=BIOLINK.curie('has_quotient'),
                      model_uri=BIOLINK.has_quotient, domain=NamedThing, range=Optional[float])

slots.has_percentage = Slot(uri=BIOLINK.has_percentage, name="has percentage", curie=BIOLINK.curie('has_percentage'),
                      model_uri=BIOLINK.has_percentage, domain=NamedThing, range=Optional[float])

slots.timepoint = Slot(uri=BIOLINK.timepoint, name="timepoint", curie=BIOLINK.curie('timepoint'),
                      model_uri=BIOLINK.timepoint, domain=NamedThing, range=Optional[Union[str, TimeType]])

slots.stage_qualifier = Slot(uri=BIOLINK.stage_qualifier, name="stage qualifier", curie=BIOLINK.curie('stage_qualifier'),
                      model_uri=BIOLINK.stage_qualifier, domain=Association, range=Optional[Union[str, LifeStageId]])

slots.quantifier_qualifier = Slot(uri=BIOLINK.quantifier_qualifier, name="quantifier qualifier", curie=BIOLINK.curie('quantifier_qualifier'),
                      model_uri=BIOLINK.quantifier_qualifier, domain=Association, range=Optional[Union[str, OntologyClassId]])

slots.qualifiers = Slot(uri=BIOLINK.qualifiers, name="qualifiers", curie=BIOLINK.curie('qualifiers'),
                      model_uri=BIOLINK.qualifiers, domain=Association, range=List[Union[str, OntologyClassId]])

slots.frequency_qualifier = Slot(uri=BIOLINK.frequency_qualifier, name="frequency qualifier", curie=BIOLINK.curie('frequency_qualifier'),
                      model_uri=BIOLINK.frequency_qualifier, domain=Association, range=Optional[Union[str, FrequencyValueId]])

slots.severity_qualifier = Slot(uri=BIOLINK.severity_qualifier, name="severity qualifier", curie=BIOLINK.curie('severity_qualifier'),
                      model_uri=BIOLINK.severity_qualifier, domain=Association, range=Optional[Union[str, SeverityValueId]])

slots.sex_qualifier = Slot(uri=BIOLINK.sex_qualifier, name="sex qualifier", curie=BIOLINK.curie('sex_qualifier'),
                      model_uri=BIOLINK.sex_qualifier, domain=Association, range=Optional[Union[str, BiologicalSexId]])

slots.onset_qualifier = Slot(uri=BIOLINK.onset_qualifier, name="onset qualifier", curie=BIOLINK.curie('onset_qualifier'),
                      model_uri=BIOLINK.onset_qualifier, domain=Association, range=Optional[Union[str, OnsetId]])

slots.clinical_modifier_qualifier = Slot(uri=BIOLINK.clinical_modifier_qualifier, name="clinical modifier qualifier", curie=BIOLINK.curie('clinical_modifier_qualifier'),
                      model_uri=BIOLINK.clinical_modifier_qualifier, domain=Association, range=Optional[Union[str, ClinicalModifierId]])

slots.sequence_variant_qualifier = Slot(uri=BIOLINK.sequence_variant_qualifier, name="sequence variant qualifier", curie=BIOLINK.curie('sequence_variant_qualifier'),
                      model_uri=BIOLINK.sequence_variant_qualifier, domain=Association, range=Optional[Union[str, SequenceVariantId]])

slots.publications = Slot(uri=BIOLINK.publications, name="publications", curie=BIOLINK.curie('publications'),
                      model_uri=BIOLINK.publications, domain=Association, range=List[Union[str, PublicationId]])

slots.change_is_catalyzed_by = Slot(uri=BIOLINK.change_is_catalyzed_by, name="change is catalyzed by", curie=BIOLINK.curie('change_is_catalyzed_by'),
                      model_uri=BIOLINK.change_is_catalyzed_by, domain=Association, range=List[Union[str, MacromolecularMachineId]])

slots.has_biological_sequence = Slot(uri=BIOLINK.has_biological_sequence, name="has biological sequence", curie=BIOLINK.curie('has_biological_sequence'),
                      model_uri=BIOLINK.has_biological_sequence, domain=NamedThing, range=Optional[Union[str, BiologicalSequence]])

slots.has_molecular_consequence = Slot(uri=BIOLINK.has_molecular_consequence, name="has molecular consequence", curie=BIOLINK.curie('has_molecular_consequence'),
                      model_uri=BIOLINK.has_molecular_consequence, domain=NamedThing, range=List[Union[str, OntologyClassId]])

slots.has_drug = Slot(uri=BIOLINK.has_drug, name="has drug", curie=BIOLINK.curie('has_drug'),
                      model_uri=BIOLINK.has_drug, domain=NamedThing, range=Optional[Union[str, DrugId]])

slots.has_gene = Slot(uri=BIOLINK.has_gene, name="has gene", curie=BIOLINK.curie('has_gene'),
                      model_uri=BIOLINK.has_gene, domain=NamedThing, range=Optional[Union[str, GeneId]])

slots.has_zygosity = Slot(uri=BIOLINK.has_zygosity, name="has zygosity", curie=BIOLINK.curie('has_zygosity'),
                      model_uri=BIOLINK.has_zygosity, domain=NamedThing, range=Optional[Union[str, ZygosityId]])

slots.filler = Slot(uri=BIOLINK.filler, name="filler", curie=BIOLINK.curie('filler'),
                      model_uri=BIOLINK.filler, domain=NamedThing, range=Optional[Union[str, NamedThingId]])

slots.phase = Slot(uri=BIOLINK.phase, name="phase", curie=BIOLINK.curie('phase'),
                      model_uri=BIOLINK.phase, domain=NamedThing, range=Optional[str])

slots.genome_build = Slot(uri=BIOLINK.genome_build, name="genome build", curie=BIOLINK.curie('genome_build'),
                      model_uri=BIOLINK.genome_build, domain=NamedThing, range=Optional[str])

slots.interbase_coordinate = Slot(uri=BIOLINK.interbase_coordinate, name="interbase coordinate", curie=BIOLINK.curie('interbase_coordinate'),
                      model_uri=BIOLINK.interbase_coordinate, domain=NamedThing, range=Optional[str])

slots.start_interbase_coordinate = Slot(uri=BIOLINK.start_interbase_coordinate, name="start interbase coordinate", curie=BIOLINK.curie('start_interbase_coordinate'),
                      model_uri=BIOLINK.start_interbase_coordinate, domain=NamedThing, range=Optional[str])

slots.end_interbase_coordinate = Slot(uri=BIOLINK.end_interbase_coordinate, name="end interbase coordinate", curie=BIOLINK.curie('end_interbase_coordinate'),
                      model_uri=BIOLINK.end_interbase_coordinate, domain=NamedThing, range=Optional[str])

slots.has_attribute = Slot(uri=BIOLINK.has_attribute, name="has attribute", curie=BIOLINK.curie('has_attribute'),
                      model_uri=BIOLINK.has_attribute, domain=None, range=List[Union[str, AttributeId]], mappings = [SIO["000008"], RO["0000053"]])

slots.has_attribute_type = Slot(uri=BIOLINK.has_attribute_type, name="has attribute type", curie=BIOLINK.curie('has_attribute_type'),
                      model_uri=BIOLINK.has_attribute_type, domain=Attribute, range=Optional[Union[str, OntologyClassId]])

slots.has_qualitative_value = Slot(uri=BIOLINK.has_qualitative_value, name="has qualitative value", curie=BIOLINK.curie('has_qualitative_value'),
                      model_uri=BIOLINK.has_qualitative_value, domain=Attribute, range=Optional[Union[str, NamedThingId]])

slots.has_quantitative_value = Slot(uri=BIOLINK.has_quantitative_value, name="has quantitative value", curie=BIOLINK.curie('has_quantitative_value'),
                      model_uri=BIOLINK.has_quantitative_value, domain=Attribute, range=List[Union[dict, "QuantityValue"]], mappings = [QUD.quantityValue])

slots.has_numeric_value = Slot(uri=BIOLINK.has_numeric_value, name="has numeric value", curie=BIOLINK.curie('has_numeric_value'),
                      model_uri=BIOLINK.has_numeric_value, domain=QuantityValue, range=Optional[float], mappings = [QUD.quantityValue])

slots.has_unit = Slot(uri=BIOLINK.has_unit, name="has unit", curie=BIOLINK.curie('has_unit'),
                      model_uri=BIOLINK.has_unit, domain=QuantityValue, range=Optional[Union[str, Unit]], mappings = [QUD.unit])

slots.interacting_molecules_category = Slot(uri=BIOLINK.interacting_molecules_category, name="interacting molecules category", curie=BIOLINK.curie('interacting_molecules_category'),
                      model_uri=BIOLINK.interacting_molecules_category, domain=None, range=Optional[Union[str, OntologyClassId]])

slots.macromolecular_machine_name = Slot(uri=BIOLINK.name, name="macromolecular machine_name", curie=BIOLINK.curie('name'),
                      model_uri=BIOLINK.macromolecular_machine_name, domain=MacromolecularMachine, range=Union[str, SymbolType])

slots.sequence_variant_has_gene = Slot(uri=BIOLINK.has_gene, name="sequence variant_has gene", curie=BIOLINK.curie('has_gene'),
                      model_uri=BIOLINK.sequence_variant_has_gene, domain=SequenceVariant, range=List[Union[str, GeneId]])

slots.sequence_variant_has_biological_sequence = Slot(uri=BIOLINK.has_biological_sequence, name="sequence variant_has biological sequence", curie=BIOLINK.curie('has_biological_sequence'),
                      model_uri=BIOLINK.sequence_variant_has_biological_sequence, domain=SequenceVariant, range=Optional[Union[str, BiologicalSequence]])

slots.sequence_variant_id = Slot(uri=BIOLINK.id, name="sequence variant_id", curie=BIOLINK.curie('id'),
                      model_uri=BIOLINK.sequence_variant_id, domain=SequenceVariant, range=Union[str, SequenceVariantId])

slots.drug_exposure_has_drug = Slot(uri=BIOLINK.has_drug, name="drug exposure_has drug", curie=BIOLINK.curie('has_drug'),
                      model_uri=BIOLINK.drug_exposure_has_drug, domain=DrugExposure, range=List[Union[str, ChemicalSubstanceId]])

slots.treatment_has_part = Slot(uri=BIOLINK.has_part, name="treatment_has part", curie=BIOLINK.curie('has_part'),
                      model_uri=BIOLINK.treatment_has_part, domain=Treatment, range=List[Union[str, DrugExposureId]])

slots.genotype_to_genotype_part_association_relation = Slot(uri=BIOLINK.relation, name="genotype to genotype part association_relation", curie=BIOLINK.curie('relation'),
                      model_uri=BIOLINK.genotype_to_genotype_part_association_relation, domain=GenotypeToGenotypePartAssociation, range=Union[str, URIorCURIE])

slots.genotype_to_genotype_part_association_subject = Slot(uri=BIOLINK.subject, name="genotype to genotype part association_subject", curie=BIOLINK.curie('subject'),
                      model_uri=BIOLINK.genotype_to_genotype_part_association_subject, domain=GenotypeToGenotypePartAssociation, range=Union[str, GenotypeId])

slots.genotype_to_genotype_part_association_object = Slot(uri=BIOLINK.object, name="genotype to genotype part association_object", curie=BIOLINK.curie('object'),
                      model_uri=BIOLINK.genotype_to_genotype_part_association_object, domain=GenotypeToGenotypePartAssociation, range=Union[str, GenotypeId])

slots.genotype_to_gene_association_relation = Slot(uri=BIOLINK.relation, name="genotype to gene association_relation", curie=BIOLINK.curie('relation'),
                      model_uri=BIOLINK.genotype_to_gene_association_relation, domain=GenotypeToGeneAssociation, range=Union[str, URIorCURIE])

slots.genotype_to_gene_association_subject = Slot(uri=BIOLINK.subject, name="genotype to gene association_subject", curie=BIOLINK.curie('subject'),
                      model_uri=BIOLINK.genotype_to_gene_association_subject, domain=GenotypeToGeneAssociation, range=Union[str, GenotypeId])

slots.genotype_to_gene_association_object = Slot(uri=BIOLINK.object, name="genotype to gene association_object", curie=BIOLINK.curie('object'),
                      model_uri=BIOLINK.genotype_to_gene_association_object, domain=GenotypeToGeneAssociation, range=Union[str, GeneId])

slots.genotype_to_variant_association_relation = Slot(uri=BIOLINK.relation, name="genotype to variant association_relation", curie=BIOLINK.curie('relation'),
                      model_uri=BIOLINK.genotype_to_variant_association_relation, domain=GenotypeToVariantAssociation, range=Union[str, URIorCURIE])

slots.genotype_to_variant_association_subject = Slot(uri=BIOLINK.subject, name="genotype to variant association_subject", curie=BIOLINK.curie('subject'),
                      model_uri=BIOLINK.genotype_to_variant_association_subject, domain=GenotypeToVariantAssociation, range=Union[str, GenotypeId])

slots.genotype_to_variant_association_object = Slot(uri=BIOLINK.object, name="genotype to variant association_object", curie=BIOLINK.curie('object'),
                      model_uri=BIOLINK.genotype_to_variant_association_object, domain=GenotypeToVariantAssociation, range=Union[str, SequenceVariantId])

slots.gene_to_gene_association_subject = Slot(uri=BIOLINK.subject, name="gene to gene association_subject", curie=BIOLINK.curie('subject'),
                      model_uri=BIOLINK.gene_to_gene_association_subject, domain=GeneToGeneAssociation, range=Union[str, GeneOrGeneProductId])

slots.gene_to_gene_association_object = Slot(uri=BIOLINK.object, name="gene to gene association_object", curie=BIOLINK.curie('object'),
                      model_uri=BIOLINK.gene_to_gene_association_object, domain=GeneToGeneAssociation, range=Union[str, GeneOrGeneProductId])

slots.gene_to_gene_homology_association_relation = Slot(uri=BIOLINK.relation, name="gene to gene homology association_relation", curie=BIOLINK.curie('relation'),
                      model_uri=BIOLINK.gene_to_gene_homology_association_relation, domain=GeneToGeneHomologyAssociation, range=Union[str, URIorCURIE])

slots.pairwise_interaction_association_subject = Slot(uri=BIOLINK.subject, name="pairwise interaction association_subject", curie=BIOLINK.curie('subject'),
                      model_uri=BIOLINK.pairwise_interaction_association_subject, domain=None, range=Union[str, MolecularEntityId])

slots.pairwise_interaction_association_id = Slot(uri=BIOLINK.id, name="pairwise interaction association_id", curie=BIOLINK.curie('id'),
                      model_uri=BIOLINK.pairwise_interaction_association_id, domain=None, range=Union[str, PairwiseInteractionAssociationId])

slots.pairwise_interaction_association_relation = Slot(uri=BIOLINK.relation, name="pairwise interaction association_relation", curie=BIOLINK.curie('relation'),
                      model_uri=BIOLINK.pairwise_interaction_association_relation, domain=None, range=Union[str, URIorCURIE])

slots.pairwise_interaction_association_object = Slot(uri=BIOLINK.object, name="pairwise interaction association_object", curie=BIOLINK.curie('object'),
                      model_uri=BIOLINK.pairwise_interaction_association_object, domain=None, range=Union[str, MolecularEntityId])

slots.pairwise_interaction_association_interacting_molecules_category = Slot(uri=BIOLINK.interacting_molecules_category, name="pairwise interaction association_interacting molecules category", curie=BIOLINK.curie('interacting_molecules_category'),
                      model_uri=BIOLINK.pairwise_interaction_association_interacting_molecules_category, domain=None, range=Optional[Union[str, OntologyClassId]])

slots.pairwise_gene_to_gene_interaction_relation = Slot(uri=BIOLINK.relation, name="pairwise gene to gene interaction_relation", curie=BIOLINK.curie('relation'),
                      model_uri=BIOLINK.pairwise_gene_to_gene_interaction_relation, domain=PairwiseGeneToGeneInteraction, range=Union[str, URIorCURIE])

slots.cell_line_to_thing_association_subject = Slot(uri=BIOLINK.subject, name="cell line to thing association_subject", curie=BIOLINK.curie('subject'),
                      model_uri=BIOLINK.cell_line_to_thing_association_subject, domain=CellLineToThingAssociation, range=Union[str, CellLineId])

slots.cell_line_to_disease_or_phenotypic_feature_association_subject = Slot(uri=BIOLINK.subject, name="cell line to disease or phenotypic feature association_subject", curie=BIOLINK.curie('subject'),
                      model_uri=BIOLINK.cell_line_to_disease_or_phenotypic_feature_association_subject, domain=CellLineToDiseaseOrPhenotypicFeatureAssociation, range=Union[str, DiseaseOrPhenotypicFeatureId])

slots.thing_to_disease_or_phenotypic_feature_association_object = Slot(uri=BIOLINK.object, name="thing to disease or phenotypic feature association_object", curie=BIOLINK.curie('object'),
                      model_uri=BIOLINK.thing_to_disease_or_phenotypic_feature_association_object, domain=ThingToDiseaseOrPhenotypicFeatureAssociation, range=Union[str, DiseaseOrPhenotypicFeatureId])

slots.chemical_to_thing_association_subject = Slot(uri=BIOLINK.subject, name="chemical to thing association_subject", curie=BIOLINK.curie('subject'),
                      model_uri=BIOLINK.chemical_to_thing_association_subject, domain=ChemicalToThingAssociation, range=Union[str, ChemicalSubstanceId])

slots.case_to_thing_association_subject = Slot(uri=BIOLINK.subject, name="case to thing association_subject", curie=BIOLINK.curie('subject'),
                      model_uri=BIOLINK.case_to_thing_association_subject, domain=CaseToThingAssociation, range=Union[str, CaseId])

slots.chemical_to_chemical_association_object = Slot(uri=BIOLINK.object, name="chemical to chemical association_object", curie=BIOLINK.curie('object'),
                      model_uri=BIOLINK.chemical_to_chemical_association_object, domain=ChemicalToChemicalAssociation, range=Union[str, ChemicalSubstanceId])

slots.chemical_to_chemical_derivation_association_subject = Slot(uri=BIOLINK.subject, name="chemical to chemical derivation association_subject", curie=BIOLINK.curie('subject'),
                      model_uri=BIOLINK.chemical_to_chemical_derivation_association_subject, domain=ChemicalToChemicalDerivationAssociation, range=Union[str, ChemicalSubstanceId])

slots.chemical_to_chemical_derivation_association_object = Slot(uri=BIOLINK.object, name="chemical to chemical derivation association_object", curie=BIOLINK.curie('object'),
                      model_uri=BIOLINK.chemical_to_chemical_derivation_association_object, domain=ChemicalToChemicalDerivationAssociation, range=Union[str, ChemicalSubstanceId])

slots.chemical_to_chemical_derivation_association_relation = Slot(uri=BIOLINK.relation, name="chemical to chemical derivation association_relation", curie=BIOLINK.curie('relation'),
                      model_uri=BIOLINK.chemical_to_chemical_derivation_association_relation, domain=ChemicalToChemicalDerivationAssociation, range=Union[str, URIorCURIE])

slots.chemical_to_chemical_derivation_association_change_is_catalyzed_by = Slot(uri=BIOLINK.change_is_catalyzed_by, name="chemical to chemical derivation association_change is catalyzed by", curie=BIOLINK.curie('change_is_catalyzed_by'),
                      model_uri=BIOLINK.chemical_to_chemical_derivation_association_change_is_catalyzed_by, domain=ChemicalToChemicalDerivationAssociation, range=List[Union[str, MacromolecularMachineId]])

slots.chemical_to_disease_or_phenotypic_feature_association_object = Slot(uri=BIOLINK.object, name="chemical to disease or phenotypic feature association_object", curie=BIOLINK.curie('object'),
                      model_uri=BIOLINK.chemical_to_disease_or_phenotypic_feature_association_object, domain=ChemicalToDiseaseOrPhenotypicFeatureAssociation, range=Union[str, DiseaseOrPhenotypicFeatureId])

slots.chemical_to_pathway_association_object = Slot(uri=BIOLINK.object, name="chemical to pathway association_object", curie=BIOLINK.curie('object'),
                      model_uri=BIOLINK.chemical_to_pathway_association_object, domain=ChemicalToPathwayAssociation, range=Union[str, PathwayId])

slots.chemical_to_gene_association_object = Slot(uri=BIOLINK.object, name="chemical to gene association_object", curie=BIOLINK.curie('object'),
                      model_uri=BIOLINK.chemical_to_gene_association_object, domain=ChemicalToGeneAssociation, range=Union[str, GeneOrGeneProductId])

slots.material_sample_to_thing_association_subject = Slot(uri=BIOLINK.subject, name="material sample to thing association_subject", curie=BIOLINK.curie('subject'),
                      model_uri=BIOLINK.material_sample_to_thing_association_subject, domain=MaterialSampleToThingAssociation, range=Union[str, MaterialSampleId])

slots.material_sample_derivation_association_subject = Slot(uri=BIOLINK.subject, name="material sample derivation association_subject", curie=BIOLINK.curie('subject'),
                      model_uri=BIOLINK.material_sample_derivation_association_subject, domain=MaterialSampleDerivationAssociation, range=Union[str, MaterialSampleId])

slots.material_sample_derivation_association_object = Slot(uri=BIOLINK.object, name="material sample derivation association_object", curie=BIOLINK.curie('object'),
                      model_uri=BIOLINK.material_sample_derivation_association_object, domain=MaterialSampleDerivationAssociation, range=Union[str, NamedThingId])

slots.material_sample_derivation_association_relation = Slot(uri=BIOLINK.relation, name="material sample derivation association_relation", curie=BIOLINK.curie('relation'),
                      model_uri=BIOLINK.material_sample_derivation_association_relation, domain=MaterialSampleDerivationAssociation, range=Union[str, URIorCURIE])

slots.disease_to_thing_association_subject = Slot(uri=BIOLINK.subject, name="disease to thing association_subject", curie=BIOLINK.curie('subject'),
                      model_uri=BIOLINK.disease_to_thing_association_subject, domain=DiseaseToThingAssociation, range=Union[str, DiseaseId])

slots.disease_to_exposure_association_subject = Slot(uri=BIOLINK.subject, name="disease to exposure association_subject", curie=BIOLINK.curie('subject'),
                      model_uri=BIOLINK.disease_to_exposure_association_subject, domain=DiseaseToExposureAssociation, range=Union[str, DiseaseId])

slots.disease_to_exposure_association_object = Slot(uri=BIOLINK.object, name="disease to exposure association_object", curie=BIOLINK.curie('object'),
                      model_uri=BIOLINK.disease_to_exposure_association_object, domain=DiseaseToExposureAssociation, range=Union[str, ExposureEventId])

slots.entity_to_phenotypic_feature_association_description = Slot(uri=BIOLINK.description, name="entity to phenotypic feature association_description", curie=BIOLINK.curie('description'),
                      model_uri=BIOLINK.entity_to_phenotypic_feature_association_description, domain=EntityToPhenotypicFeatureAssociation, range=Optional[Union[str, NarrativeText]])

slots.entity_to_phenotypic_feature_association_object = Slot(uri=BIOLINK.object, name="entity to phenotypic feature association_object", curie=BIOLINK.curie('object'),
                      model_uri=BIOLINK.entity_to_phenotypic_feature_association_object, domain=EntityToPhenotypicFeatureAssociation, range=Union[str, PhenotypicFeatureId])

slots.entity_to_disease_association_object = Slot(uri=BIOLINK.object, name="entity to disease association_object", curie=BIOLINK.curie('object'),
                      model_uri=BIOLINK.entity_to_disease_association_object, domain=None, range=Union[str, DiseaseId])

slots.disease_or_phenotypic_feature_association_to_thing_association_subject = Slot(uri=BIOLINK.subject, name="disease or phenotypic feature association to thing association_subject", curie=BIOLINK.curie('subject'),
                      model_uri=BIOLINK.disease_or_phenotypic_feature_association_to_thing_association_subject, domain=DiseaseOrPhenotypicFeatureAssociationToThingAssociation, range=Union[str, DiseaseOrPhenotypicFeatureId])

slots.disease_or_phenotypic_feature_association_to_location_association_object = Slot(uri=BIOLINK.object, name="disease or phenotypic feature association to location association_object", curie=BIOLINK.curie('object'),
                      model_uri=BIOLINK.disease_or_phenotypic_feature_association_to_location_association_object, domain=DiseaseOrPhenotypicFeatureAssociationToLocationAssociation, range=Union[str, AnatomicalEntityId])

slots.genotype_to_phenotypic_feature_association_relation = Slot(uri=BIOLINK.relation, name="genotype to phenotypic feature association_relation", curie=BIOLINK.curie('relation'),
                      model_uri=BIOLINK.genotype_to_phenotypic_feature_association_relation, domain=GenotypeToPhenotypicFeatureAssociation, range=Union[str, URIorCURIE])

slots.genotype_to_phenotypic_feature_association_subject = Slot(uri=BIOLINK.subject, name="genotype to phenotypic feature association_subject", curie=BIOLINK.curie('subject'),
                      model_uri=BIOLINK.genotype_to_phenotypic_feature_association_subject, domain=GenotypeToPhenotypicFeatureAssociation, range=Union[str, GenotypeId])

slots.genotype_to_thing_association_subject = Slot(uri=BIOLINK.subject, name="genotype to thing association_subject", curie=BIOLINK.curie('subject'),
                      model_uri=BIOLINK.genotype_to_thing_association_subject, domain=GenotypeToThingAssociation, range=Union[str, GenotypeId])

slots.exposure_event_to_phenotypic_feature_association_subject = Slot(uri=BIOLINK.subject, name="exposure event to phenotypic feature association_subject", curie=BIOLINK.curie('subject'),
                      model_uri=BIOLINK.exposure_event_to_phenotypic_feature_association_subject, domain=ExposureEventToPhenotypicFeatureAssociation, range=Union[str, ExposureEventId])

slots.gene_to_thing_association_subject = Slot(uri=BIOLINK.subject, name="gene to thing association_subject", curie=BIOLINK.curie('subject'),
                      model_uri=BIOLINK.gene_to_thing_association_subject, domain=GeneToThingAssociation, range=Union[str, GeneOrGeneProductId])

slots.variant_to_thing_association_subject = Slot(uri=BIOLINK.subject, name="variant to thing association_subject", curie=BIOLINK.curie('subject'),
                      model_uri=BIOLINK.variant_to_thing_association_subject, domain=None, range=Union[str, SequenceVariantId])

slots.gene_to_phenotypic_feature_association_subject = Slot(uri=BIOLINK.subject, name="gene to phenotypic feature association_subject", curie=BIOLINK.curie('subject'),
                      model_uri=BIOLINK.gene_to_phenotypic_feature_association_subject, domain=GeneToPhenotypicFeatureAssociation, range=Union[str, GeneOrGeneProductId])

slots.gene_to_disease_association_subject = Slot(uri=BIOLINK.subject, name="gene to disease association_subject", curie=BIOLINK.curie('subject'),
                      model_uri=BIOLINK.gene_to_disease_association_subject, domain=GeneToDiseaseAssociation, range=Union[str, GeneOrGeneProductId])

slots.variant_to_population_association_subject = Slot(uri=BIOLINK.subject, name="variant to population association_subject", curie=BIOLINK.curie('subject'),
                      model_uri=BIOLINK.variant_to_population_association_subject, domain=VariantToPopulationAssociation, range=Union[str, SequenceVariantId])

slots.variant_to_population_association_object = Slot(uri=BIOLINK.object, name="variant to population association_object", curie=BIOLINK.curie('object'),
                      model_uri=BIOLINK.variant_to_population_association_object, domain=VariantToPopulationAssociation, range=Union[str, PopulationOfIndividualOrganismsId])

slots.variant_to_population_association_has_quotient = Slot(uri=BIOLINK.has_quotient, name="variant to population association_has quotient", curie=BIOLINK.curie('has_quotient'),
                      model_uri=BIOLINK.variant_to_population_association_has_quotient, domain=VariantToPopulationAssociation, range=Optional[float])

slots.variant_to_population_association_has_count = Slot(uri=BIOLINK.has_count, name="variant to population association_has count", curie=BIOLINK.curie('has_count'),
                      model_uri=BIOLINK.variant_to_population_association_has_count, domain=VariantToPopulationAssociation, range=Optional[int])

slots.variant_to_population_association_has_total = Slot(uri=BIOLINK.has_total, name="variant to population association_has total", curie=BIOLINK.curie('has_total'),
                      model_uri=BIOLINK.variant_to_population_association_has_total, domain=VariantToPopulationAssociation, range=Optional[int])

slots.population_to_population_association_subject = Slot(uri=BIOLINK.subject, name="population to population association_subject", curie=BIOLINK.curie('subject'),
                      model_uri=BIOLINK.population_to_population_association_subject, domain=PopulationToPopulationAssociation, range=Union[str, PopulationOfIndividualOrganismsId])

slots.population_to_population_association_object = Slot(uri=BIOLINK.object, name="population to population association_object", curie=BIOLINK.curie('object'),
                      model_uri=BIOLINK.population_to_population_association_object, domain=PopulationToPopulationAssociation, range=Union[str, PopulationOfIndividualOrganismsId])

slots.population_to_population_association_relation = Slot(uri=BIOLINK.relation, name="population to population association_relation", curie=BIOLINK.curie('relation'),
                      model_uri=BIOLINK.population_to_population_association_relation, domain=PopulationToPopulationAssociation, range=Union[str, URIorCURIE])

slots.variant_to_phenotypic_feature_association_subject = Slot(uri=BIOLINK.subject, name="variant to phenotypic feature association_subject", curie=BIOLINK.curie('subject'),
                      model_uri=BIOLINK.variant_to_phenotypic_feature_association_subject, domain=VariantToPhenotypicFeatureAssociation, range=Union[str, SequenceVariantId])

slots.variant_to_disease_association_subject = Slot(uri=BIOLINK.subject, name="variant to disease association_subject", curie=BIOLINK.curie('subject'),
                      model_uri=BIOLINK.variant_to_disease_association_subject, domain=VariantToDiseaseAssociation, range=Union[str, NamedThingId])

slots.variant_to_disease_association_relation = Slot(uri=BIOLINK.relation, name="variant to disease association_relation", curie=BIOLINK.curie('relation'),
                      model_uri=BIOLINK.variant_to_disease_association_relation, domain=VariantToDiseaseAssociation, range=Union[str, URIorCURIE])

slots.variant_to_disease_association_object = Slot(uri=BIOLINK.object, name="variant to disease association_object", curie=BIOLINK.curie('object'),
                      model_uri=BIOLINK.variant_to_disease_association_object, domain=VariantToDiseaseAssociation, range=Union[str, NamedThingId])

slots.model_to_disease_mixin_subject = Slot(uri=BIOLINK.subject, name="model to disease mixin_subject", curie=BIOLINK.curie('subject'),
                      model_uri=BIOLINK.model_to_disease_mixin_subject, domain=None, range=Union[str, NamedThingId])

slots.model_to_disease_mixin_relation = Slot(uri=BIOLINK.relation, name="model to disease mixin_relation", curie=BIOLINK.curie('relation'),
                      model_uri=BIOLINK.model_to_disease_mixin_relation, domain=None, range=Union[str, URIorCURIE])

slots.gene_as_a_model_of_disease_association_subject = Slot(uri=BIOLINK.subject, name="gene as a model of disease association_subject", curie=BIOLINK.curie('subject'),
                      model_uri=BIOLINK.gene_as_a_model_of_disease_association_subject, domain=GeneAsAModelOfDiseaseAssociation, range=Union[str, GeneOrGeneProductId])

slots.gene_has_variant_that_contributes_to_disease_association_subject = Slot(uri=BIOLINK.subject, name="gene has variant that contributes to disease association_subject", curie=BIOLINK.curie('subject'),
                      model_uri=BIOLINK.gene_has_variant_that_contributes_to_disease_association_subject, domain=GeneHasVariantThatContributesToDiseaseAssociation, range=Union[str, GeneOrGeneProductId])

slots.gene_to_expression_site_association_subject = Slot(uri=BIOLINK.subject, name="gene to expression site association_subject", curie=BIOLINK.curie('subject'),
                      model_uri=BIOLINK.gene_to_expression_site_association_subject, domain=GeneToExpressionSiteAssociation, range=Union[str, GeneOrGeneProductId])

slots.gene_to_expression_site_association_object = Slot(uri=BIOLINK.object, name="gene to expression site association_object", curie=BIOLINK.curie('object'),
                      model_uri=BIOLINK.gene_to_expression_site_association_object, domain=GeneToExpressionSiteAssociation, range=Union[str, AnatomicalEntityId])

slots.gene_to_expression_site_association_relation = Slot(uri=BIOLINK.relation, name="gene to expression site association_relation", curie=BIOLINK.curie('relation'),
                      model_uri=BIOLINK.gene_to_expression_site_association_relation, domain=GeneToExpressionSiteAssociation, range=Union[str, URIorCURIE])

slots.gene_to_expression_site_association_stage_qualifier = Slot(uri=BIOLINK.stage_qualifier, name="gene to expression site association_stage qualifier", curie=BIOLINK.curie('stage_qualifier'),
                      model_uri=BIOLINK.gene_to_expression_site_association_stage_qualifier, domain=GeneToExpressionSiteAssociation, range=Optional[Union[str, LifeStageId]])

slots.gene_to_expression_site_association_quantifier_qualifier = Slot(uri=BIOLINK.quantifier_qualifier, name="gene to expression site association_quantifier qualifier", curie=BIOLINK.curie('quantifier_qualifier'),
                      model_uri=BIOLINK.gene_to_expression_site_association_quantifier_qualifier, domain=GeneToExpressionSiteAssociation, range=Optional[Union[str, OntologyClassId]])

slots.sequence_variant_modulates_treatment_association_subject = Slot(uri=BIOLINK.subject, name="sequence variant modulates treatment association_subject", curie=BIOLINK.curie('subject'),
                      model_uri=BIOLINK.sequence_variant_modulates_treatment_association_subject, domain=SequenceVariantModulatesTreatmentAssociation, range=Union[str, SequenceVariantId])

slots.sequence_variant_modulates_treatment_association_object = Slot(uri=BIOLINK.object, name="sequence variant modulates treatment association_object", curie=BIOLINK.curie('object'),
                      model_uri=BIOLINK.sequence_variant_modulates_treatment_association_object, domain=SequenceVariantModulatesTreatmentAssociation, range=Union[str, TreatmentId])

slots.functional_association_subject = Slot(uri=BIOLINK.subject, name="functional association_subject", curie=BIOLINK.curie('subject'),
                      model_uri=BIOLINK.functional_association_subject, domain=FunctionalAssociation, range=Union[str, MacromolecularMachineId])

slots.functional_association_object = Slot(uri=BIOLINK.object, name="functional association_object", curie=BIOLINK.curie('object'),
                      model_uri=BIOLINK.functional_association_object, domain=FunctionalAssociation, range=Union[str, GeneOntologyClassId])

slots.macromolecular_machine_to_molecular_activity_association_object = Slot(uri=BIOLINK.object, name="macromolecular machine to molecular activity association_object", curie=BIOLINK.curie('object'),
                      model_uri=BIOLINK.macromolecular_machine_to_molecular_activity_association_object, domain=MacromolecularMachineToMolecularActivityAssociation, range=Union[str, MolecularActivityId])

slots.macromolecular_machine_to_biological_process_association_object = Slot(uri=BIOLINK.object, name="macromolecular machine to biological process association_object", curie=BIOLINK.curie('object'),
                      model_uri=BIOLINK.macromolecular_machine_to_biological_process_association_object, domain=MacromolecularMachineToBiologicalProcessAssociation, range=Union[str, BiologicalProcessId])

slots.macromolecular_machine_to_cellular_component_association_object = Slot(uri=BIOLINK.object, name="macromolecular machine to cellular component association_object", curie=BIOLINK.curie('object'),
                      model_uri=BIOLINK.macromolecular_machine_to_cellular_component_association_object, domain=MacromolecularMachineToCellularComponentAssociation, range=Union[str, CellularComponentId])

slots.gene_to_go_term_association_subject = Slot(uri=BIOLINK.subject, name="gene to go term association_subject", curie=BIOLINK.curie('subject'),
                      model_uri=BIOLINK.gene_to_go_term_association_subject, domain=GeneToGoTermAssociation, range=Union[str, MolecularEntityId])

slots.gene_to_go_term_association_object = Slot(uri=BIOLINK.object, name="gene to go term association_object", curie=BIOLINK.curie('object'),
                      model_uri=BIOLINK.gene_to_go_term_association_object, domain=GeneToGoTermAssociation, range=Union[str, GeneOntologyClassId])

slots.genomic_sequence_localization_subject = Slot(uri=BIOLINK.subject, name="genomic sequence localization_subject", curie=BIOLINK.curie('subject'),
                      model_uri=BIOLINK.genomic_sequence_localization_subject, domain=GenomicSequenceLocalization, range=Union[str, GenomicEntityId])

slots.genomic_sequence_localization_object = Slot(uri=BIOLINK.object, name="genomic sequence localization_object", curie=BIOLINK.curie('object'),
                      model_uri=BIOLINK.genomic_sequence_localization_object, domain=GenomicSequenceLocalization, range=Union[str, GenomicEntityId])

slots.sequence_feature_relationship_subject = Slot(uri=BIOLINK.subject, name="sequence feature relationship_subject", curie=BIOLINK.curie('subject'),
                      model_uri=BIOLINK.sequence_feature_relationship_subject, domain=SequenceFeatureRelationship, range=Union[str, GenomicEntityId])

slots.sequence_feature_relationship_object = Slot(uri=BIOLINK.object, name="sequence feature relationship_object", curie=BIOLINK.curie('object'),
                      model_uri=BIOLINK.sequence_feature_relationship_object, domain=SequenceFeatureRelationship, range=Union[str, GenomicEntityId])

slots.transcript_to_gene_relationship_subject = Slot(uri=BIOLINK.subject, name="transcript to gene relationship_subject", curie=BIOLINK.curie('subject'),
                      model_uri=BIOLINK.transcript_to_gene_relationship_subject, domain=TranscriptToGeneRelationship, range=Union[str, TranscriptId])

slots.transcript_to_gene_relationship_object = Slot(uri=BIOLINK.object, name="transcript to gene relationship_object", curie=BIOLINK.curie('object'),
                      model_uri=BIOLINK.transcript_to_gene_relationship_object, domain=TranscriptToGeneRelationship, range=Union[str, GeneId])

slots.gene_to_gene_product_relationship_subject = Slot(uri=BIOLINK.subject, name="gene to gene product relationship_subject", curie=BIOLINK.curie('subject'),
                      model_uri=BIOLINK.gene_to_gene_product_relationship_subject, domain=GeneToGeneProductRelationship, range=Union[str, GeneId])

slots.gene_to_gene_product_relationship_object = Slot(uri=BIOLINK.object, name="gene to gene product relationship_object", curie=BIOLINK.curie('object'),
                      model_uri=BIOLINK.gene_to_gene_product_relationship_object, domain=GeneToGeneProductRelationship, range=Union[str, GeneProductId])

slots.gene_to_gene_product_relationship_relation = Slot(uri=BIOLINK.relation, name="gene to gene product relationship_relation", curie=BIOLINK.curie('relation'),
                      model_uri=BIOLINK.gene_to_gene_product_relationship_relation, domain=GeneToGeneProductRelationship, range=Union[str, URIorCURIE])

slots.exon_to_transcript_relationship_subject = Slot(uri=BIOLINK.subject, name="exon to transcript relationship_subject", curie=BIOLINK.curie('subject'),
                      model_uri=BIOLINK.exon_to_transcript_relationship_subject, domain=ExonToTranscriptRelationship, range=Union[str, ExonId])

slots.exon_to_transcript_relationship_object = Slot(uri=BIOLINK.object, name="exon to transcript relationship_object", curie=BIOLINK.curie('object'),
                      model_uri=BIOLINK.exon_to_transcript_relationship_object, domain=ExonToTranscriptRelationship, range=Union[str, TranscriptId])

slots.gene_regulatory_relationship_relation = Slot(uri=BIOLINK.relation, name="gene regulatory relationship_relation", curie=BIOLINK.curie('relation'),
                      model_uri=BIOLINK.gene_regulatory_relationship_relation, domain=GeneRegulatoryRelationship, range=Union[str, URIorCURIE])

slots.gene_regulatory_relationship_subject = Slot(uri=BIOLINK.subject, name="gene regulatory relationship_subject", curie=BIOLINK.curie('subject'),
                      model_uri=BIOLINK.gene_regulatory_relationship_subject, domain=GeneRegulatoryRelationship, range=Union[str, GeneOrGeneProductId])

slots.gene_regulatory_relationship_object = Slot(uri=BIOLINK.object, name="gene regulatory relationship_object", curie=BIOLINK.curie('object'),
                      model_uri=BIOLINK.gene_regulatory_relationship_object, domain=GeneRegulatoryRelationship, range=Union[str, GeneOrGeneProductId])

slots.anatomical_entity_to_anatomical_entity_association_subject = Slot(uri=BIOLINK.subject, name="anatomical entity to anatomical entity association_subject", curie=BIOLINK.curie('subject'),
                      model_uri=BIOLINK.anatomical_entity_to_anatomical_entity_association_subject, domain=AnatomicalEntityToAnatomicalEntityAssociation, range=Union[str, AnatomicalEntityId])

slots.anatomical_entity_to_anatomical_entity_association_object = Slot(uri=BIOLINK.object, name="anatomical entity to anatomical entity association_object", curie=BIOLINK.curie('object'),
                      model_uri=BIOLINK.anatomical_entity_to_anatomical_entity_association_object, domain=AnatomicalEntityToAnatomicalEntityAssociation, range=Union[str, AnatomicalEntityId])

slots.anatomical_entity_to_anatomical_entity_part_of_association_subject = Slot(uri=BIOLINK.subject, name="anatomical entity to anatomical entity part of association_subject", curie=BIOLINK.curie('subject'),
                      model_uri=BIOLINK.anatomical_entity_to_anatomical_entity_part_of_association_subject, domain=AnatomicalEntityToAnatomicalEntityPartOfAssociation, range=Union[str, AnatomicalEntityId])

slots.anatomical_entity_to_anatomical_entity_part_of_association_object = Slot(uri=BIOLINK.object, name="anatomical entity to anatomical entity part of association_object", curie=BIOLINK.curie('object'),
                      model_uri=BIOLINK.anatomical_entity_to_anatomical_entity_part_of_association_object, domain=AnatomicalEntityToAnatomicalEntityPartOfAssociation, range=Union[str, AnatomicalEntityId])

slots.anatomical_entity_to_anatomical_entity_part_of_association_relation = Slot(uri=BIOLINK.relation, name="anatomical entity to anatomical entity part of association_relation", curie=BIOLINK.curie('relation'),
                      model_uri=BIOLINK.anatomical_entity_to_anatomical_entity_part_of_association_relation, domain=AnatomicalEntityToAnatomicalEntityPartOfAssociation, range=Union[str, URIorCURIE])

slots.anatomical_entity_to_anatomical_entity_ontogenic_association_subject = Slot(uri=BIOLINK.subject, name="anatomical entity to anatomical entity ontogenic association_subject", curie=BIOLINK.curie('subject'),
                      model_uri=BIOLINK.anatomical_entity_to_anatomical_entity_ontogenic_association_subject, domain=AnatomicalEntityToAnatomicalEntityOntogenicAssociation, range=Union[str, AnatomicalEntityId])

slots.anatomical_entity_to_anatomical_entity_ontogenic_association_object = Slot(uri=BIOLINK.object, name="anatomical entity to anatomical entity ontogenic association_object", curie=BIOLINK.curie('object'),
                      model_uri=BIOLINK.anatomical_entity_to_anatomical_entity_ontogenic_association_object, domain=AnatomicalEntityToAnatomicalEntityOntogenicAssociation, range=Union[str, AnatomicalEntityId])

slots.anatomical_entity_to_anatomical_entity_ontogenic_association_relation = Slot(uri=BIOLINK.relation, name="anatomical entity to anatomical entity ontogenic association_relation", curie=BIOLINK.curie('relation'),
                      model_uri=BIOLINK.anatomical_entity_to_anatomical_entity_ontogenic_association_relation, domain=AnatomicalEntityToAnatomicalEntityOntogenicAssociation, range=Union[str, URIorCURIE])

slots.molecular_activity_has_input = Slot(uri=BIOLINK.has_input, name="molecular activity_has input", curie=BIOLINK.curie('has_input'),
                      model_uri=BIOLINK.molecular_activity_has_input, domain=MolecularActivity, range=List[Union[str, ChemicalSubstanceId]])

slots.molecular_activity_has_output = Slot(uri=BIOLINK.has_output, name="molecular activity_has output", curie=BIOLINK.curie('has_output'),
                      model_uri=BIOLINK.molecular_activity_has_output, domain=MolecularActivity, range=List[Union[str, ChemicalSubstanceId]])

slots.molecular_activity_enabled_by = Slot(uri=BIOLINK.enabled_by, name="molecular activity_enabled by", curie=BIOLINK.curie('enabled_by'),
                      model_uri=BIOLINK.molecular_activity_enabled_by, domain=MolecularActivity, range=List[Union[str, MacromolecularMachineId]])
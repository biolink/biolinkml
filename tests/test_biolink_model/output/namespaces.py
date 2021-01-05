# Auto generated from biolink-model.yaml by namespacegen.py version: 0.9.0
# Generation date: 2021-01-04 21:52
# Schema: Biolink-Model
#
# id: https://w3id.org/biolink/biolink-model
# description: Entity and association taxonomy and datamodel for life-sciences data
# license: https://creativecommons.org/publicdomain/zero/1.0/

from collections import defaultdict
from typing import Iterable, Dict, Tuple

from biolinkml.utils.curienamespace import CurieNamespace

GENE = 'gene'
DISEASE = 'disease'
CHEMICAL_SUBSTANCE = 'chemical substance'

SYMBOL = 'Approved_Symbol'


class IdentifierResolverException(RuntimeError):
    pass


class BiolinkNameSpace:
    """
    Map of BioLink Model registered URI Namespaces
    """

    _namespaces = [
        CurieNamespace('APO', 'http://purl.obolibrary.org/obo/APO_'),
        CurieNamespace('Aeolus', 'http://translator.ncats.nih.gov/Aeolus_'),
        CurieNamespace('BIOGRID', 'http://identifiers.org/biogrid/'),
        CurieNamespace('BIOSAMPLE', 'http://identifiers.org/biosample/'),
        CurieNamespace('BSPO', 'http://purl.obolibrary.org/obo/BSPO_'),
        CurieNamespace('CAID', 'http://reg.clinicalgenome.org/redmine/projects/registry/genboree_registry/by_caid?caid='),
        CurieNamespace('CHEBI', 'http://purl.obolibrary.org/obo/CHEBI_'),
        CurieNamespace('CHEMBL_COMPOUND', 'http://identifiers.org/chembl.compound/'),
        CurieNamespace('CHEMBL_MECHANISM', 'https://www.ebi.ac.uk/chembl/mechanism/inspect/'),
        CurieNamespace('CHEMBL_TARGET', 'http://identifiers.org/chembl.target/'),
        CurieNamespace('CID', 'http://pubchem.ncbi.nlm.nih.gov/compound/'),
        CurieNamespace('CL', 'http://purl.obolibrary.org/obo/CL_'),
        CurieNamespace('CLINVAR', 'http://identifiers.org/clinvar/'),
        CurieNamespace('CLO', 'http://purl.obolibrary.org/obo/CLO_'),
        CurieNamespace('COAR_RESOURCE', 'http://purl.org/coar/resource_type/'),
        CurieNamespace('CPT', 'https://www.ama-assn.org/practice-management/cpt/'),
        CurieNamespace('CTD', 'http://translator.ncats.nih.gov/CTD_'),
        CurieNamespace('ClinVarVariant', 'http://www.ncbi.nlm.nih.gov/clinvar/variation/'),
        CurieNamespace('DBSNP', 'http://identifiers.org/dbsnp/'),
        CurieNamespace('DGIdb', 'https://www.dgidb.org/interaction_types'),
        CurieNamespace('DOID', 'http://purl.obolibrary.org/obo/DOID_'),
        CurieNamespace('DRUGBANK', 'http://identifiers.org/drugbank/'),
        CurieNamespace('DrugCentral', 'http://translator.ncats.nih.gov/DrugCentral_'),
        CurieNamespace('EC', 'http://www.enzyme-database.org/query.php?ec='),
        CurieNamespace('ECTO', 'http://purl.obolibrary.org/obo/ECTO_'),
        CurieNamespace('EDAM-DATA', 'http://edamontology.org/data_'),
        CurieNamespace('EDAM-FORMAT', 'http://edamontology.org/format_'),
        CurieNamespace('EDAM-OPERATION', 'http://edamontology.org/operation_'),
        CurieNamespace('EDAM-TOPIC', 'http://edamontology.org/topic_'),
        CurieNamespace('EFO', 'http://identifiers.org/efo/'),
        CurieNamespace('ENSEMBL', 'http://identifiers.org/ensembl/'),
        CurieNamespace('ExO', 'http://purl.obolibrary.org/obo/ExO_'),
        CurieNamespace('FAO', 'http://purl.obolibrary.org/obo/FAO_'),
        CurieNamespace('FB', 'http://identifiers.org/fb/'),
        CurieNamespace('FBcv', 'http://purl.obolibrary.org/obo/FBcv_'),
        CurieNamespace('FlyBase', 'http://flybase.org/reports/'),
        CurieNamespace('GAMMA', 'http://translator.renci.org/GAMMA_'),
        CurieNamespace('GO', 'http://purl.obolibrary.org/obo/GO_'),
        CurieNamespace('GOLD_META', 'http://identifiers.org/gold.meta/'),
        CurieNamespace('GOP', 'http://purl.obolibrary.org/obo/go#'),
        CurieNamespace('GOREL', 'http://purl.obolibrary.org/obo/GOREL_'),
        CurieNamespace('GSID', 'https://scholar.google.com/citations?user='),
        CurieNamespace('GTEx', 'https://www.gtexportal.org/home/gene/'),
        CurieNamespace('HANCESTRO', 'http://www.ebi.ac.uk/ancestro/ancestro_'),
        CurieNamespace('HCPCS', 'http://purl.bioontology.org/ontology/HCPCS/'),
        CurieNamespace('HGNC', 'http://identifiers.org/hgnc/'),
        CurieNamespace('HGNC_FAMILY', 'http://identifiers.org/hgnc.family/'),
        CurieNamespace('HMDB', 'http://identifiers.org/hmdb/'),
        CurieNamespace('HP', 'http://purl.obolibrary.org/obo/HP_'),
        CurieNamespace('ICD0', 'http://translator.ncats.nih.gov/ICD0_'),
        CurieNamespace('ICD10', 'http://translator.ncats.nih.gov/ICD10_'),
        CurieNamespace('ICD9', 'http://translator.ncats.nih.gov/ICD9_'),
        CurieNamespace('INCHI', 'http://identifiers.org/inchi/'),
        CurieNamespace('INCHIKEY', 'http://identifiers.org/inchikey/'),
        CurieNamespace('INTACT', 'http://identifiers.org/intact/'),
        CurieNamespace('IUPHAR_FAMILY', 'http://identifiers.org/iuphar.family/'),
        CurieNamespace('KEGG', 'http://identifiers.org/kegg/'),
        CurieNamespace('LOINC', 'http://loinc.org/rdf/'),
        CurieNamespace('MEDDRA', 'http://identifiers.org/meddra/'),
        CurieNamespace('MESH', 'http://identifiers.org/mesh/'),
        CurieNamespace('MGI', 'http://identifiers.org/mgi/'),
        CurieNamespace('MI', 'http://purl.obolibrary.org/obo/MI_'),
        CurieNamespace('MIR', 'http://identifiers.org/mir/'),
        CurieNamespace('MONDO', 'http://purl.obolibrary.org/obo/MONDO_'),
        CurieNamespace('MP', 'http://purl.obolibrary.org/obo/MP_'),
        CurieNamespace('MSigDB', 'https://www.gsea-msigdb.org/gsea/msigdb/'),
        CurieNamespace('MetaCyc', 'http://translator.ncats.nih.gov/MetaCyc_'),
        CurieNamespace('NCBIGENE', 'http://identifiers.org/ncbigene/'),
        CurieNamespace('NCBITaxon', 'http://purl.obolibrary.org/obo/NCBITaxon_'),
        CurieNamespace('NCIT', 'http://purl.obolibrary.org/obo/NCIT_'),
        CurieNamespace('NDDF', 'http://purl.bioontology.org/ontology/NDDF/'),
        CurieNamespace('NLMID', 'https://www.ncbi.nlm.nih.gov/nlmcatalog/?term='),
        CurieNamespace('OBAN', 'http://purl.org/oban/'),
        CurieNamespace('OBOREL', 'http://purl.obolibrary.org/obo/RO_'),
        CurieNamespace('OIO', 'http://www.geneontology.org/formats/oboInOwl#'),
        CurieNamespace('OMIM', 'http://purl.obolibrary.org/obo/OMIM_'),
        CurieNamespace('ORCID', 'https://orcid.org/'),
        CurieNamespace('ORPHA', 'http://www.orpha.net/ORDO/Orphanet_'),
        CurieNamespace('ORPHANET', 'http://identifiers.org/orphanet/'),
        CurieNamespace('PANTHER_FAMILY', 'http://identifiers.org/panther.family/'),
        CurieNamespace('PATO-PROPERTY', 'http://purl.obolibrary.org/obo/pato#'),
        CurieNamespace('PDQ', 'https://www.cancer.gov/publications/pdq#'),
        CurieNamespace('PHARMGKB_DRUG', 'http://identifiers.org/pharmgkb.drug/'),
        CurieNamespace('PHARMGKB_PATHWAYS', 'http://identifiers.org/pharmgkb.pathways/'),
        CurieNamespace('PHAROS', 'http://pharos.nih.gov'),
        CurieNamespace('PMID', 'http://www.ncbi.nlm.nih.gov/pubmed/'),
        CurieNamespace('PO', 'http://purl.obolibrary.org/obo/PO_'),
        CurieNamespace('POMBASE', 'http://identifiers.org/pombase/'),
        CurieNamespace('PR', 'http://purl.obolibrary.org/obo/PR_'),
        CurieNamespace('PUBCHEM_COMPOUND', 'http://identifiers.org/pubchem.compound/'),
        CurieNamespace('PUBCHEM_SUBSTANCE', 'http://identifiers.org/pubchem.substance/'),
        CurieNamespace('PathWhiz', 'http://smpdb.ca/pathways/#'),
        CurieNamespace('REACT', 'http://www.reactome.org/PathwayBrowser/#/'),
        CurieNamespace('REPODB', 'http://apps.chiragjpgroup.org/repoDB/'),
        CurieNamespace('RGD', 'http://identifiers.org/rgd/'),
        CurieNamespace('RHEA', 'http://identifiers.org/rhea/'),
        CurieNamespace('RNACENTRAL', 'http://identifiers.org/rnacentral/'),
        CurieNamespace('RO', 'http://purl.obolibrary.org/obo/RO_'),
        CurieNamespace('RTXKG1', 'http://kg1endpoint.rtx.ai/'),
        CurieNamespace('RXNORM', 'http://purl.bioontology.org/ontology/RXNORM/'),
        CurieNamespace('ResearchID', 'https://publons.com/researcher/'),
        CurieNamespace('SEMMEDDB', 'https://skr3.nlm.nih.gov/SemMedDB'),
        CurieNamespace('SGD', 'http://identifiers.org/sgd/'),
        CurieNamespace('SIO', 'http://semanticscience.org/resource/SIO_'),
        CurieNamespace('SMPDB', 'http://identifiers.org/smpdb/'),
        CurieNamespace('SNOMEDCT', 'http://identifiers.org/snomedct/'),
        CurieNamespace('SNPEFF', 'http://translator.ncats.nih.gov/SNPEFF_'),
        CurieNamespace('ScopusID', 'https://www.scopus.com/authid/detail.uri?authorId='),
        CurieNamespace('TAXRANK', 'http://purl.obolibrary.org/obo/TAXRANK_'),
        CurieNamespace('UBERGRAPH', 'http://translator.renci.org/ubergraph-axioms.ofn#'),
        CurieNamespace('UBERON', 'http://purl.obolibrary.org/obo/UBERON_'),
        CurieNamespace('UBERON_CORE', 'http://purl.obolibrary.org/obo/uberon/core#'),
        CurieNamespace('UMLS', 'http://identifiers.org/umls/'),
        CurieNamespace('UMLSSC', 'https://metamap.nlm.nih.gov/Docs/SemanticTypes_2018AB.txt/code#'),
        CurieNamespace('UMLSSG', 'https://metamap.nlm.nih.gov/Docs/SemGroups_2018.txt/group#'),
        CurieNamespace('UMLSST', 'https://metamap.nlm.nih.gov/Docs/SemanticTypes_2018AB.txt/type#'),
        CurieNamespace('UNII', 'http://identifiers.org/unii/'),
        CurieNamespace('UO', 'http://purl.obolibrary.org/obo/UO_'),
        CurieNamespace('UPHENO', 'http://purl.obolibrary.org/obo/UPHENO_'),
        CurieNamespace('UniProtKB', 'http://identifiers.org/uniprot/'),
        CurieNamespace('VANDF', 'https://www.nlm.nih.gov/research/umls/sourcereleasedocs/current/VANDF/'),
        CurieNamespace('VMC', 'https://github.com/ga4gh/vr-spec/'),
        CurieNamespace('WB', 'http://identifiers.org/wb/'),
        CurieNamespace('WBPhenotype', 'http://purl.obolibrary.org/obo/WBPhenotype_'),
        CurieNamespace('WBVocab', 'http://bio2rdf.org/wormbase_vocabulary'),
        CurieNamespace('WIKIDATA', 'https://www.wikidata.org/wiki/'),
        CurieNamespace('WIKIDATA_PROPERTY', 'https://www.wikidata.org/wiki/Property:'),
        CurieNamespace('WIKIPATHWAYS', 'http://identifiers.org/wikipathways/'),
        CurieNamespace('WormBase', 'https://www.wormbase.org/get?name='),
        CurieNamespace('ZFIN', 'http://identifiers.org/zfin/'),
        CurieNamespace('ZP', 'http://purl.obolibrary.org/obo/ZP_'),
        CurieNamespace('alliancegenome', 'https://www.alliancegenome.org/'),
        CurieNamespace('biolink', 'https://w3id.org/biolink/vocab/'),
        CurieNamespace('biolinkml', 'https://w3id.org/biolink/biolinkml/'),
        CurieNamespace('chembio', 'http://translator.ncats.nih.gov/chembio_'),
        CurieNamespace('dcterms', 'http://purl.org/dc/terms/'),
        CurieNamespace('dictyBase', 'http://dictybase.org/gene/'),
        CurieNamespace('doi', 'https://doi.org/'),
        CurieNamespace('fabio', 'http://purl.org/spar/fabio/'),
        CurieNamespace('foaf', 'http://xmlns.com/foaf/0.1/'),
        CurieNamespace('foodb_compound', 'http://foodb.ca/compounds/'),
        CurieNamespace('gff3', 'https://github.com/The-Sequence-Ontology/Specifications/blob/master/gff3.md#'),
        CurieNamespace('gpi', 'https://github.com/geneontology/go-annotation/blob/master/specs/gpad-gpi-2-0.md#'),
        CurieNamespace('gtpo', 'https://rdf.guidetopharmacology.org/ns/gtpo#'),
        CurieNamespace('hetio', 'http://translator.ncats.nih.gov/hetio_'),
        CurieNamespace('interpro', 'https://www.ebi.ac.uk/interpro/entry/'),
        CurieNamespace('isbn', 'https://www.isbn-international.org/identifier/'),
        CurieNamespace('isni', 'https://isni.org/isni/'),
        CurieNamespace('issn', 'https://portal.issn.org/resource/ISSN/'),
        CurieNamespace('medgen', 'https://www.ncbi.nlm.nih.gov/medgen/'),
        CurieNamespace('oboformat', 'http://www.geneontology.org/formats/oboInOWL#'),
        CurieNamespace('qud', 'http://qudt.org/1.1/schema/qudt#'),
        CurieNamespace('rdf', 'http://www.w3.org/1999/02/22-rdf-syntax-ns#'),
        CurieNamespace('rdfs', 'http://www.w3.org/2000/01/rdf-schema#'),
        CurieNamespace('skos', 'https://www.w3.org/TR/skos-reference/#'),
        CurieNamespace('wgs', 'http://www.w3.org/2003/01/geo/wgs84_pos'),
        CurieNamespace('xsd', 'http://www.w3.org/2001/XMLSchema#'),
    ]

    # class level dictionaries

    _prefix_map: Dict[str, CurieNamespace] = {}

    @classmethod
    def _get_prefix_map(cls):
        if not cls._prefix_map:
            for ns in cls._namespaces:
                # index by upper case for uniformity of search
                cls._prefix_map[ns.prefix.upper()] = ns
        return cls._prefix_map

    @classmethod
    def parse_curie(cls, curie: str) -> Tuple[CurieNamespace, str]:
        """
        Parse a candidate CURIE
        :param curie: candidate curie string
        :return: CURIE namespace and object_id
        """
        found = CurieNamespace("", ""), curie  # default value if not a CURIE or unknown XMLNS prefix
        if ':' in curie:
            part = curie.split(":")
            # Normalize retrieval with upper case of prefix for lookup
            prefix = part[0].upper()
            if prefix in cls._get_prefix_map():
                found = cls._prefix_map[prefix], part[1]
        return found

    @classmethod
    def parse_uri(cls, uri: str) -> Tuple[CurieNamespace,  str]:
        """
        Parse a candidate URI
        :param uri: candidate URI string
        :return: namespace and object_id
        """
        found = CurieNamespace("", ""), uri   # default value returned if unknown URI namespace

        # TODO: is there a more efficient lookup scheme here than a linear search of namespaces?
        for ns in cls._namespaces:
            base_uri = str(ns)
            if uri.startswith(base_uri):
                # simple minded deletion of base_uri to give the object_id
                object_id = uri.replace(base_uri, "")
                found = ns, object_id
                break
        return found

    @classmethod
    def parse_identifier(cls,  identifier: str) -> Tuple[CurieNamespace,  str]:

        # trivial case of a null identifier?
        if not identifier:
            return CurieNamespace("", ""), ""

        # check if this is a candidate URI...
        if identifier.lower().startswith("http"):
            # guess that perhaps it is, so try to parse it
            return cls.parse_uri(identifier)

        else:  # attempt to parse as a CURIE
            return cls.parse_curie(identifier)


def object_id(identifier, keep_version=False) -> str:
    """
    Returns the core object_id of a CURIE, with or without the version suffix.
    Note:  not designed to be used with a URI (will give an invalid outcome)
    :param identifier: candidate CURIE identifier for processing
    :param keep_version: True if the version string suffix is to be retained in the identifier
    :return:
    """
    # trivial case: null input value?
    if not identifier:
        return identifier

    if ':' in identifier:
        identifier = identifier.split(":")[1]

    if not keep_version and '.' in identifier:
        identifier = identifier.split(".")[0]

    return identifier


def fix_curies(identifiers, prefix=''):
    """
    Applies the specified XMLNS prefix to (an) identifier(s) known
    to be "raw" IDs as keys in a dictionary or elements in a list (or a simple string)
    :param identifiers:
    :param prefix:
    :return:
    """
    if not prefix:
        # return identifiers without modification
        # Caller may already consider them in curie format
        return identifiers

    if isinstance(identifiers, dict):
        curie_dict = defaultdict(dict)
        for key in identifiers.keys():
            curie_dict[prefix + ':' + object_id(key, keep_version=True)] = identifiers[key]
        return curie_dict

    # identifiers assumed to be just a single object identifier
    elif isinstance(identifiers, str):
        # single string to convert
        return prefix + ':' + object_id(identifiers, keep_version=True)

    elif isinstance(identifiers, Iterable):
        return [prefix + ':' + object_id(x, keep_version=True) for x in identifiers]

    else:
        raise RuntimeError("fix_curie() is not sure how to fix an instance of data type '", type(identifiers))


def curie(identifier) -> str:
    # Ignore enpty strings
    if not identifier:
        return ""
    else:
        namespace: CurieNamespace
        identifier_object_id: str
        namespace, identifier_object_id = BiolinkNameSpace.parse_identifier(identifier)
        return namespace.curie(identifier_object_id)

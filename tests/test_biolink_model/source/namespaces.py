# Auto generated from biolink-model.yaml by namespacegen.py version: 0.4.0
# Generation date:
# Schema: Biolink_Model
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
        CurieNamespace('BFO', 'http://purl.obolibrary.org/obo/BFO_'),
        CurieNamespace('BIOGRID', 'http://thebiogrid.org/'),
        CurieNamespace('BioSample', 'http://example.org/UNKNOWN/BioSample/'),
        CurieNamespace('CAID', 'http://example.org/UNKNOWN/CAID/'),
        CurieNamespace('CHEBI', 'http://purl.obolibrary.org/obo/CHEBI_'),
        CurieNamespace('CHEMBL_COMPOUND', 'http://identifiers.org/chembl.compound/'),
        CurieNamespace('CHEMBL_TARGET', 'http://identifiers.org/chembl.target/'),
        CurieNamespace('CIO', 'http://purl.obolibrary.org/obo/CIO_'),
        CurieNamespace('CIViC', 'http://example.org/UNKNOWN/CIViC/'),
        CurieNamespace('CL', 'http://purl.obolibrary.org/obo/CL_'),
        CurieNamespace('CLO', 'http://purl.obolibrary.org/obo/CLO_'),
        CurieNamespace('ClinVar', 'http://www.ncbi.nlm.nih.gov/clinvar/'),
        CurieNamespace('DBSNP', 'http://identifiers.org/dbsnp/'),
        CurieNamespace('DOID', 'http://purl.obolibrary.org/obo/DOID_'),
        CurieNamespace('DRUGBANK', 'http://identifiers.org/drugbank/'),
        CurieNamespace('ECO', 'http://purl.obolibrary.org/obo/ECO_'),
        CurieNamespace('ECTO', 'http://example.org/UNKNOWN/ECTO/'),
        CurieNamespace('EFO', 'http://purl.obolibrary.org/obo/EFO_'),
        CurieNamespace('ENSEMBL', 'http://ensembl.org/id/'),
        CurieNamespace('ExO', 'http://example.org/UNKNOWN/ExO/'),
        CurieNamespace('FAO', 'http://purl.obolibrary.org/obo/FAO_'),
        CurieNamespace('GENO', 'http://purl.obolibrary.org/obo/GENO_'),
        CurieNamespace('GO', 'http://purl.obolibrary.org/obo/GO_'),
        CurieNamespace('GOLD_META', 'http://identifiers.org/gold.meta/'),
        CurieNamespace('GTOPDB', 'http://example.org/UNKNOWN/GTOPDB/'),
        CurieNamespace('HANCESTRO', 'http://example.org/UNKNOWN/HANCESTRO/'),
        CurieNamespace('HGNC', 'http://www.genenames.org/cgi-bin/gene_symbol_report?hgnc_id='),
        CurieNamespace('HGVS', 'http://example.org/UNKNOWN/HGVS/'),
        CurieNamespace('HMDB', 'http://www.hmdb.ca/metabolites/'),
        CurieNamespace('HP', 'http://purl.obolibrary.org/obo/HP_'),
        CurieNamespace('IAO', 'http://purl.obolibrary.org/obo/IAO_'),
        CurieNamespace('INCHI', 'http://identifiers.org/inchi/'),
        CurieNamespace('INCHIKEY', 'http://identifiers.org/inchikey/'),
        CurieNamespace('IUPHAR', 'http://example.org/UNKNOWN/IUPHAR/'),
        CurieNamespace('IntAct', 'http://example.org/UNKNOWN/IntAct/'),
        CurieNamespace('KEGG', 'http://identifiers.org/kegg/'),
        CurieNamespace('MEDDRA', 'http://purl.bioontology.org/ontology/MEDDRA/'),
        CurieNamespace('MESH', 'http://purl.obolibrary.org/obo/MESH_'),
        CurieNamespace('MGI', 'http://www.informatics.jax.org/accession/MGI:'),
        CurieNamespace('MIR', 'http://identifiers.org/mir/'),
        CurieNamespace('MONDO', 'http://purl.obolibrary.org/obo/MONDO_'),
        CurieNamespace('MYVARIANT_HG19', 'http://example.org/UNKNOWN/MYVARIANT_HG19/'),
        CurieNamespace('MYVARIANT_HG38', 'http://example.org/UNKNOWN/MYVARIANT_HG38/'),
        CurieNamespace('NCBIGene', 'http://www.ncbi.nlm.nih.gov/gene/'),
        CurieNamespace('NCIT', 'http://purl.obolibrary.org/obo/NCIT_'),
        CurieNamespace('OBAN', 'http://purl.org/oban/'),
        CurieNamespace('OBI', 'http://purl.obolibrary.org/obo/OBI_'),
        CurieNamespace('OGMS', 'http://purl.obolibrary.org/obo/OGMS_'),
        CurieNamespace('OIO', 'http://www.geneontology.org/formats/oboInOwl#'),
        CurieNamespace('OMIM', 'http://purl.obolibrary.org/obo/OMIM_'),
        CurieNamespace('ORPHANET', 'http://identifiers.org/orphanet/'),
        CurieNamespace('PANTHER', 'http://www.pantherdb.org/panther/family.do?clsAccession='),
        CurieNamespace('PHARMGKB', 'http://example.org/UNKNOWN/PHARMGKB/'),
        CurieNamespace('PMID', 'http://www.ncbi.nlm.nih.gov/pubmed/'),
        CurieNamespace('PO', 'http://purl.obolibrary.org/obo/PO_'),
        CurieNamespace('PR', 'http://purl.obolibrary.org/obo/PR_'),
        CurieNamespace('PUBCHEM', 'http://example.org/UNKNOWN/PUBCHEM/'),
        CurieNamespace('PW', 'http://purl.obolibrary.org/obo/PW_'),
        CurieNamespace('PomBase', 'https://www.pombase.org/spombe/result/'),
        CurieNamespace('RHEA', 'http://identifiers.org/rhea/'),
        CurieNamespace('RNAcentral', 'http://example.org/UNKNOWN/RNAcentral/'),
        CurieNamespace('RO', 'http://purl.obolibrary.org/obo/RO_'),
        CurieNamespace('Reactome', 'http://example.org/UNKNOWN/Reactome/'),
        CurieNamespace('SEMMEDDB', 'http://example.org/UNKNOWN/SEMMEDDB/'),
        CurieNamespace('SGD', 'https://www.yeastgenome.org/locus/'),
        CurieNamespace('SIO', 'http://semanticscience.org/resource/SIO_'),
        CurieNamespace('SMPDB', 'http://smpdb.ca/view/'),
        CurieNamespace('SO', 'http://purl.obolibrary.org/obo/SO_'),
        CurieNamespace('UBERON', 'http://purl.obolibrary.org/obo/UBERON_'),
        CurieNamespace('UMLS', 'http://linkedlifedata.com/resource/umls/id/'),
        CurieNamespace('UMLSSC', 'https://uts-ws.nlm.nih.gov/rest/semantic-network/semantic-network/current/TUI/'),
        CurieNamespace('UMLSSG', 'https://uts-ws.nlm.nih.gov/rest/semantic-network/semantic-network/current/GROUP/'),
        CurieNamespace('UMLSST', 'https://uts-ws.nlm.nih.gov/rest/semantic-network/semantic-network/current/STY/'),
        CurieNamespace('UNII', 'http://fdasis.nlm.nih.gov/srs/unii/'),
        CurieNamespace('UNIPROTKB', 'http://example.org/UNKNOWN/UNIPROTKB/'),
        CurieNamespace('UO', 'http://purl.obolibrary.org/obo/UO_'),
        CurieNamespace('UPHENO', 'http://purl.obolibrary.org/obo/UPHENO_'),
        CurieNamespace('UniProtKB', 'http://identifiers.org/uniprot/'),
        CurieNamespace('VMC', 'http://example.org/UNKNOWN/VMC/'),
        CurieNamespace('WB', 'http://identifiers.org/wb/'),
        CurieNamespace('WD', 'http://example.org/UNKNOWN/WD/'),
        CurieNamespace('WIKIPATHWAYS', 'http://identifiers.org/wikipathways/'),
        CurieNamespace('ZFIN', 'http://zfin.org/'),
        CurieNamespace('biolink', 'https://w3id.org/biolink/vocab/'),
        CurieNamespace('biolinkml', 'https://w3id.org/biolink/biolinkml/'),
        CurieNamespace('dct', 'http://example.org/UNKNOWN/dct/'),
        CurieNamespace('dcterms', 'http://purl.org/dc/terms/'),
        CurieNamespace('dictyBase', 'http://dictybase.org/gene/'),
        CurieNamespace('faldo', 'http://biohackathon.org/resource/faldo#'),
        CurieNamespace('owl', 'http://www.w3.org/2002/07/owl#'),
        CurieNamespace('pav', 'http://purl.org/pav/'),
        CurieNamespace('qud', 'http://qudt.org/1.1/schema/qudt#'),
        CurieNamespace('rdf', 'http://www.w3.org/1999/02/22-rdf-syntax-ns#'),
        CurieNamespace('rdfs', 'http://www.w3.org/2000/01/rdf-schema#'),
        CurieNamespace('skos', 'http://www.w3.org/2004/02/skos/core#'),
        CurieNamespace('void', 'http://rdfs.org/ns/void#'),
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

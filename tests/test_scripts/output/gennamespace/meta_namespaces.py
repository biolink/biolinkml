# Auto generated from meta.yaml by namespacegen.py version: 0.4.0
# Generation date: 2020-09-11 16:59
# Schema: metamodel
#
# id: https://w3id.org/biolink/biolinkml/meta
# description: A metamodel for defining biolink related schemas
# license: https://creativecommons.org/publicdomain/zero/1.0/

from collections import defaultdict
from functools import lru_cache
from typing import Iterable, Dict, List, Tuple
import re

from biolinkml.utils.curienamespace import CurieNamespace


class NameSpaceException(RuntimeError):
    pass


class metamodelNameSpace:
    """
    Map of metamodel registered URI Namespaces
    """

    _namespaces = [
        CurieNamespace('OIO', 'http://www.geneontology.org/formats/oboInOwl#'),
        CurieNamespace('bibo', 'http://purl.org/ontology/bibo/'),
        CurieNamespace('biolinkml', 'https://w3id.org/biolink/biolinkml/'),
        CurieNamespace('dcterms', 'http://purl.org/dc/terms/'),
        CurieNamespace('meta', 'https://w3id.org/biolink/biolinkml/meta/'),
        CurieNamespace('oslc', 'http://open-services.net/ns/core#'),
        CurieNamespace('owl', 'http://www.w3.org/2002/07/owl#'),
        CurieNamespace('pav', 'http://purl.org/pav/'),
        CurieNamespace('rdf', 'http://www.w3.org/1999/02/22-rdf-syntax-ns#'),
        CurieNamespace('rdfs', 'http://www.w3.org/2000/01/rdf-schema#'),
        CurieNamespace('schema', 'http://schema.org/'),
        CurieNamespace('skos', 'http://www.w3.org/2004/02/skos/core#'),
        CurieNamespace('xsd', 'http://www.w3.org/2001/XMLSchema#'),
    ]

    # class level dictionaries

    _prefix_map: Dict[str, CurieNamespace] = {}
    _uri_map: Dict[str, List[CurieNamespace]] = {}

    @classmethod
    def _get_prefix_map(cls):
        if not cls._prefix_map:
            for ns in cls._namespaces:
                # index by upper case for uniformity of search
                cls._prefix_map[ns.prefix.upper()] = ns
        return cls._prefix_map

    URI_REGEX = re.compile(r"^(?P<scheme>[^:]+)://(?P<host>[^/:]+):?(?P<port>[^/?#]+)?"+
                           "(?P<path>[^?#]*)?([?](?P<parameters>[^?#]+))?(#(?P<hashtag>.*))?$")

    @classmethod
    def uri_parts(cls, uri) -> Tuple[str, str, str, str, str, str]:
        """
        Parses a URI into basic component parts
        :param uri:
        :return: tuple of scheme, host, port, path, parameters, hashtag
        """
        if not uri:
            raise NameSpaceException("uri_parts() ERROR: null or empty URI string?")

        match = cls.URI_REGEX.match(str(uri))

        if not match:
            raise NameSpaceException("uri_parts() ERROR: could not parse URI"+str(uri)+"?")
        else:
            return (match.group('scheme'),
                    match.group('host'),
                    match.group('port'),
                    match.group('path'),
                    match.group('parameters'),
                    match.group('hashtag'))

    @classmethod
    def _get_uri_map(cls):
        if not cls._uri_map:
            for ns in cls._namespaces:
                nsp = cls.uri_parts(ns)
                host = nsp[1]
                # index in bucket by hostname
                if host not in cls._uri_map:
                    cls._uri_map[host] = []
                cls._uri_map[host].append(ns)

        return cls._uri_map

    @classmethod
    def parse_curie(cls, identifier: str) -> Tuple[CurieNamespace, str]:
        """
        Parse a candidate CURIE
        :param identifier: candidate curie string
        :return: CURIE namespace and object_id
        """
        found = CurieNamespace("", ""), identifier  # default value if not a CURIE or unknown XMLNS prefix
        if ':' in identifier:
            part = identifier.split(":")
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

        urip = cls.uri_parts(uri)
        host = urip[1]

        uri_map = cls._get_uri_map()

        if host not in uri_map:
            return found # empty CURIE
        else:
            uri_list = uri_map[host]
            for ns in uri_list:
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

    # Better coerce into a string, just in case
    identifier = str(identifier)

    if ':' in identifier:
        identifier = identifier.split(":")[1]

    if not keep_version and '.' in identifier:
        identifier = identifier.split(".")[0]

    return identifier


def fix_curies(identifiers, prefix=''):
    """
    Applies the specified XMLNS prefix to (an) identifier(s) known to be
    "raw" IDs as keys in a dictionary or elements in a list (or a simple string)

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

    elif isinstance(identifiers, int):
        # single string to convert
        return prefix + ':' + object_id(str(identifiers), keep_version=True)

    else:
        raise RuntimeError("fix_curie() is not sure how to fix an instance of data type '", type(identifiers))


@lru_cache(maxsize=1000)
def curie(identifier) -> str:
    # Ignore empty strings
    if not identifier:
        return ""
    else:
        namespace: CurieNamespace
        identifier_object_id: str
        namespace, identifier_object_id = metamodelNameSpace.parse_identifier(identifier)
        return namespace.curie(identifier_object_id)


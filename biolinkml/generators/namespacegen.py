import os

import click

from biolinkml.generators import PYTHON_GEN_VERSION
from biolinkml.generators.pythongen import PythonGenerator
from biolinkml.utils.formatutils import split_line, be
from biolinkml.utils.generator import shared_arguments


class NamespaceGenerator(PythonGenerator):
    generatorname = os.path.basename(__file__)
    generatorversion = PYTHON_GEN_VERSION
    valid_formats = ['py']
    visit_all_class_slots = False

    def gen_namespaces(self) -> str:
        return '\n\t\t'.join([
            f"CurieNamespace('{pfx.replace('.', '_')}', '{self.namespaces[pfx]}'),"
            for pfx in sorted(self.emit_prefixes) if pfx in self.namespaces
        ])

    def gen_schema(self) -> str:
        split_description = '\n#              '.join(split_line(be(self.schema.description), split_len=100))
        head = f'''# Auto generated from {self.schema.source_file} by {self.generatorname} version: {self.generatorversion}
# Generation date: {self.schema.generation_date}
# Schema: {self.schema.name}
#''' if self.schema.generation_date else ''

        return f'''{head}
# id: {self.schema.id}
# description: {split_description}
# license: {be(self.schema.license)}

from collections import defaultdict
from functools import lru_cache
from typing import Iterable, Dict, List, Tuple
import re

from biolinkml.utils.curienamespace import CurieNamespace


class NameSpaceException(RuntimeError):
    pass


class {self.schema.name}NameSpace:
    """
    Map of {self.schema.name} registered URI Namespaces
    """

    _namespaces = [
        {self.gen_namespaces()}
    ]

    # class level dictionaries

    _prefix_map: Dict[str, CurieNamespace] = {{}}
    _uri_map: Dict[str, List[CurieNamespace]] = {{}}

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
        Parses a URI object (which may be expressed as a str value) into its basic component parts
        
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
        :return: CURIE namespace and object_id
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
        """
        Parse and validate an identifier (may be URI or a proper CURIE) 
        into a known locally registered CURIE namespace and object_id
        
        :param identifier: 
        :return: CURIE namespace and object_id of the identifier
        """
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
    :return: object identifier string
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
    :return: identifiers with preferred prefix
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
    """
    Parses an input identifier (can be a URI), to return a proper CURIE
    
    :param identifier: 
    :return: CURIE string, properly mapped onto a known locally registered namespace
    """
    # Ignore empty strings
    if not identifier:
        return ""
    else:
        namespace: CurieNamespace
        identifier_object_id: str
        namespace, identifier_object_id = {self.schema.name}NameSpace.parse_identifier(identifier)
        return namespace.curie(identifier_object_id)
'''


@shared_arguments(NamespaceGenerator)
@click.command()
def cli(yamlfile, **args):
    """ Generate a namespace manager for all of the prefixes represented in a biolink model """
    print(NamespaceGenerator(yamlfile, **args).serialize(**args))

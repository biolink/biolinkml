# Auto generated from .yaml by pythongen.py version:
# Generation date:
# Schema: types
#
# id: https://w3id.org/biolink/biolinkml/types
# description: Shared type definitions for the core biolink mode and metamodel
# license: https://creativecommons.org/publicdomain/zero/1.0/

from typing import Optional, List, Union, Dict, ClassVar
from dataclasses import dataclass
from biolinkml.utils.metamodelcore import empty_list, empty_dict, bnode
from biolinkml.utils.yamlutils import YAMLRoot
from biolinkml.utils.formatutils import camelcase, underscore, sfx
from rdflib import Namespace
from biolinkml.utils.metamodelcore import Bool, ElementIdentifier, NCName, NodeIdentifier, URI, URIorCURIE, XSDDate, XSDDateTime, XSDTime

metamodel_version = "1.4.0"


# Namespaces
METATYPE = Namespace('https://w3id.org/biolink/biolinkml/type/')
DEFAULT_ = METATYPE


# Types
class String(str):
    """ A character string """
    pass


class Integer(int):
    """ An integer """
    pass


class Boolean(Bool):
    """ A binary (true or false) value """
    pass


class Float(float):
    """ A real number that conforms to the xsd:float specification """
    pass


class Double(float):
    """ A real number that conforms to the xsd:double specification """
    pass


class Time(XSDTime):
    """ A time object represents a (local) time of day, independent of any particular day """
    pass


class Date(XSDDate):
    """ a date (year, month and day) in an idealized calendar """
    pass


class Datetime(XSDDateTime):
    """ The combination of a date and time """
    pass


class Uriorcurie(URIorCURIE):
    """ a URI or a CURIE """
    pass


class Uri(URI):
    """ a complete URI """
    pass


class Ncname(NCName):
    """ Prefix part of CURIE """
    pass


class Objectidentifier(ElementIdentifier):
    """ A URI or CURIE that represents an object in the model. """
    pass


class Nodeidentifier(NodeIdentifier):
    """ A URI, CURIE or BNODE that represents a node in a model. """
    pass


# Class references



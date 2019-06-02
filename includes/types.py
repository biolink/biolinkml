# Auto generated from .yaml by pythongen.py version:
# Generation date:
# Schema: types
#
# id: https://w3id.org/biolink/biolinkml/types
# description: Shared type definitions for the core biolink mode and metamodel
# license: https://creativecommons.org/publicdomain/zero/1.0/

from typing import Optional, List, Union, Dict, ClassVar
from dataclasses import dataclass
from biolinkml.utils.metamodelcore import empty_list, empty_dict
from biolinkml.utils.yamlutils import YAMLRoot
from biolinkml.utils.metamodelcore import Bool, NCName, URI, URIorCURIE, XSDDate, XSDDateTime, XSDTime

metamodel_version = "1.3.4"

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


# Class references
# Auto generated from .yaml by pythongen.py version:
# Generation date:
# Schema: types
#
# id: https://w3id.org/biolink/biolinkml/types
# description: Shared type definitions
# license: https://creativecommons.org/publicdomain/zero/1.0/

from typing import Optional, List, Union, Dict, ClassVar
from dataclasses import dataclass
from biolinkml.utils.metamodelcore import empty_list, empty_dict
from biolinkml.utils.yamlutils import YAMLRoot
from biolinkml.utils.metamodelcore import Bool, NCName, URI, URIorCURIE, XSDDate, XSDDateTime, XSDTime

metamodel_version = "1.3.0"

# Types
class String(str):
    pass


class Integer(int):
    pass


class Boolean(Bool):
    """ A binary (true or false) value """
    pass


class Float(float):
    pass


class Double(float):
    pass


class Time(XSDTime):
    """ A time object represents a (local) time of day, independent of any particular day """
    pass


class Date(XSDDateTime):
    """ a date (year, month and day) in an idealized calendar """
    pass


class Datetime(XSDDate):
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
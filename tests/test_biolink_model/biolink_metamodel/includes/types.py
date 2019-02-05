# Auto generated from types.yaml by pythongen.py version: 0.1.0
# Generation date: 2019-02-04 14:59
# Schema: types
#
# id: http://w3id.org/biolink/biolinkml/types
# description: Shared type definitions
# license: https://creativecommons.org/publicdomain/zero/1.0/

from datetime import time, date, datetime
from typing import List

from biolinkml.utils.metamodelcore import Bool, URIorCURIE, NCName

metamodel_version = "1.0.0"

inherited_slots: List[str] = []


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


class Time(time):
    """ A time object represents a (local) time of day, independent of any particular day """
    pass


class Date(date):
    """ a date (year, month and day) in an idealized calendar """
    pass


class Datetime(datetime):
    pass


class Uri(URIorCURIE):
    """ a URI or a CURIE """
    pass


class Ncname(NCName):
    """ Prefix part of CURIE """
    pass


# Class references

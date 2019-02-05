# Auto generated from biolink_types.yaml by pythongen.py version: 0.1.0
# Generation date: 2019-02-04 15:01
# Schema: pes for use in the biolink model
#
# id: http://w3id.org/biolink/biolinkmodel/pes
# description: pe definitions for the biolink model definitions
# license: https://creativecommons.org/publicdomain/zero/1.0/

from datetime import time, date, datetime
from typing import List

from biolinkml.utils.metamodelcore import Bool, URIorCURIE, NCName
from tests.test_biolink_model.biolink_metamodel.includes.types import String, Uri, Double, Time

metamodel_version = "None"

inherited_slots: List[str] = []


# pes
class IdentifierType(Uri):
    """ A URI or CURIE that uniquely identifies the named thing """
    pass


class UriType(Uri):
    """ The URI that uniquely identifies the named thing """
    pass


class LabelType(String):
    """ A string that provides a human-readable name for a thing """
    pass


class NarrativeText(String):
    """ A string that provides a human-readable description of something """
    pass


class SymbolType(String):
    pass


class ChemicalFormulaType(String):
    pass


class FrequencyValue(String):
    pass


class PerecentageFrequencyValue(Double):
    pass


class Quotient(Double):
    pass


class Unit(String):
    pass


class TimeType(Time):
    """ A time object represents a (local) time of day, independent of any particular day """
    pass


class BiologicalSequence(String):
    pass


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

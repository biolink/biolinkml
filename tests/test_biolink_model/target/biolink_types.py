# Auto generated from biolink_types.yaml by pythongen.py version: 0.2.0
# Generation date: 2019-02-12 09:07
# Schema: types for use in the biolink model
#
# id: http://w3id.org/biolink/biolinkmodel/types
# description: Type definitions for the biolink model definitions
# license: https://creativecommons.org/publicdomain/zero/1.0/

from typing import Optional, List, Union, Dict
from dataclasses import dataclass
from biolinkml.utils.metamodelcore import empty_list, empty_dict
from biolinkml.utils.yamlutils import YAMLRoot
from biolinkml.utils.metamodelcore import Bool, URIorCURIE, XSDTime
from includes.types import Boolean, Double, String, Time, Uri

metamodel_version = "1.0.2"

inherited_slots: List[str] = []


# Types
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
    pass


class BiologicalSequence(String):
    pass


class BooleanType(Boolean):
    """ A true/false value with absent (None) meaning not specified """
    pass


class FileName(String):
    pass


# Class references



# Auto generated from ifabsents3.yaml by pythongen.py version: 0.9.0
# Generation date: 2021-01-05 17:39
# Schema: ifabsent
#
# id: http://example.org/tests/ifabsent
# description:
# license: https://creativecommons.org/publicdomain/zero/1.0/

import dataclasses
import sys
import re
from typing import Optional, List, Union, Dict, ClassVar, Any
from dataclasses import dataclass
from biolinkml.meta import EnumDefinition, PermissibleValue, PvFormulaOptions

from biolinkml.utils.slot import Slot
from biolinkml.utils.metamodelcore import empty_list, empty_dict, bnode
from biolinkml.utils.yamlutils import YAMLRoot, extended_str, extended_float, extended_int
if sys.version_info < (3, 7, 6):
    from biolinkml.utils.dataclass_extensions_375 import dataclasses_init_fn_with_kwargs
else:
    from biolinkml.utils.dataclass_extensions_376 import dataclasses_init_fn_with_kwargs
from biolinkml.utils.formatutils import camelcase, underscore, sfx
from biolinkml.utils.enumerations import EnumDefinitionImpl
from rdflib import Namespace, URIRef
from biolinkml.utils.curienamespace import CurieNamespace
from biolinkml.utils.metamodelcore import Bool, Decimal, ElementIdentifier, NCName, NodeIdentifier, URI, URIorCURIE, XSDDate, XSDDateTime, XSDTime

metamodel_version = "1.7.0"

# Overwrite dataclasses _init_fn to add **kwargs in __init__
dataclasses._init_fn = dataclasses_init_fn_with_kwargs

# Namespaces
SHEX = CurieNamespace('shex', 'http://www.w3.org/ns/shex#')
SKOS = CurieNamespace('skos', 'http://www.w3.org/2004/02/skos/core#')
TEST = CurieNamespace('test', 'http://example.org/tests/ifabsent/')
XSD = CurieNamespace('xsd', 'http://www.w3.org/2001/XMLSchema#')
DEFAULT_ = TEST


# Types
class String(str):
    """ A character string """
    type_class_uri = XSD.string
    type_class_curie = "xsd:string"
    type_name = "string"
    type_model_uri = TEST.String


class Integer(int):
    """ An integer """
    type_class_uri = XSD.integer
    type_class_curie = "xsd:integer"
    type_name = "integer"
    type_model_uri = TEST.Integer


class Boolean(Bool):
    """ A binary (true or false) value """
    type_class_uri = XSD.boolean
    type_class_curie = "xsd:boolean"
    type_name = "boolean"
    type_model_uri = TEST.Boolean


class Float(float):
    """ A real number that conforms to the xsd:float specification """
    type_class_uri = XSD.float
    type_class_curie = "xsd:float"
    type_name = "float"
    type_model_uri = TEST.Float


class Double(float):
    """ A real number that conforms to the xsd:double specification """
    type_class_uri = XSD.double
    type_class_curie = "xsd:double"
    type_name = "double"
    type_model_uri = TEST.Double


class Decimal(Decimal):
    """ A real number with arbitrary precision that conforms to the xsd:decimal specification """
    type_class_uri = XSD.decimal
    type_class_curie = "xsd:decimal"
    type_name = "decimal"
    type_model_uri = TEST.Decimal


class Time(XSDTime):
    """ A time object represents a (local) time of day, independent of any particular day """
    type_class_uri = XSD.dateTime
    type_class_curie = "xsd:dateTime"
    type_name = "time"
    type_model_uri = TEST.Time


class Date(XSDDate):
    """ a date (year, month and day) in an idealized calendar """
    type_class_uri = XSD.date
    type_class_curie = "xsd:date"
    type_name = "date"
    type_model_uri = TEST.Date


class Datetime(XSDDateTime):
    """ The combination of a date and time """
    type_class_uri = XSD.dateTime
    type_class_curie = "xsd:dateTime"
    type_name = "datetime"
    type_model_uri = TEST.Datetime


class Uriorcurie(URIorCURIE):
    """ a URI or a CURIE """
    type_class_uri = XSD.anyURI
    type_class_curie = "xsd:anyURI"
    type_name = "uriorcurie"
    type_model_uri = TEST.Uriorcurie


class Uri(URI):
    """ a complete URI """
    type_class_uri = XSD.anyURI
    type_class_curie = "xsd:anyURI"
    type_name = "uri"
    type_model_uri = TEST.Uri


class Ncname(NCName):
    """ Prefix part of CURIE """
    type_class_uri = XSD.string
    type_class_curie = "xsd:string"
    type_name = "ncname"
    type_model_uri = TEST.Ncname


class Objectidentifier(ElementIdentifier):
    """ A URI or CURIE that represents an object in the model. """
    type_class_uri = SHEX.iri
    type_class_curie = "shex:iri"
    type_name = "objectidentifier"
    type_model_uri = TEST.Objectidentifier


class Nodeidentifier(NodeIdentifier):
    """ A URI, CURIE or BNODE that represents a node in a model. """
    type_class_uri = SHEX.nonLiteral
    type_class_curie = "shex:nonLiteral"
    type_name = "nodeidentifier"
    type_model_uri = TEST.Nodeidentifier


# Class references



@dataclass
class C1(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = TEST.C1
    class_class_curie: ClassVar[str] = "test:C1"
    class_name: ClassVar[str] = "c1"
    class_model_uri: ClassVar[URIRef] = TEST.C1

    s1: Optional[str] = True
    s1p: Optional[str] = True
    s2: Optional[str] = False
    s2p: Optional[str] = False
    slot_uri: Optional[str] = None
    slot_curie: Optional[str] = None
    class_uri: Optional[str] = None
    class_curie: Optional[str] = None
    bnode: Optional[str] = bnode()
    txt: Optional[str] = "penguins\"doves"
    int: Optional[str] = -1403
    dfltrange: Optional[str] = None
    dfltns: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.s1 is not None and not isinstance(self.s1, str):
            self.s1 = str(self.s1)

        if self.s1p is not None and not isinstance(self.s1p, str):
            self.s1p = str(self.s1p)

        if self.s2 is not None and not isinstance(self.s2, str):
            self.s2 = str(self.s2)

        if self.s2p is not None and not isinstance(self.s2p, str):
            self.s2p = str(self.s2p)

        if self.slot_uri is not None and not isinstance(self.slot_uri, str):
            self.slot_uri = str(self.slot_uri)

        if self.slot_curie is not None and not isinstance(self.slot_curie, str):
            self.slot_curie = str(self.slot_curie)

        if self.class_uri is not None and not isinstance(self.class_uri, str):
            self.class_uri = str(self.class_uri)

        if self.class_curie is not None and not isinstance(self.class_curie, str):
            self.class_curie = str(self.class_curie)

        if self.bnode is not None and not isinstance(self.bnode, str):
            self.bnode = str(self.bnode)

        if self.txt is not None and not isinstance(self.txt, str):
            self.txt = str(self.txt)

        if self.int is not None and not isinstance(self.int, str):
            self.int = str(self.int)

        if self.dfltrange is not None and not isinstance(self.dfltrange, str):
            self.dfltrange = str(self.dfltrange)

        if self.dfltns is not None and not isinstance(self.dfltns, str):
            self.dfltns = str(self.dfltns)

        super().__post_init__(**kwargs)


# Enumerations


# Slots
class slots:
    pass

slots.s1 = Slot(uri=TEST.s1, name="s1", curie=TEST.curie('s1'),
                   model_uri=TEST.s1, domain=None, range=Optional[str])

slots.s1p = Slot(uri=TEST.s1p, name="s1p", curie=TEST.curie('s1p'),
                   model_uri=TEST.s1p, domain=None, range=Optional[str])

slots.s2 = Slot(uri=TEST.s2, name="s2", curie=TEST.curie('s2'),
                   model_uri=TEST.s2, domain=None, range=Optional[str])

slots.s2p = Slot(uri=TEST.s2p, name="s2p", curie=TEST.curie('s2p'),
                   model_uri=TEST.s2p, domain=None, range=Optional[str])

slots.slot_uri = Slot(uri=TEST.slot_uri, name="slot_uri", curie=TEST.curie('slot_uri'),
                   model_uri=TEST.slot_uri, domain=None, range=Optional[str])

slots.slot_curie = Slot(uri=TEST.slot_curie, name="slot_curie", curie=TEST.curie('slot_curie'),
                   model_uri=TEST.slot_curie, domain=None, range=Optional[str])

slots.class_uri = Slot(uri=TEST.class_uri, name="class_uri", curie=TEST.curie('class_uri'),
                   model_uri=TEST.class_uri, domain=None, range=Optional[str])

slots.class_curie = Slot(uri=TEST.class_curie, name="class_curie", curie=TEST.curie('class_curie'),
                   model_uri=TEST.class_curie, domain=None, range=Optional[str])

slots.bnode = Slot(uri=TEST.bnode, name="bnode", curie=TEST.curie('bnode'),
                   model_uri=TEST.bnode, domain=None, range=Optional[str])

slots.txt = Slot(uri=TEST.txt, name="txt", curie=TEST.curie('txt'),
                   model_uri=TEST.txt, domain=None, range=Optional[str])

slots.int = Slot(uri=TEST.int, name="int", curie=TEST.curie('int'),
                   model_uri=TEST.int, domain=None, range=Optional[str])

slots.dfltrange = Slot(uri=TEST.dfltrange, name="dfltrange", curie=TEST.curie('dfltrange'),
                   model_uri=TEST.dfltrange, domain=None, range=Optional[str])

slots.dfltns = Slot(uri=TEST.dfltns, name="dfltns", curie=TEST.curie('dfltns'),
                   model_uri=TEST.dfltns, domain=None, range=Optional[str])
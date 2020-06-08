
# id: http://example.org/tests/timepoint
# description:
# license: https://creativecommons.org/publicdomain/zero/1.0/

import dataclasses
import sys
from typing import Optional, List, Union, Dict, ClassVar, Any
from dataclasses import dataclass
from biolinkml.utils.slot import Slot
from biolinkml.utils.metamodelcore import empty_list, empty_dict, bnode
from biolinkml.utils.yamlutils import YAMLRoot, extended_str, extended_float, extended_int
if sys.version_info < (3, 7, 6):
    from biolinkml.utils.dataclass_extensions_375 import dataclasses_init_fn_with_kwargs
else:
    from biolinkml.utils.dataclass_extensions_376 import dataclasses_init_fn_with_kwargs
from biolinkml.utils.formatutils import camelcase, underscore, sfx
from rdflib import Namespace, URIRef
from biolinkml.utils.curienamespace import CurieNamespace
from biolinkml.utils.metamodelcore import Bool, ElementIdentifier, NCName, NodeIdentifier, URI, URIorCURIE, XSDDate, XSDDateTime, XSDTime

metamodel_version = "1.4.3"

# Overwrite dataclasses _init_fn to add **kwargs in __init__
dataclasses._init_fn = dataclasses_init_fn_with_kwargs

# Namespaces
SHEX = CurieNamespace('shex', 'http://www.w3.org/ns/shex#')
XSD = CurieNamespace('xsd', 'http://www.w3.org/2001/XMLSchema#')
DEFAULT_ = CurieNamespace('', 'http://example.org/tests/timepoint/')


# Types
class TimeType(Time):
    """ A time object represents a (local) time of day, independent of any particular day """
    type_class_uri = XSD.dateTime
    type_class_curie = "xsd:dateTime"
    type_name = "time type"
    type_model_uri = URIRef("http://example.org/tests/timepoint/TimeType")


class String(str):
    """ A character string """
    type_class_uri = XSD.string
    type_class_curie = "xsd:string"
    type_name = "string"
    type_model_uri = URIRef("http://example.org/tests/timepoint/String")


class Integer(int):
    """ An integer """
    type_class_uri = XSD.integer
    type_class_curie = "xsd:integer"
    type_name = "integer"
    type_model_uri = URIRef("http://example.org/tests/timepoint/Integer")


class Boolean(Bool):
    """ A binary (true or false) value """
    type_class_uri = XSD.boolean
    type_class_curie = "xsd:boolean"
    type_name = "boolean"
    type_model_uri = URIRef("http://example.org/tests/timepoint/Boolean")


class Float(float):
    """ A real number that conforms to the xsd:float specification """
    type_class_uri = XSD.float
    type_class_curie = "xsd:float"
    type_name = "float"
    type_model_uri = URIRef("http://example.org/tests/timepoint/Float")


class Double(float):
    """ A real number that conforms to the xsd:double specification """
    type_class_uri = XSD.double
    type_class_curie = "xsd:double"
    type_name = "double"
    type_model_uri = URIRef("http://example.org/tests/timepoint/Double")


class Time(XSDTime):
    """ A time object represents a (local) time of day, independent of any particular day """
    type_class_uri = XSD.dateTime
    type_class_curie = "xsd:dateTime"
    type_name = "time"
    type_model_uri = URIRef("http://example.org/tests/timepoint/Time")


class Date(XSDDate):
    """ a date (year, month and day) in an idealized calendar """
    type_class_uri = XSD.date
    type_class_curie = "xsd:date"
    type_name = "date"
    type_model_uri = URIRef("http://example.org/tests/timepoint/Date")


class Datetime(XSDDateTime):
    """ The combination of a date and time """
    type_class_uri = XSD.dateTime
    type_class_curie = "xsd:dateTime"
    type_name = "datetime"
    type_model_uri = URIRef("http://example.org/tests/timepoint/Datetime")


class Uriorcurie(URIorCURIE):
    """ a URI or a CURIE """
    type_class_uri = XSD.anyURI
    type_class_curie = "xsd:anyURI"
    type_name = "uriorcurie"
    type_model_uri = URIRef("http://example.org/tests/timepoint/Uriorcurie")


class Uri(URI):
    """ a complete URI """
    type_class_uri = XSD.anyURI
    type_class_curie = "xsd:anyURI"
    type_name = "uri"
    type_model_uri = URIRef("http://example.org/tests/timepoint/Uri")


class Ncname(NCName):
    """ Prefix part of CURIE """
    type_class_uri = XSD.string
    type_class_curie = "xsd:string"
    type_name = "ncname"
    type_model_uri = URIRef("http://example.org/tests/timepoint/Ncname")


class Objectidentifier(ElementIdentifier):
    """ A URI or CURIE that represents an object in the model. """
    type_class_uri = SHEX.iri
    type_class_curie = "shex:iri"
    type_name = "objectidentifier"
    type_model_uri = URIRef("http://example.org/tests/timepoint/Objectidentifier")


class Nodeidentifier(NodeIdentifier):
    """ A URI, CURIE or BNODE that represents a node in a model. """
    type_class_uri = SHEX.nonLiteral
    type_class_curie = "shex:nonLiteral"
    type_name = "nodeidentifier"
    type_model_uri = URIRef("http://example.org/tests/timepoint/Nodeidentifier")


# Class references
class GeographicLocationK(extended_str):
    pass


class GeographicLocationAtTimeK(GeographicLocationK):
    pass


@dataclass
class GeographicLocation(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = URIRef("http://example.org/tests/timepoint/GeographicLocation")
    class_class_curie: ClassVar[str] = None
    class_name: ClassVar[str] = "geographic location"
    class_model_uri: ClassVar[URIRef] = URIRef("http://example.org/tests/timepoint/GeographicLocation")

    k: Union[str, GeographicLocationK]

    def __post_init__(self, **kwargs: Dict[str, Any]):
        if self.k is None:
            raise ValueError(f"k must be supplied")
        if not isinstance(self.k, GeographicLocationK):
            self.k = GeographicLocationK(self.k)
        super().__post_init__(**kwargs)


@dataclass
class GeographicLocationAtTime(GeographicLocation):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = URIRef("http://example.org/tests/timepoint/GeographicLocationAtTime")
    class_class_curie: ClassVar[str] = None
    class_name: ClassVar[str] = "geographic location at time"
    class_model_uri: ClassVar[URIRef] = URIRef("http://example.org/tests/timepoint/GeographicLocationAtTime")

    k: Union[str, GeographicLocationAtTimeK] = None
    timepoint: Optional[Union[str, TimeType]] = None

    def __post_init__(self, **kwargs: Dict[str, Any]):
        if self.k is None:
            raise ValueError(f"k must be supplied")
        if not isinstance(self.k, GeographicLocationAtTimeK):
            self.k = GeographicLocationAtTimeK(self.k)
        if self.timepoint is not None and not isinstance(self.timepoint, TimeType):
            self.timepoint = TimeType(self.timepoint)
        super().__post_init__(**kwargs)



# Slots
class slots:
    pass

slots.k = Slot(uri=DEFAULT_.k, name="k", curie=DEFAULT_.curie('k'),
                      model_uri=DEFAULT_.k, domain=GeographicLocation, range=Union[str, GeographicLocationK])

slots.timepoint = Slot(uri=DEFAULT_.timepoint, name="timepoint", curie=DEFAULT_.curie('timepoint'),
                      model_uri=DEFAULT_.timepoint, domain=GeographicLocationAtTime, range=Optional[Union[str, TimeType]])
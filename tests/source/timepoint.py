
# id: http://example.org/tests/timepoint
# description:
# license: https://creativecommons.org/publicdomain/zero/1.0/

from typing import Optional, List, Union, Dict, ClassVar
from dataclasses import dataclass
from biolinkml.utils.metamodelcore import empty_list, empty_dict, bnode
from biolinkml.utils.yamlutils import YAMLRoot
from biolinkml.utils.formatutils import camelcase, underscore, sfx
from rdflib import Namespace, URIRef
from biolinkml.utils.metamodelcore import XSDTime
from includes.types import String, Time

metamodel_version = "1.4.1"


# Namespaces
SHEX = Namespace('http://www.w3.org/ns/shex#')
XSD = Namespace('http://www.w3.org/2001/XMLSchema#')
DEFAULT_ = Namespace('http://example.org/tests/timepoint/')


# Types
class TimeType(Time):
    """ A time object represents a (local) time of day, independent of any particular day """
    type_class_uri = XSD.dateTime
    type_class_curie = "xsd:dateTime"
    type_name = "time type"
    type_model_uri = URIRef("http://example.org/tests/timepoint/TimeType")


# Class references
class GeographicLocationK(str):
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

    def __post_init__(self):
        if self.k is None:
            raise ValueError(f"k must be supplied")
        if self.k is not None and not isinstance(self.k, GeographicLocationK):
            self.k = GeographicLocationK(self.k)
        super().__post_init__()


@dataclass
class GeographicLocationAtTime(GeographicLocation):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = URIRef("http://example.org/tests/timepoint/GeographicLocationAtTime")
    class_class_curie: ClassVar[str] = None
    class_name: ClassVar[str] = "geographic location at time"
    class_model_uri: ClassVar[URIRef] = URIRef("http://example.org/tests/timepoint/GeographicLocationAtTime")

    k: Union[str, GeographicLocationAtTimeK] = None
    timepoint: Optional[Union[str, TimeType]] = None

    def __post_init__(self):
        if self.k is None:
            raise ValueError(f"k must be supplied")
        if self.k is not None and not isinstance(self.k, GeographicLocationAtTimeK):
            self.k = GeographicLocationAtTimeK(self.k)
        if self.timepoint is not None and not isinstance(self.timepoint, TimeType):
            self.timepoint = TimeType(self.timepoint)
        super().__post_init__()

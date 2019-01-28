
# id: http://example.org/tests/timepoint
# description:
# license: https://creativecommons.org/publicdomain/zero/1.0/

from typing import Optional, List, Union, Dict
from dataclasses import dataclass
from biolinkml.utils.metamodelcore import empty_list, empty_dict
from biolinkml.utils.yamlutils import YAMLRoot
from biolinkml.utils.metamodelcore import Bool, URIorCURIE, NCName
from datetime import time, date, datetime

metamodel_version = "None"

inherited_slots: List[str] = []


# Types
class TimeType(Time):
    """ A time object represents a (local) time of day, independent of any particular day """
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
class GeographicLocationK(str):
    pass


class GeographicLocationAtTimeK(GeographicLocationK):
    pass


@dataclass
class GeographicLocation(YAMLRoot):

    # === geographic location ===
    k: Union[str, GeographicLocationK]

    def _fix_elements(self):
        super()._fix_elements()
        if not isinstance(self.k, GeographicLocationK):
            self.k = GeographicLocationK(self.k)


@dataclass
class GeographicLocationAtTime(GeographicLocation):

    # === geographic location ===
    k: Union[str, GeographicLocationAtTimeK]

    # === geographic location at time ===
    timepoint: Optional[Union[time, TimeType]] = None

    def _fix_elements(self):
        super()._fix_elements()
        if self.k and not isinstance(self.k, GeographicLocationAtTimeK):
            self.k = GeographicLocationAtTimeK(self.k)
        if self.timepoint and not isinstance(self.timepoint, TimeType):
            self.timepoint = TimeType(self.timepoint)

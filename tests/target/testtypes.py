
# id: http://example.org/tests/types
# description:
# license:

from typing import Optional, List, Union, Dict
from dataclasses import dataclass
from biolinkml.utils.metamodelcore import empty_list, empty_dict
from biolinkml.utils.yamlutils import YAMLRoot
from biolinkml.utils.metamodelcore import Bool

metamodel_version = "None"

inherited_slots: List[str] = []


# Types
class String(str):
    pass


class Boolean(Bool):
    pass


class BooleanType(Boolean):
    pass


class StringType(String):
    pass


# Class references



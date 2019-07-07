
# id: http://example.org/tests/types
# description:
# license:

from typing import Optional, List, Union, Dict, ClassVar
from dataclasses import dataclass
from biolinkml.utils.metamodelcore import empty_list, empty_dict, bnode
from biolinkml.utils.yamlutils import YAMLRoot
from biolinkml.utils.formatutils import camelcase, underscore, sfx
from rdflib import Namespace
from biolinkml.utils.metamodelcore import Bool

metamodel_version = "1.4.0"


# Namespaces
DEFAULT_ = Namespace('http://example.org/tests/types/')


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




# id: http://example.org/tests/namespace
# description:
# license: https://creativecommons.org/publicdomain/zero/1.0/

from typing import Optional, List, Union, Dict, ClassVar
from dataclasses import dataclass
from biolinkml.utils.metamodelcore import empty_list, empty_dict, bnode
from biolinkml.utils.yamlutils import YAMLRoot
from biolinkml.utils.formatutils import camelcase, underscore, sfx
from rdflib import Namespace
from includes.types import String

metamodel_version = "1.3.6"


# Namespaces
META = Namespace('https://w3id.org/biolink/biolinkml/meta/')
METATYPE = Namespace('https://w3id.org/biolink/biolinkml/type/')
TEST = Namespace('http://example.org/test/')
XSD = Namespace('http://www.w3.org/2001/XMLSchema#')
DEFAULT_ = Namespace('http://example.org/tests/namespace/')


# Types

# Class references



@dataclass
class C1(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    type_uri: ClassVar[str] = "http://example.org/tests/namespace/C1"
    type_curie: ClassVar[str] = None
    type_name: ClassVar[str] = "c1"

    s1: Optional[str] = None
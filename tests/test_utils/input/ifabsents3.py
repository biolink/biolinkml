# Auto generated from .yaml by pythongen.py version:
# Generation date:
# Schema: ifabsent
#
# id: http://example.org/tests/ifabsent
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
SKOS = Namespace('http://www.w3.org/2004/02/skos/core#')
TEST = Namespace('http://example.org/tests/ifabsent/')
XSD = Namespace('http://www.w3.org/2001/XMLSchema#')
DEFAULT_ = TEST


# Types

# Class references



@dataclass
class C1(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    type_uri: ClassVar[str] = "http://example.org/tests/ifabsent/C1"
    type_curie: ClassVar[str] = "test:C1"
    type_name: ClassVar[str] = "c1"

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
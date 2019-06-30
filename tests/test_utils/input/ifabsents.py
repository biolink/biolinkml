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
from rdflib import Namespace
from includes.types import String

metamodel_version = "1.3.6"


# Namespaces
META = Namespace('https://w3id.org/biolink/biolinkml/meta/')
METATYPE = Namespace('https://w3id.org/biolink/biolinkml/type/')
SKOS = Namespace('http://www.w3.org/2004/02/skos/core#')
TEST = Namespace('http://example.org/test/')
XSD = Namespace('http://www.w3.org/2001/XMLSchema#')


# Types

# Class references



@dataclass
class C1(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    type_uri: ClassVar[str] = "http://example.org/tests/ifabsent/C1"
    type_curie: ClassVar[str] = ":C1"
    type_name: ClassVar[str] = "c1"

    s1: Optional[str] = True
    s1p: Optional[str] = True
    s2: Optional[str] = False
    s2p: Optional[str] = False
    s3: Optional[str] = "http://example.org/tests/ifabsent/s3"
    s4: Optional[str] = ":s4"
    s5: Optional[str] = "http://example.org/tests/ifabsent/C1"
    s6: Optional[str] = ":C1"
    s7: Optional[str] = bnode
    s8: Optional[str] = "penguins\"doves"
    s9: Optional[str] = -1403
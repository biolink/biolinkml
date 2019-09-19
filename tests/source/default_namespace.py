
# id: http://example.org/tests/namespace
# description:
# license: https://creativecommons.org/publicdomain/zero/1.0/

from typing import Optional, List, Union, Dict, ClassVar
from dataclasses import dataclass
from biolinkml.utils.metamodelcore import empty_list, empty_dict, bnode
from biolinkml.utils.yamlutils import YAMLRoot
from biolinkml.utils.formatutils import camelcase, underscore, sfx
from rdflib import Namespace, URIRef
from includes.types import String

metamodel_version = "1.4.1"


# Namespaces
SHEX = Namespace('http://www.w3.org/ns/shex#')
XSD = Namespace('http://www.w3.org/2001/XMLSchema#')
DEFAULT_ = Namespace('http://example.org/tests/namespace/')


# Types

# Class references



@dataclass
class C1(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = URIRef("http://example.org/tests/namespace/C1")
    class_class_curie: ClassVar[str] = None
    class_name: ClassVar[str] = "c1"
    class_model_uri: ClassVar[URIRef] = URIRef("http://example.org/tests/namespace/C1")

    s1: Optional[str] = None
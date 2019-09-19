# Auto generated from .yaml by pythongen.py version:
# Generation date:
# Schema:
#
# id: http://example.com
# description:
# license:

from typing import Optional, List, Union, Dict, ClassVar
from dataclasses import dataclass
from biolinkml.utils.metamodelcore import empty_list, empty_dict, bnode
from biolinkml.utils.yamlutils import YAMLRoot
from biolinkml.utils.formatutils import camelcase, underscore, sfx
from rdflib import Namespace, URIRef


metamodel_version = "1.4.1"


# Namespaces
XSD = Namespace('http://www.w3.org/2001/XMLSchema#')
DEFAULT_ = Namespace('http://example.com/')


# Types
class String(str):
    type_class_uri = XSD.string
    type_class_curie = "xsd:string"
    type_name = "string"
    type_model_uri = URIRef("http://example.com/String")


# Class references
class TestClass1Id(str):
    pass


class TestClass2Id(str):
    pass


class TestClass3Id(str):
    pass


@dataclass
class TestClass1(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = URIRef("http://example.com/TestClass1")
    class_class_curie: ClassVar[str] = None
    class_name: ClassVar[str] = "test class 1"
    class_model_uri: ClassVar[URIRef] = URIRef("http://example.com/TestClass1")

    id: Union[str, TestClass1Id]
    required_mixin_slot: str

    def __post_init__(self):
        if self.id is None:
            raise ValueError(f"id must be supplied")
        if self.id is not None and not isinstance(self.id, TestClass1Id):
            self.id = TestClass1Id(self.id)
        super().__post_init__()


@dataclass
class TestClass2(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = URIRef("http://example.com/TestClass2")
    class_class_curie: ClassVar[str] = None
    class_name: ClassVar[str] = "test class 2"
    class_model_uri: ClassVar[URIRef] = URIRef("http://example.com/TestClass2")

    id: Union[str, TestClass2Id]
    required_mixin_slot: str
    optional_mixin_slot: Optional[str] = None

    def __post_init__(self):
        if self.id is None:
            raise ValueError(f"id must be supplied")
        if self.id is not None and not isinstance(self.id, TestClass2Id):
            self.id = TestClass2Id(self.id)
        if self.required_mixin_slot is None:
            raise ValueError(f"required_mixin_slot must be supplied")
        super().__post_init__()


@dataclass
class TestClass3(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = URIRef("http://example.com/TestClass3")
    class_class_curie: ClassVar[str] = None
    class_name: ClassVar[str] = "test class 3"
    class_model_uri: ClassVar[URIRef] = URIRef("http://example.com/TestClass3")

    id: Union[str, TestClass3Id]
    required_domain_slot: str

    def __post_init__(self):
        if self.id is None:
            raise ValueError(f"id must be supplied")
        if self.id is not None and not isinstance(self.id, TestClass3Id):
            self.id = TestClass3Id(self.id)
        super().__post_init__()

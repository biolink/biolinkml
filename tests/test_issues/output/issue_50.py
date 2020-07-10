# Auto generated from issue_50.yaml by pythongen.py version: 0.4.0
# Generation date: 2020-07-10 13:32
# Schema:
#
# id: http://example.com
# description:
# license:

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


metamodel_version = "1.5.1"

# Overwrite dataclasses _init_fn to add **kwargs in __init__
dataclasses._init_fn = dataclasses_init_fn_with_kwargs

# Namespaces
XSD = CurieNamespace('xsd', 'http://www.w3.org/2001/XMLSchema#')
DEFAULT_ = CurieNamespace('', 'http://example.com/')


# Types
class String(str):
    type_class_uri = XSD.string
    type_class_curie = "xsd:string"
    type_name = "string"
    type_model_uri = URIRef("http://example.com/String")


# Class references
class TestClass1Id(extended_str):
    pass


class TestClass2Id(extended_str):
    pass


class TestClass3Id(extended_str):
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
    optional_mixin_slot: Optional[str] = None

    def __post_init__(self, **kwargs: Dict[str, Any]):
        if self.id is None:
            raise ValueError(f"id must be supplied")
        if not isinstance(self.id, TestClass1Id):
            self.id = TestClass1Id(self.id)
        if self.required_mixin_slot is None:
            raise ValueError(f"required_mixin_slot must be supplied")
        super().__post_init__(**kwargs)


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

    def __post_init__(self, **kwargs: Dict[str, Any]):
        if self.id is None:
            raise ValueError(f"id must be supplied")
        if not isinstance(self.id, TestClass2Id):
            self.id = TestClass2Id(self.id)
        if self.required_mixin_slot is None:
            raise ValueError(f"required_mixin_slot must be supplied")
        super().__post_init__(**kwargs)


@dataclass
class TestClass3(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = URIRef("http://example.com/TestClass3")
    class_class_curie: ClassVar[str] = None
    class_name: ClassVar[str] = "test class 3"
    class_model_uri: ClassVar[URIRef] = URIRef("http://example.com/TestClass3")

    id: Union[str, TestClass3Id]

    def __post_init__(self, **kwargs: Dict[str, Any]):
        if self.id is None:
            raise ValueError(f"id must be supplied")
        if not isinstance(self.id, TestClass3Id):
            self.id = TestClass3Id(self.id)
        super().__post_init__(**kwargs)



# Slots
class slots:
    pass

slots.id = Slot(uri=DEFAULT_.id, name="id", curie=DEFAULT_.curie('id'),
                      model_uri=DEFAULT_.id, domain=None, range=URIRef)

slots.optional_mixin_slot = Slot(uri=DEFAULT_.optional_mixin_slot, name="optional_mixin_slot", curie=DEFAULT_.curie('optional_mixin_slot'),
                      model_uri=DEFAULT_.optional_mixin_slot, domain=None, range=Optional[str])

slots.required_mixin_slot = Slot(uri=DEFAULT_.required_mixin_slot, name="required_mixin_slot", curie=DEFAULT_.curie('required_mixin_slot'),
                      model_uri=DEFAULT_.required_mixin_slot, domain=None, range=str)

slots.optional_domain_slot = Slot(uri=DEFAULT_.optional_domain_slot, name="optional_domain_slot", curie=DEFAULT_.curie('optional_domain_slot'),
                      model_uri=DEFAULT_.optional_domain_slot, domain=TestClass3, range=Optional[str])

slots.required_domain_slot = Slot(uri=DEFAULT_.required_domain_slot, name="required_domain_slot", curie=DEFAULT_.curie('required_domain_slot'),
                      model_uri=DEFAULT_.required_domain_slot, domain=TestClass3, range=str)
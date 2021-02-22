# Auto generated from issue_14.yaml by pythongen.py version: 0.9.0
# Generation date: 2021-01-04 21:53
# Schema: test14
#
# id: https://example.com/test14
# description:
# license: https://creativecommons.org/publicdomain/zero/1.0/

import dataclasses
import sys
import re
from typing import Optional, List, Union, Dict, ClassVar, Any
from dataclasses import dataclass
from biolinkml.meta import EnumDefinition, PermissibleValue, PvFormulaOptions

from biolinkml.utils.slot import Slot
from biolinkml.utils.metamodelcore import empty_list, empty_dict, bnode
from biolinkml.utils.yamlutils import YAMLRoot, extended_str, extended_float, extended_int
if sys.version_info < (3, 7, 6):
    from biolinkml.utils.dataclass_extensions_375 import dataclasses_init_fn_with_kwargs
else:
    from biolinkml.utils.dataclass_extensions_376 import dataclasses_init_fn_with_kwargs
from biolinkml.utils.formatutils import camelcase, underscore, sfx
from biolinkml.utils.enumerations import EnumDefinitionImpl
from rdflib import Namespace, URIRef
from biolinkml.utils.curienamespace import CurieNamespace
from includes.types import String

metamodel_version = "1.7.0"

# Overwrite dataclasses _init_fn to add **kwargs in __init__
dataclasses._init_fn = dataclasses_init_fn_with_kwargs

# Namespaces
META = CurieNamespace('meta', 'https://w3id.org/biolink/biolinkml/')
DEFAULT_ = CurieNamespace('', 'https://example.com/test14/')


# Types

# Class references
class NamedThingId(extended_str):
    pass


class MixinOwnerId(NamedThingId):
    pass


class SubjectRange1Id(NamedThingId):
    pass


class ObjectRange1Id(NamedThingId):
    pass


@dataclass
class NamedThing(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = URIRef("https://example.com/test14/NamedThing")
    class_class_curie: ClassVar[str] = None
    class_name: ClassVar[str] = "named thing"
    class_model_uri: ClassVar[URIRef] = URIRef("https://example.com/test14/NamedThing")

    id: Union[str, NamedThingId] = None
    name: str = None
    subject: Union[str, NamedThingId] = None
    object: Union[str, NamedThingId] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.id is None:
            raise ValueError("id must be supplied")
        if not isinstance(self.id, NamedThingId):
            self.id = NamedThingId(self.id)

        if self.name is None:
            raise ValueError("name must be supplied")
        if not isinstance(self.name, str):
            self.name = str(self.name)

        if self.subject is None:
            raise ValueError("subject must be supplied")
        if not isinstance(self.subject, NamedThingId):
            self.subject = NamedThingId(self.subject)

        if self.object is None:
            raise ValueError("object must be supplied")
        if not isinstance(self.object, NamedThingId):
            self.object = NamedThingId(self.object)

        super().__post_init__(**kwargs)


@dataclass
class MixinOwner(NamedThing):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = URIRef("https://example.com/test14/MixinOwner")
    class_class_curie: ClassVar[str] = None
    class_name: ClassVar[str] = "mixin_owner"
    class_model_uri: ClassVar[URIRef] = URIRef("https://example.com/test14/MixinOwner")

    id: Union[str, MixinOwnerId] = None
    name: str = None
    object: Union[str, NamedThingId] = None
    subject: Union[str, SubjectRange1Id] = None
    sex_qualifier: Optional[Union[str, NamedThingId]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.id is None:
            raise ValueError("id must be supplied")
        if not isinstance(self.id, MixinOwnerId):
            self.id = MixinOwnerId(self.id)

        if self.subject is None:
            raise ValueError("subject must be supplied")
        if not isinstance(self.subject, SubjectRange1Id):
            self.subject = SubjectRange1Id(self.subject)

        if self.sex_qualifier is not None and not isinstance(self.sex_qualifier, NamedThingId):
            self.sex_qualifier = NamedThingId(self.sex_qualifier)

        super().__post_init__(**kwargs)


@dataclass
class SubjectRange1(NamedThing):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = URIRef("https://example.com/test14/SubjectRange1")
    class_class_curie: ClassVar[str] = None
    class_name: ClassVar[str] = "subject_range_1"
    class_model_uri: ClassVar[URIRef] = URIRef("https://example.com/test14/SubjectRange1")

    id: Union[str, SubjectRange1Id] = None
    name: str = None
    subject: Union[str, NamedThingId] = None
    object: Union[str, NamedThingId] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.id is None:
            raise ValueError("id must be supplied")
        if not isinstance(self.id, SubjectRange1Id):
            self.id = SubjectRange1Id(self.id)

        super().__post_init__(**kwargs)


@dataclass
class ObjectRange1(NamedThing):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = URIRef("https://example.com/test14/ObjectRange1")
    class_class_curie: ClassVar[str] = None
    class_name: ClassVar[str] = "object_range_1"
    class_model_uri: ClassVar[URIRef] = URIRef("https://example.com/test14/ObjectRange1")

    id: Union[str, ObjectRange1Id] = None
    name: str = None
    subject: Union[str, NamedThingId] = None
    object: Union[str, NamedThingId] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.id is None:
            raise ValueError("id must be supplied")
        if not isinstance(self.id, ObjectRange1Id):
            self.id = ObjectRange1Id(self.id)

        super().__post_init__(**kwargs)


@dataclass
class MixinClass(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = URIRef("https://example.com/test14/MixinClass")
    class_class_curie: ClassVar[str] = None
    class_name: ClassVar[str] = "mixin_class"
    class_model_uri: ClassVar[URIRef] = URIRef("https://example.com/test14/MixinClass")

    object: Union[str, ObjectRange1Id] = None
    sex_qualifier: Optional[Union[str, NamedThingId]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.object is None:
            raise ValueError("object must be supplied")
        if not isinstance(self.object, ObjectRange1Id):
            self.object = ObjectRange1Id(self.object)

        if self.sex_qualifier is not None and not isinstance(self.sex_qualifier, NamedThingId):
            self.sex_qualifier = NamedThingId(self.sex_qualifier)

        super().__post_init__(**kwargs)


# Enumerations


# Slots
class slots:
    pass

slots.id = Slot(uri=DEFAULT_.id, name="id", curie=DEFAULT_.curie('id'),
                   model_uri=DEFAULT_.id, domain=NamedThing, range=Union[str, NamedThingId])

slots.name = Slot(uri=DEFAULT_.name, name="name", curie=DEFAULT_.curie('name'),
                   model_uri=DEFAULT_.name, domain=NamedThing, range=str)

slots.subject = Slot(uri=DEFAULT_.subject, name="subject", curie=DEFAULT_.curie('subject'),
                   model_uri=DEFAULT_.subject, domain=None, range=Union[str, NamedThingId])

slots.object = Slot(uri=DEFAULT_.object, name="object", curie=DEFAULT_.curie('object'),
                   model_uri=DEFAULT_.object, domain=None, range=Union[str, NamedThingId])

slots.sex_qualifier = Slot(uri=DEFAULT_.sex_qualifier, name="sex qualifier", curie=DEFAULT_.curie('sex_qualifier'),
                   model_uri=DEFAULT_.sex_qualifier, domain=None, range=Optional[Union[str, NamedThingId]])

slots.mixin_owner_subject = Slot(uri=DEFAULT_.subject, name="mixin_owner_subject", curie=DEFAULT_.curie('subject'),
                   model_uri=DEFAULT_.mixin_owner_subject, domain=MixinOwner, range=Union[str, SubjectRange1Id])

slots.mixin_class_object = Slot(uri=DEFAULT_.object, name="mixin_class_object", curie=DEFAULT_.curie('object'),
                   model_uri=DEFAULT_.mixin_class_object, domain=MixinClass, range=Union[str, ObjectRange1Id])
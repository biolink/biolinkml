# Auto generated from issue_80.yaml by pythongen.py version: 0.9.0
# Generation date: 2021-01-04 21:53
# Schema: Issue_80_test_case
#
# id: http://example.org/issues/80
# description: Example identifier
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
from biolinkml.utils.metamodelcore import ElementIdentifier
from includes.types import Integer, Objectidentifier, String

metamodel_version = "1.7.0"

# Overwrite dataclasses _init_fn to add **kwargs in __init__
dataclasses._init_fn = dataclasses_init_fn_with_kwargs

# Namespaces
BIOLINK = CurieNamespace('biolink', 'https://w3id.org/biolink/vocab/')
BIOLINKML = CurieNamespace('biolinkml', 'https://w3id.org/biolink/biolinkml/')
EX = CurieNamespace('ex', 'http://example.org/')
MODEL = CurieNamespace('model', 'https://w3id.org/biolink/')
DEFAULT_ = BIOLINK


# Types

# Class references
class PersonId(ElementIdentifier):
    pass


@dataclass
class Person(YAMLRoot):
    """
    A person, living or dead
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = EX.PERSON
    class_class_curie: ClassVar[str] = "ex:PERSON"
    class_name: ClassVar[str] = "person"
    class_model_uri: ClassVar[URIRef] = BIOLINK.Person

    id: Union[str, PersonId] = None
    name: str = None
    age: Optional[int] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.id is None:
            raise ValueError("id must be supplied")
        if not isinstance(self.id, PersonId):
            self.id = PersonId(self.id)

        if self.name is None:
            raise ValueError("name must be supplied")
        if not isinstance(self.name, str):
            self.name = str(self.name)

        if self.age is not None and not isinstance(self.age, int):
            self.age = int(self.age)

        super().__post_init__(**kwargs)


# Enumerations


# Slots
class slots:
    pass

slots.id = Slot(uri=BIOLINK.id, name="id", curie=BIOLINK.curie('id'),
                   model_uri=BIOLINK.id, domain=None, range=URIRef)

slots.name = Slot(uri=BIOLINK.name, name="name", curie=BIOLINK.curie('name'),
                   model_uri=BIOLINK.name, domain=None, range=str)

slots.age = Slot(uri=BIOLINK.age, name="age", curie=BIOLINK.curie('age'),
                   model_uri=BIOLINK.age, domain=None, range=Optional[int])
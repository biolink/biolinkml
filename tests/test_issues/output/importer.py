# Auto generated from importer.yaml by pythongen.py version: 0.9.0
# Generation date: 2021-01-04 21:53
# Schema: importer
#
# id: https://example.org/importer
# description: Test of local import with an identifier
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
from . importee import Base, BaseId, String

metamodel_version = "1.7.0"

# Overwrite dataclasses _init_fn to add **kwargs in __init__
dataclasses._init_fn = dataclasses_init_fn_with_kwargs

# Namespaces
EX = CurieNamespace('ex', 'https://example.org/importee/')
DEFAULT_ = EX


# Types

# Class references
class ChildId(BaseId):
    pass


@dataclass
class Child(Base):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = EX.Child
    class_class_curie: ClassVar[str] = "ex:Child"
    class_name: ClassVar[str] = "child"
    class_model_uri: ClassVar[URIRef] = EX.Child

    id: Union[str, ChildId] = None
    value: str = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.id is None:
            raise ValueError("id must be supplied")
        if not isinstance(self.id, ChildId):
            self.id = ChildId(self.id)

        super().__post_init__(**kwargs)


# Enumerations


# Slots
class slots:
    pass


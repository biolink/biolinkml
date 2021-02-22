# Auto generated from issue_368.yaml by pythongen.py version: 0.9.0
# Generation date: 2021-02-16 19:05
# Schema: schema
#
# id: https://microbiomedata/schema
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
from . issues_368_imports import E, ParentClass

metamodel_version = "1.7.0"

# Overwrite dataclasses _init_fn to add **kwargs in __init__
dataclasses._init_fn = dataclasses_init_fn_with_kwargs

# Namespaces
BIOLINKML = CurieNamespace('biolinkml', 'https://w3id.org/biolink/biolinkml/')
DEFAULT_ = CurieNamespace('', 'https://microbiomedata/schema/')


# Types

# Class references



@dataclass
class C(ParentClass):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = URIRef("https://microbiomedata/schema/C")
    class_class_curie: ClassVar[str] = None
    class_name: ClassVar[str] = "c"
    class_model_uri: ClassVar[URIRef] = URIRef("https://microbiomedata/schema/C")

    s: Optional[Union[str, "E"]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.s is not None and not isinstance(self.s, E):
            self.s = E(self.s)

        super().__post_init__(**kwargs)


# Enumerations


# Slots
class slots:
    pass

slots.s = Slot(uri=DEFAULT_.s, name="s", curie=DEFAULT_.curie('s'),
                   model_uri=DEFAULT_.s, domain=None, range=Optional[Union[str, "E"]])
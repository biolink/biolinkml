# Auto generated from file2.yaml by pythongen.py version: 0.9.0
# Generation date: 2021-01-04 21:53
# Schema: valuesetresolution
#
# id: https://hotecosystem.org/tccm/valuesetresolution
# description:
# license:

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


metamodel_version = "1.7.0"

# Overwrite dataclasses _init_fn to add **kwargs in __init__
dataclasses._init_fn = dataclasses_init_fn_with_kwargs

# Namespaces
BIOLINKML = CurieNamespace('biolinkml', 'https://w3id.org/biolink/biolinkml/')
TCCM = CurieNamespace('tccm', 'https://hotecosystem.org/tccm/')
DEFAULT_ = TCCM


# Types

# Class references



@dataclass
class IterableResolvedValueSet(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = TCCM.IterableResolvedValueSet
    class_class_curie: ClassVar[str] = "tccm:IterableResolvedValueSet"
    class_name: ClassVar[str] = "IterableResolvedValueSet"
    class_model_uri: ClassVar[URIRef] = TCCM.IterableResolvedValueSet

    complete: Union[str, "CompleteDirectory"] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.complete is None:
            raise ValueError("complete must be supplied")
        if not isinstance(self.complete, CompleteDirectory):
            self.complete = CompleteDirectory(self.complete)

        super().__post_init__(**kwargs)


@dataclass
class Directory(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = TCCM["directories_and_lists/Directory"]
    class_class_curie: ClassVar[str] = "tccm:directories_and_lists/Directory"
    class_name: ClassVar[str] = "Directory"
    class_model_uri: ClassVar[URIRef] = TCCM.Directory

    complete: Union[str, "CompleteDirectory"] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.complete is None:
            raise ValueError("complete must be supplied")
        if not isinstance(self.complete, CompleteDirectory):
            self.complete = CompleteDirectory(self.complete)

        super().__post_init__(**kwargs)


# Enumerations
class CompleteDirectory(EnumDefinitionImpl):

    COMPLETE = PermissibleValue(text="COMPLETE",
                                       description="The Directory contains all of the qualifying entries")
    PARTIAL = PermissibleValue(text="PARTIAL",
                                     description="The directory contains only a partial listing of the qualifying entries.")

    _defn = EnumDefinition(
        name="CompleteDirectory",
    )

# Slots
class slots:
    pass

slots.directory__complete = Slot(uri=TCCM.complete, name="directory__complete", curie=TCCM.curie('complete'),
                   model_uri=TCCM.directory__complete, domain=None, range=Union[str, "CompleteDirectory"])
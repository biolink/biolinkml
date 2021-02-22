# Auto generated from issue_260.yaml by pythongen.py version: 0.9.0
# Generation date: 2021-01-04 21:53
# Schema: issue_260
#
# id: http://example.org/tests/issue_260
# description: Test relative imports
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
from . issue_260a import C260a, String
from ..issue_260.issue_260b import C260b
from .issue_260c import C260c

metamodel_version = "1.7.0"

# Overwrite dataclasses _init_fn to add **kwargs in __init__
dataclasses._init_fn = dataclasses_init_fn_with_kwargs

# Namespaces
DEFAULT_ = CurieNamespace('', 'http://example.org/tests/issue_260/')


# Types

# Class references



class C2601(C260a):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = URIRef("http://example.org/tests/issue_260/C2601")
    class_class_curie: ClassVar[str] = None
    class_name: ClassVar[str] = "c2601"
    class_model_uri: ClassVar[URIRef] = URIRef("http://example.org/tests/issue_260/C2601")


class C2602(C260b):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = URIRef("http://example.org/tests/issue_260/C2602")
    class_class_curie: ClassVar[str] = None
    class_name: ClassVar[str] = "c2602"
    class_model_uri: ClassVar[URIRef] = URIRef("http://example.org/tests/issue_260/C2602")


class C2603(C260c):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = URIRef("http://example.org/tests/issue_260/C2603")
    class_class_curie: ClassVar[str] = None
    class_name: ClassVar[str] = "c2603"
    class_model_uri: ClassVar[URIRef] = URIRef("http://example.org/tests/issue_260/C2603")


# Enumerations


# Slots
class slots:
    pass


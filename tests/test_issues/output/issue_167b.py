# Auto generated from issue_167b.yaml by pythongen.py version: 0.9.0
# Generation date: 2021-01-05 21:36
# Schema: annotations_test
#
# id: http://example.org/tests/issue167b
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


metamodel_version = "1.7.0"

# Overwrite dataclasses _init_fn to add **kwargs in __init__
dataclasses._init_fn = dataclasses_init_fn_with_kwargs

# Namespaces
BIOLINKML = CurieNamespace('biolinkml', 'https://w3id.org/biolink/biolinkml/')
EX = CurieNamespace('ex', 'http://example.org/')
DEFAULT_ = EX


# Types

# Class references



class MyClass(YAMLRoot):
    """
    Annotations as tag value pairs. Note that altLabel is defined in the default namespace, not in the SKOS namespace
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = EX.MyClass
    class_class_curie: ClassVar[str] = "ex:MyClass"
    class_name: ClassVar[str] = "my class"
    class_model_uri: ClassVar[URIRef] = EX.MyClass


class MyClass2(YAMLRoot):
    """
    -> This form of annotations is a tag/value format, which allows annotations to be annotated. Note, however, that
    the annotation source is NOT a CURIE, rather just a string.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = EX.MyClass2
    class_class_curie: ClassVar[str] = "ex:MyClass2"
    class_name: ClassVar[str] = "my class 2"
    class_model_uri: ClassVar[URIRef] = EX.MyClass2


# Enumerations


# Slots
class slots:
    pass


# Auto generated from issue_167b.yaml by pythongen.py version: 0.4.0
# Generation date: 2020-08-04 17:48
# Schema: annotations_test
#
# id: http://example.org/tests/issue167b
# description:
# license: https://creativecommons.org/publicdomain/zero/1.0/

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
from biolinkml.utils.metamodelcore import Bool
from includes.annotations import Annotation
from includes.types import Boolean

metamodel_version = "1.5.3"

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



# Slots
class slots:
    pass

slots.annotation_extension_value = Slot(uri=EX.value, name="annotation_extension_value", curie=EX.curie('value'),
                      model_uri=EX.annotation_extension_value, domain=Annotation, range=Bool)
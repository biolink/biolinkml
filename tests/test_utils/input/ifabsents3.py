# Auto generated from .yaml by pythongen.py version:
# Generation date:
# Schema: ifabsent
#
# id: http://example.org/tests/ifabsent
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
from includes.types import String

metamodel_version = "1.4.3"

# Overwrite dataclasses _init_fn to add **kwargs in __init__
dataclasses._init_fn = dataclasses_init_fn_with_kwargs

# Namespaces
SKOS = CurieNamespace('skos', 'http://www.w3.org/2004/02/skos/core#')
TEST = CurieNamespace('test', 'http://example.org/tests/ifabsent/')
DEFAULT_ = TEST


# Types

# Class references



@dataclass
class C1(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = TEST.C1
    class_class_curie: ClassVar[str] = "test:C1"
    class_name: ClassVar[str] = "c1"
    class_model_uri: ClassVar[URIRef] = TEST.C1

    s1: Optional[str] = True
    s1p: Optional[str] = True
    s2: Optional[str] = False
    s2p: Optional[str] = False
    slot_uri: Optional[str] = None
    slot_curie: Optional[str] = None
    class_uri: Optional[str] = None
    class_curie: Optional[str] = None
    bnode: Optional[str] = bnode()
    txt: Optional[str] = "penguins\"doves"
    int: Optional[str] = -1403
    dfltrange: Optional[str] = None
    dfltns: Optional[str] = None


# Slots
class slots:
    pass

slots.s1 = Slot(uri=TEST.s1, name="s1", curie=TEST.curie('s1'),
                      model_uri=TEST.s1, domain=None, range=Optional[str])

slots.s1p = Slot(uri=TEST.s1p, name="s1p", curie=TEST.curie('s1p'),
                      model_uri=TEST.s1p, domain=None, range=Optional[str])

slots.s2 = Slot(uri=TEST.s2, name="s2", curie=TEST.curie('s2'),
                      model_uri=TEST.s2, domain=None, range=Optional[str])

slots.s2p = Slot(uri=TEST.s2p, name="s2p", curie=TEST.curie('s2p'),
                      model_uri=TEST.s2p, domain=None, range=Optional[str])

slots.slot_uri = Slot(uri=TEST.slot_uri, name="slot_uri", curie=TEST.curie('slot_uri'),
                      model_uri=TEST.slot_uri, domain=None, range=Optional[str])

slots.slot_curie = Slot(uri=TEST.slot_curie, name="slot_curie", curie=TEST.curie('slot_curie'),
                      model_uri=TEST.slot_curie, domain=None, range=Optional[str])

slots.class_uri = Slot(uri=TEST.class_uri, name="class_uri", curie=TEST.curie('class_uri'),
                      model_uri=TEST.class_uri, domain=None, range=Optional[str])

slots.class_curie = Slot(uri=TEST.class_curie, name="class_curie", curie=TEST.curie('class_curie'),
                      model_uri=TEST.class_curie, domain=None, range=Optional[str])

slots.bnode = Slot(uri=TEST.bnode, name="bnode", curie=TEST.curie('bnode'),
                      model_uri=TEST.bnode, domain=None, range=Optional[str])

slots.txt = Slot(uri=TEST.txt, name="txt", curie=TEST.curie('txt'),
                      model_uri=TEST.txt, domain=None, range=Optional[str])

slots.int = Slot(uri=TEST.int, name="int", curie=TEST.curie('int'),
                      model_uri=TEST.int, domain=None, range=Optional[str])

slots.dfltrange = Slot(uri=TEST.dfltrange, name="dfltrange", curie=TEST.curie('dfltrange'),
                      model_uri=TEST.dfltrange, domain=None, range=Optional[str])

slots.dfltns = Slot(uri=TEST.dfltns, name="dfltns", curie=TEST.curie('dfltns'),
                      model_uri=TEST.dfltns, domain=None, range=Optional[str])
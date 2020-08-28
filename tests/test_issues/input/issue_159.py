# Auto generated from issue_159.yaml by pythongen.py version: 0.4.0
# Generation date: 2020-08-28 11:36
# Schema: Templatetest
#
# id: https://github.com/biolink/biolinkml/tests/test_issues/test_issue_159
# description: Outline of a formatting template proposal
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
from includes.types import Float, String
import parse

metamodel_version = "1.5.3"

# Overwrite dataclasses _init_fn to add **kwargs in __init__
dataclasses._init_fn = dataclasses_init_fn_with_kwargs

# Namespaces
BIOLINKML = CurieNamespace('biolinkml', 'https://w3id.org/biolink/biolinkml/')
TT = CurieNamespace('tt', 'https://github.com/biolink/biolinkml/tests/test_issues/test_issue_159/')
DEFAULT_ = TT


# Types

# Class references



@dataclass
class C1(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = TT.C1
    class_class_curie: ClassVar[str] = "tt:C1"
    class_name: ClassVar[str] = "c1"
    class_model_uri: ClassVar[URIRef] = TT.C1
    string_template: ClassVar[str] = "{value}:{units}"

    value: float
    units: Optional[str] = None

    def __post_init__(self, **kwargs: Dict[str, Any]):
        if self.value is None:
            raise ValueError(f"value must be supplied")
        super().__post_init__(**kwargs)

    def __str__(self):
        return C1.string_template.format(**{k: '' if v is None else v for k, v in self.__dict__.items()})

    @classmethod
    def parse(cls, text: str) -> "C1":
        v = parse.parse(C1.string_template, text)
        return C1(*v.fixed, **v.named)



# Slots
class slots:
    pass

slots.value = Slot(uri=TT.value, name="value", curie=TT.curie('value'),
                      model_uri=TT.value, domain=None, range=float)

slots.units = Slot(uri=TT.units, name="units", curie=TT.curie('units'),
                      model_uri=TT.units, domain=None, range=Optional[str])
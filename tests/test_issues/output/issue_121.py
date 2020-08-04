# Auto generated from issue_121.yaml by pythongen.py version: 0.4.0
# Generation date: 2020-08-04 09:37
# Schema: schema
#
# id: https://microbiomedata/schema
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

metamodel_version = "1.5.3"

# Overwrite dataclasses _init_fn to add **kwargs in __init__
dataclasses._init_fn = dataclasses_init_fn_with_kwargs

# Namespaces
BIOLINKML = CurieNamespace('biolinkml', 'https://w3id.org/biolink/biolinkml/')
DEFAULT_ = CurieNamespace('', 'https://microbiomedata/schema/')


# Types

# Class references



@dataclass
class Biosample(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = URIRef("https://microbiomedata/schema/Biosample")
    class_class_curie: ClassVar[str] = None
    class_name: ClassVar[str] = "biosample"
    class_model_uri: ClassVar[URIRef] = URIRef("https://microbiomedata/schema/Biosample")

    depth: Optional[str] = None

class ImportedClass(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = URIRef("https://microbiomedata/schema/mixs/ImportedClass")
    class_class_curie: ClassVar[str] = None
    class_name: ClassVar[str] = "imported class"
    class_model_uri: ClassVar[URIRef] = URIRef("https://microbiomedata/schema/ImportedClass")



# Slots
class slots:
    pass

slots.depth = Slot(uri=DEFAULT_['mixs/depth'], name="depth", curie=DEFAULT_.curie('mixs/depth'),
                      model_uri=DEFAULT_.depth, domain=None, range=Optional[str])

slots.biosample_depth = Slot(uri=DEFAULT_.depth, name="biosample_depth", curie=DEFAULT_.curie('depth'),
                      model_uri=DEFAULT_.biosample_depth, domain=Biosample, range=Optional[str])
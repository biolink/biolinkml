# Auto generated from .yaml by pythongen.py version:
# Generation date:
# Schema: extensions
#
# id: https://w3id.org/biolink/biolinkml/extensions
# description: Extension mixin
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
from biolinkml.utils.metamodelcore import URIorCURIE
from includes.types import String, Uriorcurie

metamodel_version = "1.5.3"

# Overwrite dataclasses _init_fn to add **kwargs in __init__
dataclasses._init_fn = dataclasses_init_fn_with_kwargs

# Namespaces
BIOLINKML = CurieNamespace('biolinkml', 'https://w3id.org/biolink/biolinkml/')
META = CurieNamespace('meta', 'https://w3id.org/biolink/biolinkml/meta/')
DEFAULT_ = META


# Types

# Class references



@dataclass
class Extension(YAMLRoot):
    """
    a tag/value pair used to add non-model information to an entry
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = META.Extension
    class_class_curie: ClassVar[str] = "meta:Extension"
    class_name: ClassVar[str] = "extension"
    class_model_uri: ClassVar[URIRef] = META.Extension

    tag: Union[str, URIorCURIE]
    value: str
    extensions: List[Union[dict, "Extension"]] = empty_list()

    def __post_init__(self, **kwargs: Dict[str, Any]):
        if self.tag is None:
            raise ValueError(f"tag must be supplied")
        if not isinstance(self.tag, URIorCURIE):
            self.tag = URIorCURIE(self.tag)
        if self.value is None:
            raise ValueError(f"value must be supplied")
        self.extensions = [Extension(*e) for e in self.extensions.items()] if isinstance(self.extensions, dict) \
                           else [v if isinstance(v, Extension) else Extension(**v)
                                 for v in ([self.extensions] if isinstance(self.extensions, str) else self.extensions)]
        super().__post_init__(**kwargs)



# Slots
class slots:
    pass

slots.extensions = Slot(uri=META.extensions, name="extensions", curie=META.curie('extensions'),
                      model_uri=META.extensions, domain=None, range=List[Union[dict, Extension]])

slots.extension_tag = Slot(uri=META.tag, name="extension_tag", curie=META.curie('tag'),
                      model_uri=META.extension_tag, domain=Extension, range=Union[str, URIorCURIE])

slots.extension_value = Slot(uri=META.value, name="extension_value", curie=META.curie('value'),
                      model_uri=META.extension_value, domain=Extension, range=str)
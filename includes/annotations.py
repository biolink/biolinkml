# Auto generated from .yaml by pythongen.py version:
# Generation date:
# Schema: annotations
#
# id: https://w3id.org/biolink/biolinkml/annotations
# description: Annotations mixin
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
from biolinkml.utils.metamodelcore import Bool, URIorCURIE
from includes.extensions import Extension
from includes.types import Boolean, Uriorcurie

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
class Annotation(Extension):
    """
    a tag/value pair with the semantics of OWL Annotation
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = META.Annotation
    class_class_curie: ClassVar[str] = "meta:Annotation"
    class_name: ClassVar[str] = "annotation"
    class_model_uri: ClassVar[URIRef] = META.Annotation

    tag: Union[str, URIorCURIE] = None
    value: Bool = None
    annotations: List[Union[dict, "Annotation"]] = empty_list()

    def __post_init__(self, **kwargs: Dict[str, Any]):
        self.annotations = [Annotation(*e) for e in self.annotations.items()] if isinstance(self.annotations, dict) \
                            else [v if isinstance(v, Annotation) else Annotation(**v)
                                  for v in ([self.annotations] if isinstance(self.annotations, str) else self.annotations)]
        if self.value is None:
            raise ValueError(f"value must be supplied")
        super().__post_init__(**kwargs)



# Slots
class slots:
    pass

slots.annotations = Slot(uri=META.annotations, name="annotations", curie=META.curie('annotations'),
                      model_uri=META.annotations, domain=None, range=List[Union[dict, Annotation]])

slots.annotation_extension_value = Slot(uri=META.value, name="annotation_extension_value", curie=META.curie('value'),
                      model_uri=META.annotation_extension_value, domain=Annotation, range=Bool)
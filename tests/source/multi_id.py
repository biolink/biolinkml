
# id: http://example.org/example/multi_id
# description:
# license:

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

metamodel_version = "1.4.3"

# Overwrite dataclasses _init_fn to add **kwargs in __init__
dataclasses._init_fn = dataclasses_init_fn_with_kwargs

# Namespaces
XSD = CurieNamespace('xsd', 'http://www.w3.org/2001/XMLSchema#')
DEFAULT_ = CurieNamespace('', 'http://example.org/example/multi_id/')


# Types
class Uri(URIorCURIE):
    type_class_uri = XSD.anyURI
    type_class_curie = "xsd:anyURI"
    type_name = "uri"
    type_model_uri = URIRef("http://example.org/example/multi_id/Uri")


class IdentifierType(Uri):
    type_class_uri = XSD.anyURI
    type_class_curie = "xsd:anyURI"
    type_name = "identifier type"
    type_model_uri = URIRef("http://example.org/example/multi_id/IdentifierType")


# Class references
class NamedThingId(URIorCURIE):
    pass


class SequenceVariantId(NamedThingId):
    pass


@dataclass
class NamedThing(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = ["node_property", "id"]

    class_class_uri: ClassVar[URIRef] = URIRef("http://example.org/example/multi_id/NamedThing")
    class_class_curie: ClassVar[str] = None
    class_name: ClassVar[str] = "named thing"
    class_model_uri: ClassVar[URIRef] = URIRef("http://example.org/example/multi_id/NamedThing")

    id: Union[URIorCURIE, NamedThingId]
    node_property: Optional[Union[URIorCURIE, IdentifierType]] = None
    not_overridden: Optional[Union[URIorCURIE, IdentifierType]] = None

    def __post_init__(self, **kwargs: Dict[str, Any]):
        if self.id is None:
            raise ValueError(f"id must be supplied")
        if not isinstance(self.id, NamedThingId):
            self.id = NamedThingId(self.id)
        if self.node_property is not None and not isinstance(self.node_property, IdentifierType):
            self.node_property = IdentifierType(self.node_property)
        if self.not_overridden is not None and not isinstance(self.not_overridden, IdentifierType):
            self.not_overridden = IdentifierType(self.not_overridden)
        super().__post_init__(**kwargs)


@dataclass
class SequenceVariant(NamedThing):
    _inherited_slots: ClassVar[List[str]] = ["node_property", "id"]

    class_class_uri: ClassVar[URIRef] = URIRef("http://example.org/example/multi_id/SequenceVariant")
    class_class_curie: ClassVar[str] = None
    class_name: ClassVar[str] = "sequence variant"
    class_model_uri: ClassVar[URIRef] = URIRef("http://example.org/example/multi_id/SequenceVariant")

    id: Union[URIorCURIE, SequenceVariantId] = None
    node_property: Optional[Union[URIorCURIE, IdentifierType]] = None

    def __post_init__(self, **kwargs: Dict[str, Any]):
        if self.id is None:
            raise ValueError(f"id must be supplied")
        if not isinstance(self.id, SequenceVariantId):
            self.id = SequenceVariantId(self.id)
        if self.node_property is not None and not isinstance(self.node_property, IdentifierType):
            self.node_property = IdentifierType(self.node_property)
        super().__post_init__(**kwargs)



# Slots
class slots:
    pass

slots.node_property = Slot(uri=DEFAULT_.node_property, name="node property", curie=DEFAULT_.curie('node_property'),
                      model_uri=DEFAULT_.node_property, domain=NamedThing, range=Optional[Union[URIorCURIE, IdentifierType]])

slots.not_overridden = Slot(uri=DEFAULT_.not_overridden, name="not overridden", curie=DEFAULT_.curie('not_overridden'),
                      model_uri=DEFAULT_.not_overridden, domain=NamedThing, range=Optional[Union[URIorCURIE, IdentifierType]])

slots.id = Slot(uri=DEFAULT_.id, name="id", curie=DEFAULT_.curie('id'),
                      model_uri=DEFAULT_.id, domain=NamedThing, range=Union[URIorCURIE, NamedThingId])

slots.sequence_variant_id = Slot(uri=DEFAULT_.id, name="sequence variant_id", curie=DEFAULT_.curie('id'),
                      model_uri=DEFAULT_.sequence_variant_id, domain=SequenceVariant, range=Union[URIorCURIE, SequenceVariantId])

slots.sequence_variant_node_property = Slot(uri=DEFAULT_.node_property, name="sequence variant_node property", curie=DEFAULT_.curie('node_property'),
                      model_uri=DEFAULT_.sequence_variant_node_property, domain=SequenceVariant, range=Optional[Union[URIorCURIE, IdentifierType]])
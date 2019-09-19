
# id: http://example.org/example/multi_id
# description:
# license:

from typing import Optional, List, Union, Dict, ClassVar
from dataclasses import dataclass
from biolinkml.utils.metamodelcore import empty_list, empty_dict, bnode
from biolinkml.utils.yamlutils import YAMLRoot
from biolinkml.utils.formatutils import camelcase, underscore, sfx
from rdflib import Namespace, URIRef
from biolinkml.utils.metamodelcore import URIorCURIE

metamodel_version = "1.4.1"


# Namespaces
XSD = Namespace('http://www.w3.org/2001/XMLSchema#')
DEFAULT_ = Namespace('http://example.org/example/multi_id/')


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

    def __post_init__(self):
        if self.id is None:
            raise ValueError(f"id must be supplied")
        if not isinstance(self.id, NamedThingId):
            self.id = NamedThingId(self.id)
        if self.node_property is not None and not isinstance(self.node_property, IdentifierType):
            self.node_property = IdentifierType(self.node_property)
        if self.not_overridden is not None and not isinstance(self.not_overridden, IdentifierType):
            self.not_overridden = IdentifierType(self.not_overridden)
        super().__post_init__()


@dataclass
class SequenceVariant(NamedThing):
    _inherited_slots: ClassVar[List[str]] = ["node_property", "id"]

    class_class_uri: ClassVar[URIRef] = URIRef("http://example.org/example/multi_id/SequenceVariant")
    class_class_curie: ClassVar[str] = None
    class_name: ClassVar[str] = "sequence variant"
    class_model_uri: ClassVar[URIRef] = URIRef("http://example.org/example/multi_id/SequenceVariant")

    id: Union[URIorCURIE, SequenceVariantId] = None
    node_property: Optional[Union[URIorCURIE, IdentifierType]] = None

    def __post_init__(self):
        if self.id is None:
            raise ValueError(f"id must be supplied")
        if not isinstance(self.id, SequenceVariantId):
            self.id = SequenceVariantId(self.id)
        if self.node_property is not None and not isinstance(self.node_property, IdentifierType):
            self.node_property = IdentifierType(self.node_property)
        super().__post_init__()

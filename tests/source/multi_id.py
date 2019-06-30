
# id: http://example.org/example/multi_id
# description:
# license:

from typing import Optional, List, Union, Dict, ClassVar
from dataclasses import dataclass
from biolinkml.utils.metamodelcore import empty_list, empty_dict
from biolinkml.utils.yamlutils import YAMLRoot
from biolinkml.utils.metamodelcore import URIorCURIE

metamodel_version = "1.3.6"


# Types
class Uri(URIorCURIE):
    pass


class IdentifierType(Uri):
    pass


# Class references
class NamedThingId(URIorCURIE):
    pass


class SequenceVariantId(NamedThingId):
    pass


@dataclass
class NamedThing(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = ["node_property", "id"]

    type_uri: ClassVar[str] = "http://example.org/example/multi_id/NamedThing"
    type_curie: ClassVar[str] = ":NamedThing"
    type_name: ClassVar[str] = "named thing"

    id: Union[URIorCURIE, NamedThingId]
    node_property: Optional[Union[URIorCURIE, IdentifierType]] = None
    not_overridden: Optional[Union[URIorCURIE, IdentifierType]] = None

    def _fix_elements(self):
        super()._fix_elements()
        if not isinstance(self.id, NamedThingId):
            self.id = NamedThingId(self.id)
        if self.node_property is not None and not isinstance(self.node_property, IdentifierType):
            self.node_property = IdentifierType(self.node_property)
        if self.not_overridden is not None and not isinstance(self.not_overridden, IdentifierType):
            self.not_overridden = IdentifierType(self.not_overridden)


@dataclass
class SequenceVariant(NamedThing):
    _inherited_slots: ClassVar[List[str]] = ["node_property", "id"]

    type_uri: ClassVar[str] = "http://example.org/example/multi_id/SequenceVariant"
    type_curie: ClassVar[str] = ":SequenceVariant"
    type_name: ClassVar[str] = "sequence variant"

    id: Union[URIorCURIE, SequenceVariantId] = None

    def _fix_elements(self):
        super()._fix_elements()
        if self.id is not None and not isinstance(self.id, SequenceVariantId):
            self.id = SequenceVariantId(self.id)
        if self.node_property is not None and not isinstance(self.node_property, IdentifierType):
            self.node_property = IdentifierType(self.node_property)

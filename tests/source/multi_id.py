
# id: http://example.org/example/multi_id
# description:
# license:

from typing import Optional, List, Union, Dict
from dataclasses import dataclass
from biolinkml.utils.metamodelcore import empty_list, empty_dict
from biolinkml.utils.yamlutils import YAMLRoot
from biolinkml.utils.metamodelcore import Uri

metamodel_version = "None"

inherited_slots: List[str] = []


# Type names
class IdentifierType(Union[Uri, Uri]):
    pass




# Class references
class NamedThingId(Uri):
    pass


class SequenceVariantId(NamedThingId):
    pass


@dataclass
class NamedThing(YAMLRoot):

    # === named thing ===
    id: Uri
    node_property: Optional[Union[Uri, IdentifierType]] = None
    not_overridden: Optional[Union[Uri, IdentifierType]] = None

    def _fix_elements(self):
        super()._fix_elements()
        if self.node_property and not isinstance(self.node_property, IdentifierType):
            self.node_property = IdentifierType(self.node_property)
        if self.not_overridden and not isinstance(self.not_overridden, IdentifierType):
            self.not_overridden = IdentifierType(self.not_overridden)


@dataclass
class SequenceVariant(NamedThing):

    # === named thing ===
    not_overridden: Optional[Union[Uri, IdentifierType]] = None

    # === sequence variant ===
    id: Uri = None
    node_property: Optional[Union[Uri, IdentifierType]] = None

    def _fix_elements(self):
        super()._fix_elements()
        if self.node_property and not isinstance(self.node_property, IdentifierType):
            self.node_property = IdentifierType(self.node_property)

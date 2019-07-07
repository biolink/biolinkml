
# id: https://example.org/inheritedid
# description: Test
# license: https://creativecommons.org/publicdomain/zero/1.0/

from typing import Optional, List, Union, Dict, ClassVar
from dataclasses import dataclass
from biolinkml.utils.metamodelcore import empty_list, empty_dict, bnode
from biolinkml.utils.yamlutils import YAMLRoot
from biolinkml.utils.formatutils import camelcase, underscore, sfx
from rdflib import Namespace
from biolinkml.utils.metamodelcore import URI

metamodel_version = "1.4.0"


# Namespaces
BIOLINKML = Namespace('https://w3id.org/biolink/biolinkml/')
DEFAULT_ = BIOLINKML


# Types
class String(str):
    pass


class Uri(URI):
    """ a complete URI """
    pass


class IdentifierType(String):
    """ A string that is intended to uniquely identify a thing May be URI in full or compact (CURIE) form """
    pass


class LabelType(String):
    """ A string that provides a human-readable name for a thing """
    pass


# Class references
class AttributeId(IdentifierType):
    pass


class BiologicalSexId(AttributeId):
    pass


class OntologyClassId(NamedThingId):
    pass


class NamedThingId(IdentifierType):
    pass


@dataclass
class Attribute(YAMLRoot):
    """
    A property or characteristic of an entity
    """
    _inherited_slots: ClassVar[List[str]] = []

    type_uri: ClassVar[str] = "https://w3id.org/biolink/biolinkml/Attribute"
    type_curie: ClassVar[str] = "biolinkml:Attribute"
    type_name: ClassVar[str] = "attribute"

    id: Union[str, AttributeId]

    def __post_init__(self):
        if not isinstance(self.id, AttributeId):
            self.id = AttributeId(self.id)
        super().__post_init__()


@dataclass
class BiologicalSex(Attribute):
    _inherited_slots: ClassVar[List[str]] = []

    type_uri: ClassVar[str] = "https://w3id.org/biolink/biolinkml/BiologicalSex"
    type_curie: ClassVar[str] = "biolinkml:BiologicalSex"
    type_name: ClassVar[str] = "biological sex"

    id: Union[str, BiologicalSexId] = None

    def __post_init__(self):
        if self.id is not None and not isinstance(self.id, BiologicalSexId):
            self.id = BiologicalSexId(self.id)
        super().__post_init__()


@dataclass
class OntologyClass(NamedThing):
    """
    a concept or class in an ontology, vocabulary or thesaurus
    """
    _inherited_slots: ClassVar[List[str]] = []

    type_uri: ClassVar[str] = "https://w3id.org/biolink/biolinkml/OntologyClass"
    type_curie: ClassVar[str] = "biolinkml:OntologyClass"
    type_name: ClassVar[str] = "ontology class"

    id: Union[str, OntologyClassId] = None

    def __post_init__(self):
        if self.id is not None and not isinstance(self.id, OntologyClassId):
            self.id = OntologyClassId(self.id)
        super().__post_init__()


@dataclass
class NamedThing(YAMLRoot):
    """
    a databased entity or concept/class
    """
    _inherited_slots: ClassVar[List[str]] = []

    type_uri: ClassVar[str] = "https://w3id.org/biolink/biolinkml/NamedThing"
    type_curie: ClassVar[str] = "biolinkml:NamedThing"
    type_name: ClassVar[str] = "named thing"

    id: Union[str, NamedThingId]
    name: Optional[Union[str, LabelType]] = None

    def __post_init__(self):
        if not isinstance(self.id, NamedThingId):
            self.id = NamedThingId(self.id)
        if self.name is not None and not isinstance(self.name, LabelType):
            self.name = LabelType(self.name)
        super().__post_init__()

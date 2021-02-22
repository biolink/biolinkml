
# id: https://example.org/inheritedid
# description: Test
# license: https://creativecommons.org/publicdomain/zero/1.0/

import dataclasses
import sys
import re
from typing import Optional, List, Union, Dict, ClassVar, Any
from dataclasses import dataclass
from biolinkml.meta import EnumDefinition, PermissibleValue, PvFormulaOptions

from biolinkml.utils.slot import Slot
from biolinkml.utils.metamodelcore import empty_list, empty_dict, bnode
from biolinkml.utils.yamlutils import YAMLRoot, extended_str, extended_float, extended_int
if sys.version_info < (3, 7, 6):
    from biolinkml.utils.dataclass_extensions_375 import dataclasses_init_fn_with_kwargs
else:
    from biolinkml.utils.dataclass_extensions_376 import dataclasses_init_fn_with_kwargs
from biolinkml.utils.formatutils import camelcase, underscore, sfx
from biolinkml.utils.enumerations import EnumDefinitionImpl
from rdflib import Namespace, URIRef
from biolinkml.utils.curienamespace import CurieNamespace
from biolinkml.utils.metamodelcore import URI

metamodel_version = "1.7.0"

# Overwrite dataclasses _init_fn to add **kwargs in __init__
dataclasses._init_fn = dataclasses_init_fn_with_kwargs

# Namespaces
BIOLINKML = CurieNamespace('biolinkml', 'https://w3id.org/biolink/biolinkml/')
XSD = CurieNamespace('xsd', 'http://www.w3.org/2001/XMLSchema#')
DEFAULT_ = BIOLINKML


# Types
class String(str):
    type_class_uri = XSD.string
    type_class_curie = "xsd:string"
    type_name = "string"
    type_model_uri = BIOLINKML.String


class Uri(URI):
    """ a complete URI """
    type_class_uri = XSD.anyURI
    type_class_curie = "xsd:anyURI"
    type_name = "uri"
    type_model_uri = BIOLINKML.Uri


class IdentifierType(String):
    """ A string that is intended to uniquely identify a thing May be URI in full or compact (CURIE) form """
    type_class_uri = XSD.string
    type_class_curie = "xsd:string"
    type_name = "identifier type"
    type_model_uri = BIOLINKML.IdentifierType


class LabelType(String):
    """ A string that provides a human-readable name for a thing """
    type_class_uri = XSD.string
    type_class_curie = "xsd:string"
    type_name = "label type"
    type_model_uri = BIOLINKML.LabelType


# Class references
class NamedThingId(IdentifierType):
    pass


class AttributeId(IdentifierType):
    pass


class BiologicalSexId(AttributeId):
    pass


class OntologyClassId(NamedThingId):
    pass


@dataclass
class NamedThing(YAMLRoot):
    """
    a databased entity or concept/class
    """
    id: Union[str, NamedThingId] = None
    name: Optional[Union[str, LabelType]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.id is None:
            raise ValueError("id must be supplied")
        if not isinstance(self.id, NamedThingId):
            self.id = NamedThingId(self.id)

        if self.name is not None and not isinstance(self.name, LabelType):
            self.name = LabelType(self.name)

        super().__post_init__(**kwargs)


@dataclass
class Attribute(YAMLRoot):
    """
    A property or characteristic of an entity
    """
    id: Union[str, AttributeId] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.id is None:
            raise ValueError("id must be supplied")
        if not isinstance(self.id, AttributeId):
            self.id = AttributeId(self.id)

        super().__post_init__(**kwargs)


@dataclass
class BiologicalSex(Attribute):
    id: Union[str, BiologicalSexId] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.id is None:
            raise ValueError("id must be supplied")
        if not isinstance(self.id, BiologicalSexId):
            self.id = BiologicalSexId(self.id)

        super().__post_init__(**kwargs)


@dataclass
class OntologyClass(NamedThing):
    """
    a concept or class in an ontology, vocabulary or thesaurus
    """
    id: Union[str, OntologyClassId] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.id is None:
            raise ValueError("id must be supplied")
        if not isinstance(self.id, OntologyClassId):
            self.id = OntologyClassId(self.id)

        super().__post_init__(**kwargs)


# Enumerations


# Slots


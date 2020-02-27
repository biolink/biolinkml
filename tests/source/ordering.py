
# id: https://example.org/inheritedid
# description: Test
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
from biolinkml.utils.metamodelcore import URI

metamodel_version = "1.4.3"

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

    class_class_uri: ClassVar[URIRef] = BIOLINKML.Attribute
    class_class_curie: ClassVar[str] = "biolinkml:Attribute"
    class_name: ClassVar[str] = "attribute"
    class_model_uri: ClassVar[URIRef] = BIOLINKML.Attribute

    id: Union[str, AttributeId]

    def __post_init__(self, **kwargs: Dict[str, Any]):
        if self.id is None:
            raise ValueError(f"id must be supplied")
        if not isinstance(self.id, AttributeId):
            self.id = AttributeId(self.id)
        super().__post_init__(**kwargs)


@dataclass
class BiologicalSex(Attribute):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = BIOLINKML.BiologicalSex
    class_class_curie: ClassVar[str] = "biolinkml:BiologicalSex"
    class_name: ClassVar[str] = "biological sex"
    class_model_uri: ClassVar[URIRef] = BIOLINKML.BiologicalSex

    id: Union[str, BiologicalSexId] = None

    def __post_init__(self, **kwargs: Dict[str, Any]):
        if self.id is None:
            raise ValueError(f"id must be supplied")
        if not isinstance(self.id, BiologicalSexId):
            self.id = BiologicalSexId(self.id)
        super().__post_init__(**kwargs)


@dataclass
class OntologyClass(NamedThing):
    """
    a concept or class in an ontology, vocabulary or thesaurus
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = BIOLINKML.OntologyClass
    class_class_curie: ClassVar[str] = "biolinkml:OntologyClass"
    class_name: ClassVar[str] = "ontology class"
    class_model_uri: ClassVar[URIRef] = BIOLINKML.OntologyClass

    id: Union[str, OntologyClassId] = None

    def __post_init__(self, **kwargs: Dict[str, Any]):
        if self.id is None:
            raise ValueError(f"id must be supplied")
        if not isinstance(self.id, OntologyClassId):
            self.id = OntologyClassId(self.id)
        super().__post_init__(**kwargs)


@dataclass
class NamedThing(YAMLRoot):
    """
    a databased entity or concept/class
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = BIOLINKML.NamedThing
    class_class_curie: ClassVar[str] = "biolinkml:NamedThing"
    class_name: ClassVar[str] = "named thing"
    class_model_uri: ClassVar[URIRef] = BIOLINKML.NamedThing

    id: Union[str, NamedThingId]
    name: Optional[Union[str, LabelType]] = None

    def __post_init__(self, **kwargs: Dict[str, Any]):
        if self.id is None:
            raise ValueError(f"id must be supplied")
        if not isinstance(self.id, NamedThingId):
            self.id = NamedThingId(self.id)
        if self.name is not None and not isinstance(self.name, LabelType):
            self.name = LabelType(self.name)
        super().__post_init__(**kwargs)



# Slots
class slots:
    pass

slots.id = Slot(uri=BIOLINKML.id, name="id", curie=BIOLINKML.curie('id'),
                      model_uri=BIOLINKML.id, domain=NamedThing, range=Union[str, NamedThingId])

slots.name = Slot(uri=BIOLINKML.name, name="name", curie=BIOLINKML.curie('name'),
                      model_uri=BIOLINKML.name, domain=NamedThing, range=Optional[Union[str, LabelType]])
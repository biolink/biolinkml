
# id: https://example.com/test44
# description:
# license: https://creativecommons.org/publicdomain/zero/1.0/

from typing import Optional, List, Union, Dict, ClassVar
from dataclasses import dataclass
from biolinkml.utils.slot import Slot
from biolinkml.utils.metamodelcore import empty_list, empty_dict, bnode
from biolinkml.utils.yamlutils import YAMLRoot
from biolinkml.utils.formatutils import camelcase, underscore, sfx
from rdflib import Namespace, URIRef
from biolinkml.utils.curienamespace import CurieNamespace
from biolinkml.utils.metamodelcore import URIorCURIE
from includes.types import Uriorcurie

metamodel_version = "1.4.3"


# Namespaces
META = CurieNamespace('meta', 'https://w3id.org/biolink/biolinkml/')
RDFS = CurieNamespace('rdfs', 'http://example.org/UNKNOWN/rdfs/')
XSD = CurieNamespace('xsd', 'http://www.w3.org/2001/XMLSchema#')
DEFAULT_ = CurieNamespace('', 'https://example.com/test44/')


# Types
class IriType(Uriorcurie):
    """ An IRI """
    type_class_uri = XSD.anyURI
    type_class_curie = "xsd:anyURI"
    type_name = "iri type"
    type_model_uri = URIRef("https://example.com/test44/IriType")


# Class references



@dataclass
class NamedThing(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = URIRef("https://example.com/test44/NamedThing")
    class_class_curie: ClassVar[str] = None
    class_name: ClassVar[str] = "named thing"
    class_model_uri: ClassVar[URIRef] = URIRef("https://example.com/test44/NamedThing")

    category: List[Union[str, IriType]] = empty_list()

    def __post_init__(self):
        if not isinstance(self.category, list) or len(self.category) == 0:
            raise ValueError(f"category must be a non-empty list")
        self.category = [v if isinstance(v, IriType)
                         else IriType(v) for v in self.category]
        super().__post_init__()



# Slots
class slots:
    pass

slots.category = Slot(uri=RDFS.subClassOf, name="category", curie=RDFS.curie('subClassOf'),
                      model_uri=DEFAULT_.category, domain=NamedThing, range=List[Union[str, IriType]])
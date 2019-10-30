from dataclasses import dataclass
from typing import Type, List, Optional

from rdflib import URIRef


@dataclass
class Slot:
    """ Runtime slot definition """
    uri: URIRef
    name: str
    curie: Optional[str]
    model_uri: URIRef

    domain: Optional[Type]
    range: Type
    mappings: Optional[List[URIRef]] = None

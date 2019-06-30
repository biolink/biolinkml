import re
from typing import Callable, Optional, Text, List, Tuple, Match

from biolinkml.meta import ClassDefinition, SlotDefinition
from biolinkml.utils.schemaloader import SchemaLoader


def strval(txt: str) -> str:
    txt = str(txt).replace('"', '\\"')
    return f'"{txt}"'


# Library of named default values -- this is here to prevent code injection
default_library: List[Tuple[Text, Callable[[Match[str], SchemaLoader, ClassDefinition, SlotDefinition], str]]] = [
    (r"[Tt]rue", lambda _, __, ___, ____: "True"),
    (r"[Ff]alse", lambda _, __, ___, ____: "False"),
    (r"int\((-?[1-9][0-9]*)\)", lambda m, __, ___, ____: int(m[1])),
    ("class_uri", lambda _, loader, cls, ____: strval(
        loader.namespaces.uri_or_curie_for(loader.schema.default_prefix, loader.class_or_type_name(cls.name)))),
    ("slot_uri", lambda _, loader, ___, slot: strval(
        loader.namespaces.uri_for(
            loader.namespaces.uri_or_curie_for(loader.schema.default_prefix, loader.slot_name(slot.name))))),
    ("class_curie", lambda _, loader, cls, ____: strval(
        loader.namespaces.curie_for(loader.namespaces.uri_for(
            loader.namespaces.uri_or_curie_for(loader.schema.default_prefix, loader.class_or_type_name(cls.name)))))),
    ("slot_curie", lambda _, loader, ___, slot: strval(
        loader.namespaces.curie_for(loader.namespaces.uri_for(
            loader.namespaces.uri_or_curie_for(loader.schema.default_prefix, loader.slot_name(slot.name)))))),
    ("default_range", lambda _, loader, __, ____: loader.schema.default_range),
    ("bnode", lambda _, __, ___, ____: "bnode"),
    (r"string\((.*)\)", lambda m, __, ___, ____: strval(m[1]))
]


def isabsent_match(txt: Text) -> \
        Optional[Tuple[Match[str], Callable[[Match[str], SchemaLoader, ClassDefinition, SlotDefinition], str]]]:
    txt = str(txt)
    for pattern, f in default_library:
        m = re.match(pattern + '$', txt)
        if m:
            return m, f


def ifabsent_value(txt: Text, loader, cls, slot) -> Optional[str]:
    m, f = isabsent_match(txt)
    if m:
        return f(m, loader, cls, slot)

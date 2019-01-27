import dataclasses
from copy import deepcopy
from typing import Dict, Optional, Union

from biolinkml.meta import SchemaDefinition, Element, SlotDefinition, ClassDefinition, TypeDefinition, SlotDefinitionName
from biolinkml.utils.namespaces import Namespaces


def merge_schemas(target: SchemaDefinition, mergee: SchemaDefinition, namespaces: Optional[Namespaces] = None) -> None:
    assert target.name is not None, "Schema name must be supplied"
    if target.license is None:
        target.license = mergee.license

    target.imports += [imp for imp in mergee.imports if imp not in target.imports]
    set_from_schema(mergee)

    if namespaces:
        merge_namespaces(target, mergee, namespaces)

    merge_dicts(target.classes, mergee.classes)
    merge_dicts(target.slots, mergee.slots)
    merge_dicts(target.types, mergee.types)


def merge_namespaces(target: SchemaDefinition, mergee: SchemaDefinition, namespaces) -> None:
    """
    Add the mergee namespace definitions to target

    :param target:
    :param mergee:
    :param namespaces:
    :return:
    """
    for prefix in mergee.prefixes.values():
        namespaces[prefix.local_name] = prefix.prefix_uri
        if prefix.local_name not in target.prefixes:
            target.prefixes[prefix.local_name] = prefix
        elif target.prefixes[prefix.local_name].prefix_uri != prefix.prefix_uri:
            raise ValueError(f'Prefix: {prefix.local_name} mismatch between {target.name} and {mergee.name}')
    for mmap in mergee.default_curi_maps:
        namespaces.add_prefixmap(mmap)


def set_from_schema(schema: SchemaDefinition) -> None:
    for t in [schema.subsets, schema.classes, schema.slots, schema.types]:
        for k in t.keys():
            t[k].from_schema = schema.id


def merge_dicts(target: Dict[str, Element], source: Dict[str, Element]) -> None:
    for k, v in source.items():
        if k in target:
            raise ValueError(f"Conflicting definitions for {k}")
        target[k] = deepcopy(v)


def merge_slots(target: Union[SlotDefinition, TypeDefinition], source: Union[SlotDefinition, TypeDefinition]) -> None:
    for k, v in dataclasses.asdict(source).items():
        if v is not None and getattr(target, k, None) is None:
            setattr(target, k, deepcopy(v))

def slot_usage_name(usage_name: SlotDefinitionName, owning_class: ClassDefinition) -> SlotDefinitionName:
    """
     Synthesize a unique name for an overridden slot

    :param usage_name:
    :param owning_class:
    :return: Synthesized name
    """
    return SlotDefinitionName(owning_class.name + '_' + usage_name)

def alias_root(schema: SchemaDefinition, slotname: SlotDefinitionName) -> Optional[SlotDefinitionName]:
    """ Return the ultimate alias of a slot """
    alias = schema.slots[slotname].alias if slotname in schema.slots else None
    return alias_root(schema, alias) if alias else slotname

def merge_classes(schema: SchemaDefinition, target: ClassDefinition, source: ClassDefinition,
                  at_end: bool = False) -> None:
    """ Merge the slots in source into target

    :param schema: Containing schema
    :param target: mergee
    :param source: class to merge
    :param at_end: True means add mergee to the end.  False to the front
    """

    # List of grounded slots referenced in the target class
    target_base_slots = set(alias_root(schema, s) for s in target.slots)

    for slotname in source.slots if at_end else source.slots[::-1]:
        slotbase = alias_root(schema, slotname)
        if slotbase in target.slot_usage:
            slotname = slot_usage_name(slotbase, target)
        if slotbase not in target_base_slots:
            target.slots.append(slotname) if at_end else target.slots.insert(0, slotname)
            target_base_slots.add(slotbase)

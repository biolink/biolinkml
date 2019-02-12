import dataclasses
from copy import deepcopy
from typing import Dict, Optional, Union, cast, List
from biolinkml.utils.namespaces import Namespaces
from tests.source.multi_id import NamedThing
from tests.test_biolink_model.biolink_metamodel.biolink_metamodel import Model, inherited_slots
from tests.test_biolink_model.model_constants import model_components


def merge_models(target: Model, mergee: Model, imported_from: Optional[str] = None,
                 namespaces: Optional[Namespaces] = None) -> None:
    """ Merge mergee into target """
    assert target.name is not None, "Model name must be supplied"
    if target.license is None:
        target.license = mergee.license

    target.imports += [imp for imp in mergee.imports if imp not in target.imports]
    set_from_model(mergee)

    if namespaces:
        merge_namespaces(target, mergee, namespaces)

    for component in model_components:
        merge_dicts(target[component], mergee[component], imported_from)


def merge_slots(target: NamedThing, source: NamedThing, slot_def_slot: str, skip: List[NamedThing] = None) -> None:
    if skip is None:
        skip = []
    for k, v in dataclasses.asdict(source).items():
        if k not in skip and v is not None and getattr(target, k, None) is None:
            if k in inherited_slots:
                setattr(target, k, deepcopy(v))
            else:
                setattr(target, k, None)

def merge_namespaces(target: Model, mergee: Model, namespaces) -> None:
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


def set_from_model(model: Model) -> None:
    for t in [model.subsets, model.classes, model.slots, model.types]:
        for k in t.keys():
            t[k].from_schema = model.id


def merge_dicts(target: Dict[str, NamedThing], source: Dict[str, NamedThing], imported_from: str) -> None:
    for k, v in source.items():
        if k in target:
            raise ValueError(f"Conflicting definitions for {k}")
        target[k] = deepcopy(v)
        target[k].imported_from = imported_from

from dataclasses import dataclass
from typing import Optional, Union

import yaml
from jsonasobj import JsonObj, as_dict
from yaml import SafeDumper, ScalarNode
from yaml.representer import BaseRepresenter


@dataclass(init=True)
class YAMLRoot(JsonObj):
    """
    The root object for all python YAML representations
    """
    def __post_init__(self):
        self._fix_elements()

    def _fix_elements(self):
        pass

    def _default(self, obj):
        """ JSON serializer callback.
        1) Filter out empty values (None, {}, [] and False) and mangle the names
        2) Add ID entries for dictionary entries

        :param obj: YAMLRoot object to serialize
        :return: Serialized version of obj
        """

        if isinstance(obj, JsonObj):
            rval = dict()
            for k, v in obj.__dict__.items():
                if not k.startswith('_') and v is not None and (not isinstance(v, (dict, list, bool)) or v):
                    if isinstance(v, dict):
                        itemslist = []
                        for vk, vv in v.items():
                            # if isinstance(vv, ClassDefinition):
                            #     vv['@id'] = camelcase(vk)
                            # elif isinstance(vv, (SlotDefinition, TypeDefinition)):
                            #     if k != 'slot_usage':
                            #         vv['@id'] = underscore(vk)
                            itemslist.append(vv)
                        rval[k] = itemslist
                    else:
                        rval[k] = v
            return rval
        else:
            return super()._default(obj)


def root_representer(dumper: yaml.Dumper, data: YAMLRoot):
    """ YAML callback -- used to filter out empty values (None, {}, [] and false)

    @param dumper: data dumper
    @param data: data to be dumped
    @return:
    """
    rval = dict()
    for k, v in data.__dict__.items():
        if not k.startswith('_') and v is not None and (not isinstance(v, (dict, list)) or v):
            rval[k] = v
    return dumper.represent_data(rval)


yaml.add_multi_representer(YAMLRoot, root_representer)


def as_yaml(schema: YAMLRoot) -> str:
    """
    Return schema in a YAML representation

    :param schema: YAML object
    :return: Stringified representation
    """
    # TODO: figure out how do to a safe dump;
    # def default_representer(_, data) -> str:
    #     return ScalarNode(None, str(data))
    # SafeDumper.add_representer(None, default_representer)
    return yaml.dump(schema)


def as_json(schema: YAMLRoot, context: Optional[Union[JsonObj, dict]] = None) -> JsonObj:
    rval = JsonObj(**schema.__dict__)
    rval['type'] = schema.__class__.__name__
    if context:
        if isinstance(context, JsonObj):
            context = context.__dict__
        for k, v in context.items():
            rval[k] = JsonObj(**v) if isinstance(v, dict) else v
    return rval


class DupCheckYamlLoader(yaml.loader.SafeLoader):
    """
    A YAML loader that throws an error when the same key appears twice
    """
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.add_constructor(yaml.resolver.BaseResolver.DEFAULT_MAPPING_TAG, self.map_constructor)

    def map_constructor(self, loader,  node, deep=False):
        """ Walk the mapping, recording any duplicate keys.

        """
        mapping = {}
        for key_node, value_node in node.value:
            key = loader.construct_object(key_node, deep=deep)
            value = loader.construct_object(value_node, deep=deep)
            if key in mapping:
                raise ValueError(f"Duplicate key: \"{key}\"")
            mapping[key] = value

        return mapping

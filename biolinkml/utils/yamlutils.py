from dataclasses import dataclass, InitVar
from typing import Union, Any, Dict, List

import yaml
import os
from jsonasobj import JsonObj, as_json
from rdflib import Graph
from yaml.constructor import ConstructorError

from biolinkml.utils.context_utils import CONTEXTS_PARAM_TYPE, merge_contexts


class YAMLRoot(JsonObj):

    """
    The root object for all python YAML representations
    """
    def __post_init__(self, **kwargs):
        if kwargs:
            messages: List[str] = []
            for k in kwargs.keys():
                v = repr(kwargs[k])[:40].replace('\n', '\\n')
                messages.append(f"Unknown argument: {k} = {v}  {k.loc() if getattr(k, 'loc', None) else ''}")
            raise ValueError('\n'.join(messages))

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
                is_classvar = k.startswith("type_") and hasattr(type(obj), k)
                if is_classvar:
                    print(f"***** {k} is classvar ")
                if not is_classvar and not k.startswith('_') and v is not None and\
                        (not isinstance(v, (dict, list, bool)) or v):
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


def as_yaml(element: YAMLRoot) -> str:
    """
    Return element in a YAML representation

    :param element: YAML object
    :return: Stringified representation
    """
    return yaml.dump(element, Dumper=yaml.SafeDumper)


def as_json_object(element: YAMLRoot, contexts: CONTEXTS_PARAM_TYPE = None) -> JsonObj:
    """
    Return the representation of element as a JsonObj object
    :param element: element to return
    :param contexts: context(s) to include in the output
    :return: JsonObj representation of element
    """
    rval = JsonObj(**element.__dict__)
    rval['type'] = element.__class__.__name__
    context_element = merge_contexts(contexts)
    if context_element:
        rval['@context'] = context_element['@context']
    return rval


class TypedNode:
    def __init__(self, v: Union[Any, "TypedNode"]):
        self._s = v._s if isinstance(v, TypedNode) else None
        self._len = v._len if isinstance(v, TypedNode) else None
        super().__init__()

    def add_node(self, node):
        self._s = node.start_mark
        self._len = node.end_mark.index - node.start_mark.index
        return self

    def loc(self) -> str:
        return f"{self._s.name}: line {self._s.line + 1} col {self._s.column + 1}"


class extended_str(str, TypedNode):
    pass


class extended_int(int, TypedNode):
    pass


class extended_float(float, TypedNode):
    pass


class DupCheckYamlLoader(yaml.loader.SafeLoader):
    """
    A YAML loader that throws an error when the same key appears twice
    """

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.add_constructor(yaml.resolver.BaseResolver.DEFAULT_MAPPING_TAG, DupCheckYamlLoader.map_constructor)
        self.add_constructor('tag:yaml.org,2002:str', DupCheckYamlLoader.construct_yaml_str)
        self.add_constructor('tag:yaml.org,2002:int', DupCheckYamlLoader.construct_yaml_int)
        self.add_constructor('tag:yaml.org,2002:float', DupCheckYamlLoader.construct_yaml_float)

    def construct_yaml_int(self, node):
        """ Scalar constructor that returns the node information as the value """
        return extended_int(super().construct_yaml_int(node)).add_node(node)

    def construct_yaml_str(self, node):
        """ Scalar constructor that returns the node information as the value """
        return extended_str(super().construct_yaml_str(node)).add_node(node)

    def construct_yaml_float(self, node):
        """ Scalar constructor that returns the node information as the value """
        return extended_float(super().construct_yaml_float(node)).add_node(node)

    @staticmethod
    def map_constructor(loader,  node, deep=False):
        """ Duplicate of constructor.construct_mapping w/ exception that we check for dups

        """
        if not isinstance(node, yaml.MappingNode):
            raise ConstructorError(None, None,
                    "expected a mapping node, but found %s" % node.id,
                    node.start_mark)
        mapping = {}
        for key_node, value_node in node.value:
            key = loader.construct_object(key_node, deep=deep)
            value = loader.construct_object(value_node, deep=deep)
            if key in mapping:
                raise ValueError(f"Duplicate key: \"{key}\"")
            mapping[key] = value
        return mapping


yaml.SafeDumper.add_multi_representer(YAMLRoot, root_representer)
yaml.SafeDumper.add_multi_representer(extended_str, yaml.SafeDumper.represent_str)
yaml.SafeDumper.add_multi_representer(extended_int, yaml.SafeDumper.represent_int)
yaml.SafeDumper.add_multi_representer(extended_float, yaml.SafeDumper.represent_float)


def as_rdf(element: YAMLRoot, contexts: CONTEXTS_PARAM_TYPE = None) -> Graph:
    """
    Convert element into an RDF graph guided by the context(s) in contexts
    :param element: element to represent in RDF
    :param contexts: JSON-LD context(s) in the form of a file or URL name, a json string or a json obj
    :return: rdflib Graph containing element
    """

    jsonld = as_json_object(element, contexts)
    graph = Graph()
    graph.parse(data=as_json(jsonld), format="json-ld", prefix=True)
    return graph



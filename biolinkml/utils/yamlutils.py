from dataclasses import dataclass

import yaml
from jsonasobj import JsonObj, as_json
from rdflib import Graph

from biolinkml.utils.context_utils import CONTEXTS_PARAM_TYPE, merge_contexts


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


yaml.add_multi_representer(YAMLRoot, root_representer)


def as_yaml(element: YAMLRoot) -> str:
    """
    Return element in a YAML representation

    :param element: YAML object
    :return: Stringified representation
    """
    # TODO: figure out how do to a safe dump;
    # def default_representer(_, data) -> str:
    #     return ScalarNode(None, str(data))
    # SafeDumper.add_representer(None, default_representer)
    return yaml.dump(element)


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


def as_rdf(element: YAMLRoot, contexts: CONTEXTS_PARAM_TYPE = None) -> Graph:
    """
    Convert element into an RDF graph guided by the context(s) in contexts
    :param element: element to represent in RDF
    :param contexts: JSON-LD context(s) in the form of a file or URL name, a json string or a json obj
    :return: rdflib Graph containing element
    """

    jsonld = as_json_object(element, contexts)
    graph = Graph()
    graph.parse(data=as_json(jsonld), format="json-ld")
    return graph

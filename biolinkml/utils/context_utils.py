import os
from typing import Optional, Union, List, Any

from jsonasobj import JsonObj, loads

CONTEXT_TYPE = Union[str, dict, JsonObj]
CONTEXTS_PARAM_TYPE = Optional[Union[CONTEXT_TYPE, List[CONTEXT_TYPE]]]


def merge_contexts(contexts: CONTEXTS_PARAM_TYPE = None, base: Optional[Any] = None,
                   root_directory: Optional[str] = None) -> JsonObj:
    """ Take a list of JSON-LD contexts, which can be one of:
        * the name of a JSON-LD file
        * the URI of a JSON-lD file
        * JSON-LD text
        * A JsonObj object that contains JSON-LD
        * A dictionary that contains JSON-LD

    And turn it into an object that can be tacked onto the end of any JSON object for conversion into RDF

    The base is added back in because @base is ignored in imported and nested contexts -- it must be at the
    root in the object itself.

    :param contexts: Ordered list of contexts to add
    :param base: base to add in (optional)
    :return: aggregated context
    """
    def prune_context_node(ctxt: Union[str, JsonObj]) -> Union[str, JsonObj]:
        return ctxt['@context'] if isinstance(ctxt, JsonObj) and '@context' in ctxt else ctxt

    def to_file_uri(fname: str) -> str:
        return 'file://' + fname

    context_list = []
    for context in [] if contexts is None else [contexts] if not isinstance(contexts, (list, tuple, set)) else contexts:
        if isinstance(context, str):
            # One of filename, URL or json text
            if context.strip().startswith("{"):
                context = loads(context)
            elif '://' not in context:
                context = to_file_uri(context)
        elif not isinstance(context, (JsonObj, str)):
            context = JsonObj(**context)    # dict
        context_list.append(prune_context_node(context))
    if base:
        context_list.append(JsonObj(**{'@base': str(base)}))
    return None if not context_list else \
        JsonObj(**{"@context": context_list[0] if len(context_list) == 1 else context_list})

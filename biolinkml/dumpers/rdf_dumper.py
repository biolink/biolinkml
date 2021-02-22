import json
from typing import Optional

from hbreader import hbread
from jsonasobj import as_dict
from pyld.jsonld import expand
from rdflib import Graph
from rdflib_pyld_compat import rdflib_graph_from_pyld_jsonld

from biolinkml.utils.context_utils import CONTEXTS_PARAM_TYPE, CONTEXT_TYPE
from biolinkml.utils.yamlutils import YAMLRoot
from biolinkml.loaders.requests_ssl_patch import no_ssl_verification


def as_rdf_graph(element: YAMLRoot, contexts: CONTEXTS_PARAM_TYPE, namespaces: CONTEXT_TYPE = None) -> Graph:
    """
    Convert element into an RDF graph guided by the context(s) in contexts
    :param element: element to represent in RDF
    :param contexts: JSON-LD context(s) in the form of:
        * file name
        * URL
        * JSON String
        * dict
        * JSON Object
        * A list containing elements of any type named above
    :param namespaces: A file name, URL, JSON String, dict or JSON object that includes the set of namespaces to
    be bound to the return graph
    :return: rdflib Graph containing element
    """
    if isinstance(contexts, list):
        inp_contexts = [json.loads(hbread(c)) for c in contexts]
    else:
        inp_contexts = json.loads(hbread(contexts))

    rdf_jsonld = expand(as_dict(element), options=dict(expandContext=inp_contexts))
    g = rdflib_graph_from_pyld_jsonld(rdf_jsonld)

    # TODO: find the official prefix loader module.  For the moment we pull this from the namespaces module
    # with open(os.path.join(LD_11_DIR, 'termci_namespaces.context.jsonld')) as cf:
    #     prefixes = json.load(cf)
    # for pfx, ns in prefixes['@context'].items():
    #     if isinstance(ns, dict):
    #         if '@id' in ns and ns.get('@prefix', True):
    #             ns = ns['@id']
    #         else:
    #             continue
    #     if not ns.startswith('@'):
    #         g.bind(pfx, ns)
    return g


def dump(element: YAMLRoot, to_file: str, contexts: CONTEXTS_PARAM_TYPE, fmt: str = 'turtle') -> None:
    """
    Write element as rdf to to_file
    :param element: LinkML object to be emitted
    :param to_file: file to write to
    :param contexts: JSON-LD context(s) in the form of:
        * file name
        * URL
        * JSON String
        * dict
        * JSON Object
        * A list containing elements of any type named above
    :param fmt: RDF format
    """
    with open(to_file, 'w') as outf:
        outf.write(dumps(element, contexts, fmt))


def dumps(element: YAMLRoot, contexts: CONTEXTS_PARAM_TYPE, fmt: Optional[str] = 'turtle') -> str:
    """
    Convert element into an RDF graph guided by the context(s) in contexts
    :param element: element to represent in RDF
    :param contexts: JSON-LD context(s) in the form of a file or URL, a json string or a json obj
    :param fmt: rdf format
    :return: rdflib Graph containing element
    """
    return as_rdf_graph(element, contexts).serialize(format=fmt).decode()
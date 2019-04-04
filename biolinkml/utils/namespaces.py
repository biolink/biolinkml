import sys
from collections import OrderedDict
from typing import Any, Tuple, Optional, List, Union

from rdflib import Namespace, URIRef, Graph

from biolinkml.utils.metamodelcore import NCName

from prefixcommons import curie_util


META_NS = "meta"
META_URI = "https://w3id.org/biolink/biolinkml/meta"


class Namespaces(OrderedDict):
    """ Namespace manager.  Functions as both a dictionary and a python
     namespace.

     Supports:  namespaces.NS [= uri]
                namespaces[NS] [= uri]
                namespaces._default [= uri]    # namespace for ':'
                namespaces._base [= uri]       # namespace for @base

     Functions: namespaces.curie_for(uri) --> curie
                namespaces.prefix_for(uri_or_curie) --> NCName
                namespaces.add_prefixmap(map name)
     """
    _default_key = '@default'
    _base_key = '@base'

    def __init__(self):
        self._prefixmaps: List[str] = []

    def __setitem__(self, key, value):
        k = NCName(key)
        v = Namespace(str(value))
        if k in self:
            if self[k] != v:
                raise ValueError(f"Namespace {k} is already mapped to {self[k]}")
        else:
            super().__setitem__(k, v)

    def __getattr__(self, item):
        return self[item]

    def __setattr__(self, key: str, value):
        if key.startswith('_'):
            super().__setattr__(key, value)
        else:
            self[key] = value

    @property
    def _default(self) -> Optional[URIRef]:
        return self.get(self._default_key, None)

    @_default.setter
    def _default(self, item: Any) -> None:
        v = Namespace(str(item))
        if self._default is not None:
            if self._default != v:
                raise ValueError(f"Default value is already set to {self._default}")
        else:
            super().__setitem__(self._default_key, v)

    @_default.deleter
    def _default(self) -> None:
        super().__delitem__(self._default_key)

    @property
    def _base(self) -> Optional[URIRef]:
        return self.get(self._base_key, None)

    @_base.setter
    def _base(self, item: Any) -> None:
        v = Namespace(str(item))
        if self._base is not None:
            if self._base != v:
                raise ValueError(f"Default value is already set to {self._default}")
        else:
            super().__setitem__(self._base_key, v)

    @_base.deleter
    def _base(self) -> None:
        super().__delitem__(self._base_key)

    def curie_for(self, uri: Any) -> Optional[str]:
        """
        Return the most appropriate CURIE for URI.  The first longest matching prefix used, if any.  If no CURIE is
        present, None is returned

        @param uri: URI to create the CURIE for
        """
        match: Tuple[str, Namespace] = ('', None)     # match string / prefix
        u = str(uri)

        # Find the longest match
        for k, v in self.items():
            vs = str(v)
            if u.startswith(vs):
                if len(vs) > len(match[0]):
                    match = (vs, k)
        if len(match[0]):
            return u.replace(match[0], match[1] + ':')
        return None

    def prefix_for(self, uri_or_curie: Any) -> Optional[str]:
        uri_or_curie = str(uri_or_curie)
        if ':/' in uri_or_curie:
            uri_or_curie = self.curie_for(uri_or_curie)
        return uri_or_curie.split(':')[0] if uri_or_curie else None

    def uri_for(self, uri_or_curie: Any) -> URIRef:
        """
        Map a curie or URI into a full URIRef.

        :param uri_or_curie: "NCNAME ':' suffix" or plain URI
        :return: Corresponding URI
        """
        uri_or_curie = str(uri_or_curie)
        if '://' in uri_or_curie:
            return URIRef(uri_or_curie)
        if ':' in uri_or_curie:
            prefix, local = str(uri_or_curie).split(':', 1)
            if not prefix:
                prefix = self._default_key
            elif not NCName.is_valid(prefix):
                raise ValueError(f"Not a valid CURIE: {uri_or_curie}")
        else:
            prefix, local = self._base_key, uri_or_curie

        if prefix not in self:
            raise ValueError(f"Unknown CURIE prefix: {prefix}")
        return URIRef(self.join(self[prefix], local))

    def uri_or_curie_for(self, prefix: Union[str, URIRef], suffix: str) -> str:
        """ Return a CURIE for prefix/suffix in possible, else a URI """
        if isinstance(prefix, URIRef) or ':/' in prefix:
            prefix_as_uri = str(prefix)
            for k, v in self.items():
                if not k.startswith('@') and prefix_as_uri == str(v):
                    return k + ':' + suffix
            return self.join(str(prefix), suffix)
        elif prefix not in self:
            raise ValueError(f"Unrecognized prefix: {prefix}")
        else:
            return prefix + ':' + suffix

    def load_graph(self, g: Graph) -> Graph:
        for k, v in self.items():
            if not k.startswith('_') and not k.startswith('@'):
                g.bind(k, URIRef(v))
        return g

    @staticmethod
    def join(prefix: str, suffix: str) -> str:
        return Namespaces.sfx(prefix) + suffix

    @staticmethod
    def sfx(uri: str) -> str:
        return str(uri) + ('' if uri.endswith(('/', '#')) else '/')

    def add_prefixmap(self, map_name: str, include_defaults: bool= True) -> None:
        """
        Add a prefixcommons map.  Only prefixes that have not been previously defined are added.

        :param map_name: prefixcommons map name
        :param include_defaults: if True, take defaults from the map.
        :return:
        """
        for k, v in curie_util.read_biocontext(map_name).items():
            if not k:
                if include_defaults and not self._default:
                    self._default = v
            elif k not in self:
                if NCName.is_valid(k):
                    self[k] = v
                else:
                    print(f"Warning: biocontext map {map_name} has illegal prefix: {k}", file=sys.stderr)

"""Generate JSON-LD contexts

"""
import os
import sys
from typing import Union, TextIO, Dict, Set, Optional

import click
from jsonasobj import JsonObj, as_json
from rdflib import XSD

from biolinkml.meta import SchemaDefinition, ClassDefinition, SlotDefinition, Definition, TypeDefinition, \
    Element
from biolinkml.utils.formatutils import camelcase, underscore, be
from biolinkml.utils.generator import Generator


class ContextGenerator(Generator):
    generatorname = os.path.basename(__file__)
    generatorversion = "0.0.2"
    valid_formats = ['json']
    visit_all_class_slots = False

    def __init__(self, schema: Union[str, TextIO, SchemaDefinition], fmt: str='json') -> None:
        super().__init__(schema, fmt)
        if self.namespaces is None:
            raise TypeError("Schema text must be supplied to context generater.  Preparsed schema will not work")
        self.emit_prefixes: Set[str] = set()
        self.default_ns = None
        self.context_body = dict()
        self.slot_class_maps = dict()

    def visit_schema(self, base: Optional[str]=None, output: Optional[str]=None, **_):

        # Add any explicitly declared prefixes
        for prefix in self.schema.prefixes.values():
            self.emit_prefixes.add(prefix.prefix_prefix)

        # Add any prefixes explicitly declared
        for pfx in self.schema.emit_prefixes:
            self.add_prefix(pfx)

        # Add the default prefix
        if self.schema.default_prefix:
            dflt = self.namespaces.prefix_for(self.schema.default_prefix)
            if dflt:
                self.default_ns = dflt
            default_uri = self.namespaces[self.default_ns]
            self.emit_prefixes.add(self.default_ns)
            self.context_body['@vocab'] = default_uri
            # self.context_body['@base'] = self.base_dir

    def end_schema(self, base: Optional[str] = None, output: Optional[str] = None, **_) -> None:
        comments = f'''Auto generated from {self.schema.source_file} by {self.generatorname} version: {self.generatorversion}
Generation date: {self.schema.generation_date}
Schema: {self.schema.name}

id: {self.schema.id}
description: {be(self.schema.description)}
license: {be(self.schema.license)}
'''
        context = JsonObj()
        context["_comments"] = comments
        context_content = {"_comments": None, "type": "@type"}
        if base:
            if '://' not in base:
                self.context_body['@base'] = os.path.relpath(base, os.path.dirname(self.schema.source_file))
            else:
                self.context_body['@base'] = base
        for prefix in sorted(self.emit_prefixes):
            if self.namespaces[prefix] != self.context_body['@vocab']:
                context_content[prefix] = self.namespaces[prefix]
        for k, v in self.context_body.items():
            context_content[k] = v
        for k, v in self.slot_class_maps.items():
            context_content[k] = v
        context['@context'] = context_content
        if output:
            with open(output, 'w') as outf:
                outf.write(as_json(context))
        else:
            print(as_json(context))

    def visit_class(self, cls: ClassDefinition) -> bool:
        class_def = {}
        cn = camelcase(cls.name)
        cls_prefix = self.namespaces.prefix_for(cls.class_uri)
        if not self.default_ns or not cls_prefix or cls_prefix != self.default_ns:
            class_def['@id'] = cls.class_uri
            if cls_prefix:
                self.emit_prefixes.add(cls_prefix)
        if class_def:
            self.slot_class_maps[cn] = class_def

        # We don't bother to visit class slots - just all slots
        return False

    def visit_slot(self, aliased_slot_name: str, slot: SlotDefinition) -> None:
        if slot.identifier:
            slot_def = '@id'
        else:
            slot_def = {}
            # TODO: clean up slot_usage items and figure out what we want to do here
            # Proxy for a slot_usage entry for the moment
            if not slot.is_a:
                if slot.range in self.schema.classes:
                    slot_def['@type'] = '@id'
                else:
                    range_type = self.schema.types[slot.range]
                    if self.namespaces.uri_for(range_type.uri) == XSD.string:
                        pass
                    elif self.namespaces.uri_for(range_type.uri) == XSD.anyURI:
                        slot_def['@type'] = '@id'
                    else:
                        slot_def['@type'] = range_type.uri
                slot_prefix = self.namespaces.prefix_for(slot.slot_uri)
                if not self.default_ns or not slot_prefix or slot_prefix != self.default_ns:
                    slot_def['@id'] = slot.slot_uri
                    if slot_prefix:
                        self.emit_prefixes.add(slot_prefix)
                # if slot.multivalued:
                #     slot_def['@container'] = '@list'
        if slot_def:
            self.context_body[underscore(aliased_slot_name)] = slot_def

    def add_prefix(self, ncname: str) -> None:
        """ Add a prefix to the list of prefixes to emit

        @param ncname: name to add
        """
        if ncname not in self.namespaces:
            print(f"Unrecognized prefix: {ncname}", file=sys.stderr)
            self.namespaces[ncname] = f"http://example.org/UNKNOWN/{ncname}/"
        self.emit_prefixes.add(ncname)



@click.command()
@click.argument("yamlfile", type=click.Path(exists=True, dir_okay=False))
@click.option("--format", "-f", default='json', type=click.Choice(ContextGenerator.valid_formats), help="Output format")
@click.option("-o", "--output", help="Output file name")
@click.option("--base", help="Base URI for model")
def cli(yamlfile, format, base, output):
    """ Generate jsonld @context definition from biolink model """
    print(ContextGenerator(yamlfile, format).serialize(base=base, output=output))

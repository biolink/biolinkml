""" Generate JSONld

"""
import os
from typing import Any, Optional

import click
from jsonasobj import as_json, loads

from biolinkml import METAMODEL_CONTEXT_URI
from biolinkml.meta import ClassDefinitionName, SlotDefinitionName, TypeDefinitionName, \
    ElementName, SlotDefinition, ClassDefinition, TypeDefinition
from biolinkml.utils.formatutils import camelcase, underscore
from biolinkml.utils.generator import Generator
from biolinkml.utils.yamlutils import YAMLRoot


class JSONLDGenerator(Generator):
    generatorname = os.path.basename(__file__)
    generatorversion = "0.0.2"
    valid_formats = ['jsonld']

    def _visit(self, node: Any) -> Optional[Any]:
        if isinstance(node, (YAMLRoot, dict)):
            if isinstance(node, YAMLRoot):
                node = node.__dict__
            for k, v in list(node.items()):
                if v:
                    new_v = self._visit(v)
                    if new_v is not None:
                        node[k] = new_v
        elif isinstance(node, list):
            for i in range(0, len(node)):
                new_v = self._visit(node[i])
                if new_v is not None:
                    node[i] = new_v
        elif isinstance(node, set):
            for v in list(node):
                new_v = self._visit(v)
                if new_v is not None:
                    node.remove(v)
                    node.add(new_v)
        elif isinstance(node, ClassDefinitionName):
            return ClassDefinitionName(camelcase(node))
        elif isinstance(node, SlotDefinitionName):
            return SlotDefinitionName(underscore(node))
        elif isinstance(node, TypeDefinitionName):
            return TypeDefinitionName(underscore(node))
        elif isinstance(node, ElementName):
            return ClassDefinitionName(camelcase(node)) if node in self.schema.classes else \
                SlotDefinitionName(underscore(node)) if node in self.schema.slots else \
                TypeDefinitionName(underscore(node)) if node in self.schema.types else None
        return None

    def adjust_slot(self, slot: SlotDefinition) -> None:
        if slot.range in self.schema.classes:
            slot.range = ClassDefinitionName(camelcase(slot.range))
        elif slot.range in self.schema.slots:
            slot.range = SlotDefinitionName(underscore(slot.range))
        elif slot.range in self.schema.types:
            slot.range = TypeDefinitionName(underscore(slot.range))
        slot.slot_uri = self.namespaces.uri_for(slot.slot_uri)

    def visit_class(self, cls: ClassDefinition) -> bool:
        self._visit(cls)
        for slot_usage in cls.slot_usage.values():
            self.adjust_slot(slot_usage)
        cls.class_uri = self.namespaces.uri_for(cls.class_uri)
        return False

    def visit_slot(self, aliased_slot_name: str, slot: SlotDefinition) -> None:
        self._visit(slot)
        self.adjust_slot(slot)

    def visit_type(self, typ: TypeDefinition) -> None:
        typ.uri = self.namespaces.uri_for(typ.uri)

    def end_schema(self, context: str = None) -> None:
        # self._visit(self.schema)
        json_str = as_json(self.schema)
        json_obj = loads(json_str)
        base_prefix = self.default_prefix()

        # JSON LD adjusts context reference using '@base'.  If context is supplied and not a URI, generate an
        # absolute URI for it
        if context is None:
            context = METAMODEL_CONTEXT_URI
        elif '://' not in context:
            context = 'file://' + os.path.abspath(os.path.join(os.getcwd(), context))

        json_obj["@context"] = [context, {'@base': base_prefix}] if base_prefix else context
        json_obj["@id"] = self.schema.id
        print(as_json(json_obj, indent="  "))


@click.command()
@click.argument("yamlfile", type=click.Path(exists=True, dir_okay=False))
@click.option("--format", "-f", default='jsonld', type=click.Choice(['jsonld']), help="Output format")
@click.option("--context", default=METAMODEL_CONTEXT_URI,
              help=f"JSONLD context file (default: {METAMODEL_CONTEXT_URI})")
def cli(yamlfile, format, context):
    """ Generate JSONLD file from biolink schema """
    print(JSONLDGenerator(yamlfile, format).serialize(context=context))

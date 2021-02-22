"""
Flatten a schema by:


"""
import os
from typing import Union, TextIO

import click

from biolinkml.generators.yamlgen import YAMLGenerator
from biolinkml.meta import SchemaDefinition, ClassDefinition, SlotDefinition
from biolinkml.utils.generator import shared_arguments
from biolinkml.utils.mergeutils import merge_schemas
from biolinkml.utils.schemaloader import SchemaLoader


class Flattener(YAMLGenerator):
    generatorname = os.path.basename(__file__)
    generatorversion = "0.1.1"
    valid_formats = ['yaml']
    visit_all_class_slots = True

    def __init__(self, schema: Union[str, TextIO, SchemaDefinition], **kwargs) -> None:
        super().__init__(schema, **kwargs)
        self.target_schema: SchemaDefinition = None

    def visit_schema(self, **kwargs) -> None:
        self.target_schema = SchemaDefinition(name=self.schema.name + '_LINK', id=self.schema.id + '_LINK')
        # self.target_schema.imports.append(self.schema.id)

    def visit_class(self, cls: ClassDefinition) -> bool:
        # Only process concrete classes that have actual slots
        return not cls.mixin and not cls.abstract and cls.slots

    def visit_class_slot(self, cls: ClassDefinition, aliased_slot_name: str, slot: SlotDefinition) -> None:
        # Multi-valued slots need to be mapped to a linking class
        if slot.multivalued:
            # TODO: there is code in the generator to make these names and copy these aliases.  If we are clever, we
            # may be able to avoid the loader call below
            linking_class = ClassDefinition(cls.name + '__' + aliased_slot_name)
            singlevalued_slot = SlotDefinition(name=cls.name + '__' + slot.name, is_a=slot.name, alias=aliased_slot_name,
                                               multivalued=False)
            base_slot = SlotDefinition(name='has_'+cls.name, domain=linking_class.name, range=singlevalued_slot.name)
            self.target_schema.slots[singlevalued_slot.name] = singlevalued_slot
            self.target_schema.slots[base_slot.name] = base_slot
            linking_class.slots = [singlevalued_slot.name, base_slot.name]
            self.target_schema.classes[linking_class.name] = linking_class

    def end_schema(self, **kwargs) -> None:
        # Merge the schema we generated with the additional classes
        merge_schemas(self.schema, self.target_schema)
        self.schema = SchemaLoader(self.schema).resolve()


@shared_arguments(Flattener)
@click.command()
def cli(yamlfile, **args):
    """ Transform and flatten the input schema  """
    print(Flattener(yamlfile, **args).serialize(**args))

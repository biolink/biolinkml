import os
from typing import Union, TextIO

import click

from biolinkml.meta import ClassDefinition, SlotDefinition, SchemaDefinition
from biolinkml.utils.formatutils import camelcase, lcamelcase
from biolinkml.utils.generator import Generator, shared_arguments


class SQLDDLGenerator(Generator):
    """
    A `Generator` for creating SQL DDL

    TODO: allow configuration between camelcase and snake case for tanle names
    
    """
    generatorname = os.path.basename(__file__)
    generatorversion = "0.1.1"
    valid_formats = ['proto']
    visit_all_class_slots = True

    def __init__(self, schema: Union[str, TextIO, SchemaDefinition], **kwargs) -> None:
        super().__init__(schema, **kwargs)
        self.relative_slot_num = 0

    def visit_class(self, cls: ClassDefinition) -> bool:
        # TODO: use sqlalchemy over prints
        #if cls.mixin or cls.abstract or not cls.slots:
        #    return False
        if cls.description:
            for dline in cls.description.split('\n'):
                print(f'// {dline}')
        print(f'CREATE TABLE {camelcase(cls.name)}')
        print(" (")
        self.relative_slot_num = 0
        return True

    def end_class(self, cls: ClassDefinition) -> None:
        print("\n)", end='')
        if cls.is_a:
            # postgresql supports inheritance
            # if you want to use plain SQL DDL then use sqlutils to unfold hierarchy
            # TODO: raise error if the target is standard SQL
            p = camelcase(cls.is_a)
            print(f' INHERITS (p)')
        print(";\n")
        # TODO: COMMENT ON TABLE

    def visit_class_slot(self, cls: ClassDefinition, aliased_slot_name: str, slot: SlotDefinition) -> None:
        #qual = 'repeated ' if slot.multivalued else 'optional ' if not slot.required or slot.key else ''
        slotname = lcamelcase(aliased_slot_name)
        slot_range = camelcase(slot.range)
        if self.relative_slot_num > 0:
            print(",")
        self.relative_slot_num += 1
        print(f"  {slotname} {slot_range}", end='')


@shared_arguments(SQLDDLGenerator)
@click.command()
def cli(yamlfile, **args):
    """ Generate SQL DDL representation of biolink model """
    print(ProtoGenerator(yamlfile, **args).serialize(**args))

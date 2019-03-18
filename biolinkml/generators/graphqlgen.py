import os
from typing import Union, TextIO, Optional

import click

from biolinkml.meta import SchemaDefinition, ClassDefinition, SlotDefinition
from biolinkml.utils.formatutils import camelcase, lcamelcase
from biolinkml.utils.generator import Generator


class GraphqlGenerator(Generator):
    generatorname = os.path.basename(__file__)
    generatorversion = "0.0.2"
    valid_formats = ['graphql']
    visit_all_class_slots = True

    def __init__(self, schema: Union[str, TextIO, SchemaDefinition], fmt: Optional[str] = None) -> None:
        super().__init__(schema, fmt)

    def visit_class(self, cls: ClassDefinition) -> bool:
        etype = 'interface' if (cls.abstract or cls.mixin) and not cls.mixins else 'type'
        mixins = ', '.join([camelcase(mixin) for mixin in cls.mixins])
        print(f"{etype} {camelcase(cls.name)}" + (f" implements {mixins}" if mixins else ""))
        print("  {")
        return True

    def end_class(self, cls: ClassDefinition) -> None:
        print("  }")
        print()

    def visit_class_slot(self, cls: ClassDefinition, aliased_slot_name: str, slot: SlotDefinition) -> None:
        slotrange = camelcase(slot.range) if slot.range in self.schema.classes or slot.range in self.schema.types else "String"
        if slot.multivalued:
            slotrange = f"[{slotrange}]"
        if slot.required:
            slotrange = slotrange + '!'
        print(f"    {lcamelcase(aliased_slot_name)}: {slotrange}")


@click.command()
@click.argument("yamlfile", type=click.Path(exists=True, dir_okay=False))
@click.option("--format", "-f", default='graphql', type=click.Choice(['graphql']), help="Output format")
def cli(yamlfile, format):
    """ Generate graphql representation of a biolink model """
    print(GraphqlGenerator(yamlfile, format).serialize())

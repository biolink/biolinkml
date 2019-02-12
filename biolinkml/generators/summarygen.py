"""Generate Summary Spreadsheets

"""
import os
import sys
from csv import DictWriter
from typing import Union, TextIO

import click

from biolinkml.meta import ClassDefinition, SchemaDefinition, SlotDefinition
from biolinkml.utils.formatutils import camelcase
from biolinkml.utils.generator import Generator


class SummaryGenerator(Generator):
    generatorname = os.path.basename(__file__)
    generatorversion = "0.1.0"
    valid_formats = ['tsv']

    def __init__(self, schema: Union[str, TextIO, SchemaDefinition], fmt: str = 'tsv') -> None:
        super().__init__(schema, fmt)
        self.dirname = None
        self.classtab: DictWriter = None
        self.slottab: DictWriter = None
        self.dialect = 'excel-tab'

    def visit_schema(self, **kwargs) -> None:
        self.classtab = DictWriter(sys.stdout,
                                   ['Class Name', 'Parent Class', 'YAML Class Name', 'Description',
                                    'Flags', 'Slot Name', 'YAML Slot Name', 'Range', 'Card', 'Slot Description', 'URI'],
                                   dialect=self.dialect)
        self.classtab.writeheader()

    def visit_class(self, cls: ClassDefinition) -> bool:
        self.classtab.writerow({'Class Name': camelcase(cls.name),
                                'Parent Class': camelcase(cls.is_a) if cls.is_a else '',
                                'YAML Class Name': cls.name,
                                'Description': cls.description})
        return True

    def visit_class_slot(self, cls: ClassDefinition, aliased_slot_name: str, slot: SlotDefinition) -> None:
        min_card = 1 if slot.required else 0
        max_card = "*" if slot.multivalued else 1
        abstract = 'A' if slot.abstract else ''
        key = 'K' if slot.key else ''
        identifier = 'I' if slot.identifier else ''
        readonly = 'R' if slot.readonly else ''
        ref = '*' if slot.range in self.schema.classes and not slot.inlined else ''
        self.classtab.writerow({'Slot Name': aliased_slot_name,
                                'Flags': abstract + key + identifier + readonly,
                                'Card': f"{min_card}..{max_card}",
                                'YAML Slot Name': slot.name if slot.name != aliased_slot_name else '',
                                'Range': ref + self.class_or_type_name(slot.range),
                                'Slot Description': slot.description,
                                'URI': slot.slot_uri})


@click.command()
@click.argument("yamlfile", type=click.Path(exists=True, dir_okay=False))
@click.option("--format", "-f", default=SummaryGenerator.valid_formats[0],
              type=click.Choice(SummaryGenerator.valid_formats), help="Output format")
def cli(yamlfile, format):
    """ Generate TSV summary files for viewing in Excel and the like """
    print(SummaryGenerator(yamlfile, format).serialize())

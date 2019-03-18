"""Generate CSVs

"""
import os
import sys
from csv import DictWriter
from typing import List, Union, TextIO, Set

import click

from biolinkml.meta import ClassDefinition, ClassDefinitionName, SchemaDefinition
from biolinkml.utils.formatutils import underscore, be
from biolinkml.utils.generator import Generator


class CsvGenerator(Generator):
    generatorname = os.path.basename(__file__)
    generatorversion = "0.1.0"
    valid_formats = ['csv', 'tsv']

    def __init__(self, schema: Union[str, TextIO, SchemaDefinition], fmt: str=None) -> None:
        super().__init__(schema, fmt)
        self.sep: str = None
        self.closure: Set[ClassDefinitionName] = None       # List of classes to include in output
        self.writer: DictWriter = None
        
    def visit_schema(self, classes: List[ClassDefinitionName] = None) -> None:
        # Note: classes comes from the "root" argument
        self.closure = set()

        if classes is None:
            classes = []

        # Validate the supplied list of classes
        for clsname in classes:
            if clsname not in self.schema.classes:
                raise ValueError(f"Unrecognized class: {clsname}")
            else:
                self.closure.update(self.ancestors(self.schema.classes[clsname]))

        dialect: str = "excel" if self.format == 'csv' else "excel-tab"
        self.writer = DictWriter(sys.stdout, ['id', 'mappings', 'description'], dialect=dialect)
        self.writer.writeheader()

    def visit_class(self, cls: ClassDefinition) -> bool:
        # TODO: find out what to do with mappings
        if not self.closure or cls.name in self.closure:
            self.writer.writerow({'id': underscore(cls.name),
                                  # 'mappings': "|".join(cls.mappings),
                                  'mappings': '',
                                  'description': be(cls.description)})
            return True
        return False


@click.command()
@click.argument("yamlfile", type=click.Path(exists=True, dir_okay=False))
@click.option("--root", "-r", default=None, multiple=True, help="Class(es) to transform")
@click.option("--format", "-f", default='csv', type=click.Choice(['csv', 'tsv']), help="Output format")
def cli(yamlfile, root, format):
    """ Generate CSV/TSV file from biolink model """
    print(CsvGenerator(yamlfile, format).serialize(classes=root))

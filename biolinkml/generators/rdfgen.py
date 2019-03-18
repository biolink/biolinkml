"""
YAML Schema to RDF Generator

Generate a JSON LD representation of the model

"""
import os
from typing import Union, TextIO, Optional

import click
from rdflib import Graph
from rdflib.plugin import plugins as rdflib_plugins, Parser as rdflib_Parser

from biolinkml import METAMODEL_CONTEXT_URI
from biolinkml.generators.jsonldgen import JSONLDGenerator
from biolinkml.meta import SchemaDefinition
from biolinkml.utils.generator import Generator


class RDFGenerator(Generator):
    generatorname = os.path.basename(__file__)
    generatorversion = "0.0.2"
    valid_formats = [x.name for x in rdflib_plugins(None, rdflib_Parser) if '/' not in str(x.name)]
    visit_all_class_slots = False

    def __init__(self, schema: Union[str, TextIO, SchemaDefinition], fmt: str = 'ttl') -> None:
        super().__init__(schema, fmt)

    def _data(self, g: Graph) -> str:
        return g.serialize(format='turtle' if self.format == 'ttl' else self.format).decode()

    def end_schema(self, output: Optional[str] = None, context: str = METAMODEL_CONTEXT_URI) -> None:
        gen = JSONLDGenerator(self, fmt=JSONLDGenerator.valid_formats[0], emit_metadata=self.emit_metadata)
        jsonld_str = gen.serialize(context=context)
        graph = Graph()
        graph.parse(data=jsonld_str, format="json-ld", base=self.namespaces._base)
        if output:
            with open(output, 'w') as outf:
                outf.write(self._data(graph))
        else:
            print(self._data(graph))


@click.command()
@click.argument("yamlfile", type=click.Path(exists=True, dir_okay=False))
@click.option("--format", "-f", default='ttl', type=click.Choice(RDFGenerator.valid_formats),
              help="Output format")
@click.option("-o", "--output", help="Output file name")
@click.option("--context", default=METAMODEL_CONTEXT_URI,
              help=f"JSONLD context file (default: {METAMODEL_CONTEXT_URI})")
def cli(yamlfile, format, output, context):
    """ Generate an RDF representation of a biolink model """
    print(RDFGenerator(yamlfile, format).serialize(output=output, context=context))

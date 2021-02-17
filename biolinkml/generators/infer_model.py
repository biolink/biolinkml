"""Infer a schema from a TSV

"""
import os
from typing import Union
from typing.io import TextIO

import click
import yaml
import csv

from biolinkml.meta import SchemaDefinition
from biolinkml.utils.generator import Generator, shared_arguments
from biolinkml.utils.yamlutils import as_yaml


def infer_model(tsvfile: str, sep="\t", class_name='example') -> dict:
    with open(tsvfile, newline='') as tsvfile:
        rr = csv.DictReader(tsvfile, delimiter=sep)
        slots = {}
        for row in rr:
            for k,v in row.items():
                if k not in slots:
                    slots[k] = {'range': None}
                if v is not None and v != "":
                    slots[k]['examples'] = {'value': v}
                slots[k]['range'] = intersect_ranges(slots[k]['range'], v)

    schema = {
        'classes': {
            class_name: {
                'slots': list(slots.keys()),
            }
        },
        'slots': slots
    }
    return schema

def intersect_ranges(current: str, v: str) -> str:
    t = None
    if v == "":
        t = None
    elif v.isdigit():
        t = 'integer'
    else:
        t = 'string'
    if current is None:
        return t
    elif current == t:
        return t
    elif t == None:
        return current
    else:
        return 'string'



def convert_range(k: str, dt: str) -> str:
    t = 'string'
    if dt == 'float64':
        t = 'float'
    return t


@click.command()
@click.argument('tsvfile') ## input TSV (must have column headers
@click.option('--class_name', '-c', default='example', help='Core class name in schema')
@click.option('--sep', '-s', default='\t', help='separator')
def cli(tsvfile, **args):
    """ Infer a model from a TSV """
    yamlobj = infer_model(tsvfile, **args)
    print(yaml.dump(yamlobj))


if __name__ == '__main__':
    cli()

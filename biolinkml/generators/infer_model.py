"""Infer a schema from a TSV

"""
import os
import requests
from typing import Union
from typing.io import TextIO

import logging
import click
import yaml
import csv
import time

from biolinkml.meta import SchemaDefinition
from biolinkml.utils.generator import Generator, shared_arguments
from biolinkml.utils.yamlutils import as_yaml


def infer_model(tsvfile: str, sep="\t", class_name='example', enum_threshold=0.1,
                max_enum_size=50,
                zooma_confidence=None) -> dict:
    with open(tsvfile, newline='') as tsvfile:
        rr = csv.DictReader(tsvfile, delimiter=sep)
        slots = {}
        slot_values = {}
        n = 0
        enums = {}
        for row in rr:
            n += 1
            for k,v in row.items():
                if k not in slots:
                    slots[k] = {'range': None}
                    slot_values[k] = set()
                if v is not None and v != "":
                    slots[k]['examples'] = {'value': v}
                    slot_values[k].add(v)
                slots[k]['range'] = intersect_ranges(slots[k]['range'], v)
        for sn,s in slots.items():
            if s['range'] == 'string':
                vals = slot_values[sn]
                n_distinct = len(vals)
                if (n_distinct / n) < enum_threshold and n_distinct <= max_enum_size:
                    enum_name = sn.replace(' ', '_')
                    enum_name = f'{enum_name}_enum'
                    s['range'] = enum_name
                    enums[enum_name] = {
                        'permissible_values': {v:get_pv_element(v, zooma_confidence) for v in vals}
                    }


    schema = {
        'classes': {
            class_name: {
                'slots': list(slots.keys()),
            }
        },
        'slots': slots,
        'enums': enums
    }
    return schema

def get_pv_element(v: str, zooma_confidence: str) -> dict:
    if zooma_confidence is None:
        return {}
    params = {'propertyValue': v}
    time.sleep(1)
    r = requests.get('http://www.ebi.ac.uk/spot/zooma/v2/api/services/annotate',params=params)
    for hit in r.json():
        id = hit['semanticTags'][0]
        logging.error(f'HIT: {id}')
        return {'meaning': id}

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
@click.option('--zooma-confidence', '-Z', help='zooma confidence')
def cli(tsvfile, **args):
    """ Infer a model from a TSV """
    yamlobj = infer_model(tsvfile, **args)
    print(yaml.dump(yamlobj, default_flow_style=False, sort_keys=False))


if __name__ == '__main__':
    cli()

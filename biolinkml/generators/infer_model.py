"""Infer a schema from a TSV

"""
import os
import re
import copy
import requests
from dataclasses import dataclass
from typing import Union, List
from typing.io import TextIO

import logging
import click
import yaml
import csv
import time

from biolinkml.meta import SchemaDefinition
from biolinkml.utils.generator import Generator, shared_arguments
from biolinkml.utils.yamlutils import as_yaml
from dateutil.parser import parse

def infer_model(tsvfile: str, sep="\t", class_name='example',
                schema_name: str = 'example',
                robot:bool = False,
                enum_columns: List[str]=[],
                enum_threshold=0.1,
                max_enum_size=50) -> dict:
    with open(tsvfile, newline='') as tsvfile:
        rr = csv.DictReader(tsvfile, delimiter=sep)
        slots = {}
        slot_values = {}
        n = 0
        enums = {}
        robot_defs = {}
        slot_usage = {}
        for row in rr:
            n += 1
            if n == 1 and robot:
                for k,v in row.items():
                    robot_defs[k] = v
                continue
            for k,v in row.items():
                vs = v.split('|')
                if k not in slots:
                    slots[k] = {'range': None}
                    slot_values[k] = set()
                if v is not None and v != "":
                    slots[k]['examples'] = {'value': v}
                    slot_values[k].update(vs)
                if len(vs) > 1:
                    slots[k]['multivalued'] = True
        types = {}
        equiv_str = None
        for sn,s in slots.items():
            vals = slot_values[sn]
            s['range'] = infer_range(s, vals, types)
            if s['range'] == 'string' or sn in enum_columns:
                n_distinct = len(vals)
                if sn in enum_columns or \
                        ((n_distinct / n) < enum_threshold and n_distinct <= max_enum_size):
                    enum_name = sn.replace(' ', '_').replace('(s)', '')
                    enum_name = f'{enum_name}_enum'
                    s['range'] = enum_name
                    enums[enum_name] = {
                        'permissible_values': {v:{'description': v} for v in vals}
                    }
            if k in robot_defs:
                rd = robot_defs[sn]
                if 'SPLIT' in rd:
                    rd = re.sub(' SPLIT.*', '', rd)
                if rd.startswith("EC"):
                    equiv_str = rd.replace('EC ', '').replace('%', '{' + k + '}')
                elif rd == 'TYPE':
                    s['slot_uri'] = 'rdf:type'
                elif rd.startswith("A "):
                    s['slot_uri'] = rd.replace('A ', '')

        if equiv_str is not None:
            slot_usage['equivalence axiom'] = { 'string_serialization': equiv_str }

    schema = {
        'id': f'https://w3id.org/{schema_name}',
        'name': schema_name,
        'description': schema_name,
        'imports': ['biolinkml:types'],
        'prefixes': {
            'biolinkml': 'https://w3id.org/biolink/biolinkml/',
            schema_name: f'https://w3id.org/{schema_name}'
        },
        'default_prefix': schema_name,
        'types': types,
        'classes': {
            class_name: {
                'slots': list(slots.keys()),
                'slot_usage': slot_usage
            }
        },
        'slots': slots,
        'enums': enums
    }
    return schema

def infer_range(slot: dict, vals: set, types: dict) -> str:
    nn_vals = [v for v in vals if v is not None and v != ""]
    if len(nn_vals) == 0:
        return 'string'
    if all(v.isdigit() for v in nn_vals):
        return 'integer'
    if all(is_date(v) for v in nn_vals):
        return 'datetime'
    v0 = nn_vals[0]
    db = get_db(v0)
    if db is not None:
        if all(get_db(v) == db for v in nn_vals):
            t = f'{db} identifier'
            types[t] = {'typeof': 'string'}
            return t
        if all(get_db(v) is not None for v in nn_vals):
            t = 'identifier'
            types[t] = {'typeof': 'string'}
            return t
    return 'string'

def get_db(id: str) -> str:
    parts = id.split(':')
    if len(parts) > 1:
        return parts[0]
    else:
        return None

def is_date(string, fuzzy=False):
    """
    Return whether the string can be interpreted as a date.

    :param string: str, string to check for date
    :param fuzzy: bool, ignore unknown tokens in string if True
    """
    try:
        parse(string, fuzzy=fuzzy)
        return True

    except ValueError:
        return False

@dataclass
class Hit():
    term_id: str
    name: str
    score: float

def get_pv_element(v: str, zooma_confidence: str, cache: dict = {}) -> Hit:
    """
    uses ZOOMA to guess a meaning of an enum permissible value

    :param v:
    :param zooma_confidence:
    :param cache:
    :return:
    """
    if v in cache:
        return cache[v][0]
    if zooma_confidence is None:
        return None

    def confidence_to_int(c: str) -> int:
        if c == 'HIGH':
            return 5
        elif c == 'GOOD':
            return 4
        elif c == 'MEDIUM':
            return 2
        elif c == 'LOW':
            return 1
        else:
            raise Exception(f'Unknown: {c}')
    confidence_threshold = confidence_to_int(zooma_confidence)

    ontscores = {
        'NCBITaxon': 1.0,
        'OMIT': -1.0,

    }

    # zooma doesn't seem to do much pre-processing, so we convert
    label = v
    if 'SARS-CoV' not in label:
        label = re.sub("([a-z])([A-Z])","\g<1> \g<2>",label) # expand CamelCase
    label = label.replace('.', ' ').replace('_', ' ')
    params = {'propertyValue': label}
    time.sleep(1) # don't overload service
    logging.info(f'Q: {params}')
    r = requests.get('http://www.ebi.ac.uk/spot/zooma/v2/api/services/annotate',params=params)
    hits = [] # List[hit]
    for hit in r.json():
        confidence = float(confidence_to_int(hit['confidence']))
        id = hit['semanticTags'][0]
        if confidence >= confidence_threshold:
            hit = Hit(term_id= id,
                            name= hit['annotatedProperty']['propertyValue'],
                            score= confidence)
            hits.append(hit)
        else:
            logging.warning(f'Skipping {id} {confidence}')
    hits = sorted(hits, key=lambda h: h.score, reverse=True)
    logging.error(f'Hits for {label} = {hits}')
    if len(hits) > 0:
        cache[label] = hits
        return hits[0]
    else:
        return None





def convert_range(k: str, dt: str) -> str:
    t = 'string'
    if dt == 'float64':
        t = 'float'
    return t

def infer_enum_meanings(schema: dict,
                        zooma_confidence: str = 'MEDIUM',
                        cache={}) -> None:
    for _,e in schema['enums'].items():
        pvs = e['permissible_values']
        for k, pv in pvs.items():
            if pv == None:
                pv = {}
                pvs[k] = pv
            if 'meaning' not in pv or pv['meaning'] is not None:
                hit = get_pv_element(k, zooma_confidence=zooma_confidence, cache=cache)
                if hit is not None:
                    pv['meaning'] = hit.term_id
                    if 'description' not in pv:
                        pv['description'] = hit.name


def merge_schemas(schemas):
    schema = copy.deepcopy(schemas[0])
    for s in schemas:
        for n,x in s['classes'].items():
            if n not in schema['classes']:
                schema['classes'][n] = x
        for n,x in s['slots'].items():
            if n not in schema['slots']:
                schema['slots'][n] = x
            else:
                None # TODO
        for n,x in s['types'].items():
            if n not in schema['types']:
                schema['types'][n] = x
            else:
                None # TODO
        for n,x in s['enums'].items():
            if n not in schema['enums']:
                schema['enums'][n] = x
            else:
                None # TODO
    return schema



@click.group()
def main():
    pass

@main.command()
@click.argument('tsvfile') ## input TSV (must have column headers
@click.option('--class_name', '-c', default='example', help='Core class name in schema')
@click.option('--schema_name', '-n', default='example', help='Schema name')
@click.option('--sep', '-s', default='\t', help='separator')
@click.option('--enum-columns', '-E', multiple=True, help='column that is forced to be an enum')
@click.option('--robot/--no-robot', default=False, help='set if the TSV is a ROBOT template')
def tsv2model(tsvfile, **args):
    """ Infer a model from a TSV """
    yamlobj = infer_model(tsvfile, **args)
    print(yaml.dump(yamlobj, default_flow_style=False, sort_keys=False))

@main.command()
@click.argument('tsvfiles', nargs=-1) ## input TSV (must have column headers
@click.option('--schema_name', '-n', default='example', help='Schema name')
@click.option('--sep', '-s', default='\t', help='separator')
@click.option('--enum-columns', '-E', multiple=True, help='column that is forced to be an enum')
@click.option('--robot/--no-robot', default=False, help='set if the TSV is a ROBOT template')
def tsvs2model(tsvfiles, **args):
    """ Infer a model from a TSV """
    yamlobjs = []
    for tsvfile in tsvfiles:
        c = os.path.splitext(os.path.basename(tsvfile))[0]
        yamlobjs.append(infer_model(tsvfile, class_name=c, **args))
    yamlobj = merge_schemas(yamlobjs)
    print(yaml.dump(yamlobj, default_flow_style=False, sort_keys=False))

@main.command()
@click.argument('yamlfile')
@click.option('--zooma-confidence', '-Z', help='zooma confidence')
@click.option('--results', '-r', help='mapping results file')
def enrich(yamlfile, results, **args):
    """ Infer a model from a TSV """
    yamlobj = yaml.load(open(yamlfile))
    cache = {}
    infer_enum_meanings(yamlobj, cache=cache)
    if results is not None:
        with open(results, "w") as io:
            #io.write(str(cache))
            io.write(yaml.dump(cache))
    print(yaml.dump(yamlobj, default_flow_style=False, sort_keys=False))

if __name__ == '__main__':
    main()

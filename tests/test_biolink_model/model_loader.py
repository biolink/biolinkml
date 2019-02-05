import os
import time
from datetime import datetime
from io import StringIO
from typing import Union, TextIO, Optional, List
from urllib.parse import urlparse
from urllib.request import Request, urlopen

import yaml

from tests.test_biolink_model.biolink_metamodel.biolink_metamodel import Model
from biolinkml.utils.namespaces import Namespaces
from biolinkml.utils.yamlutils import DupCheckYamlLoader


def load_raw_schema(data: Union[str, TextIO],
                    source_file: Optional[str] = None,
                    source_file_date: Optional[str] = None,
                    source_file_size: Optional[int] = None,
                    base_dir: Optional[str] = None) -> Model:
    """ Load and flatten SchemaDefinition from a file name, a URL or a block of text

    @param data: URL, file name or block of text
    @param source_file: Source file name for the schema if data is type TextIO
    @param source_file_date: timestamp of source file if data is type TextIO
    @param source_file_size: size of source file if data is type TextIO
    @param base_dir: Working directory or base URL of sources

    @return: Map from schema name to SchemaDefinition
    """
    def _name_from_url(url) -> str:
        return urlparse(url).path.rsplit('/', 1)[-1].rsplit('.', 1)[0]

    if isinstance(data, str):
        if '\n' in data:
            # Actual data file being passed
            return load_raw_schema(StringIO(data), source_file, source_file_date, source_file_size, base_dir)

        assert source_file is None, "source_file parameter not allowed if data is a file or URL"
        assert source_file_date is None, "source_file_date parameter not allowed if data is a file or URL"
        assert source_file_size is None, "source_file_size parameter not allowed if data is a file or URL"

        if '://' in data or (base_dir and '://' in base_dir):
            # URL being passed
            fname = Namespaces.join(base_dir, data) if '://' not in data else data
            req = Request(fname)
            req.add_header("Accept", "application/yaml, text/yaml;q=0.9")
            with urlopen(req) as response:
                return load_raw_schema(response, fname, response.info()['Last-Modified'],
                                       response.info()['Content-Length'])
        else:
            # File name being passed
            if not base_dir:
                fname = os.path.abspath(data)
                base_dir = os.path.dirname(fname)
            else:
                fname = data if os.path.isabs(data) else os.path.join(base_dir, data)
            with open(fname) as f:
                return load_raw_schema(f, fname, time.ctime(os.path.getmtime(fname)), os.path.getsize(fname), base_dir)
    else:
        model = yaml.load(data, DupCheckYamlLoader)

        # Convert the schema into a "name: definition" form
        if not all(isinstance(e, dict) for e in model.values()):
            if 'name' in model:
                modelname = model.pop('name')
            elif 'id' in model:
                modelname = _name_from_url(model['id'])
            else:
                raise ValueError("Unable to determine model name")
            model_body = [model]
            modeldefs = {modelname: model}
        else:
            model_body = list(model.values())

        def check_is_dict(element: str) -> None:
            for modelname, body in model.items():
                if element in body and not isinstance(body[element], dict):
                    raise ValueError(f'Model: {model} - {element} must be a dictionary')

        def fix_multiples(container:  str, element: str) -> None:
            """ Convert strings to lists in common elements that have both single and multiple options """
            for body in model_body:
                if container in body:
                    for c in body[container].values():
                        if c and element in c and isinstance(c[element], str):
                            c[element] = [c[element]]

        for e in ['slots', 'classes', 'types', 'subsets']:
            check_is_dict(e)

        fix_multiples('classes', 'apply_to')
        for e in ['imports']:
            for body in model_body:
                if e in body:
                    if isinstance(body[e], str):
                        body[e] = [body[e]]

        # Add the implicit domain to the slot usages
        for body in model_body:
            for cname, cls in body.get('classes', {}).items():
                if cls is None:
                    cls = {}
                    body['classes'][cname] = cls
                for uname, usage in cls.get('slot_usage', {}).items():
                    if usage is None:
                        usage = {}
                        cls['slot_usage'][uname] = usage
                    if 'domain' not in usage:
                        usage['domain'] = cname

        model: Model = None
        for sname, mdef in {k: Model(name=k, **v) for k, v in modeldefs.items()}.items():
            if model is None:
                model = mdef
                if source_file:
                    model.source_file = source_file
                model.source_file_date = source_file_date
                model.source_file_size = source_file_size
                model.generation_date = datetime.now().strftime("%Y-%m-%d %H:%M")
                # model.metamodel_version = metamodel_version
                # set_from_schema(model)
            else:
                # TODO: Is this needed
                # merge_models(model, mdef)
                pass
        return model


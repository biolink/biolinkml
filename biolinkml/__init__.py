import os

from rdflib import Namespace

""" 
URIs, Local Names and Namespaces 

Physical layout:
    biolinkml/
        |
        +------ meta.yaml
        |
        +------ context.jsonld
        |
        +------ meta.shex
        |
        +------ meta.shexj
        |
        +------ meta.ttl
        |
        +------ meta.owl
        |
        +------ includes/
        |          |
        |          +--- types.yaml
        |          |
        |          +--- types.py
        |
        +------ biolinkml/
        |          |
        |           +--- meta.py
        +------ docs/
                  |
                  +--- abstract.md
                  |
                  +--- Element.md
                  |
                  +---    ...
                  |
                  +--- types/
                         |
                         +--- boolean.md


URI Maps:
    # Access to the root directory -- the whole project
    https://w3id.org/biolink/biolinkml        --> biolinkml
    
    # Access to the entire metamodel in various formats
    https://w3id.org/biolink/biolinkml/meta   --> biolinkml/meta   (.yaml, .shex, .ttl, .owl) -- conneg
    
    # Access to documentation on metamodel components
    https://w3id.org/biolink/biolinkml/meta/  --> biolink/docs/
    
    # Access to the entire types model in various formats
    https://w3id.org/biolink/biolinkml/types  --> biolink/includes/types (.yaml, .shex, .ttl, .owl) -- conneg
    
    # Access to documentation on type components
    https://w3id.org/biolink/biolinkml/types/ --> biolink/docs/types/



"""

METAMODEL_FILE_NAME = 'meta.yaml'
METAMODEL_LDCONTEXT_NAME = 'context.jsonld'
METAMODEL_SHEXC_NAME = 'meta.shex'
METAMODEL_SHEXJ_NAME = 'meta.shexj'
METAMODEL_RDF_NAME = 'meta.ttl'
TYPES_FILE_NAME = 'types.yaml'


MODULE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
INCLUDES_DIR = os.path.join(MODULE_DIR, 'includes')

# Local location of meta.yaml and types.yaml
LOCAL_YAML_PATH = os.path.join(MODULE_DIR, METAMODEL_FILE_NAME)
LOCAL_TYPES_PATH = os.path.join(INCLUDES_DIR, TYPES_FILE_NAME)

# Local location of metamodel context.jsonld file
LOCAL_CONTEXT_PATH = os.path.join(MODULE_DIR, METAMODEL_LDCONTEXT_NAME)

# Local location of metamodel shex file
LOCAL_SHEXJ_PATH = os.path.join(MODULE_DIR, METAMODEL_SHEXJ_NAME)

# Local location of the metamodel rdf file
LOCAL_RDF_PATH = os.path.join(MODULE_DIR, METAMODEL_RDF_NAME)

# Base URI for all things meta
META_BASE_URI = 'https://w3id.org/biolink/biolinkml/'

# URI for the entire metamodel itself.
METAMODEL_URI = META_BASE_URI + 'meta'
METATYPE_URI = META_BASE_URI + 'types'

# Preferred local name for metamodel elements
METAMODEL_LOCAL_NAME = "meta"
METATYPE_LOCAL_NAME = 'metatype'

# Namespace for metamodel elements
METAMODEL_NAMESPACE = Namespace(METAMODEL_URI + '/')
METATYPE_NAMESPACE = Namespace(META_BASE_URI + 'type/')

# Metamodel Context URI
METAMODEL_CONTEXT_URI = META_BASE_URI + METAMODEL_LDCONTEXT_NAME

# Metamodel ShEx URI
METAMODEL_SHEXJ_URI = META_BASE_URI + 'meta.shexj'
METAMODEL_SHEXC_URI = META_BASE_URI + 'meta.shexc'

# Metamodel YAML file
METAMODEL_YAML_URI = META_BASE_URI + 'meta.yaml'

# Biolink model file -- this needs a more official fix
BIOLINK_MODEL_URI = "https://w3id.org/biolink/biolink-model"
BIOLINK_MODEL_PYTHON_LOC = "biolink.model"

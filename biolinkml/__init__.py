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
METAMODEL_SHEX_NAME = 'meta.shex'
METAMODEL_RDF_NAME = 'meta.ttl'
TYPES_FILE_NAME = 'types.yaml'


# Location of meta.yaml and types.yaml
MODULE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
LOCAL_YAML_PATH = os.path.join(MODULE_DIR, METAMODEL_FILE_NAME)
LOCAL_TYPES_PATH = os.path.join(MODULE_DIR, 'includes', TYPES_FILE_NAME)

# Location of metamodel context.jsonld
LOCAL_CONTEXT_PATH = os.path.join(MODULE_DIR, METAMODEL_LDCONTEXT_NAME)

# Location of metamodel shex file
LOCAL_SHEX_PATH = os.path.join(MODULE_DIR, METAMODEL_SHEX_NAME)

# Location of the metamodel rdf file
LOCAL_RDF_PATH = os.path.join(MODULE_DIR, METAMODEL_RDF_NAME)

# Base URI for all things meta
META_BASE_URI = 'https://w3id.org/biolink/biolinkml'

# URI for the entire metamodel itself.
METAMODEL_URI = META_BASE_URI + '/meta'
METATYPE_URI = META_BASE_URI + '/types'

# Preferred local name for metamodel elements
METAMODEL_LOCAL_NAME = "meta"
METATYPE_LOCAL_NAME = 'metatype'

# Namespace for metamodel elements
METAMODEL_NAMESPACE = Namespace(METAMODEL_URI + '/')
METATYPE_NAMESPACE = Namespace(META_BASE_URI + '/type/')

# Metamodel Context URI
METAMODEL_CONTEXT_URI = META_BASE_URI + '/context.jsonld'

# Metamodel ShEx URI
METAMODEL_SHEX_URI = META_BASE_URI + '/meta.shex'

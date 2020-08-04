# Auto generated from issue_84.yaml by pythongen.py version: 0.4.0
# Generation date: 2020-08-04 09:38
# Schema: nmdc_schema
#
# id: https://microbiomedata/schema
# description: Schema for NMDC. Alpha. Currently focuses on samples
# license: https://creativecommons.org/publicdomain/zero/1.0/

import dataclasses
import sys
from typing import Optional, List, Union, Dict, ClassVar, Any
from dataclasses import dataclass
from biolinkml.utils.slot import Slot
from biolinkml.utils.metamodelcore import empty_list, empty_dict, bnode
from biolinkml.utils.yamlutils import YAMLRoot, extended_str, extended_float, extended_int
if sys.version_info < (3, 7, 6):
    from biolinkml.utils.dataclass_extensions_375 import dataclasses_init_fn_with_kwargs
else:
    from biolinkml.utils.dataclass_extensions_376 import dataclasses_init_fn_with_kwargs
from biolinkml.utils.formatutils import camelcase, underscore, sfx
from rdflib import Namespace, URIRef
from biolinkml.utils.curienamespace import CurieNamespace
from biolinkml.utils.metamodelcore import ElementIdentifier
from includes.types import Double, Float, String

metamodel_version = "1.5.3"

# Overwrite dataclasses _init_fn to add **kwargs in __init__
dataclasses._init_fn = dataclasses_init_fn_with_kwargs

# Namespaces
UO = CurieNamespace('UO', 'http://purl.obolibrary.org/obo/UO_')
BIOLINKML = CurieNamespace('biolinkml', 'https://w3id.org/biolink/biolinkml/')
DCTERMS = CurieNamespace('dcterms', 'http://example.org/UNKNOWN/dcterms/')
NMDC = CurieNamespace('nmdc', 'https://microbiomedata/meta/')
QUD = CurieNamespace('qud', 'http://qudt.org/1.1/schema/qudt#')
RDF = CurieNamespace('rdf', 'http://example.org/UNKNOWN/rdf/')
RDFS = CurieNamespace('rdfs', 'http://example.org/UNKNOWN/rdfs/')
SKOS = CurieNamespace('skos', 'http://example.org/UNKNOWN/skos/')
WGS = CurieNamespace('wgs', 'http://www.w3.org/2003/01/geo/wgs84_pos')
XSD = CurieNamespace('xsd', 'http://www.w3.org/2001/XMLSchema#')
DEFAULT_ = NMDC


# Types
class IdentifierType(ElementIdentifier):
    """ A string that is intended to uniquely identify a thing May be URI in full or compact (CURIE) form """
    type_class_uri = XSD.anyURI
    type_class_curie = "xsd:anyURI"
    type_name = "identifier type"
    type_model_uri = NMDC.IdentifierType


# Class references
class BiosampleId(ElementIdentifier):
    pass


class CharacteristicId(ElementIdentifier):
    pass


class OntologyClassId(ElementIdentifier):
    pass


@dataclass
class Biosample(YAMLRoot):
    """
    A material sample. May be environmental (encompassing many organisms) or isolate or tissue
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = NMDC.Biosample
    class_class_curie: ClassVar[str] = "nmdc:Biosample"
    class_name: ClassVar[str] = "biosample"
    class_model_uri: ClassVar[URIRef] = NMDC.Biosample

    id: Union[ElementIdentifier, BiosampleId]
    name: Optional[str] = None
    annotations: List[Union[dict, "Annotation"]] = empty_list()
    alternate_identifiers: List[ElementIdentifier] = empty_list()

    def __post_init__(self, **kwargs: Dict[str, Any]):
        if self.id is None:
            raise ValueError(f"id must be supplied")
        if not isinstance(self.id, BiosampleId):
            self.id = BiosampleId(self.id)
        self.annotations = [Annotation(*e) for e in self.annotations.items()] if isinstance(self.annotations, dict) \
                            else [v if isinstance(v, Annotation) else Annotation(**v)
                                  for v in ([self.annotations] if isinstance(self.annotations, str) else self.annotations)]
        super().__post_init__(**kwargs)


@dataclass
class BiosampleProcessing(YAMLRoot):
    """
    A process that takes one or more biosamples as inputs and generates one or more as output
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = NMDC.BiosampleProcessing
    class_class_curie: ClassVar[str] = "nmdc:BiosampleProcessing"
    class_name: ClassVar[str] = "biosample processing"
    class_model_uri: ClassVar[URIRef] = NMDC.BiosampleProcessing

    input: List[Union[ElementIdentifier, BiosampleId]] = empty_list()
    output: List[Union[ElementIdentifier, BiosampleId]] = empty_list()

    def __post_init__(self, **kwargs: Dict[str, Any]):
        self.input = [v if isinstance(v, BiosampleId)
                      else BiosampleId(v) for v in ([self.input] if isinstance(self.input, str) else self.input)]
        self.output = [v if isinstance(v, BiosampleId)
                       else BiosampleId(v) for v in ([self.output] if isinstance(self.output, str) else self.output)]
        super().__post_init__(**kwargs)


@dataclass
class Annotation(YAMLRoot):
    """
    An annotation on a sample. This is essentially a key value pair
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = NMDC.Annotation
    class_class_curie: ClassVar[str] = "nmdc:Annotation"
    class_name: ClassVar[str] = "annotation"
    class_model_uri: ClassVar[URIRef] = NMDC.Annotation

    has_raw_value: str
    has_characteristic: Optional[Union[ElementIdentifier, CharacteristicId]] = None
    has_normalized_value: Optional[Union[dict, "NormalizedValue"]] = None

    def __post_init__(self, **kwargs: Dict[str, Any]):
        if self.has_characteristic is not None and not isinstance(self.has_characteristic, CharacteristicId):
            self.has_characteristic = CharacteristicId(self.has_characteristic)
        if self.has_raw_value is None:
            raise ValueError(f"has_raw_value must be supplied")
        if self.has_normalized_value is not None and not isinstance(self.has_normalized_value, NormalizedValue):
            self.has_normalized_value = NormalizedValue()
        super().__post_init__(**kwargs)


@dataclass
class Characteristic(YAMLRoot):
    """
    A characteristic of a biosample. Examples: depth, habitat, material, ... For NMDC, characteristics SHOULD be
    mapped to fields within a MIxS template
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = NMDC.Characteristic
    class_class_curie: ClassVar[str] = "nmdc:Characteristic"
    class_name: ClassVar[str] = "characteristic"
    class_model_uri: ClassVar[URIRef] = NMDC.Characteristic

    id: Union[ElementIdentifier, CharacteristicId]
    name: Optional[str] = None
    description: Optional[str] = None
    alternate_identifiers: List[ElementIdentifier] = empty_list()

    def __post_init__(self, **kwargs: Dict[str, Any]):
        if self.id is None:
            raise ValueError(f"id must be supplied")
        if not isinstance(self.id, CharacteristicId):
            self.id = CharacteristicId(self.id)
        super().__post_init__(**kwargs)


class NormalizedValue(YAMLRoot):
    """
    The value that was specified for an annotation in parsed/normalized form. This could be a range of different types
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = NMDC.NormalizedValue
    class_class_curie: ClassVar[str] = "nmdc:NormalizedValue"
    class_name: ClassVar[str] = "normalized value"
    class_model_uri: ClassVar[URIRef] = NMDC.NormalizedValue


@dataclass
class QuantityValue(NormalizedValue):
    """
    A simple quantity, e.g. 2cm
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = NMDC.QuantityValue
    class_class_curie: ClassVar[str] = "nmdc:QuantityValue"
    class_name: ClassVar[str] = "quantity value"
    class_model_uri: ClassVar[URIRef] = NMDC.QuantityValue

    has_unit: Optional[Union[dict, "Unit"]] = None
    has_numeric_value: Optional[float] = None

    def __post_init__(self, **kwargs: Dict[str, Any]):
        if self.has_unit is not None and not isinstance(self.has_unit, Unit):
            self.has_unit = Unit()
        super().__post_init__(**kwargs)


@dataclass
class ControlledTermValue(NormalizedValue):
    """
    A controlled term or class from an ontology
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = NMDC.ControlledTermValue
    class_class_curie: ClassVar[str] = "nmdc:ControlledTermValue"
    class_name: ClassVar[str] = "controlled term value"
    class_model_uri: ClassVar[URIRef] = NMDC.ControlledTermValue

    instance_of: Optional[Union[ElementIdentifier, OntologyClassId]] = None

    def __post_init__(self, **kwargs: Dict[str, Any]):
        if self.instance_of is not None and not isinstance(self.instance_of, OntologyClassId):
            self.instance_of = OntologyClassId(self.instance_of)
        super().__post_init__(**kwargs)


@dataclass
class GeolocationValue(NormalizedValue):
    """
    A normalized value for a location on the earth's surface
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = NMDC.GeolocationValue
    class_class_curie: ClassVar[str] = "nmdc:GeolocationValue"
    class_name: ClassVar[str] = "geolocation value"
    class_model_uri: ClassVar[URIRef] = NMDC.GeolocationValue

    latitude: Optional[float] = None
    longitude: Optional[float] = None

class Unit(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = NMDC.Unit
    class_class_curie: ClassVar[str] = "nmdc:Unit"
    class_name: ClassVar[str] = "unit"
    class_model_uri: ClassVar[URIRef] = NMDC.Unit


@dataclass
class OntologyClass(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = NMDC.OntologyClass
    class_class_curie: ClassVar[str] = "nmdc:OntologyClass"
    class_name: ClassVar[str] = "ontology class"
    class_model_uri: ClassVar[URIRef] = NMDC.OntologyClass

    id: Union[ElementIdentifier, OntologyClassId]
    name: Optional[str] = None

    def __post_init__(self, **kwargs: Dict[str, Any]):
        if self.id is None:
            raise ValueError(f"id must be supplied")
        if not isinstance(self.id, OntologyClassId):
            self.id = OntologyClassId(self.id)
        super().__post_init__(**kwargs)



# Slots
class slots:
    pass

slots.id = Slot(uri=NMDC.id, name="id", curie=NMDC.curie('id'),
                      model_uri=NMDC.id, domain=None, range=URIRef)

slots.name = Slot(uri=NMDC.name, name="name", curie=NMDC.curie('name'),
                      model_uri=NMDC.name, domain=None, range=Optional[str])

slots.description = Slot(uri=DCTERMS.description, name="description", curie=DCTERMS.curie('description'),
                      model_uri=NMDC.description, domain=None, range=Optional[str])

slots.has_characteristic = Slot(uri=NMDC.has_characteristic, name="has characteristic", curie=NMDC.curie('has_characteristic'),
                      model_uri=NMDC.has_characteristic, domain=Annotation, range=Optional[Union[ElementIdentifier, CharacteristicId]])

slots.instance_of = Slot(uri=NMDC.instance_of, name="instance of", curie=NMDC.curie('instance_of'),
                      model_uri=NMDC.instance_of, domain=None, range=Optional[Union[ElementIdentifier, OntologyClassId]])

slots.has_raw_value = Slot(uri=NMDC.has_raw_value, name="has raw value", curie=NMDC.curie('has_raw_value'),
                      model_uri=NMDC.has_raw_value, domain=Annotation, range=str)

slots.has_normalized_value = Slot(uri=NMDC.has_normalized_value, name="has normalized value", curie=NMDC.curie('has_normalized_value'),
                      model_uri=NMDC.has_normalized_value, domain=Annotation, range=Optional[Union[dict, "NormalizedValue"]])

slots.has_unit = Slot(uri=NMDC.has_unit, name="has unit", curie=NMDC.curie('has_unit'),
                      model_uri=NMDC.has_unit, domain=None, range=Optional[Union[dict, Unit]], mappings = [QUD.unit])

slots.has_numeric_value = Slot(uri=NMDC.has_numeric_value, name="has numeric value", curie=NMDC.curie('has_numeric_value'),
                      model_uri=NMDC.has_numeric_value, domain=None, range=Optional[float], mappings = [QUD.quantityValue])

slots.alternate_identifiers = Slot(uri=NMDC.alternate_identifiers, name="alternate identifiers", curie=NMDC.curie('alternate_identifiers'),
                      model_uri=NMDC.alternate_identifiers, domain=None, range=List[ElementIdentifier])

slots.annotations = Slot(uri=NMDC.annotations, name="annotations", curie=NMDC.curie('annotations'),
                      model_uri=NMDC.annotations, domain=Biosample, range=List[Union[dict, "Annotation"]])

slots.latitude = Slot(uri=WGS.lat, name="latitude", curie=WGS.curie('lat'),
                      model_uri=NMDC.latitude, domain=None, range=Optional[float])

slots.longitude = Slot(uri=WGS.long, name="longitude", curie=WGS.curie('long'),
                      model_uri=NMDC.longitude, domain=None, range=Optional[float])

slots.input = Slot(uri=NMDC.input, name="input", curie=NMDC.curie('input'),
                      model_uri=NMDC.input, domain=None, range=List[Union[ElementIdentifier, BiosampleId]])

slots.output = Slot(uri=NMDC.output, name="output", curie=NMDC.curie('output'),
                      model_uri=NMDC.output, domain=None, range=List[Union[ElementIdentifier, BiosampleId]])

slots.biosample_id = Slot(uri=NMDC.id, name="biosample_id", curie=NMDC.curie('id'),
                      model_uri=NMDC.biosample_id, domain=Biosample, range=Union[ElementIdentifier, BiosampleId])

slots.biosample_name = Slot(uri=NMDC.name, name="biosample_name", curie=NMDC.curie('name'),
                      model_uri=NMDC.biosample_name, domain=Biosample, range=Optional[str])

slots.biosample_alternate_identifiers = Slot(uri=NMDC.alternate_identifiers, name="biosample_alternate identifiers", curie=NMDC.curie('alternate_identifiers'),
                      model_uri=NMDC.biosample_alternate_identifiers, domain=Biosample, range=List[ElementIdentifier])
# Auto generated from .yaml by pythongen.py version:
# Generation date:
# Schema: metamodel
#
# id: https://w3id.org/biolink/biolinkml/meta
# description: A metamodel for defining biolink related schemas
# license: https://creativecommons.org/publicdomain/zero/1.0/

from typing import Optional, List, Union, Dict, ClassVar
from dataclasses import dataclass
from biolinkml.utils.metamodelcore import empty_list, empty_dict, bnode
from biolinkml.utils.yamlutils import YAMLRoot
from biolinkml.utils.formatutils import camelcase, underscore, sfx
from rdflib import Namespace, URIRef
from biolinkml.utils.metamodelcore import Bool, NCName, URI, URIorCURIE, XSDDateTime
from includes.types import Boolean, Datetime, Integer, Ncname, String, Uri, Uriorcurie

metamodel_version = "1.4.1"


# Namespaces
OIO = Namespace('http://www.geneontology.org/formats/oboInOwl#')
DCTERMS = Namespace('http://purl.org/dc/terms/')
META = Namespace('https://w3id.org/biolink/biolinkml/meta/')
OWL = Namespace('http://www.w3.org/2002/07/owl#')
PAV = Namespace('http://purl.org/pav/')
RDF = Namespace('http://www.w3.org/1999/02/22-rdf-syntax-ns#')
RDFS = Namespace('http://www.w3.org/2000/01/rdf-schema#')
SHEX = Namespace('http://www.w3.org/ns/shex#')
SKOS = Namespace('http://www.w3.org/2004/02/skos/core#')
XSD = Namespace('http://www.w3.org/2001/XMLSchema#')
DEFAULT_ = META


# Types

# Class references
class ElementName(str):
    pass


class SchemaDefinitionName(ElementName):
    pass


class TypeDefinitionName(ElementName):
    pass


class SubsetDefinitionName(ElementName):
    pass


class DefinitionName(ElementName):
    pass


class SlotDefinitionName(DefinitionName):
    pass


class ClassDefinitionName(DefinitionName):
    pass


class PrefixPrefixPrefix(NCName):
    pass


class LocalNameLocalNameSource(NCName):
    pass


class AltDescriptionSource(NCName):
    pass


@dataclass
class Element(YAMLRoot):
    """
    a named element in the model
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = META.Element
    class_class_curie: ClassVar[str] = "meta:Element"
    class_name: ClassVar[str] = "element"
    class_model_uri: ClassVar[URIRef] = META.Element

    name: Union[str, ElementName]
    id_prefixes: List[Union[str, NCName]] = empty_list()
    aliases: List[str] = empty_list()
    local_names: Union[dict, "LocalName"] = empty_dict()
    mappings: List[Union[str, URIorCURIE]] = empty_list()
    description: Optional[str] = None
    alt_descriptions: Union[dict, "AltDescription"] = empty_dict()
    deprecated: Optional[str] = None
    todos: List[str] = empty_list()
    notes: List[str] = empty_list()
    comments: List[str] = empty_list()
    examples: List[Union[dict, "Example"]] = empty_list()
    in_subset: List[Union[str, SubsetDefinitionName]] = empty_list()
    from_schema: Optional[Union[str, URI]] = None
    imported_from: Optional[str] = None
    see_also: List[Union[str, URIorCURIE]] = empty_list()

    def __post_init__(self):
        self.id_prefixes = [v if isinstance(v, NCName)
                            else NCName(v) for v in self.id_prefixes]
        if self.name is None:
            raise ValueError(f"name must be supplied")
        if not isinstance(self.name, ElementName):
            self.name = ElementName(self.name)
        for k, v in self.local_names.items():
            if not isinstance(v, LocalName):
                self.local_names[k] = LocalName(k, v)
        self.mappings = [v if isinstance(v, URIorCURIE)
                         else URIorCURIE(v) for v in self.mappings]
        for k, v in self.alt_descriptions.items():
            if not isinstance(v, AltDescription):
                self.alt_descriptions[k] = AltDescription(k, v)
        self.examples = [v if isinstance(v, Example)
                         else Example(**v) for v in self.examples]
        self.in_subset = [v if isinstance(v, SubsetDefinitionName)
                          else SubsetDefinitionName(v) for v in self.in_subset]
        if self.from_schema is not None and not isinstance(self.from_schema, URI):
            self.from_schema = URI(self.from_schema)
        self.see_also = [v if isinstance(v, URIorCURIE)
                         else URIorCURIE(v) for v in self.see_also]
        super().__post_init__()


@dataclass
class SchemaDefinition(Element):
    """
    a collection of subset, type, slot and class definitions
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = META.SchemaDefinition
    class_class_curie: ClassVar[str] = "meta:SchemaDefinition"
    class_name: ClassVar[str] = "schema_definition"
    class_model_uri: ClassVar[URIRef] = META.SchemaDefinition

    name: Union[str, SchemaDefinitionName] = None
    id: Union[str, URI] = None
    title: Optional[str] = None
    version: Optional[str] = None
    imports: List[Union[str, URIorCURIE]] = empty_list()
    license: Optional[str] = None
    prefixes: Union[dict, "Prefix"] = empty_dict()
    emit_prefixes: List[Union[str, NCName]] = empty_list()
    default_curi_maps: List[str] = empty_list()
    default_prefix: Optional[str] = None
    default_range: Optional[Union[str, TypeDefinitionName]] = None
    subsets: Dict[Union[str, SubsetDefinitionName], Union[dict, "SubsetDefinition"]] = empty_dict()
    types: Dict[Union[str, TypeDefinitionName], Union[dict, "TypeDefinition"]] = empty_dict()
    slots: Dict[Union[str, SlotDefinitionName], Union[dict, "SlotDefinition"]] = empty_dict()
    classes: Dict[Union[str, ClassDefinitionName], Union[dict, "ClassDefinition"]] = empty_dict()
    metamodel_version: Optional[str] = None
    source_file: Optional[str] = None
    source_file_date: Optional[Union[str, XSDDateTime]] = None
    source_file_size: Optional[int] = None
    generation_date: Optional[Union[str, XSDDateTime]] = None

    def __post_init__(self):
        if self.default_prefix is None:
            self.default_prefix = sfx(str(self.id))
        if self.name is None:
            raise ValueError(f"name must be supplied")
        if not isinstance(self.name, SchemaDefinitionName):
            self.name = SchemaDefinitionName(self.name)
        if self.id is None:
            raise ValueError(f"id must be supplied")
        if not isinstance(self.id, URI):
            self.id = URI(self.id)
        self.imports = [v if isinstance(v, URIorCURIE)
                        else URIorCURIE(v) for v in self.imports]
        for k, v in self.prefixes.items():
            if not isinstance(v, Prefix):
                self.prefixes[k] = Prefix(k, v)
        self.emit_prefixes = [v if isinstance(v, NCName)
                              else NCName(v) for v in self.emit_prefixes]
        if self.default_range is not None and not isinstance(self.default_range, TypeDefinitionName):
            self.default_range = TypeDefinitionName(self.default_range)
        for k, v in self.subsets.items():
            if not isinstance(v, SubsetDefinition):
                self.subsets[k] = SubsetDefinition(name=k, **({} if v is None else v))
        for k, v in self.types.items():
            if not isinstance(v, TypeDefinition):
                self.types[k] = TypeDefinition(name=k, **({} if v is None else v))
        for k, v in self.slots.items():
            if not isinstance(v, SlotDefinition):
                self.slots[k] = SlotDefinition(name=k, **({} if v is None else v))
        for k, v in self.classes.items():
            if not isinstance(v, ClassDefinition):
                self.classes[k] = ClassDefinition(name=k, **({} if v is None else v))
        if self.source_file_date is not None and not isinstance(self.source_file_date, XSDDateTime):
            self.source_file_date = XSDDateTime(self.source_file_date)
        if self.generation_date is not None and not isinstance(self.generation_date, XSDDateTime):
            self.generation_date = XSDDateTime(self.generation_date)
        super().__post_init__()


@dataclass
class TypeDefinition(Element):
    """
    A data type definition.
    """
    _inherited_slots: ClassVar[List[str]] = ["base", "uri", "repr"]

    class_class_uri: ClassVar[URIRef] = META.TypeDefinition
    class_class_curie: ClassVar[str] = "meta:TypeDefinition"
    class_name: ClassVar[str] = "type_definition"
    class_model_uri: ClassVar[URIRef] = META.TypeDefinition

    name: Union[str, TypeDefinitionName] = None
    typeof: Optional[Union[str, TypeDefinitionName]] = None
    base: Optional[str] = None
    uri: Optional[Union[str, URIorCURIE]] = None
    repr: Optional[str] = None

    def __post_init__(self):
        if self.name is None:
            raise ValueError(f"name must be supplied")
        if not isinstance(self.name, TypeDefinitionName):
            self.name = TypeDefinitionName(self.name)
        if self.typeof is not None and not isinstance(self.typeof, TypeDefinitionName):
            self.typeof = TypeDefinitionName(self.typeof)
        if self.uri is not None and not isinstance(self.uri, URIorCURIE):
            self.uri = URIorCURIE(self.uri)
        super().__post_init__()


@dataclass
class SubsetDefinition(Element):
    """
    the name and description of a subset
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = META.SubsetDefinition
    class_class_curie: ClassVar[str] = "meta:SubsetDefinition"
    class_name: ClassVar[str] = "subset_definition"
    class_model_uri: ClassVar[URIRef] = META.SubsetDefinition

    name: Union[str, SubsetDefinitionName] = None

    def __post_init__(self):
        if self.name is None:
            raise ValueError(f"name must be supplied")
        if not isinstance(self.name, SubsetDefinitionName):
            self.name = SubsetDefinitionName(self.name)
        super().__post_init__()


@dataclass
class Definition(Element):
    """
    base class for definitions
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = META.Definition
    class_class_curie: ClassVar[str] = "meta:Definition"
    class_name: ClassVar[str] = "definition"
    class_model_uri: ClassVar[URIRef] = META.Definition

    name: Union[str, DefinitionName] = None
    is_a: Optional[Union[str, DefinitionName]] = None
    abstract: Optional[Bool] = None
    mixin: Optional[Bool] = None
    mixins: List[Union[str, DefinitionName]] = empty_list()
    apply_to: List[Union[str, DefinitionName]] = empty_list()
    values_from: List[Union[str, URIorCURIE]] = empty_list()

    def __post_init__(self):
        if self.is_a is not None and not isinstance(self.is_a, DefinitionName):
            self.is_a = DefinitionName(self.is_a)
        self.mixins = [v if isinstance(v, DefinitionName)
                       else DefinitionName(v) for v in self.mixins]
        self.apply_to = [v if isinstance(v, DefinitionName)
                         else DefinitionName(v) for v in self.apply_to]
        self.values_from = [v if isinstance(v, URIorCURIE)
                            else URIorCURIE(v) for v in self.values_from]
        super().__post_init__()


@dataclass
class SlotDefinition(Definition):
    """
    the definition of a property or a slot
    """
    _inherited_slots: ClassVar[List[str]] = ["domain", "range", "multivalued", "inherited", "readonly", "ifabsent", "required", "inlined", "key", "identifier", "role"]

    class_class_uri: ClassVar[URIRef] = META.SlotDefinition
    class_class_curie: ClassVar[str] = "meta:SlotDefinition"
    class_name: ClassVar[str] = "slot_definition"
    class_model_uri: ClassVar[URIRef] = META.SlotDefinition

    name: Union[str, SlotDefinitionName] = None
    is_a: Optional[Union[str, SlotDefinitionName]] = None
    mixins: List[Union[str, SlotDefinitionName]] = empty_list()
    apply_to: List[Union[str, SlotDefinitionName]] = empty_list()
    singular_name: Optional[str] = None
    domain: Optional[Union[str, ClassDefinitionName]] = None
    range: Optional[Union[str, ElementName]] = None
    slot_uri: Optional[Union[str, URIorCURIE]] = None
    multivalued: Optional[Bool] = None
    inherited: Optional[Bool] = None
    readonly: Optional[str] = None
    ifabsent: Optional[str] = None
    required: Optional[Bool] = None
    inlined: Optional[Bool] = None
    key: Optional[Bool] = None
    identifier: Optional[Bool] = None
    alias: Optional[str] = None
    owner: Optional[Union[str, DefinitionName]] = None
    subproperty_of: Optional[Union[str, URIorCURIE]] = None
    symmetric: Optional[Bool] = None
    inverse: Optional[Union[str, SlotDefinitionName]] = None
    is_class_field: Optional[Bool] = None
    role: Optional[str] = None
    is_usage_slot: Optional[Bool] = None

    def __post_init__(self):
        if self.name is None:
            raise ValueError(f"name must be supplied")
        if not isinstance(self.name, SlotDefinitionName):
            self.name = SlotDefinitionName(self.name)
        if self.is_a is not None and not isinstance(self.is_a, SlotDefinitionName):
            self.is_a = SlotDefinitionName(self.is_a)
        self.mixins = [v if isinstance(v, SlotDefinitionName)
                       else SlotDefinitionName(v) for v in self.mixins]
        self.apply_to = [v if isinstance(v, SlotDefinitionName)
                         else SlotDefinitionName(v) for v in self.apply_to]
        if self.domain is not None and not isinstance(self.domain, ClassDefinitionName):
            self.domain = ClassDefinitionName(self.domain)
        if self.range is not None and not isinstance(self.range, ElementName):
            self.range = ElementName(self.range)
        if self.slot_uri is not None and not isinstance(self.slot_uri, URIorCURIE):
            self.slot_uri = URIorCURIE(self.slot_uri)
        if self.owner is not None and not isinstance(self.owner, DefinitionName):
            self.owner = DefinitionName(self.owner)
        if self.subproperty_of is not None and not isinstance(self.subproperty_of, URIorCURIE):
            self.subproperty_of = URIorCURIE(self.subproperty_of)
        if self.inverse is not None and not isinstance(self.inverse, SlotDefinitionName):
            self.inverse = SlotDefinitionName(self.inverse)
        super().__post_init__()


@dataclass
class ClassDefinition(Definition):
    """
    the definition of a class or interface
    """
    _inherited_slots: ClassVar[List[str]] = ["defining_slots"]

    class_class_uri: ClassVar[URIRef] = META.ClassDefinition
    class_class_curie: ClassVar[str] = "meta:ClassDefinition"
    class_name: ClassVar[str] = "class_definition"
    class_model_uri: ClassVar[URIRef] = META.ClassDefinition

    name: Union[str, ClassDefinitionName] = None
    is_a: Optional[Union[str, ClassDefinitionName]] = None
    mixins: List[Union[str, ClassDefinitionName]] = empty_list()
    apply_to: List[Union[str, ClassDefinitionName]] = empty_list()
    slots: List[Union[str, SlotDefinitionName]] = empty_list()
    slot_usage: Dict[Union[str, SlotDefinitionName], Union[dict, SlotDefinition]] = empty_dict()
    class_uri: Optional[Union[str, URIorCURIE]] = None
    subclass_of: Optional[Union[str, URIorCURIE]] = None
    union_of: List[Union[str, ClassDefinitionName]] = empty_list()
    defining_slots: List[Union[str, SlotDefinitionName]] = empty_list()

    def __post_init__(self):
        if self.name is None:
            raise ValueError(f"name must be supplied")
        if not isinstance(self.name, ClassDefinitionName):
            self.name = ClassDefinitionName(self.name)
        if self.is_a is not None and not isinstance(self.is_a, ClassDefinitionName):
            self.is_a = ClassDefinitionName(self.is_a)
        self.mixins = [v if isinstance(v, ClassDefinitionName)
                       else ClassDefinitionName(v) for v in self.mixins]
        self.apply_to = [v if isinstance(v, ClassDefinitionName)
                         else ClassDefinitionName(v) for v in self.apply_to]
        self.slots = [v if isinstance(v, SlotDefinitionName)
                      else SlotDefinitionName(v) for v in self.slots]
        for k, v in self.slot_usage.items():
            if not isinstance(v, SlotDefinition):
                self.slot_usage[k] = SlotDefinition(name=k, **({} if v is None else v))
        if self.class_uri is not None and not isinstance(self.class_uri, URIorCURIE):
            self.class_uri = URIorCURIE(self.class_uri)
        if self.subclass_of is not None and not isinstance(self.subclass_of, URIorCURIE):
            self.subclass_of = URIorCURIE(self.subclass_of)
        self.union_of = [v if isinstance(v, ClassDefinitionName)
                         else ClassDefinitionName(v) for v in self.union_of]
        self.defining_slots = [v if isinstance(v, SlotDefinitionName)
                               else SlotDefinitionName(v) for v in self.defining_slots]
        super().__post_init__()


@dataclass
class Prefix(YAMLRoot):
    """
    prefix URI tuple
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = META.Prefix
    class_class_curie: ClassVar[str] = "meta:Prefix"
    class_name: ClassVar[str] = "prefix"
    class_model_uri: ClassVar[URIRef] = META.Prefix

    prefix_prefix: Union[str, PrefixPrefixPrefix]
    prefix_reference: Union[str, URI]

    def __post_init__(self):
        if self.prefix_prefix is None:
            raise ValueError(f"prefix_prefix must be supplied")
        if not isinstance(self.prefix_prefix, PrefixPrefixPrefix):
            self.prefix_prefix = PrefixPrefixPrefix(self.prefix_prefix)
        if self.prefix_reference is None:
            raise ValueError(f"prefix_reference must be supplied")
        if not isinstance(self.prefix_reference, URI):
            self.prefix_reference = URI(self.prefix_reference)
        super().__post_init__()


@dataclass
class LocalName(YAMLRoot):
    """
    an attributed label
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = META.LocalName
    class_class_curie: ClassVar[str] = "meta:LocalName"
    class_name: ClassVar[str] = "local_name"
    class_model_uri: ClassVar[URIRef] = META.LocalName

    local_name_source: Union[str, LocalNameLocalNameSource]
    local_name_value: str

    def __post_init__(self):
        if self.local_name_source is None:
            raise ValueError(f"local_name_source must be supplied")
        if not isinstance(self.local_name_source, LocalNameLocalNameSource):
            self.local_name_source = LocalNameLocalNameSource(self.local_name_source)
        if self.local_name_value is None:
            raise ValueError(f"local_name_value must be supplied")
        super().__post_init__()


@dataclass
class Example(YAMLRoot):
    """
    usage example and description
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = META.Example
    class_class_curie: ClassVar[str] = "meta:Example"
    class_name: ClassVar[str] = "example"
    class_model_uri: ClassVar[URIRef] = META.Example

    value: Optional[str] = None
    description: Optional[str] = None

@dataclass
class AltDescription(YAMLRoot):
    """
    an attributed description
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = META.AltDescription
    class_class_curie: ClassVar[str] = "meta:AltDescription"
    class_name: ClassVar[str] = "alt_description"
    class_model_uri: ClassVar[URIRef] = META.AltDescription

    source: Union[str, AltDescriptionSource]
    description: str

    def __post_init__(self):
        if self.source is None:
            raise ValueError(f"source must be supplied")
        if not isinstance(self.source, AltDescriptionSource):
            self.source = AltDescriptionSource(self.source)
        if self.description is None:
            raise ValueError(f"description must be supplied")
        super().__post_init__()

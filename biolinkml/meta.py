# Auto generated from meta.yaml by pythongen.py version: 0.4.0
# Generation date: 2020-01-27 12:55
# Schema: metamodel
#
# id: https://w3id.org/biolink/biolinkml/meta
# description: A metamodel for defining biolink related schemas
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
from biolinkml.utils.metamodelcore import Bool, NCName, URI, URIorCURIE, XSDDateTime
from includes.types import Boolean, Datetime, Integer, Ncname, String, Uri, Uriorcurie

metamodel_version = "1.4.3"

# Overwrite dataclasses _init_fn to add **kwargs in __init__
dataclasses._init_fn = dataclasses_init_fn_with_kwargs

# Namespaces
OIO = CurieNamespace('OIO', 'http://www.geneontology.org/formats/oboInOwl#')
BIOLINKML = CurieNamespace('biolinkml', 'https://w3id.org/biolink/biolinkml/')
DCTERMS = CurieNamespace('dcterms', 'http://purl.org/dc/terms/')
META = CurieNamespace('meta', 'https://w3id.org/biolink/biolinkml/meta/')
OWL = CurieNamespace('owl', 'http://www.w3.org/2002/07/owl#')
PAV = CurieNamespace('pav', 'http://purl.org/pav/')
RDF = CurieNamespace('rdf', 'http://www.w3.org/1999/02/22-rdf-syntax-ns#')
RDFS = CurieNamespace('rdfs', 'http://www.w3.org/2000/01/rdf-schema#')
SKOS = CurieNamespace('skos', 'http://www.w3.org/2004/02/skos/core#')
XSD = CurieNamespace('xsd', 'http://www.w3.org/2001/XMLSchema#')
DEFAULT_ = META


# Types

# Class references
class ElementName(extended_str):
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
    definition_uri: Optional[Union[str, URIorCURIE]] = None
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
    exact_mappings: List[Union[str, URIorCURIE]] = empty_list()
    close_mappings: List[Union[str, URIorCURIE]] = empty_list()
    related_mappings: List[Union[str, URIorCURIE]] = empty_list()
    deprecated_element_has_exact_replacement: Optional[Union[str, URIorCURIE]] = None
    deprecated_element_has_possible_replacement: Optional[Union[str, URIorCURIE]] = None

    def __post_init__(self, **kwargs: Dict[str, Any]):
        self.id_prefixes = [v if isinstance(v, NCName)
                            else NCName(v) for v in self.id_prefixes]
        if self.name is None:
            raise ValueError(f"name must be supplied")
        if not isinstance(self.name, ElementName):
            self.name = ElementName(self.name)
        if self.definition_uri is not None and not isinstance(self.definition_uri, URIorCURIE):
            self.definition_uri = URIorCURIE(self.definition_uri)
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
        self.exact_mappings = [v if isinstance(v, URIorCURIE)
                               else URIorCURIE(v) for v in self.exact_mappings]
        self.close_mappings = [v if isinstance(v, URIorCURIE)
                               else URIorCURIE(v) for v in self.close_mappings]
        self.related_mappings = [v if isinstance(v, URIorCURIE)
                                 else URIorCURIE(v) for v in self.related_mappings]
        if self.deprecated_element_has_exact_replacement is not None and not isinstance(self.deprecated_element_has_exact_replacement, URIorCURIE):
            self.deprecated_element_has_exact_replacement = URIorCURIE(self.deprecated_element_has_exact_replacement)
        if self.deprecated_element_has_possible_replacement is not None and not isinstance(self.deprecated_element_has_possible_replacement, URIorCURIE):
            self.deprecated_element_has_possible_replacement = URIorCURIE(self.deprecated_element_has_possible_replacement)
        super().__post_init__(**kwargs)


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

    def __post_init__(self, **kwargs: Dict[str, Any]):
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
        super().__post_init__(**kwargs)


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

    def __post_init__(self, **kwargs: Dict[str, Any]):
        if self.name is None:
            raise ValueError(f"name must be supplied")
        if not isinstance(self.name, TypeDefinitionName):
            self.name = TypeDefinitionName(self.name)
        if self.typeof is not None and not isinstance(self.typeof, TypeDefinitionName):
            self.typeof = TypeDefinitionName(self.typeof)
        if self.uri is not None and not isinstance(self.uri, URIorCURIE):
            self.uri = URIorCURIE(self.uri)
        super().__post_init__(**kwargs)


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

    def __post_init__(self, **kwargs: Dict[str, Any]):
        if self.name is None:
            raise ValueError(f"name must be supplied")
        if not isinstance(self.name, SubsetDefinitionName):
            self.name = SubsetDefinitionName(self.name)
        super().__post_init__(**kwargs)


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

    def __post_init__(self, **kwargs: Dict[str, Any]):
        if self.is_a is not None and not isinstance(self.is_a, DefinitionName):
            self.is_a = DefinitionName(self.is_a)
        self.mixins = [v if isinstance(v, DefinitionName)
                       else DefinitionName(v) for v in self.mixins]
        self.apply_to = [v if isinstance(v, DefinitionName)
                         else DefinitionName(v) for v in self.apply_to]
        self.values_from = [v if isinstance(v, URIorCURIE)
                            else URIorCURIE(v) for v in self.values_from]
        super().__post_init__(**kwargs)


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

    def __post_init__(self, **kwargs: Dict[str, Any]):
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
        super().__post_init__(**kwargs)


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

    def __post_init__(self, **kwargs: Dict[str, Any]):
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
        super().__post_init__(**kwargs)


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

    def __post_init__(self, **kwargs: Dict[str, Any]):
        if self.prefix_prefix is None:
            raise ValueError(f"prefix_prefix must be supplied")
        if not isinstance(self.prefix_prefix, PrefixPrefixPrefix):
            self.prefix_prefix = PrefixPrefixPrefix(self.prefix_prefix)
        if self.prefix_reference is None:
            raise ValueError(f"prefix_reference must be supplied")
        if not isinstance(self.prefix_reference, URI):
            self.prefix_reference = URI(self.prefix_reference)
        super().__post_init__(**kwargs)


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

    def __post_init__(self, **kwargs: Dict[str, Any]):
        if self.local_name_source is None:
            raise ValueError(f"local_name_source must be supplied")
        if not isinstance(self.local_name_source, LocalNameLocalNameSource):
            self.local_name_source = LocalNameLocalNameSource(self.local_name_source)
        if self.local_name_value is None:
            raise ValueError(f"local_name_value must be supplied")
        super().__post_init__(**kwargs)


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

    def __post_init__(self, **kwargs: Dict[str, Any]):
        if self.source is None:
            raise ValueError(f"source must be supplied")
        if not isinstance(self.source, AltDescriptionSource):
            self.source = AltDescriptionSource(self.source)
        if self.description is None:
            raise ValueError(f"description must be supplied")
        super().__post_init__(**kwargs)



# Slots
class slots:
    pass

slots.name = Slot(uri=RDFS.label, name="name", curie=RDFS.curie('label'),
                      model_uri=META.name, domain=Element, range=Union[str, ElementName])

slots.definition_uri = Slot(uri=META.definition_uri, name="definition_uri", curie=META.curie('definition_uri'),
                      model_uri=META.definition_uri, domain=Element, range=Optional[Union[str, URIorCURIE]])

slots.id_prefixes = Slot(uri=META.id_prefixes, name="id_prefixes", curie=META.curie('id_prefixes'),
                      model_uri=META.id_prefixes, domain=Element, range=List[Union[str, NCName]])

slots.description = Slot(uri=SKOS.definition, name="description", curie=SKOS.curie('definition'),
                      model_uri=META.description, domain=Element, range=Optional[str])

slots.aliases = Slot(uri=SKOS.altLabel, name="aliases", curie=SKOS.curie('altLabel'),
                      model_uri=META.aliases, domain=Element, range=List[str])

slots.deprecated = Slot(uri=META.deprecated, name="deprecated", curie=META.curie('deprecated'),
                      model_uri=META.deprecated, domain=Element, range=Optional[str])

slots.todos = Slot(uri=META.todos, name="todos", curie=META.curie('todos'),
                      model_uri=META.todos, domain=Element, range=List[str])

slots.notes = Slot(uri=SKOS.editorialNote, name="notes", curie=SKOS.curie('editorialNote'),
                      model_uri=META.notes, domain=Element, range=List[str])

slots.comments = Slot(uri=SKOS.note, name="comments", curie=SKOS.curie('note'),
                      model_uri=META.comments, domain=Element, range=List[str])

slots.in_subset = Slot(uri=OIO.inSubset, name="in_subset", curie=OIO.curie('inSubset'),
                      model_uri=META.in_subset, domain=Element, range=List[Union[str, SubsetDefinitionName]])

slots.from_schema = Slot(uri=SKOS.inScheme, name="from_schema", curie=SKOS.curie('inScheme'),
                      model_uri=META.from_schema, domain=Element, range=Optional[Union[str, URI]])

slots.imported_from = Slot(uri=META.imported_from, name="imported_from", curie=META.curie('imported_from'),
                      model_uri=META.imported_from, domain=Element, range=Optional[str])

slots.see_also = Slot(uri=RDFS.seeAlso, name="see_also", curie=RDFS.curie('seeAlso'),
                      model_uri=META.see_also, domain=Element, range=List[Union[str, URIorCURIE]])

slots.is_a = Slot(uri=META.is_a, name="is_a", curie=META.curie('is_a'),
                      model_uri=META.is_a, domain=Definition, range=Optional[Union[str, DefinitionName]])

slots.abstract = Slot(uri=META.abstract, name="abstract", curie=META.curie('abstract'),
                      model_uri=META.abstract, domain=Definition, range=Optional[Bool])

slots.mixin = Slot(uri=META.mixin, name="mixin", curie=META.curie('mixin'),
                      model_uri=META.mixin, domain=Definition, range=Optional[Bool])

slots.mixins = Slot(uri=META.mixins, name="mixins", curie=META.curie('mixins'),
                      model_uri=META.mixins, domain=Definition, range=List[Union[str, DefinitionName]])

slots.apply_to = Slot(uri=META.apply_to, name="apply_to", curie=META.curie('apply_to'),
                      model_uri=META.apply_to, domain=Definition, range=List[Union[str, DefinitionName]])

slots.values_from = Slot(uri=META.values_from, name="values_from", curie=META.curie('values_from'),
                      model_uri=META.values_from, domain=Definition, range=List[Union[str, URIorCURIE]])

slots.id = Slot(uri=META.id, name="id", curie=META.curie('id'),
                      model_uri=META.id, domain=SchemaDefinition, range=Union[str, URI])

slots.emit_prefixes = Slot(uri=META.emit_prefixes, name="emit_prefixes", curie=META.curie('emit_prefixes'),
                      model_uri=META.emit_prefixes, domain=SchemaDefinition, range=List[Union[str, NCName]])

slots.title = Slot(uri=DCTERMS.title, name="title", curie=DCTERMS.curie('title'),
                      model_uri=META.title, domain=SchemaDefinition, range=Optional[str])

slots.version = Slot(uri=PAV.version, name="version", curie=PAV.curie('version'),
                      model_uri=META.version, domain=SchemaDefinition, range=Optional[str])

slots.imports = Slot(uri=META.imports, name="imports", curie=META.curie('imports'),
                      model_uri=META.imports, domain=SchemaDefinition, range=List[Union[str, URIorCURIE]])

slots.license = Slot(uri=DCTERMS.license, name="license", curie=DCTERMS.curie('license'),
                      model_uri=META.license, domain=SchemaDefinition, range=Optional[str])

slots.default_curi_maps = Slot(uri=META.default_curi_maps, name="default_curi_maps", curie=META.curie('default_curi_maps'),
                      model_uri=META.default_curi_maps, domain=SchemaDefinition, range=List[str])

slots.default_prefix = Slot(uri=META.default_prefix, name="default_prefix", curie=META.curie('default_prefix'),
                      model_uri=META.default_prefix, domain=SchemaDefinition, range=Optional[str])

slots.default_range = Slot(uri=META.default_range, name="default_range", curie=META.curie('default_range'),
                      model_uri=META.default_range, domain=SchemaDefinition, range=Optional[Union[str, TypeDefinitionName]])

slots.subsets = Slot(uri=META.subsets, name="subsets", curie=META.curie('subsets'),
                      model_uri=META.subsets, domain=SchemaDefinition, range=Dict[Union[str, SubsetDefinitionName], Union[dict, "SubsetDefinition"]])

slots.types = Slot(uri=META.types, name="types", curie=META.curie('types'),
                      model_uri=META.types, domain=SchemaDefinition, range=Dict[Union[str, TypeDefinitionName], Union[dict, "TypeDefinition"]])

slots.slot_definitions = Slot(uri=META.slots, name="slot_definitions", curie=META.curie('slots'),
                      model_uri=META.slot_definitions, domain=SchemaDefinition, range=Dict[Union[str, SlotDefinitionName], Union[dict, "SlotDefinition"]])

slots.classes = Slot(uri=META.classes, name="classes", curie=META.curie('classes'),
                      model_uri=META.classes, domain=SchemaDefinition, range=Dict[Union[str, ClassDefinitionName], Union[dict, "ClassDefinition"]])

slots.metamodel_version = Slot(uri=META.metamodel_version, name="metamodel_version", curie=META.curie('metamodel_version'),
                      model_uri=META.metamodel_version, domain=SchemaDefinition, range=Optional[str])

slots.source_file = Slot(uri=META.source_file, name="source_file", curie=META.curie('source_file'),
                      model_uri=META.source_file, domain=SchemaDefinition, range=Optional[str])

slots.source_file_date = Slot(uri=META.source_file_date, name="source_file_date", curie=META.curie('source_file_date'),
                      model_uri=META.source_file_date, domain=SchemaDefinition, range=Optional[Union[str, XSDDateTime]])

slots.source_file_size = Slot(uri=META.source_file_size, name="source_file_size", curie=META.curie('source_file_size'),
                      model_uri=META.source_file_size, domain=SchemaDefinition, range=Optional[int])

slots.generation_date = Slot(uri=META.generation_date, name="generation_date", curie=META.curie('generation_date'),
                      model_uri=META.generation_date, domain=SchemaDefinition, range=Optional[Union[str, XSDDateTime]])

slots.slots = Slot(uri=META.slots, name="slots", curie=META.curie('slots'),
                      model_uri=META.slots, domain=ClassDefinition, range=List[Union[str, SlotDefinitionName]])

slots.slot_usage = Slot(uri=META.slot_usage, name="slot_usage", curie=META.curie('slot_usage'),
                      model_uri=META.slot_usage, domain=ClassDefinition, range=Dict[Union[str, SlotDefinitionName], Union[dict, SlotDefinition]])

slots.class_uri = Slot(uri=META.class_uri, name="class_uri", curie=META.curie('class_uri'),
                      model_uri=META.class_uri, domain=ClassDefinition, range=Optional[Union[str, URIorCURIE]])

slots.subclass_of = Slot(uri=RDFS.subClassOf, name="subclass_of", curie=RDFS.curie('subClassOf'),
                      model_uri=META.subclass_of, domain=ClassDefinition, range=Optional[Union[str, URIorCURIE]])

slots.defining_slots = Slot(uri=META.defining_slots, name="defining_slots", curie=META.curie('defining_slots'),
                      model_uri=META.defining_slots, domain=ClassDefinition, range=List[Union[str, SlotDefinitionName]])

slots.union_of = Slot(uri=META.union_of, name="union_of", curie=META.curie('union_of'),
                      model_uri=META.union_of, domain=ClassDefinition, range=List[Union[str, ClassDefinitionName]])

slots.domain = Slot(uri=META.domain, name="domain", curie=META.curie('domain'),
                      model_uri=META.domain, domain=SlotDefinition, range=Optional[Union[str, ClassDefinitionName]])

slots.range = Slot(uri=META.range, name="range", curie=META.curie('range'),
                      model_uri=META.range, domain=SlotDefinition, range=Optional[Union[str, ElementName]])

slots.slot_uri = Slot(uri=META.slot_uri, name="slot_uri", curie=META.curie('slot_uri'),
                      model_uri=META.slot_uri, domain=SlotDefinition, range=Optional[Union[str, URIorCURIE]])

slots.multivalued = Slot(uri=META.multivalued, name="multivalued", curie=META.curie('multivalued'),
                      model_uri=META.multivalued, domain=SlotDefinition, range=Optional[Bool])

slots.inherited = Slot(uri=META.inherited, name="inherited", curie=META.curie('inherited'),
                      model_uri=META.inherited, domain=SlotDefinition, range=Optional[Bool])

slots.readonly = Slot(uri=META.readonly, name="readonly", curie=META.curie('readonly'),
                      model_uri=META.readonly, domain=SlotDefinition, range=Optional[str])

slots.ifabsent = Slot(uri=META.ifabsent, name="ifabsent", curie=META.curie('ifabsent'),
                      model_uri=META.ifabsent, domain=SlotDefinition, range=Optional[str])

slots.singular_name = Slot(uri=SKOS.altLabel, name="singular_name", curie=SKOS.curie('altLabel'),
                      model_uri=META.singular_name, domain=SlotDefinition, range=Optional[str])

slots.required = Slot(uri=META.required, name="required", curie=META.curie('required'),
                      model_uri=META.required, domain=SlotDefinition, range=Optional[Bool])

slots.inlined = Slot(uri=META.inlined, name="inlined", curie=META.curie('inlined'),
                      model_uri=META.inlined, domain=SlotDefinition, range=Optional[Bool])

slots.key = Slot(uri=META.key, name="key", curie=META.curie('key'),
                      model_uri=META.key, domain=SlotDefinition, range=Optional[Bool])

slots.identifier = Slot(uri=META.identifier, name="identifier", curie=META.curie('identifier'),
                      model_uri=META.identifier, domain=SlotDefinition, range=Optional[Bool])

slots.alias = Slot(uri=META.alias, name="alias", curie=META.curie('alias'),
                      model_uri=META.alias, domain=SlotDefinition, range=Optional[str])

slots.owner = Slot(uri=META.owner, name="owner", curie=META.curie('owner'),
                      model_uri=META.owner, domain=SlotDefinition, range=Optional[Union[str, DefinitionName]])

slots.is_usage_slot = Slot(uri=META.is_usage_slot, name="is_usage_slot", curie=META.curie('is_usage_slot'),
                      model_uri=META.is_usage_slot, domain=SlotDefinition, range=Optional[Bool])

slots.subproperty_of = Slot(uri=RDFS.subPropertyOf, name="subproperty_of", curie=RDFS.curie('subPropertyOf'),
                      model_uri=META.subproperty_of, domain=SlotDefinition, range=Optional[Union[str, URIorCURIE]])

slots.symmetric = Slot(uri=META.symmetric, name="symmetric", curie=META.curie('symmetric'),
                      model_uri=META.symmetric, domain=SlotDefinition, range=Optional[Bool])

slots.inverse = Slot(uri=OWL.inverseOf, name="inverse", curie=OWL.curie('inverseOf'),
                      model_uri=META.inverse, domain=SlotDefinition, range=Optional[Union[str, SlotDefinitionName]])

slots.is_class_field = Slot(uri=META.is_class_field, name="is_class_field", curie=META.curie('is_class_field'),
                      model_uri=META.is_class_field, domain=SlotDefinition, range=Optional[Bool])

slots.role = Slot(uri=META.role, name="role", curie=META.curie('role'),
                      model_uri=META.role, domain=SlotDefinition, range=Optional[str])

slots.typeof = Slot(uri=META.typeof, name="typeof", curie=META.curie('typeof'),
                      model_uri=META.typeof, domain=TypeDefinition, range=Optional[Union[str, TypeDefinitionName]])

slots.base = Slot(uri=META.base, name="base", curie=META.curie('base'),
                      model_uri=META.base, domain=TypeDefinition, range=Optional[str])

slots.type_uri = Slot(uri=META.uri, name="type_uri", curie=META.curie('uri'),
                      model_uri=META.type_uri, domain=TypeDefinition, range=Optional[Union[str, URIorCURIE]])

slots.repr = Slot(uri=META.repr, name="repr", curie=META.curie('repr'),
                      model_uri=META.repr, domain=TypeDefinition, range=Optional[str])

slots.alt_description_text = Slot(uri=META.description, name="alt_description_text", curie=META.curie('description'),
                      model_uri=META.alt_description_text, domain=AltDescription, range=str)

slots.alt_description_source = Slot(uri=META.source, name="alt_description_source", curie=META.curie('source'),
                      model_uri=META.alt_description_source, domain=AltDescription, range=Union[str, AltDescriptionSource])

slots.alt_descriptions = Slot(uri=META.alt_descriptions, name="alt_descriptions", curie=META.curie('alt_descriptions'),
                      model_uri=META.alt_descriptions, domain=Element, range=Union[dict, "AltDescription"])

slots.value = Slot(uri=SKOS.example, name="value", curie=SKOS.curie('example'),
                      model_uri=META.value, domain=Example, range=Optional[str])

slots.value_description = Slot(uri=META.description, name="value_description", curie=META.curie('description'),
                      model_uri=META.value_description, domain=Example, range=Optional[str])

slots.examples = Slot(uri=META.examples, name="examples", curie=META.curie('examples'),
                      model_uri=META.examples, domain=Element, range=List[Union[dict, "Example"]])

slots.prefix_prefix = Slot(uri=META.prefix_prefix, name="prefix_prefix", curie=META.curie('prefix_prefix'),
                      model_uri=META.prefix_prefix, domain=Prefix, range=Union[str, PrefixPrefixPrefix])

slots.prefix_reference = Slot(uri=META.prefix_reference, name="prefix_reference", curie=META.curie('prefix_reference'),
                      model_uri=META.prefix_reference, domain=Prefix, range=Union[str, URI])

slots.prefixes = Slot(uri=META.prefixes, name="prefixes", curie=META.curie('prefixes'),
                      model_uri=META.prefixes, domain=SchemaDefinition, range=Union[dict, "Prefix"])

slots.local_name_source = Slot(uri=META.local_name_source, name="local_name_source", curie=META.curie('local_name_source'),
                      model_uri=META.local_name_source, domain=LocalName, range=Union[str, LocalNameLocalNameSource])

slots.local_name_value = Slot(uri=SKOS.altLabel, name="local_name_value", curie=SKOS.curie('altLabel'),
                      model_uri=META.local_name_value, domain=LocalName, range=str)

slots.local_names = Slot(uri=META.local_names, name="local_names", curie=META.curie('local_names'),
                      model_uri=META.local_names, domain=Element, range=Union[dict, "LocalName"])

slots.slot_definition_is_a = Slot(uri=META.is_a, name="slot_definition_is_a", curie=META.curie('is_a'),
                      model_uri=META.slot_definition_is_a, domain=SlotDefinition, range=Optional[Union[str, SlotDefinitionName]])

slots.slot_definition_mixins = Slot(uri=META.mixins, name="slot_definition_mixins", curie=META.curie('mixins'),
                      model_uri=META.slot_definition_mixins, domain=SlotDefinition, range=List[Union[str, SlotDefinitionName]])

slots.slot_definition_apply_to = Slot(uri=META.apply_to, name="slot_definition_apply_to", curie=META.curie('apply_to'),
                      model_uri=META.slot_definition_apply_to, domain=SlotDefinition, range=List[Union[str, SlotDefinitionName]])

slots.class_definition_is_a = Slot(uri=META.is_a, name="class_definition_is_a", curie=META.curie('is_a'),
                      model_uri=META.class_definition_is_a, domain=ClassDefinition, range=Optional[Union[str, ClassDefinitionName]])

slots.class_definition_mixins = Slot(uri=META.mixins, name="class_definition_mixins", curie=META.curie('mixins'),
                      model_uri=META.class_definition_mixins, domain=ClassDefinition, range=List[Union[str, ClassDefinitionName]])

slots.class_definition_apply_to = Slot(uri=META.apply_to, name="class_definition_apply_to", curie=META.curie('apply_to'),
                      model_uri=META.class_definition_apply_to, domain=ClassDefinition, range=List[Union[str, ClassDefinitionName]])
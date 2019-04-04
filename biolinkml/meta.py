# Auto generated from meta.yaml by pythongen.py version: 0.2.0
# Generation date: 2019-04-02 15:50
# Schema: metamodel
#
# id: https://w3id.org/biolink/biolinkml/meta
# description: A metamodel for defining biolink related schemas
# license: https://creativecommons.org/publicdomain/zero/1.0/

from typing import Optional, List, Union, Dict, ClassVar
from dataclasses import dataclass
from biolinkml.utils.metamodelcore import empty_list, empty_dict
from biolinkml.utils.yamlutils import YAMLRoot
from biolinkml.utils.metamodelcore import Bool, NCName, URI, URIorCURIE, XSDDate
from includes.types import Boolean, Datetime, Integer, Ncname, String, Uri, Uriorcurie

metamodel_version = "1.3.1"

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

    # === element ===
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

    def _fix_elements(self):
        super()._fix_elements()
        self.id_prefixes = [v if isinstance(v, NCName)
                            else NCName(v) for v in self.id_prefixes]
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


@dataclass
class SchemaDefinition(Element):
    """
    a collection of subset, type, slot and class definitions
    """
    _inherited_slots: ClassVar[List[str]] = []

    # === element ===
    name: Union[str, SchemaDefinitionName] = None
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

    # === schema_definition ===
    id: Union[str, URI] = None
    title: Optional[str] = None
    version: Optional[str] = None
    imports: List[Union[str, URI]] = empty_list()
    license: Optional[str] = None
    prefixes: Union[dict, "Prefix"] = empty_dict()
    emit_prefixes: List[Union[str, NCName]] = empty_list()
    default_curi_maps: List[str] = empty_list()
    default_prefix: Optional[str] = None
    default_range: Optional[Union[str, DefinitionName]] = None
    subsets: Dict[Union[str, SubsetDefinitionName], Union[dict, "SubsetDefinition"]] = empty_dict()
    types: Dict[Union[str, TypeDefinitionName], Union[dict, "TypeDefinition"]] = empty_dict()
    slots: Dict[Union[str, SlotDefinitionName], Union[dict, "SlotDefinition"]] = empty_dict()
    classes: Dict[Union[str, ClassDefinitionName], Union[dict, "ClassDefinition"]] = empty_dict()
    metamodel_version: Optional[str] = None
    source_file: Optional[str] = None
    source_file_date: Optional[Union[str, XSDDate]] = None
    source_file_size: Optional[int] = None
    generation_date: Optional[Union[str, XSDDate]] = None

    def _fix_elements(self):
        super()._fix_elements()
        if self.name is not None and not isinstance(self.name, SchemaDefinitionName):
            self.name = SchemaDefinitionName(self.name)
        if self.id is not None and not isinstance(self.id, URI):
            self.id = URI(self.id)
        self.imports = [v if isinstance(v, URI)
                        else URI(v) for v in self.imports]
        for k, v in self.prefixes.items():
            if not isinstance(v, Prefix):
                self.prefixes[k] = Prefix(k, v)
        self.emit_prefixes = [v if isinstance(v, NCName)
                              else NCName(v) for v in self.emit_prefixes]
        if self.default_range is not None and not isinstance(self.default_range, DefinitionName):
            self.default_range = DefinitionName(self.default_range)
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
        if self.source_file_date is not None and not isinstance(self.source_file_date, XSDDate):
            self.source_file_date = XSDDate(self.source_file_date)
        if self.generation_date is not None and not isinstance(self.generation_date, XSDDate):
            self.generation_date = XSDDate(self.generation_date)


@dataclass
class TypeDefinition(Element):
    """
    A data type definition.
    """
    _inherited_slots: ClassVar[List[str]] = ["base", "uri", "repr"]

    # === element ===
    name: Union[str, TypeDefinitionName] = None
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

    # === type_definition ===
    typeof: Optional[Union[str, TypeDefinitionName]] = None
    base: Optional[str] = None
    uri: Optional[Union[str, URIorCURIE]] = None
    repr: Optional[str] = None

    def _fix_elements(self):
        super()._fix_elements()
        if self.name is not None and not isinstance(self.name, TypeDefinitionName):
            self.name = TypeDefinitionName(self.name)
        if self.typeof is not None and not isinstance(self.typeof, TypeDefinitionName):
            self.typeof = TypeDefinitionName(self.typeof)
        if self.uri is not None and not isinstance(self.uri, URIorCURIE):
            self.uri = URIorCURIE(self.uri)


@dataclass
class SubsetDefinition(Element):
    """
    the name and description of a subset
    """
    _inherited_slots: ClassVar[List[str]] = []

    # === element ===
    name: Union[str, SubsetDefinitionName] = None
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

    # === subset_definition ===

    def _fix_elements(self):
        super()._fix_elements()
        if self.name is not None and not isinstance(self.name, SubsetDefinitionName):
            self.name = SubsetDefinitionName(self.name)


@dataclass
class Definition(Element):
    """
    base class for definitions
    """
    _inherited_slots: ClassVar[List[str]] = []

    # === element ===
    name: Union[str, DefinitionName] = None
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

    # === definition ===
    is_a: Optional[Union[str, DefinitionName]] = None
    abstract: Optional[Bool] = None
    mixin: Optional[Bool] = None
    mixins: List[Union[str, DefinitionName]] = empty_list()
    apply_to: List[Union[str, DefinitionName]] = empty_list()
    values_from: List[Union[str, URIorCURIE]] = empty_list()

    def _fix_elements(self):
        super()._fix_elements()
        if self.is_a is not None and not isinstance(self.is_a, DefinitionName):
            self.is_a = DefinitionName(self.is_a)
        self.mixins = [v if isinstance(v, DefinitionName)
                       else DefinitionName(v) for v in self.mixins]
        self.apply_to = [v if isinstance(v, DefinitionName)
                         else DefinitionName(v) for v in self.apply_to]
        self.values_from = [v if isinstance(v, URIorCURIE)
                            else URIorCURIE(v) for v in self.values_from]


@dataclass
class SlotDefinition(Definition):
    """
    the definition of a property or a slot
    """
    _inherited_slots: ClassVar[List[str]] = ["domain", "range", "slot_uri", "multivalued", "inherited", "readonly", "ifabsent", "required", "inlined", "key", "identifier"]

    # === element ===
    name: Union[str, SlotDefinitionName] = None
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

    # === definition ===
    abstract: Optional[Bool] = None
    mixin: Optional[Bool] = None
    values_from: List[Union[str, URIorCURIE]] = empty_list()

    # === slot_definition ===
    domain: Union[str, ClassDefinitionName] = None
    is_a: Optional[Union[str, SlotDefinitionName]] = None
    mixins: List[Union[str, SlotDefinitionName]] = empty_list()
    apply_to: List[Union[str, SlotDefinitionName]] = empty_list()
    singular_name: Optional[str] = None
    range: Optional[Union[str, ElementName]] = None
    slot_uri: Optional[Union[str, URI]] = None
    multivalued: Optional[Bool] = None
    inherited: Optional[Bool] = None
    readonly: Optional[str] = None
    ifabsent: Optional[str] = None
    required: Optional[Bool] = None
    inlined: Optional[Bool] = None
    key: Optional[Bool] = None
    identifier: Optional[Bool] = None
    alias: Optional[str] = None
    subproperty_of: Optional[Union[str, URIorCURIE]] = None
    is_usage_slot: Optional[Bool] = None

    def _fix_elements(self):
        super()._fix_elements()
        if self.name is not None and not isinstance(self.name, SlotDefinitionName):
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
        if self.slot_uri is not None and not isinstance(self.slot_uri, URI):
            self.slot_uri = URI(self.slot_uri)
        if self.subproperty_of is not None and not isinstance(self.subproperty_of, URIorCURIE):
            self.subproperty_of = URIorCURIE(self.subproperty_of)


@dataclass
class ClassDefinition(Definition):
    """
    the definition of a class or interface
    """
    _inherited_slots: ClassVar[List[str]] = ["class_uri", "defining_slots"]

    # === element ===
    name: Union[str, ClassDefinitionName] = None
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

    # === definition ===
    abstract: Optional[Bool] = None
    mixin: Optional[Bool] = None
    values_from: List[Union[str, URIorCURIE]] = empty_list()

    # === class_definition ===
    is_a: Optional[Union[str, ClassDefinitionName]] = None
    mixins: List[Union[str, ClassDefinitionName]] = empty_list()
    apply_to: List[Union[str, ClassDefinitionName]] = empty_list()
    slots: List[Union[str, SlotDefinitionName]] = empty_list()
    slot_usage: Dict[Union[str, SlotDefinitionName], Union[dict, SlotDefinition]] = empty_dict()
    class_uri: Optional[Union[str, URIorCURIE]] = None
    subclass_of: Optional[Union[str, URIorCURIE]] = None
    defining_slots: List[Union[str, SlotDefinitionName]] = empty_list()

    def _fix_elements(self):
        super()._fix_elements()
        if self.name is not None and not isinstance(self.name, ClassDefinitionName):
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
        self.defining_slots = [v if isinstance(v, SlotDefinitionName)
                               else SlotDefinitionName(v) for v in self.defining_slots]


@dataclass
class Prefix(YAMLRoot):
    """
    prefix URI tuple
    """
    _inherited_slots: ClassVar[List[str]] = []

    # === prefix ===
    prefix_prefix: Union[str, PrefixPrefixPrefix]
    prefix_reference: Union[str, URI]

    def _fix_elements(self):
        super()._fix_elements()
        if not isinstance(self.prefix_prefix, PrefixPrefixPrefix):
            self.prefix_prefix = PrefixPrefixPrefix(self.prefix_prefix)
        if not isinstance(self.prefix_reference, URI):
            self.prefix_reference = URI(self.prefix_reference)


@dataclass
class LocalName(YAMLRoot):
    """
    an attributed label
    """
    _inherited_slots: ClassVar[List[str]] = []

    # === local_name ===
    local_name_source: Union[str, LocalNameLocalNameSource]
    local_name_value: str

    def _fix_elements(self):
        super()._fix_elements()
        if not isinstance(self.local_name_source, LocalNameLocalNameSource):
            self.local_name_source = LocalNameLocalNameSource(self.local_name_source)


@dataclass
class Example(YAMLRoot):
    """
    usage example and description
    """
    _inherited_slots: ClassVar[List[str]] = []

    # === example ===
    value: Optional[str] = None
    description: Optional[str] = None


@dataclass
class AltDescription(YAMLRoot):
    """
    an attributed description
    """
    _inherited_slots: ClassVar[List[str]] = []

    # === alt_description ===
    source: Union[str, AltDescriptionSource]
    description: str

    def _fix_elements(self):
        super()._fix_elements()
        if not isinstance(self.source, AltDescriptionSource):
            self.source = AltDescriptionSource(self.source)

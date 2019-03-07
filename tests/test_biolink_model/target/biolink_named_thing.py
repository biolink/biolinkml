# Auto generated from biolink_named_thing.yaml by pythongen.py version: 0.2.0
# Generation date: 2019-03-05 09:14
# Schema: biolink named_thing
#
# id: http://w3id.org/biolink/biolink-model/named-thing
# description: Basic entity for taxonomy and data model for life-sciences data
# license: https://creativecommons.org/publicdomain/zero/1.0/

from typing import Optional, List, Union, Dict
from dataclasses import dataclass
from biolinkml.utils.metamodelcore import empty_list, empty_dict
from biolinkml.utils.yamlutils import YAMLRoot
from tests.test_biolink_model.biolink_metamodel.includes.biolink_types import BooleanType, FileName, IdentifierType, LabelType, NarrativeText, UriType
from biolinkml.utils.metamodelcore import Bool, NCName, URIorCURIE, XSDDate
from includes.types import Boolean, Datetime, Ncname, String, Uri

metamodel_version = "1.0.2"

inherited_slots: List[str] = ["slots"]


# Types

# Class references
class PossibleValuePossibleValueValue(LabelType):
    pass


class NamedThingId(IdentifierType):
    pass


class TypeDefinitionId(NamedThingId):
    pass


class ValuesetDefinitionId(NamedThingId):
    pass


class OntologicalClassId(NamedThingId):
    pass


class NodeTypeId(OntologicalClassId):
    pass


class RelationshipTypeId(OntologicalClassId):
    pass


class PropertyTypeId(OntologicalClassId):
    pass


class InformationContentEntityId(NamedThingId):
    pass


class AdministrativeEntityId(NamedThingId):
    pass


class ProviderId(AdministrativeEntityId):
    pass


class SubsetDefinitionId(NamedThingId):
    pass


class RelationshipQuantifierId(NamedThingId):
    pass


class PropertyDefinitionId(NamedThingId):
    pass


class NodePropertyDefinitionId(PropertyDefinitionId):
    pass


class QualifierTypeId(NamedThingId):
    pass


@dataclass
class AltDescription(YAMLRoot):
    """
    attributed definition or description
    """

    # === alt description ===
    description: Union[str, NarrativeText]
    source: Optional[Union[str, UriType]] = None

    def _fix_elements(self):
        super()._fix_elements()
        if self.source is not None and not isinstance(self.source, UriType):
            self.source = UriType(self.source)
        if not isinstance(self.description, NarrativeText):
            self.description = NarrativeText(self.description)


@dataclass
class Example(YAMLRoot):
    """
    usage example and/or accompanying description
    """

    # === example ===
    value: Optional[Union[str, NarrativeText]] = None
    description: Optional[Union[str, NarrativeText]] = None

    def _fix_elements(self):
        super()._fix_elements()
        if self.value is not None and not isinstance(self.value, NarrativeText):
            self.value = NarrativeText(self.value)
        if self.description is not None and not isinstance(self.description, NarrativeText):
            self.description = NarrativeText(self.description)


@dataclass
class PossibleValue(YAMLRoot):
    """
    a possible value for a value set
    """

    # === possible_value ===
    possible_value_value: Union[str, PossibleValuePossibleValueValue]
    possible_value_description: Optional[Union[str, NarrativeText]] = None

    def _fix_elements(self):
        super()._fix_elements()
        if not isinstance(self.possible_value_value, PossibleValuePossibleValueValue):
            self.possible_value_value = PossibleValuePossibleValueValue(self.possible_value_value)
        if self.possible_value_description is not None and not isinstance(self.possible_value_description, NarrativeText):
            self.possible_value_description = NarrativeText(self.possible_value_description)


@dataclass
class Thing(YAMLRoot):
    """
    Abstract base class for everything in a model
    """

    # === thing ===
    name: Optional[Union[str, LabelType]] = None
    iri: Optional[Union[str, UriType]] = None
    full_name: Optional[Union[str, LabelType]] = None
    local_names: List[Union[str, LabelType]] = empty_list()
    description: Optional[Union[str, NarrativeText]] = None
    alt_descriptions: List[Union[dict, AltDescription]] = empty_list()
    aliases: List[Union[str, LabelType]] = empty_list()
    comments: List[Union[str, NarrativeText]] = empty_list()
    notes: List[Union[str, NarrativeText]] = empty_list()
    examples: List[Union[dict, Example]] = empty_list()
    deprecated: Optional[str] = None
    in_subset: List[Union[str, SubsetDefinitionId]] = empty_list()
    see_also: List[Union[str, IdentifierType]] = empty_list()
    id_prefixes: List[Union[str, NCName]] = empty_list()
    creation_date: Optional[Union[str, XSDDate]] = None
    update_date: Optional[Union[str, XSDDate]] = None
    from_model: Optional[Union[str, UriType]] = None
    source_file: Optional[Union[str, FileName]] = None
    mixin: Optional[Union[Bool, BooleanType]] = None
    abstract: Optional[Union[Bool, BooleanType]] = None
    mappings: List[Union[str, UriType]] = empty_list()

    def _fix_elements(self):
        super()._fix_elements()
        if self.name is not None and not isinstance(self.name, LabelType):
            self.name = LabelType(self.name)
        if self.iri is not None and not isinstance(self.iri, UriType):
            self.iri = UriType(self.iri)
        if self.full_name is not None and not isinstance(self.full_name, LabelType):
            self.full_name = LabelType(self.full_name)
        self.local_names = [v if isinstance(v, LabelType)
                            else LabelType(v) for v in self.local_names]
        if self.description is not None and not isinstance(self.description, NarrativeText):
            self.description = NarrativeText(self.description)
        self.alt_descriptions = [v if isinstance(v, AltDescription)
                                 else AltDescription(**v) for v in self.alt_descriptions]
        self.aliases = [v if isinstance(v, LabelType)
                        else LabelType(v) for v in self.aliases]
        self.comments = [v if isinstance(v, NarrativeText)
                         else NarrativeText(v) for v in self.comments]
        self.notes = [v if isinstance(v, NarrativeText)
                      else NarrativeText(v) for v in self.notes]
        self.examples = [v if isinstance(v, Example)
                         else Example(**v) for v in self.examples]
        self.in_subset = [v if isinstance(v, SubsetDefinitionId)
                          else SubsetDefinitionId(v) for v in self.in_subset]
        self.see_also = [v if isinstance(v, IdentifierType)
                         else IdentifierType(v) for v in self.see_also]
        self.id_prefixes = [v if isinstance(v, NCName)
                            else NCName(v) for v in self.id_prefixes]
        if self.creation_date is not None and not isinstance(self.creation_date, XSDDate):
            self.creation_date = XSDDate(self.creation_date)
        if self.update_date is not None and not isinstance(self.update_date, XSDDate):
            self.update_date = XSDDate(self.update_date)
        if self.from_model is not None and not isinstance(self.from_model, UriType):
            self.from_model = UriType(self.from_model)
        if self.source_file is not None and not isinstance(self.source_file, FileName):
            self.source_file = FileName(self.source_file)
        if self.mixin is not None and not isinstance(self.mixin, BooleanType):
            self.mixin = BooleanType(self.mixin)
        if self.abstract is not None and not isinstance(self.abstract, BooleanType):
            self.abstract = BooleanType(self.abstract)
        self.mappings = [v if isinstance(v, UriType)
                         else UriType(v) for v in self.mappings]


@dataclass
class NamedThing(Thing):
    """
    all non-association things
    """

    # === thing ===
    name: Optional[Union[str, LabelType]] = None
    iri: Optional[Union[str, UriType]] = None
    full_name: Optional[Union[str, LabelType]] = None
    local_names: List[Union[str, LabelType]] = empty_list()
    description: Optional[Union[str, NarrativeText]] = None
    alt_descriptions: List[Union[dict, AltDescription]] = empty_list()
    aliases: List[Union[str, LabelType]] = empty_list()
    comments: List[Union[str, NarrativeText]] = empty_list()
    notes: List[Union[str, NarrativeText]] = empty_list()
    examples: List[Union[dict, Example]] = empty_list()
    deprecated: Optional[str] = None
    in_subset: List[Union[str, SubsetDefinitionId]] = empty_list()
    see_also: List[Union[str, IdentifierType]] = empty_list()
    id_prefixes: List[Union[str, NCName]] = empty_list()
    creation_date: Optional[Union[str, XSDDate]] = None
    update_date: Optional[Union[str, XSDDate]] = None
    from_model: Optional[Union[str, UriType]] = None
    source_file: Optional[Union[str, FileName]] = None
    mixin: Optional[Union[Bool, BooleanType]] = None
    abstract: Optional[Union[Bool, BooleanType]] = None
    mappings: List[Union[str, UriType]] = empty_list()

    # === named_thing ===
    id: Union[str, NamedThingId] = None
    category: List[Union[str, NamedThingId]] = empty_list()
    is_a: Optional[Union[str, NamedThingId]] = None
    mixins: List[Union[str, NamedThingId]] = empty_list()
    apply_to: List[Union[str, NamedThingId]] = empty_list()

    def _fix_elements(self):
        super()._fix_elements()
        if self.id is not None and not isinstance(self.id, NamedThingId):
            self.id = NamedThingId(self.id)
        self.category = [v if isinstance(v, NamedThingId)
                         else NamedThingId(v) for v in self.category]
        if self.is_a is not None and not isinstance(self.is_a, NamedThingId):
            self.is_a = NamedThingId(self.is_a)
        self.mixins = [v if isinstance(v, NamedThingId)
                       else NamedThingId(v) for v in self.mixins]
        self.apply_to = [v if isinstance(v, NamedThingId)
                         else NamedThingId(v) for v in self.apply_to]


@dataclass
class TypeDefinition(NamedThing):
    """
    the range of a literal target of a model_slot or association_slot
    """

    # === thing ===
    name: Optional[Union[str, LabelType]] = None
    iri: Optional[Union[str, UriType]] = None
    full_name: Optional[Union[str, LabelType]] = None
    local_names: List[Union[str, LabelType]] = empty_list()
    description: Optional[Union[str, NarrativeText]] = None
    alt_descriptions: List[Union[dict, AltDescription]] = empty_list()
    aliases: List[Union[str, LabelType]] = empty_list()
    comments: List[Union[str, NarrativeText]] = empty_list()
    notes: List[Union[str, NarrativeText]] = empty_list()
    examples: List[Union[dict, Example]] = empty_list()
    deprecated: Optional[str] = None
    in_subset: List[Union[str, SubsetDefinitionId]] = empty_list()
    see_also: List[Union[str, IdentifierType]] = empty_list()
    id_prefixes: List[Union[str, NCName]] = empty_list()
    creation_date: Optional[Union[str, XSDDate]] = None
    update_date: Optional[Union[str, XSDDate]] = None
    from_model: Optional[Union[str, UriType]] = None
    source_file: Optional[Union[str, FileName]] = None
    mixin: Optional[Union[Bool, BooleanType]] = None
    abstract: Optional[Union[Bool, BooleanType]] = None
    mappings: List[Union[str, UriType]] = empty_list()

    # === named_thing ===
    id: Union[str, TypeDefinitionId] = None
    category: List[Union[str, NamedThingId]] = empty_list()
    is_a: Optional[Union[str, NamedThingId]] = None
    mixins: List[Union[str, NamedThingId]] = empty_list()
    apply_to: List[Union[str, NamedThingId]] = empty_list()

    # === type definition ===
    typeof: Optional[Union[str, TypeDefinitionId]] = None
    base: Optional[str] = None
    uri: Optional[Union[str, IdentifierType]] = None
    repr: Optional[str] = None

    def _fix_elements(self):
        super()._fix_elements()
        if self.id is not None and not isinstance(self.id, TypeDefinitionId):
            self.id = TypeDefinitionId(self.id)
        if self.typeof is not None and not isinstance(self.typeof, TypeDefinitionId):
            self.typeof = TypeDefinitionId(self.typeof)
        if self.uri is not None and not isinstance(self.uri, IdentifierType):
            self.uri = IdentifierType(self.uri)


@dataclass
class ValuesetDefinition(NamedThing):
    """
    a discrete set of possible literals or URI's
    """

    # === thing ===
    name: Optional[Union[str, LabelType]] = None
    iri: Optional[Union[str, UriType]] = None
    full_name: Optional[Union[str, LabelType]] = None
    local_names: List[Union[str, LabelType]] = empty_list()
    description: Optional[Union[str, NarrativeText]] = None
    alt_descriptions: List[Union[dict, AltDescription]] = empty_list()
    aliases: List[Union[str, LabelType]] = empty_list()
    comments: List[Union[str, NarrativeText]] = empty_list()
    notes: List[Union[str, NarrativeText]] = empty_list()
    examples: List[Union[dict, Example]] = empty_list()
    deprecated: Optional[str] = None
    in_subset: List[Union[str, SubsetDefinitionId]] = empty_list()
    see_also: List[Union[str, IdentifierType]] = empty_list()
    id_prefixes: List[Union[str, NCName]] = empty_list()
    creation_date: Optional[Union[str, XSDDate]] = None
    update_date: Optional[Union[str, XSDDate]] = None
    from_model: Optional[Union[str, UriType]] = None
    source_file: Optional[Union[str, FileName]] = None
    mixin: Optional[Union[Bool, BooleanType]] = None
    abstract: Optional[Union[Bool, BooleanType]] = None
    mappings: List[Union[str, UriType]] = empty_list()

    # === named_thing ===
    id: Union[str, ValuesetDefinitionId] = None
    category: List[Union[str, NamedThingId]] = empty_list()
    is_a: Optional[Union[str, NamedThingId]] = None
    mixins: List[Union[str, NamedThingId]] = empty_list()
    apply_to: List[Union[str, NamedThingId]] = empty_list()

    # === valueset definition ===
    values_from: List[Union[str, IdentifierType]] = empty_list()
    possible_values: Union[dict, PossibleValue] = empty_dict()

    def _fix_elements(self):
        super()._fix_elements()
        if self.id is not None and not isinstance(self.id, ValuesetDefinitionId):
            self.id = ValuesetDefinitionId(self.id)
        self.values_from = [v if isinstance(v, IdentifierType)
                            else IdentifierType(v) for v in self.values_from]
        for k, v in self.possible_values.items():
            if not isinstance(v, PossibleValue):
                self.possible_values[k] = PossibleValue(k, v)


@dataclass
class OntologicalClass(NamedThing):
    """
    named things that belong in the ontological space
    """

    # === thing ===
    name: Optional[Union[str, LabelType]] = None
    iri: Optional[Union[str, UriType]] = None
    full_name: Optional[Union[str, LabelType]] = None
    local_names: List[Union[str, LabelType]] = empty_list()
    description: Optional[Union[str, NarrativeText]] = None
    alt_descriptions: List[Union[dict, AltDescription]] = empty_list()
    aliases: List[Union[str, LabelType]] = empty_list()
    comments: List[Union[str, NarrativeText]] = empty_list()
    notes: List[Union[str, NarrativeText]] = empty_list()
    examples: List[Union[dict, Example]] = empty_list()
    deprecated: Optional[str] = None
    in_subset: List[Union[str, SubsetDefinitionId]] = empty_list()
    see_also: List[Union[str, IdentifierType]] = empty_list()
    id_prefixes: List[Union[str, NCName]] = empty_list()
    creation_date: Optional[Union[str, XSDDate]] = None
    update_date: Optional[Union[str, XSDDate]] = None
    from_model: Optional[Union[str, UriType]] = None
    source_file: Optional[Union[str, FileName]] = None
    mixin: Optional[Union[Bool, BooleanType]] = None
    abstract: Optional[Union[Bool, BooleanType]] = None
    mappings: List[Union[str, UriType]] = empty_list()

    # === named_thing ===
    id: Union[str, OntologicalClassId] = None
    category: List[Union[str, NamedThingId]] = empty_list()
    is_a: Optional[Union[str, NamedThingId]] = None
    mixins: List[Union[str, NamedThingId]] = empty_list()
    apply_to: List[Union[str, NamedThingId]] = empty_list()

    # === ontological_class ===
    subclass_of: List[Union[str, UriType]] = empty_list()
    exact_matches: List[Union[str, UriType]] = empty_list()
    broader_matches: List[Union[str, UriType]] = empty_list()
    narrower_matches: List[Union[str, UriType]] = empty_list()
    close_matches: List[Union[str, UriType]] = empty_list()
    slots: Dict[Union[str, NodePropertyDefinitionId], Union[dict, "NodePropertyDefinition"]] = empty_dict()
    properties: List[str] = empty_list()

    def _fix_elements(self):
        super()._fix_elements()
        self.subclass_of = [v if isinstance(v, UriType)
                            else UriType(v) for v in self.subclass_of]
        self.exact_matches = [v if isinstance(v, UriType)
                              else UriType(v) for v in self.exact_matches]
        self.broader_matches = [v if isinstance(v, UriType)
                                else UriType(v) for v in self.broader_matches]
        self.narrower_matches = [v if isinstance(v, UriType)
                                 else UriType(v) for v in self.narrower_matches]
        self.close_matches = [v if isinstance(v, UriType)
                              else UriType(v) for v in self.close_matches]
        for k, v in self.slots.items():
            if not isinstance(v, NodePropertyDefinition):
                self.slots[k] = NodePropertyDefinition(id=k, **({} if v is None else v))


@dataclass
class NodeType(OntologicalClass):
    """
    the subject or object of a biolink association
    """

    # === thing ===
    name: Optional[Union[str, LabelType]] = None
    iri: Optional[Union[str, UriType]] = None
    full_name: Optional[Union[str, LabelType]] = None
    local_names: List[Union[str, LabelType]] = empty_list()
    description: Optional[Union[str, NarrativeText]] = None
    alt_descriptions: List[Union[dict, AltDescription]] = empty_list()
    aliases: List[Union[str, LabelType]] = empty_list()
    comments: List[Union[str, NarrativeText]] = empty_list()
    notes: List[Union[str, NarrativeText]] = empty_list()
    examples: List[Union[dict, Example]] = empty_list()
    deprecated: Optional[str] = None
    in_subset: List[Union[str, SubsetDefinitionId]] = empty_list()
    see_also: List[Union[str, IdentifierType]] = empty_list()
    id_prefixes: List[Union[str, NCName]] = empty_list()
    creation_date: Optional[Union[str, XSDDate]] = None
    update_date: Optional[Union[str, XSDDate]] = None
    from_model: Optional[Union[str, UriType]] = None
    source_file: Optional[Union[str, FileName]] = None
    mixin: Optional[Union[Bool, BooleanType]] = None
    abstract: Optional[Union[Bool, BooleanType]] = None
    mappings: List[Union[str, UriType]] = empty_list()

    # === named_thing ===
    id: Union[str, NodeTypeId] = None
    category: List[Union[str, NamedThingId]] = empty_list()
    is_a: Optional[Union[str, NamedThingId]] = None
    mixins: List[Union[str, NamedThingId]] = empty_list()
    apply_to: List[Union[str, NamedThingId]] = empty_list()

    # === ontological_class ===
    subclass_of: List[Union[str, UriType]] = empty_list()
    exact_matches: List[Union[str, UriType]] = empty_list()
    broader_matches: List[Union[str, UriType]] = empty_list()
    narrower_matches: List[Union[str, UriType]] = empty_list()
    close_matches: List[Union[str, UriType]] = empty_list()
    slots: Dict[Union[str, NodePropertyDefinitionId], Union[dict, "NodePropertyDefinition"]] = empty_dict()
    properties: List[str] = empty_list()

    # === node_type ===
    union_of: List[Union[str, NodeTypeId]] = empty_list()

    def _fix_elements(self):
        super()._fix_elements()
        if self.id is not None and not isinstance(self.id, NodeTypeId):
            self.id = NodeTypeId(self.id)
        self.union_of = [v if isinstance(v, NodeTypeId)
                         else NodeTypeId(v) for v in self.union_of]


@dataclass
class RelationshipType(OntologicalClass):
    """
    the predicate or relationship of a biolink association
    """

    # === thing ===
    name: Optional[Union[str, LabelType]] = None
    iri: Optional[Union[str, UriType]] = None
    full_name: Optional[Union[str, LabelType]] = None
    local_names: List[Union[str, LabelType]] = empty_list()
    description: Optional[Union[str, NarrativeText]] = None
    alt_descriptions: List[Union[dict, AltDescription]] = empty_list()
    aliases: List[Union[str, LabelType]] = empty_list()
    comments: List[Union[str, NarrativeText]] = empty_list()
    notes: List[Union[str, NarrativeText]] = empty_list()
    examples: List[Union[dict, Example]] = empty_list()
    deprecated: Optional[str] = None
    in_subset: List[Union[str, SubsetDefinitionId]] = empty_list()
    see_also: List[Union[str, IdentifierType]] = empty_list()
    id_prefixes: List[Union[str, NCName]] = empty_list()
    creation_date: Optional[Union[str, XSDDate]] = None
    update_date: Optional[Union[str, XSDDate]] = None
    from_model: Optional[Union[str, UriType]] = None
    source_file: Optional[Union[str, FileName]] = None
    mixin: Optional[Union[Bool, BooleanType]] = None
    abstract: Optional[Union[Bool, BooleanType]] = None
    mappings: List[Union[str, UriType]] = empty_list()

    # === named_thing ===
    id: Union[str, RelationshipTypeId] = None
    category: List[Union[str, NamedThingId]] = empty_list()
    is_a: Optional[Union[str, NamedThingId]] = None
    mixins: List[Union[str, NamedThingId]] = empty_list()
    apply_to: List[Union[str, NamedThingId]] = empty_list()

    # === ontological_class ===
    subclass_of: List[Union[str, UriType]] = empty_list()
    exact_matches: List[Union[str, UriType]] = empty_list()
    broader_matches: List[Union[str, UriType]] = empty_list()
    narrower_matches: List[Union[str, UriType]] = empty_list()
    close_matches: List[Union[str, UriType]] = empty_list()
    slots: Dict[Union[str, NodePropertyDefinitionId], Union[dict, "NodePropertyDefinition"]] = empty_dict()
    properties: List[str] = empty_list()

    # === relationship_type ===
    domain: Optional[Union[str, NodeTypeId]] = None
    range: Optional[Union[str, NodeTypeId]] = None
    inverse: Optional[Union[str, RelationshipTypeId]] = None
    symmetric: Optional[Union[str, RelationshipTypeId]] = None

    def _fix_elements(self):
        super()._fix_elements()
        if self.id is not None and not isinstance(self.id, RelationshipTypeId):
            self.id = RelationshipTypeId(self.id)
        if self.domain is not None and not isinstance(self.domain, NodeTypeId):
            self.domain = NodeTypeId(self.domain)
        if self.range is not None and not isinstance(self.range, NodeTypeId):
            self.range = NodeTypeId(self.range)
        if self.inverse is not None and not isinstance(self.inverse, RelationshipTypeId):
            self.inverse = RelationshipTypeId(self.inverse)
        if self.symmetric is not None and not isinstance(self.symmetric, RelationshipTypeId):
            self.symmetric = RelationshipTypeId(self.symmetric)


@dataclass
class PropertyType(OntologicalClass):
    """
    elements that inhere in nodes
    """

    # === thing ===
    name: Optional[Union[str, LabelType]] = None
    iri: Optional[Union[str, UriType]] = None
    full_name: Optional[Union[str, LabelType]] = None
    local_names: List[Union[str, LabelType]] = empty_list()
    description: Optional[Union[str, NarrativeText]] = None
    alt_descriptions: List[Union[dict, AltDescription]] = empty_list()
    aliases: List[Union[str, LabelType]] = empty_list()
    comments: List[Union[str, NarrativeText]] = empty_list()
    notes: List[Union[str, NarrativeText]] = empty_list()
    examples: List[Union[dict, Example]] = empty_list()
    deprecated: Optional[str] = None
    in_subset: List[Union[str, SubsetDefinitionId]] = empty_list()
    see_also: List[Union[str, IdentifierType]] = empty_list()
    id_prefixes: List[Union[str, NCName]] = empty_list()
    creation_date: Optional[Union[str, XSDDate]] = None
    update_date: Optional[Union[str, XSDDate]] = None
    from_model: Optional[Union[str, UriType]] = None
    source_file: Optional[Union[str, FileName]] = None
    mixin: Optional[Union[Bool, BooleanType]] = None
    abstract: Optional[Union[Bool, BooleanType]] = None
    mappings: List[Union[str, UriType]] = empty_list()

    # === named_thing ===
    id: Union[str, PropertyTypeId] = None
    category: List[Union[str, NamedThingId]] = empty_list()
    is_a: Optional[Union[str, NamedThingId]] = None
    mixins: List[Union[str, NamedThingId]] = empty_list()
    apply_to: List[Union[str, NamedThingId]] = empty_list()

    # === ontological_class ===
    subclass_of: List[Union[str, UriType]] = empty_list()
    exact_matches: List[Union[str, UriType]] = empty_list()
    broader_matches: List[Union[str, UriType]] = empty_list()
    narrower_matches: List[Union[str, UriType]] = empty_list()
    close_matches: List[Union[str, UriType]] = empty_list()
    slots: Dict[Union[str, NodePropertyDefinitionId], Union[dict, "NodePropertyDefinition"]] = empty_dict()
    properties: List[str] = empty_list()

    # === property_type ===

    def _fix_elements(self):
        super()._fix_elements()
        if self.id is not None and not isinstance(self.id, PropertyTypeId):
            self.id = PropertyTypeId(self.id)


@dataclass
class InformationContentEntity(NamedThing):
    """
    a piece of information that typically describes some piece of biology or is used as support.
    """

    # === thing ===
    name: Optional[Union[str, LabelType]] = None
    iri: Optional[Union[str, UriType]] = None
    full_name: Optional[Union[str, LabelType]] = None
    local_names: List[Union[str, LabelType]] = empty_list()
    description: Optional[Union[str, NarrativeText]] = None
    alt_descriptions: List[Union[dict, AltDescription]] = empty_list()
    aliases: List[Union[str, LabelType]] = empty_list()
    comments: List[Union[str, NarrativeText]] = empty_list()
    notes: List[Union[str, NarrativeText]] = empty_list()
    examples: List[Union[dict, Example]] = empty_list()
    deprecated: Optional[str] = None
    in_subset: List[Union[str, SubsetDefinitionId]] = empty_list()
    see_also: List[Union[str, IdentifierType]] = empty_list()
    id_prefixes: List[Union[str, NCName]] = empty_list()
    creation_date: Optional[Union[str, XSDDate]] = None
    update_date: Optional[Union[str, XSDDate]] = None
    from_model: Optional[Union[str, UriType]] = None
    source_file: Optional[Union[str, FileName]] = None
    mixin: Optional[Union[Bool, BooleanType]] = None
    abstract: Optional[Union[Bool, BooleanType]] = None
    mappings: List[Union[str, UriType]] = empty_list()

    # === named_thing ===
    id: Union[str, InformationContentEntityId] = None
    category: List[Union[str, NamedThingId]] = empty_list()
    is_a: Optional[Union[str, NamedThingId]] = None
    mixins: List[Union[str, NamedThingId]] = empty_list()
    apply_to: List[Union[str, NamedThingId]] = empty_list()

    # === information_content_entity ===


@dataclass
class AdministrativeEntity(NamedThing):

    # === thing ===
    name: Optional[Union[str, LabelType]] = None
    iri: Optional[Union[str, UriType]] = None
    full_name: Optional[Union[str, LabelType]] = None
    local_names: List[Union[str, LabelType]] = empty_list()
    description: Optional[Union[str, NarrativeText]] = None
    alt_descriptions: List[Union[dict, AltDescription]] = empty_list()
    aliases: List[Union[str, LabelType]] = empty_list()
    comments: List[Union[str, NarrativeText]] = empty_list()
    notes: List[Union[str, NarrativeText]] = empty_list()
    examples: List[Union[dict, Example]] = empty_list()
    deprecated: Optional[str] = None
    in_subset: List[Union[str, SubsetDefinitionId]] = empty_list()
    see_also: List[Union[str, IdentifierType]] = empty_list()
    id_prefixes: List[Union[str, NCName]] = empty_list()
    creation_date: Optional[Union[str, XSDDate]] = None
    update_date: Optional[Union[str, XSDDate]] = None
    from_model: Optional[Union[str, UriType]] = None
    source_file: Optional[Union[str, FileName]] = None
    mixin: Optional[Union[Bool, BooleanType]] = None
    abstract: Optional[Union[Bool, BooleanType]] = None
    mappings: List[Union[str, UriType]] = empty_list()

    # === named_thing ===
    id: Union[str, AdministrativeEntityId] = None
    category: List[Union[str, NamedThingId]] = empty_list()
    is_a: Optional[Union[str, NamedThingId]] = None
    mixins: List[Union[str, NamedThingId]] = empty_list()
    apply_to: List[Union[str, NamedThingId]] = empty_list()

    # === administrative_entity ===


@dataclass
class Provider(AdministrativeEntity):
    """
    person, group, organization or project that provides a piece of information
    """

    # === thing ===
    name: Optional[Union[str, LabelType]] = None
    iri: Optional[Union[str, UriType]] = None
    full_name: Optional[Union[str, LabelType]] = None
    local_names: List[Union[str, LabelType]] = empty_list()
    description: Optional[Union[str, NarrativeText]] = None
    alt_descriptions: List[Union[dict, AltDescription]] = empty_list()
    aliases: List[Union[str, LabelType]] = empty_list()
    comments: List[Union[str, NarrativeText]] = empty_list()
    notes: List[Union[str, NarrativeText]] = empty_list()
    examples: List[Union[dict, Example]] = empty_list()
    deprecated: Optional[str] = None
    in_subset: List[Union[str, SubsetDefinitionId]] = empty_list()
    see_also: List[Union[str, IdentifierType]] = empty_list()
    id_prefixes: List[Union[str, NCName]] = empty_list()
    creation_date: Optional[Union[str, XSDDate]] = None
    update_date: Optional[Union[str, XSDDate]] = None
    from_model: Optional[Union[str, UriType]] = None
    source_file: Optional[Union[str, FileName]] = None
    mixin: Optional[Union[Bool, BooleanType]] = None
    abstract: Optional[Union[Bool, BooleanType]] = None
    mappings: List[Union[str, UriType]] = empty_list()

    # === named_thing ===
    id: Union[str, ProviderId] = None
    category: List[Union[str, NamedThingId]] = empty_list()
    is_a: Optional[Union[str, NamedThingId]] = None
    mixins: List[Union[str, NamedThingId]] = empty_list()
    apply_to: List[Union[str, NamedThingId]] = empty_list()

    # === administrative_entity ===

    # === provider ===

    def _fix_elements(self):
        super()._fix_elements()
        if self.id is not None and not isinstance(self.id, ProviderId):
            self.id = ProviderId(self.id)


@dataclass
class SubsetDefinition(NamedThing):
    """
    the name and description of a subset used to classify or categorize things
    """

    # === thing ===
    name: Optional[Union[str, LabelType]] = None
    iri: Optional[Union[str, UriType]] = None
    full_name: Optional[Union[str, LabelType]] = None
    local_names: List[Union[str, LabelType]] = empty_list()
    description: Optional[Union[str, NarrativeText]] = None
    alt_descriptions: List[Union[dict, AltDescription]] = empty_list()
    aliases: List[Union[str, LabelType]] = empty_list()
    comments: List[Union[str, NarrativeText]] = empty_list()
    notes: List[Union[str, NarrativeText]] = empty_list()
    examples: List[Union[dict, Example]] = empty_list()
    deprecated: Optional[str] = None
    in_subset: List[Union[str, SubsetDefinitionId]] = empty_list()
    see_also: List[Union[str, IdentifierType]] = empty_list()
    id_prefixes: List[Union[str, NCName]] = empty_list()
    creation_date: Optional[Union[str, XSDDate]] = None
    update_date: Optional[Union[str, XSDDate]] = None
    from_model: Optional[Union[str, UriType]] = None
    source_file: Optional[Union[str, FileName]] = None
    mixin: Optional[Union[Bool, BooleanType]] = None
    abstract: Optional[Union[Bool, BooleanType]] = None
    mappings: List[Union[str, UriType]] = empty_list()

    # === named_thing ===
    id: Union[str, SubsetDefinitionId] = None
    category: List[Union[str, NamedThingId]] = empty_list()
    is_a: Optional[Union[str, NamedThingId]] = None
    mixins: List[Union[str, NamedThingId]] = empty_list()
    apply_to: List[Union[str, NamedThingId]] = empty_list()

    # === subset_definition ===

    def _fix_elements(self):
        super()._fix_elements()
        if self.id is not None and not isinstance(self.id, SubsetDefinitionId):
            self.id = SubsetDefinitionId(self.id)


@dataclass
class RelationshipQuantifier(NamedThing):
    """
    A quantifier over an association
    """

    # === thing ===
    name: Optional[Union[str, LabelType]] = None
    iri: Optional[Union[str, UriType]] = None
    full_name: Optional[Union[str, LabelType]] = None
    local_names: List[Union[str, LabelType]] = empty_list()
    description: Optional[Union[str, NarrativeText]] = None
    alt_descriptions: List[Union[dict, AltDescription]] = empty_list()
    aliases: List[Union[str, LabelType]] = empty_list()
    comments: List[Union[str, NarrativeText]] = empty_list()
    notes: List[Union[str, NarrativeText]] = empty_list()
    examples: List[Union[dict, Example]] = empty_list()
    deprecated: Optional[str] = None
    in_subset: List[Union[str, SubsetDefinitionId]] = empty_list()
    see_also: List[Union[str, IdentifierType]] = empty_list()
    id_prefixes: List[Union[str, NCName]] = empty_list()
    creation_date: Optional[Union[str, XSDDate]] = None
    update_date: Optional[Union[str, XSDDate]] = None
    from_model: Optional[Union[str, UriType]] = None
    source_file: Optional[Union[str, FileName]] = None
    mixin: Optional[Union[Bool, BooleanType]] = None
    abstract: Optional[Union[Bool, BooleanType]] = None
    mappings: List[Union[str, UriType]] = empty_list()

    # === named_thing ===
    id: Union[str, RelationshipQuantifierId] = None
    category: List[Union[str, NamedThingId]] = empty_list()
    is_a: Optional[Union[str, NamedThingId]] = None
    mixins: List[Union[str, NamedThingId]] = empty_list()
    apply_to: List[Union[str, NamedThingId]] = empty_list()

    # === relationship_quantifier ===

    def _fix_elements(self):
        super()._fix_elements()
        if self.id is not None and not isinstance(self.id, RelationshipQuantifierId):
            self.id = RelationshipQuantifierId(self.id)


@dataclass
class PropertyDefinition(NamedThing):
    """
    An extension property for a node or association
    """

    # === thing ===
    name: Optional[Union[str, LabelType]] = None
    iri: Optional[Union[str, UriType]] = None
    full_name: Optional[Union[str, LabelType]] = None
    local_names: List[Union[str, LabelType]] = empty_list()
    description: Optional[Union[str, NarrativeText]] = None
    alt_descriptions: List[Union[dict, AltDescription]] = empty_list()
    aliases: List[Union[str, LabelType]] = empty_list()
    comments: List[Union[str, NarrativeText]] = empty_list()
    notes: List[Union[str, NarrativeText]] = empty_list()
    examples: List[Union[dict, Example]] = empty_list()
    deprecated: Optional[str] = None
    in_subset: List[Union[str, SubsetDefinitionId]] = empty_list()
    see_also: List[Union[str, IdentifierType]] = empty_list()
    id_prefixes: List[Union[str, NCName]] = empty_list()
    creation_date: Optional[Union[str, XSDDate]] = None
    update_date: Optional[Union[str, XSDDate]] = None
    from_model: Optional[Union[str, UriType]] = None
    source_file: Optional[Union[str, FileName]] = None
    mixin: Optional[Union[Bool, BooleanType]] = None
    abstract: Optional[Union[Bool, BooleanType]] = None
    mappings: List[Union[str, UriType]] = empty_list()

    # === named_thing ===
    id: Union[str, PropertyDefinitionId] = None
    category: List[Union[str, NamedThingId]] = empty_list()
    is_a: Optional[Union[str, NamedThingId]] = None
    mixins: List[Union[str, NamedThingId]] = empty_list()
    apply_to: List[Union[str, NamedThingId]] = empty_list()

    # === property_definition ===
    domain: Optional[Union[str, IdentifierType]] = None
    range: Optional[Union[str, NamedThingId]] = None
    path: Optional[str] = None
    multivalued: Optional[Bool] = None
    required: Optional[Bool] = None
    inherited: Optional[Bool] = None

    def _fix_elements(self):
        super()._fix_elements()
        if self.domain is not None and not isinstance(self.domain, IdentifierType):
            self.domain = IdentifierType(self.domain)
        if self.range is not None and not isinstance(self.range, NamedThingId):
            self.range = NamedThingId(self.range)


@dataclass
class NodePropertyDefinition(PropertyDefinition):
    """
    An additional property for a node
    """

    # === thing ===
    name: Optional[Union[str, LabelType]] = None
    iri: Optional[Union[str, UriType]] = None
    full_name: Optional[Union[str, LabelType]] = None
    local_names: List[Union[str, LabelType]] = empty_list()
    description: Optional[Union[str, NarrativeText]] = None
    alt_descriptions: List[Union[dict, AltDescription]] = empty_list()
    aliases: List[Union[str, LabelType]] = empty_list()
    comments: List[Union[str, NarrativeText]] = empty_list()
    notes: List[Union[str, NarrativeText]] = empty_list()
    examples: List[Union[dict, Example]] = empty_list()
    deprecated: Optional[str] = None
    in_subset: List[Union[str, SubsetDefinitionId]] = empty_list()
    see_also: List[Union[str, IdentifierType]] = empty_list()
    id_prefixes: List[Union[str, NCName]] = empty_list()
    creation_date: Optional[Union[str, XSDDate]] = None
    update_date: Optional[Union[str, XSDDate]] = None
    from_model: Optional[Union[str, UriType]] = None
    source_file: Optional[Union[str, FileName]] = None
    mixin: Optional[Union[Bool, BooleanType]] = None
    abstract: Optional[Union[Bool, BooleanType]] = None
    mappings: List[Union[str, UriType]] = empty_list()

    # === named_thing ===
    id: Union[str, NodePropertyDefinitionId] = None
    category: List[Union[str, NamedThingId]] = empty_list()
    is_a: Optional[Union[str, NamedThingId]] = None
    mixins: List[Union[str, NamedThingId]] = empty_list()
    apply_to: List[Union[str, NamedThingId]] = empty_list()

    # === property_definition ===
    domain: Optional[Union[str, IdentifierType]] = None
    range: Optional[Union[str, NamedThingId]] = None
    path: Optional[str] = None
    multivalued: Optional[Bool] = None
    required: Optional[Bool] = None
    inherited: Optional[Bool] = None

    # === node_property_definition ===


@dataclass
class QualifierType(NamedThing):
    """
    information that modifies or qualifies the meaning of a biolink association
    """

    # === thing ===
    name: Optional[Union[str, LabelType]] = None
    iri: Optional[Union[str, UriType]] = None
    full_name: Optional[Union[str, LabelType]] = None
    local_names: List[Union[str, LabelType]] = empty_list()
    description: Optional[Union[str, NarrativeText]] = None
    alt_descriptions: List[Union[dict, AltDescription]] = empty_list()
    aliases: List[Union[str, LabelType]] = empty_list()
    comments: List[Union[str, NarrativeText]] = empty_list()
    notes: List[Union[str, NarrativeText]] = empty_list()
    examples: List[Union[dict, Example]] = empty_list()
    deprecated: Optional[str] = None
    in_subset: List[Union[str, SubsetDefinitionId]] = empty_list()
    see_also: List[Union[str, IdentifierType]] = empty_list()
    id_prefixes: List[Union[str, NCName]] = empty_list()
    creation_date: Optional[Union[str, XSDDate]] = None
    update_date: Optional[Union[str, XSDDate]] = None
    from_model: Optional[Union[str, UriType]] = None
    source_file: Optional[Union[str, FileName]] = None
    mixin: Optional[Union[Bool, BooleanType]] = None
    abstract: Optional[Union[Bool, BooleanType]] = None
    mappings: List[Union[str, UriType]] = empty_list()

    # === named_thing ===
    id: Union[str, QualifierTypeId] = None
    category: List[Union[str, NamedThingId]] = empty_list()
    is_a: Optional[Union[str, NamedThingId]] = None
    mixins: List[Union[str, NamedThingId]] = empty_list()
    apply_to: List[Union[str, NamedThingId]] = empty_list()

    # === qualifier_type ===

    def _fix_elements(self):
        super()._fix_elements()
        if self.id is not None and not isinstance(self.id, QualifierTypeId):
            self.id = QualifierTypeId(self.id)

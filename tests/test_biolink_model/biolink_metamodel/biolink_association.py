# Auto generated from tests.test_biolink_model.biolink_metamodel.biolink_association .yaml by pythongen.py version: 0.2.0
# Generation date: 2019-02-12 13:58
# Schema: biolink association
#
# id: http://w3id.org/biolink/biolink-model/association
# description: A model of the biolink reified association class
# license: https://creativecommons.org/publicdomain/zero/1.0/

from typing import Optional, List, Union, Dict
from dataclasses import dataclass
from biolinkml.utils.metamodelcore import empty_list, empty_dict
from biolinkml.utils.yamlutils import YAMLRoot
from tests.test_biolink_model.biolink_metamodel.biolink_named_thing import AltDescription, Example, InformationContentEntity, InformationContentEntityId, NamedThingId, NodeTypeId, PropertyDefinition, PropertyDefinitionId, ProviderId, QualifierType, QualifierTypeId, RelationshipTypeId, SubsetDefinitionId, Thing
from tests.test_biolink_model.biolink_metamodel.includes.biolink_types import BooleanType, FileName, IdentifierType, LabelType, NarrativeText, UriType
from biolinkml.utils.metamodelcore import Bool, NCName, URIorCURIE, XSDDate
from includes.types import Boolean, Datetime, Ncname, String, Uri

metamodel_version = "1.0.2"

inherited_slots: List[str] = ["slot_class_range", "slot_relation_range", "definitional", "slots"]


# Types

# Class references
class AssociationAssociationId(IdentifierType):
    pass


class EvidenceTypeId(InformationContentEntityId):
    pass


class ConfidenceLevelId(InformationContentEntityId):
    pass


class PublicationId(InformationContentEntityId):
    pass


class AssocPropertyDefinitionId(PropertyDefinitionId):
    pass


@dataclass
class Association(Thing):
    """
    A relation between two entities, supported by evidence.
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

    # === association ===
    association_id: Union[str, AssociationAssociationId] = None
    association_type: Optional[Union[str, RelationshipTypeId]] = None
    subject: Optional[Union[dict, "SlotClassDescription"]] = None
    relation: Optional[Union[dict, "SlotRelationDescription"]] = None
    object: Optional[Union[dict, "SlotClassDescription"]] = None
    is_a: Optional[Union[str, AssociationAssociationId]] = None
    edge_label: Optional[Union[str, LabelType]] = None
    negated: Optional[Union[Bool, BooleanType]] = None
    has_confidence_level: Optional[Union[str, ConfidenceLevelId]] = None
    has_evidence: List[Union[str, EvidenceTypeId]] = empty_list()
    provided_by: Optional[Union[str, ProviderId]] = None
    qualifiers: Dict[Union[str, QualifierTypeId], Union[dict, QualifierType]] = empty_dict()
    publications: List[Union[str, PublicationId]] = empty_list()
    mixins: List[Union[str, AssociationAssociationId]] = empty_list()
    apply_to: List[Union[str, AssociationAssociationId]] = empty_list()
    association_slot: List[Union[dict, "SlotDescription"]] = empty_list()

    def _fix_elements(self):
        super()._fix_elements()
        if not isinstance(self.association_id, AssociationAssociationId):
            self.association_id = AssociationAssociationId(self.association_id)
        if self.association_type and not isinstance(self.association_type, RelationshipTypeId):
            self.association_type = RelationshipTypeId(self.association_type)
        if self.subject and not isinstance(self.subject, SlotClassDescription):
            self.subject = SlotClassDescription(**self.subject)
        if self.relation and not isinstance(self.relation, SlotRelationDescription):
            self.relation = SlotRelationDescription(**self.relation)
        if self.object and not isinstance(self.object, SlotClassDescription):
            self.object = SlotClassDescription(**self.object)
        if self.is_a and not isinstance(self.is_a, AssociationAssociationId):
            self.is_a = AssociationAssociationId(self.is_a)
        if self.edge_label and not isinstance(self.edge_label, LabelType):
            self.edge_label = LabelType(self.edge_label)
        if self.negated and not isinstance(self.negated, BooleanType):
            self.negated = BooleanType(self.negated)
        if self.has_confidence_level and not isinstance(self.has_confidence_level, ConfidenceLevelId):
            self.has_confidence_level = ConfidenceLevelId(self.has_confidence_level)
        self.has_evidence = [v if isinstance(v, EvidenceTypeId)
                             else EvidenceTypeId(v) for v in self.has_evidence]
        if self.provided_by and not isinstance(self.provided_by, ProviderId):
            self.provided_by = ProviderId(self.provided_by)
        for k, v in self.qualifiers.items():
            if not isinstance(v, QualifierType):
                self.qualifiers[k] = QualifierType(id=k, **({} if v is None else v))
        self.publications = [v if isinstance(v, PublicationId)
                             else PublicationId(v) for v in self.publications]
        self.mixins = [v if isinstance(v, AssociationAssociationId)
                       else AssociationAssociationId(v) for v in self.mixins]
        self.apply_to = [v if isinstance(v, AssociationAssociationId)
                         else AssociationAssociationId(v) for v in self.apply_to]
        self.association_slot = [v if isinstance(v, SlotDescription)
                                 else SlotDescription(**v) for v in self.association_slot]


@dataclass
class EvidenceType(InformationContentEntity):
    """
    Class of evidence that supports an association
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
    id: Union[str, EvidenceTypeId] = None
    category: List[Union[str, NamedThingId]] = empty_list()
    is_a: Optional[Union[str, NamedThingId]] = None
    mixins: List[Union[str, NamedThingId]] = empty_list()
    apply_to: List[Union[str, NamedThingId]] = empty_list()

    # === information_content_entity ===

    # === evidence_type ===

    def _fix_elements(self):
        super()._fix_elements()
        if not isinstance(self.id, EvidenceTypeId):
            self.id = EvidenceTypeId(self.id)


@dataclass
class ConfidenceLevel(InformationContentEntity):
    """
    Level of confidence in a statement
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
    id: Union[str, ConfidenceLevelId] = None
    category: List[Union[str, NamedThingId]] = empty_list()
    is_a: Optional[Union[str, NamedThingId]] = None
    mixins: List[Union[str, NamedThingId]] = empty_list()
    apply_to: List[Union[str, NamedThingId]] = empty_list()

    # === information_content_entity ===

    # === confidence_level ===

    def _fix_elements(self):
        super()._fix_elements()
        if not isinstance(self.id, ConfidenceLevelId):
            self.id = ConfidenceLevelId(self.id)


@dataclass
class Publication(InformationContentEntity):
    """
    Any published piece of information. Can refer to a whole publication, or to a part of it (e.g. a figure, figure
    legend, or section highlighted by NLP). The scope is intended to be general and include information published on
    the web as well as journals.
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
    id: Union[str, PublicationId] = None
    category: List[Union[str, NamedThingId]] = empty_list()
    is_a: Optional[Union[str, NamedThingId]] = None
    mixins: List[Union[str, NamedThingId]] = empty_list()
    apply_to: List[Union[str, NamedThingId]] = empty_list()

    # === information_content_entity ===

    # === publication ===

    def _fix_elements(self):
        super()._fix_elements()
        if not isinstance(self.id, PublicationId):
            self.id = PublicationId(self.id)


@dataclass
class SlotDescription(Thing):
    """
    Additional documentation and information accompanying an association_slot
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

    # === slot_description ===
    definitional: Optional[Bool] = None
    values_from: List[Union[str, URIorCURIE]] = empty_list()

    def _fix_elements(self):
        super()._fix_elements()
        self.values_from = [v if isinstance(v, URIorCURIE)
                            else URIorCURIE(v) for v in self.values_from]


@dataclass
class SlotClassDescription(SlotDescription):
    """
    The description of the link between an association and its subject or object
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

    # === slot_description ===
    definitional: Optional[Bool] = None
    values_from: List[Union[str, URIorCURIE]] = empty_list()

    # === slot_class_description ===
    range: Union[str, NodeTypeId] = None
    subclass_of: Optional[Union[str, IdentifierType]] = None

    def _fix_elements(self):
        super()._fix_elements()
        if self.subclass_of and not isinstance(self.subclass_of, IdentifierType):
            self.subclass_of = IdentifierType(self.subclass_of)
        if not isinstance(self.range, NodeTypeId):
            self.range = NodeTypeId(self.range)


@dataclass
class SlotRelationDescription(SlotDescription):
    """
    The description of the link between an association and its relation
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

    # === slot_description ===
    definitional: Optional[Bool] = None
    values_from: List[Union[str, URIorCURIE]] = empty_list()

    # === slot_relation_description ===
    range: Union[str, RelationshipTypeId] = None
    subproperty_of: Optional[Union[str, IdentifierType]] = None

    def _fix_elements(self):
        super()._fix_elements()
        if self.subproperty_of and not isinstance(self.subproperty_of, IdentifierType):
            self.subproperty_of = IdentifierType(self.subproperty_of)
        if not isinstance(self.range, RelationshipTypeId):
            self.range = RelationshipTypeId(self.range)


@dataclass
class AssocPropertyDefinition(PropertyDefinition):
    """
    An additional property for a association
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
    id: Union[str, AssocPropertyDefinitionId] = None
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

    # === assoc_property_definition ===

    def _fix_elements(self):
        super()._fix_elements()
        if not isinstance(self.id, AssocPropertyDefinitionId):
            self.id = AssocPropertyDefinitionId(self.id)

# Auto generated from tests.test_biolink_model.biolink_metamodel.biolink_association .yaml by pythongen.py version: 0.2.0
# Generation date: 2019-02-05 16:34
# Schema: biolink association
#
# id: http://w3id.org/biolink/biolink-model/association
# description: Reified association model for life-sciences data
# license: https://creativecommons.org/publicdomain/zero/1.0/

from typing import Optional, List, Union, Dict
from dataclasses import dataclass
from biolinkml.utils.metamodelcore import empty_list, empty_dict
from biolinkml.utils.yamlutils import YAMLRoot
from tests.test_biolink_model.biolink_metamodel.biolink_named_thing import InformationContentEntity, InformationContentEntityId, NamedThingId, OntologyClassId, ProviderId, PublicationId, RelationshipTypeId, Thing
from tests.test_biolink_model.biolink_metamodel.includes.biolink_types import IdentifierType, LabelType, NarrativeText, TimeType, UriType
from biolinkml.utils.metamodelcore import Bool, XSDDateTime
from includes.types import Boolean, Date, String, Time, Uri

metamodel_version = "1.0.1"

inherited_slots: List[str] = []


# Types

# Class references
class AssociationAssociationId(IdentifierType):
    pass


class ConfidenceLevelId(InformationContentEntityId):
    pass


class EvidenceTypeId(InformationContentEntityId):
    pass


@dataclass
class Association(YAMLRoot):
    """
    A typed association between two entities, supported by evidence
    """

    # === association ===
    association_id: Union[str, AssociationAssociationId]
    subject: Union[str, NamedThingId]
    object: Union[str, NamedThingId]
    relation: Union[str, RelationshipTypeId]
    association_slot: Optional[str] = None
    edge_label: Optional[Union[str, LabelType]] = None
    negated: Optional[Bool] = None
    has_confidence_level: Optional[Union[str, ConfidenceLevelId]] = None
    has_evidence: Optional[Union[str, EvidenceTypeId]] = None
    provided_by: Optional[Union[str, ProviderId]] = None
    association_type: Optional[Union[str, OntologyClassId]] = None
    qualifiers: List[Union[str, OntologyClassId]] = empty_list()
    publications: List[Union[str, PublicationId]] = empty_list()

    def _fix_elements(self):
        super()._fix_elements()
        if not isinstance(self.association_id, AssociationAssociationId):
            self.association_id = AssociationAssociationId(self.association_id)
        if not isinstance(self.subject, NamedThingId):
            self.subject = NamedThingId(self.subject)
        if not isinstance(self.object, NamedThingId):
            self.object = NamedThingId(self.object)
        if self.edge_label and not isinstance(self.edge_label, LabelType):
            self.edge_label = LabelType(self.edge_label)
        if not isinstance(self.relation, RelationshipTypeId):
            self.relation = RelationshipTypeId(self.relation)
        if self.has_confidence_level and not isinstance(self.has_confidence_level, ConfidenceLevelId):
            self.has_confidence_level = ConfidenceLevelId(self.has_confidence_level)
        if self.has_evidence and not isinstance(self.has_evidence, EvidenceTypeId):
            self.has_evidence = EvidenceTypeId(self.has_evidence)
        if self.provided_by and not isinstance(self.provided_by, ProviderId):
            self.provided_by = ProviderId(self.provided_by)
        if self.association_type and not isinstance(self.association_type, OntologyClassId):
            self.association_type = OntologyClassId(self.association_type)
        self.qualifiers = [v if isinstance(v, OntologyClassId)
                           else OntologyClassId(v) for v in self.qualifiers]
        self.publications = [v if isinstance(v, PublicationId)
                             else PublicationId(v) for v in self.publications]


@dataclass
class ConfidenceLevel(InformationContentEntity):
    """
    Level of confidence in a statement
    """

    # === thing ===
    related_to: Optional[Union[dict, Thing]] = None
    iri: Optional[Union[str, UriType]] = None
    name: Optional[Union[str, LabelType]] = None
    category: List[Union[dict, Thing]] = empty_list()
    full_name: Optional[Union[str, LabelType]] = None
    description: Optional[Union[str, NarrativeText]] = None
    creation_date: Optional[Union[str, XSDDateTime]] = None
    update_date: Optional[Union[str, XSDDateTime]] = None
    aggregate_statistic: Optional[str] = None
    timepoint: Optional[Union[str, TimeType]] = None

    # === named thing ===
    id: Union[str, ConfidenceLevelId] = None

    # === information content entity ===

    # === confidence level ===

    def _fix_elements(self):
        super()._fix_elements()
        if self.id and not isinstance(self.id, ConfidenceLevelId):
            self.id = ConfidenceLevelId(self.id)


@dataclass
class EvidenceType(InformationContentEntity):
    """
    Class of evidence that supports an association
    """

    # === thing ===
    related_to: Optional[Union[dict, Thing]] = None
    iri: Optional[Union[str, UriType]] = None
    name: Optional[Union[str, LabelType]] = None
    category: List[Union[dict, Thing]] = empty_list()
    full_name: Optional[Union[str, LabelType]] = None
    description: Optional[Union[str, NarrativeText]] = None
    creation_date: Optional[Union[str, XSDDateTime]] = None
    update_date: Optional[Union[str, XSDDateTime]] = None
    aggregate_statistic: Optional[str] = None
    timepoint: Optional[Union[str, TimeType]] = None

    # === named thing ===
    id: Union[str, EvidenceTypeId] = None

    # === information content entity ===

    # === evidence type ===

    def _fix_elements(self):
        super()._fix_elements()
        if self.id and not isinstance(self.id, EvidenceTypeId):
            self.id = EvidenceTypeId(self.id)

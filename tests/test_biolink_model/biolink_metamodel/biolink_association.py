# Auto generated from biolink_association.yaml by pythongen.py version: 0.1.0
# Generation date: 2019-02-04 15:26
# Schema: biolink association
#
# id: http://w3id.org/biolink/biolink-model/association
# description: Reified association model for life-sciences data
# license: https://creativecommons.org/publicdomain/zero/1.0/

from dataclasses import dataclass
from datetime import time, date
from typing import Optional, List, Union

from biolinkml.utils.metamodelcore import Bool, URIorCURIE
from biolinkml.utils.metamodelcore import empty_list
from biolinkml.utils.yamlutils import YAMLRoot
from tests.test_biolink_model.biolink_metamodel import biolink_named_thing
from tests.test_biolink_model.biolink_metamodel.includes import biolink_types

metamodel_version = "None"

inherited_slots: List[str] = []


# Types


# Class references
class AssociationAssociationId(biolink_types.IdentifierType):
    pass


class ConfidenceLevelId(biolink_named_thing.InformationContentEntityId):
    pass


class EvidenceTypeId(biolink_named_thing.InformationContentEntityId):
    pass


@dataclass
class Association(YAMLRoot):
    """
    A typed association between two entities, supported by evidence
    """

    # === association ===
    association_id: Union[URIorCURIE, AssociationAssociationId]
    subject: Union[dict, biolink_named_thing.NamedThingId]
    object: Union[dict, biolink_named_thing.NamedThingId]
    relation: Union[dict, biolink_named_thing.RelationshipTypeId]
    association_slot: Optional[str] = None
    edge_label: Optional[Union[str, biolink_types.LabelType]] = None
    negated: Optional[Bool] = None
    has_confidence_level: Optional[Union[dict, ConfidenceLevelId]] = None
    has_evidence: Optional[Union[dict, EvidenceTypeId]] = None
    provided_by: Optional[Union[dict, biolink_named_thing.ProviderId]] = None
    association_type: Optional[Union[dict, biolink_named_thing.OntologyClassId]] = None
    qualifiers: List[Union[dict, biolink_named_thing.OntologyClassId]] = empty_list()
    publications: List[Union[dict, biolink_named_thing.PublicationId]] = empty_list()

    def _fix_elements(self):
        super()._fix_elements()
        if not isinstance(self.association_id, AssociationAssociationId):
            self.association_id = AssociationAssociationId(self.association_id)
        if not isinstance(self.subject, biolink_named_thing.NamedThingId):
            self.subject = biolink_named_thing.NamedThingId(self.subject)
        if not isinstance(self.object, biolink_named_thing.NamedThingId):
            self.object = biolink_named_thing.NamedThingId(self.object)
        if self.edge_label and not isinstance(self.edge_label, biolink_types.LabelType):
            self.edge_label = biolink_types.LabelType(self.edge_label)
        if not isinstance(self.relation, biolink_named_thing.RelationshipTypeId):
            self.relation = biolink_named_thing.RelationshipTypeId(self.relation)
        if self.has_confidence_level and not isinstance(self.has_confidence_level, ConfidenceLevelId):
            self.has_confidence_level = ConfidenceLevelId(self.has_confidence_level)
        if self.has_evidence and not isinstance(self.has_evidence, EvidenceTypeId):
            self.has_evidence = EvidenceTypeId(self.has_evidence)
        if self.provided_by and not isinstance(self.provided_by, biolink_named_thing.ProviderId):
            self.provided_by = biolink_named_thing.ProviderId(self.provided_by)
        if self.association_type and not isinstance(self.association_type, biolink_named_thing.OntologyClassId):
            self.association_type = biolink_named_thing.OntologyClassId(self.association_type)
        self.qualifiers = [v if isinstance(v, biolink_named_thing.OntologyClassId)
                           else biolink_named_thing.OntologyClassId(v) for v in self.qualifiers]
        self.publications = [v if isinstance(v, biolink_named_thing.PublicationId)
                             else biolink_named_thing.PublicationId(v) for v in self.publications]


@dataclass
class ConfidenceLevel(biolink_named_thing.InformationContentEntity):
    """
    Level of confidence in a statement
    """

    # === thing ===
    related_to: Optional[Union[dict, "Thing"]] = None
    iri: Optional[Union[URIorCURIE, biolink_types.UriType]] = None
    name: Optional[Union[str, biolink_types.LabelType]] = None
    category: List[Union[dict, "Thing"]] = empty_list()
    full_name: Optional[Union[str, biolink_types.LabelType]] = None
    description: Optional[Union[str, biolink_types.NarrativeText]] = None
    creation_date: Optional[date] = None
    update_date: Optional[date] = None
    aggregate_statistic: Optional[str] = None
    timepoint: Optional[Union[time, biolink_types.TimeType]] = None

    # === named thing ===
    id: Union[dict, ConfidenceLevelId] = None

    # === information content entity ===

    # === confidence level ===

    def _fix_elements(self):
        super()._fix_elements()
        if self.id and not isinstance(self.id, ConfidenceLevelId):
            self.id = ConfidenceLevelId(self.id)


@dataclass
class EvidenceType(biolink_named_thing.InformationContentEntity):
    """
    Class of evidence that supports an association
    """

    # === thing ===
    related_to: Optional[Union[dict, "Thing"]] = None
    iri: Optional[Union[URIorCURIE, biolink_types.UriType]] = None
    name: Optional[Union[str, biolink_types.LabelType]] = None
    category: List[Union[dict, "Thing"]] = empty_list()
    full_name: Optional[Union[str, biolink_types.LabelType]] = None
    description: Optional[Union[str, biolink_types.NarrativeText]] = None
    creation_date: Optional[date] = None
    update_date: Optional[date] = None
    aggregate_statistic: Optional[str] = None
    timepoint: Optional[Union[time, biolink_types.TimeType]] = None

    # === named thing ===
    id: Union[dict, EvidenceTypeId] = None

    # === information content entity ===

    # === evidence type ===

    def _fix_elements(self):
        super()._fix_elements()
        if self.id and not isinstance(self.id, EvidenceTypeId):
            self.id = EvidenceTypeId(self.id)


@dataclass
class Thing(YAMLRoot):
    """
    Top level class for both associations and named things
    """

    # === thing ===
    related_to: Optional[Union[dict, "Thing"]] = None
    iri: Optional[Union[URIorCURIE, biolink_types.UriType]] = None
    name: Optional[Union[str, biolink_types.LabelType]] = None
    category: List[Union[dict, "Thing"]] = empty_list()
    full_name: Optional[Union[str, biolink_types.LabelType]] = None
    description: Optional[Union[str, biolink_types.NarrativeText]] = None
    creation_date: Optional[date] = None
    update_date: Optional[date] = None
    aggregate_statistic: Optional[str] = None
    timepoint: Optional[Union[time, biolink_types.TimeType]] = None

    def _fix_elements(self):
        super()._fix_elements()
        if self.related_to and not isinstance(self.related_to, Thing):
            self.related_to = Thing(**self.related_to)
        if self.iri and not isinstance(self.iri, biolink_types.UriType):
            self.iri = biolink_types.UriType(self.iri)
        if self.name and not isinstance(self.name, biolink_types.LabelType):
            self.name = biolink_types.LabelType(self.name)
        self.category = [v if isinstance(v, Thing)
                         else Thing(**v) for v in self.category]
        if self.full_name and not isinstance(self.full_name, biolink_types.LabelType):
            self.full_name = biolink_types.LabelType(self.full_name)
        if self.description and not isinstance(self.description, biolink_types.NarrativeText):
            self.description = biolink_types.NarrativeText(self.description)
        if self.timepoint and not isinstance(self.timepoint, biolink_types.TimeType):
            self.timepoint = biolink_types.TimeType(self.timepoint)


@dataclass
class NamedThing(Thing):
    """
    a databased entity or concept/class
    """

    # === thing ===
    related_to: Optional[Union[dict, Thing]] = None
    iri: Optional[Union[URIorCURIE, biolink_types.UriType]] = None
    name: Optional[Union[str, biolink_types.LabelType]] = None
    category: List[Union[dict, Thing]] = empty_list()
    full_name: Optional[Union[str, biolink_types.LabelType]] = None
    description: Optional[Union[str, biolink_types.NarrativeText]] = None
    creation_date: Optional[date] = None
    update_date: Optional[date] = None
    aggregate_statistic: Optional[str] = None
    timepoint: Optional[Union[time, biolink_types.TimeType]] = None

    # === named thing ===
    id: Union[dict, biolink_named_thing.NamedThingId] = None

    def _fix_elements(self):
        super()._fix_elements()
        if self.id and not isinstance(self.id, biolink_named_thing.NamedThingId):
            self.id = biolink_named_thing.NamedThingId(self.id)


@dataclass
class InformationContentEntity(NamedThing):
    """
    a piece of information that typically describes some piece of biology or is used as support.
    """

    # === thing ===
    related_to: Optional[Union[dict, Thing]] = None
    iri: Optional[Union[URIorCURIE, biolink_types.UriType]] = None
    name: Optional[Union[str, biolink_types.LabelType]] = None
    category: List[Union[dict, Thing]] = empty_list()
    full_name: Optional[Union[str, biolink_types.LabelType]] = None
    description: Optional[Union[str, biolink_types.NarrativeText]] = None
    creation_date: Optional[date] = None
    update_date: Optional[date] = None
    aggregate_statistic: Optional[str] = None
    timepoint: Optional[Union[time, biolink_types.TimeType]] = None

    # === named thing ===
    id: Union[dict, biolink_named_thing.InformationContentEntityId] = None

    # === information content entity ===


@dataclass
class Publication(InformationContentEntity):
    """
    Any published piece of information. Can refer to a whole publication, or to a part of it (e.g. a figure, figure
    legend, or section highlighted by NLP). The scope is intended to be general and include information published on
    the web as well as journals.
    """

    # === thing ===
    related_to: Optional[Union[dict, Thing]] = None
    iri: Optional[Union[URIorCURIE, biolink_types.UriType]] = None
    name: Optional[Union[str, biolink_types.LabelType]] = None
    category: List[Union[dict, Thing]] = empty_list()
    full_name: Optional[Union[str, biolink_types.LabelType]] = None
    description: Optional[Union[str, biolink_types.NarrativeText]] = None
    creation_date: Optional[date] = None
    update_date: Optional[date] = None
    aggregate_statistic: Optional[str] = None
    timepoint: Optional[Union[time, biolink_types.TimeType]] = None

    # === named thing ===
    id: Union[dict, biolink_named_thing.PublicationId] = None

    # === information content entity ===

    # === publication ===

    def _fix_elements(self):
        super()._fix_elements()
        if self.id and not isinstance(self.id, biolink_named_thing.PublicationId):
            self.id = biolink_named_thing.PublicationId(self.id)


@dataclass
class OntologyClass(NamedThing):
    """
    a concept or class in an ontology, vocabulary or thesaurus
    """

    # === thing ===
    related_to: Optional[Union[dict, Thing]] = None
    iri: Optional[Union[URIorCURIE, biolink_types.UriType]] = None
    name: Optional[Union[str, biolink_types.LabelType]] = None
    category: List[Union[dict, Thing]] = empty_list()
    full_name: Optional[Union[str, biolink_types.LabelType]] = None
    description: Optional[Union[str, biolink_types.NarrativeText]] = None
    creation_date: Optional[date] = None
    update_date: Optional[date] = None
    aggregate_statistic: Optional[str] = None
    timepoint: Optional[Union[time, biolink_types.TimeType]] = None

    # === named thing ===
    id: Union[dict, biolink_named_thing.OntologyClassId] = None

    # === ontology class ===

    def _fix_elements(self):
        super()._fix_elements()
        if self.id and not isinstance(self.id, biolink_named_thing.OntologyClassId):
            self.id = biolink_named_thing.OntologyClassId(self.id)


@dataclass
class RelationshipType(OntologyClass):
    """
    An OWL property used as an edge label
    """

    # === thing ===
    related_to: Optional[Union[dict, Thing]] = None
    iri: Optional[Union[URIorCURIE, biolink_types.UriType]] = None
    name: Optional[Union[str, biolink_types.LabelType]] = None
    category: List[Union[dict, Thing]] = empty_list()
    full_name: Optional[Union[str, biolink_types.LabelType]] = None
    description: Optional[Union[str, biolink_types.NarrativeText]] = None
    creation_date: Optional[date] = None
    update_date: Optional[date] = None
    aggregate_statistic: Optional[str] = None
    timepoint: Optional[Union[time, biolink_types.TimeType]] = None

    # === named thing ===
    id: Union[dict, biolink_named_thing.RelationshipTypeId] = None

    # === ontology class ===

    # === relationship type ===

    def _fix_elements(self):
        super()._fix_elements()
        if self.id and not isinstance(self.id, biolink_named_thing.RelationshipTypeId):
            self.id = biolink_named_thing.RelationshipTypeId(self.id)


@dataclass
class AdministrativeEntity(NamedThing):

    # === thing ===
    related_to: Optional[Union[dict, Thing]] = None
    iri: Optional[Union[URIorCURIE, biolink_types.UriType]] = None
    name: Optional[Union[str, biolink_types.LabelType]] = None
    category: List[Union[dict, Thing]] = empty_list()
    full_name: Optional[Union[str, biolink_types.LabelType]] = None
    description: Optional[Union[str, biolink_types.NarrativeText]] = None
    creation_date: Optional[date] = None
    update_date: Optional[date] = None
    aggregate_statistic: Optional[str] = None
    timepoint: Optional[Union[time, biolink_types.TimeType]] = None

    # === named thing ===
    id: Union[dict, biolink_named_thing.AdministrativeEntityId] = None

    # === administrative entity ===


@dataclass
class Provider(AdministrativeEntity):
    """
    person, group, organization or project that provides a piece of information
    """

    # === thing ===
    related_to: Optional[Union[dict, Thing]] = None
    iri: Optional[Union[URIorCURIE, biolink_types.UriType]] = None
    name: Optional[Union[str, biolink_types.LabelType]] = None
    category: List[Union[dict, Thing]] = empty_list()
    full_name: Optional[Union[str, biolink_types.LabelType]] = None
    description: Optional[Union[str, biolink_types.NarrativeText]] = None
    creation_date: Optional[date] = None
    update_date: Optional[date] = None
    aggregate_statistic: Optional[str] = None
    timepoint: Optional[Union[time, biolink_types.TimeType]] = None

    # === named thing ===
    id: Union[dict, biolink_named_thing.ProviderId] = None

    # === administrative entity ===

    # === provider ===

    def _fix_elements(self):
        super()._fix_elements()
        if self.id and not isinstance(self.id, biolink_named_thing.ProviderId):
            self.id = biolink_named_thing.ProviderId(self.id)

# Auto generated from biolink_named_thing.yaml by pythongen.py version: 0.1.0
# Generation date: 2019-02-03 14:34
# Schema: biolink named thing
#
# id: http://w3id.org/biolink/biolink-model/named-thing
# description: Basic entity for taxonomy and data model for life-sciences data
# license: https://creativecommons.org/publicdomain/zero/1.0/

from dataclasses import dataclass
from datetime import date, time
from typing import Optional, List, Union

from biolinkml.utils.metamodelcore import URIorCURIE
from biolinkml.utils.metamodelcore import empty_list
from biolinkml.utils.yamlutils import YAMLRoot
from tests.test_biolink_model.biolink_metamodel.includes.biolink_types import IdentifierType, UriType, LabelType, \
    NarrativeText, TimeType

metamodel_version = "None"

inherited_slots: List[str] = []


# Types

# Class references
class NamedThingId(IdentifierType):
    pass


class InformationContentEntityId(NamedThingId):
    pass


class PublicationId(InformationContentEntityId):
    pass


class OntologyClassId(NamedThingId):
    pass


class RelationshipTypeId(OntologyClassId):
    pass


class AdministrativeEntityId(NamedThingId):
    pass


class ProviderId(AdministrativeEntityId):
    pass


@dataclass
class Thing(YAMLRoot):
    """
    Top level class for both associations and named things
    """

    # === thing ===
    related_to: Optional[Union[dict, "Thing"]] = None
    iri: Optional[Union[URIorCURIE,  UriType]] = None
    name: Optional[Union[str, LabelType]] = None
    category: List[Union[dict, "Thing"]] = empty_list()
    full_name: Optional[Union[str, LabelType]] = None
    description: Optional[Union[str, NarrativeText]] = None
    creation_date: Optional[date] = None
    update_date: Optional[date] = None
    aggregate_statistic: Optional[str] = None
    timepoint: Optional[Union[time, TimeType]] = None

    def _fix_elements(self):
        super()._fix_elements()
        if self.related_to and not isinstance(self.related_to, Thing):
            self.related_to = Thing(**self.related_to)
        if self.iri and not isinstance(self.iri,  UriType):
            self.iri = UriType(self.iri)
        if self.name and not isinstance(self.name, LabelType):
            self.name = LabelType(self.name)
        self.category = [v if isinstance(v, Thing)
                         else Thing(**v) for v in self.category]
        if self.full_name and not isinstance(self.full_name, LabelType):
            self.full_name = LabelType(self.full_name)
        if self.description and not isinstance(self.description, NarrativeText):
            self.description = NarrativeText(self.description)
        if self.timepoint and not isinstance(self.timepoint, TimeType):
            self.timepoint = TimeType(self.timepoint)


@dataclass
class NamedThing(Thing):
    """
    a databased entity or concept/class
    """

    # === thing ===
    related_to: Optional[Union[dict, Thing]] = None
    iri: Optional[Union[URIorCURIE,  UriType]] = None
    name: Optional[Union[str, LabelType]] = None
    category: List[Union[dict, Thing]] = empty_list()
    full_name: Optional[Union[str, LabelType]] = None
    description: Optional[Union[str, NarrativeText]] = None
    creation_date: Optional[date] = None
    update_date: Optional[date] = None
    aggregate_statistic: Optional[str] = None
    timepoint: Optional[Union[time, TimeType]] = None

    # === named thing ===
    id: Union[dict, NamedThingId] = None

    def _fix_elements(self):
        super()._fix_elements()
        if self.id and not isinstance(self.id, NamedThingId):
            self.id = NamedThingId(self.id)


@dataclass
class InformationContentEntity(NamedThing):
    """
    a piece of information that typically describes some piece of biology or is used as support.
    """

    # === thing ===
    related_to: Optional[Union[dict, Thing]] = None
    iri: Optional[Union[URIorCURIE,  UriType]] = None
    name: Optional[Union[str, LabelType]] = None
    category: List[Union[dict, Thing]] = empty_list()
    full_name: Optional[Union[str, LabelType]] = None
    description: Optional[Union[str, NarrativeText]] = None
    creation_date: Optional[date] = None
    update_date: Optional[date] = None
    aggregate_statistic: Optional[str] = None
    timepoint: Optional[Union[time, TimeType]] = None

    # === named thing ===
    id: Union[dict, InformationContentEntityId] = None

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
    iri: Optional[Union[URIorCURIE,  UriType]] = None
    name: Optional[Union[str, LabelType]] = None
    category: List[Union[dict, Thing]] = empty_list()
    full_name: Optional[Union[str, LabelType]] = None
    description: Optional[Union[str, NarrativeText]] = None
    creation_date: Optional[date] = None
    update_date: Optional[date] = None
    aggregate_statistic: Optional[str] = None
    timepoint: Optional[Union[time, TimeType]] = None

    # === named thing ===
    id: Union[dict, PublicationId] = None

    # === information content entity ===

    # === publication ===

    def _fix_elements(self):
        super()._fix_elements()
        if self.id and not isinstance(self.id, PublicationId):
            self.id = PublicationId(self.id)


@dataclass
class OntologyClass(NamedThing):
    """
    a concept or class in an ontology, vocabulary or thesaurus
    """

    # === thing ===
    related_to: Optional[Union[dict, Thing]] = None
    iri: Optional[Union[URIorCURIE,  UriType]] = None
    name: Optional[Union[str, LabelType]] = None
    category: List[Union[dict, Thing]] = empty_list()
    full_name: Optional[Union[str, LabelType]] = None
    description: Optional[Union[str, NarrativeText]] = None
    creation_date: Optional[date] = None
    update_date: Optional[date] = None
    aggregate_statistic: Optional[str] = None
    timepoint: Optional[Union[time, TimeType]] = None

    # === named thing ===
    id: Union[dict, OntologyClassId] = None

    # === ontology class ===

    def _fix_elements(self):
        super()._fix_elements()
        if self.id and not isinstance(self.id, OntologyClassId):
            self.id = OntologyClassId(self.id)


@dataclass
class RelationshipType(OntologyClass):
    """
    An OWL property used as an edge label
    """

    # === thing ===
    related_to: Optional[Union[dict, Thing]] = None
    iri: Optional[Union[URIorCURIE,  UriType]] = None
    name: Optional[Union[str, LabelType]] = None
    category: List[Union[dict, Thing]] = empty_list()
    full_name: Optional[Union[str, LabelType]] = None
    description: Optional[Union[str, NarrativeText]] = None
    creation_date: Optional[date] = None
    update_date: Optional[date] = None
    aggregate_statistic: Optional[str] = None
    timepoint: Optional[Union[time, TimeType]] = None

    # === named thing ===
    id: Union[dict, RelationshipTypeId] = None

    # === ontology class ===

    # === relationship type ===

    def _fix_elements(self):
        super()._fix_elements()
        if self.id and not isinstance(self.id, RelationshipTypeId):
            self.id = RelationshipTypeId(self.id)


@dataclass
class AdministrativeEntity(NamedThing):

    # === thing ===
    related_to: Optional[Union[dict, Thing]] = None
    iri: Optional[Union[URIorCURIE,  UriType]] = None
    name: Optional[Union[str, LabelType]] = None
    category: List[Union[dict, Thing]] = empty_list()
    full_name: Optional[Union[str, LabelType]] = None
    description: Optional[Union[str, NarrativeText]] = None
    creation_date: Optional[date] = None
    update_date: Optional[date] = None
    aggregate_statistic: Optional[str] = None
    timepoint: Optional[Union[time, TimeType]] = None

    # === named thing ===
    id: Union[dict, AdministrativeEntityId] = None

    # === administrative entity ===


@dataclass
class Provider(AdministrativeEntity):
    """
    person, group, organization or project that provides a piece of information
    """

    # === thing ===
    related_to: Optional[Union[dict, Thing]] = None
    iri: Optional[Union[URIorCURIE,  UriType]] = None
    name: Optional[Union[str, LabelType]] = None
    category: List[Union[dict, Thing]] = empty_list()
    full_name: Optional[Union[str, LabelType]] = None
    description: Optional[Union[str, NarrativeText]] = None
    creation_date: Optional[date] = None
    update_date: Optional[date] = None
    aggregate_statistic: Optional[str] = None
    timepoint: Optional[Union[time, TimeType]] = None

    # === named thing ===
    id: Union[dict, ProviderId] = None

    # === administrative entity ===

    # === provider ===

    def _fix_elements(self):
        super()._fix_elements()
        if self.id and not isinstance(self.id, ProviderId):
            self.id = ProviderId(self.id)

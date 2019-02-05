# Auto generated from biolink_metamodel.yaml by pythongen.py version: 0.1.0
# Generation date: 2019-02-04 15:35
# Schema: biolink model
#
# id: http://w3id.org/biolink/biolink-model/model
# description: Model of a container for life sciences data
# license: https://creativecommons.org/publicdomain/zero/1.0/

from dataclasses import dataclass
from datetime import time, date
from typing import Optional, List, Union, Dict

from biolinkml.utils.metamodelcore import URIorCURIE, NCName
from biolinkml.utils.metamodelcore import empty_list, empty_dict
from biolinkml.utils.yamlutils import YAMLRoot
from tests.test_biolink_model.biolink_metamodel import biolink_named_thing
from tests.test_biolink_model.biolink_metamodel.biolink_named_thing import NamedThingId

metamodel_version = "None"

inherited_slots: List[str] = []


# Types

# Class references
class PrefixLocalName(NCName):
    pass


class ModelId(NamedThingId):
    pass


@dataclass
class Prefix(YAMLRoot):
    """
    prefix URI tuple
    """

    # === prefix ===
    local_name: Union[NCName, PrefixLocalName]
    prefix_uri: URIorCURIE

    def _fix_elements(self):
        super()._fix_elements()
        if not isinstance(self.local_name, PrefixLocalName):
            self.local_name = PrefixLocalName(self.local_name)


@dataclass
class Model(biolink_named_thing.NamedThing):

    # === thing ===
    related_to: Optional[Union[dict, biolink_named_thing.Thing]] = None
    iri: Optional[Union[URIorCURIE, biolink_named_thing.UriType]] = None
    name: Optional[Union[str, biolink_named_thing.LabelType]] = None
    category: List[Union[dict, biolink_named_thing.Thing]] = empty_list()
    full_name: Optional[Union[str, biolink_named_thing.LabelType]] = None
    description: Optional[Union[str, biolink_named_thing.NarrativeText]] = None
    creation_date: Optional[date] = None
    update_date: Optional[date] = None
    aggregate_statistic: Optional[str] = None
    timepoint: Optional[Union[time, biolink_named_thing.TimeType]] = None

    # === named thing ===
    id: Union[dict, ModelId] = None

    # === model ===
    license: Optional[str] = None
    prefixes: Union[dict, Prefix] = empty_dict()
    default_curi_maps: List[str] = empty_list()
    default_prefix: Optional[str] = None
    biolink_named_thing.providers: Dict[Union[dict, biolink_named_thing.ProviderId], Union[dict, biolink_named_thing.Provider]] = empty_dict()
    relationship_types: Dict[Union[dict, biolink_named_thing.RelationshipTypeId], Union[dict, biolink_named_thing.RelationshipType]] = empty_dict()
    biolink_named_thing.associations: Dict[Union[URIorCURIE, biolink_named_thing.AssociationAssociationId], Union[dict, biolink_named_thing.Association]] = empty_dict()
    ontology_classes: Dict[Union[dict, biolink_named_thing.OntologyClassId], Union[dict, biolink_named_thing.OntologyClassf]] = empty_dict()

    def _fix_elements(self):
        super()._fix_elements()
        if self.id and not isinstance(self.id, ModelId):
            self.id = ModelId(self.id)
        for k, v in self.prefixes.items():
            if not isinstance(v, Prefix):
                self.prefixes[k] = Prefix(k, v)
        for k, v in self.providers.items():
            if not isinstance(v, biolink_named_thing.Provider):
                self.providers[k] = biolink_named_thing.Provider(id=k, **({} if v is None else v))
        for k, v in self.relationship_types.items():
            if not isinstance(v, biolink_named_thing.RelationshipType):
                self.relationship_types[k] = biolink_named_thing.RelationshipType(id=k, **({} if v is None else v))
        for k, v in self.associations.items():
            if not isinstance(v, biolink_named_thing.Association):
                self.associations[k] = biolink_named_thing.Association(association_id=k, **({} if v is None else v))
        for k, v in self.ontology_classes.items():
            if not isinstance(v, biolink_named_thing.OntologyClass):
                self.ontology_classes[k] = biolink_named_thing.OntologyClass(id=k, **({} if v is None else v))

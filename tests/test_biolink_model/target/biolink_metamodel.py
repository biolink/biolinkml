# Auto generated from biolink_metamodel.yaml by pythongen.py version: 0.2.0
# Generation date: 2019-02-05 16:34
# Schema: biolink model
#
# id: http://w3id.org/biolink/biolink-model/model
# description: Model of a container for life sciences data
# license: https://creativecommons.org/publicdomain/zero/1.0/

from typing import Optional, List, Union, Dict
from dataclasses import dataclass
from biolinkml.utils.metamodelcore import empty_list, empty_dict
from biolinkml.utils.yamlutils import YAMLRoot
from tests.test_biolink_model.biolink_metamodel.biolink_association  import Association, AssociationAssociationId
from tests.test_biolink_model.biolink_metamodel.biolink_named_thing import NamedThing, NamedThingId, OntologyClass, OntologyClassId, Provider, ProviderId, RelationshipType, RelationshipTypeId, Thing
from tests.test_biolink_model.biolink_metamodel.includes.biolink_types import IdentifierType, LabelType, NarrativeText, TimeType, UriType
from biolinkml.utils.metamodelcore import NCName, URIorCURIE, XSDDateTime
from includes.types import Date, Ncname, String, Time, Uri

metamodel_version = "1.0.1"

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
    local_name: Union[str, PrefixLocalName]
    prefix_uri: Union[str, URIorCURIE]

    def _fix_elements(self):
        super()._fix_elements()
        if not isinstance(self.local_name, PrefixLocalName):
            self.local_name = PrefixLocalName(self.local_name)
        if not isinstance(self.prefix_uri, URIorCURIE):
            self.prefix_uri = URIorCURIE(self.prefix_uri)


@dataclass
class Model(NamedThing):

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
    id: Union[str, ModelId] = None

    # === model ===
    license: Optional[str] = None
    prefixes: Union[dict, Prefix] = empty_dict()
    default_curi_maps: List[str] = empty_list()
    default_prefix: Optional[str] = None
    providers: Dict[Union[str, ProviderId], Union[dict, Provider]] = empty_dict()
    relationship_types: Dict[Union[str, RelationshipTypeId], Union[dict, RelationshipType]] = empty_dict()
    associations: Dict[Union[str, AssociationAssociationId], Union[dict, Association]] = empty_dict()
    ontology_classes: Dict[Union[str, OntologyClassId], Union[dict, OntologyClass]] = empty_dict()

    def _fix_elements(self):
        super()._fix_elements()
        if self.id and not isinstance(self.id, ModelId):
            self.id = ModelId(self.id)
        for k, v in self.prefixes.items():
            if not isinstance(v, Prefix):
                self.prefixes[k] = Prefix(k, v)
        for k, v in self.providers.items():
            if not isinstance(v, Provider):
                self.providers[k] = Provider(id=k, **({} if v is None else v))
        for k, v in self.relationship_types.items():
            if not isinstance(v, RelationshipType):
                self.relationship_types[k] = RelationshipType(id=k, **({} if v is None else v))
        for k, v in self.associations.items():
            if not isinstance(v, Association):
                self.associations[k] = Association(association_id=k, **({} if v is None else v))
        for k, v in self.ontology_classes.items():
            if not isinstance(v, OntologyClass):
                self.ontology_classes[k] = OntologyClass(id=k, **({} if v is None else v))

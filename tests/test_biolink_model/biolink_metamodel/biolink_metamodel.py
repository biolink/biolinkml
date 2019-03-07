# Auto generated from biolink_metamodel.yaml by pythongen.py version: 0.2.0
# Generation date: 2019-02-12 13:58
# Schema: biolink model
#
# id: http://w3id.org/biolink/biolink-model/model
# description: Model of a container for life sciences data
# license: https://creativecommons.org/publicdomain/zero/1.0/

from typing import Optional, List, Union, Dict
from dataclasses import dataclass
from biolinkml.utils.metamodelcore import empty_list, empty_dict
from biolinkml.utils.yamlutils import YAMLRoot
from tests.test_biolink_model.biolink_metamodel.biolink_association  import Association, AssociationAssociationId, EvidenceType, EvidenceTypeId, Publication, PublicationId
from tests.test_biolink_model.biolink_metamodel.biolink_named_thing import AltDescription, Example, NamedThing, NamedThingId, NodeType, NodeTypeId, Provider, ProviderId, RelationshipType, RelationshipTypeId, SubsetDefinition, SubsetDefinitionId, TypeDefinition, TypeDefinitionId, ValuesetDefinition, ValuesetDefinitionId
from tests.test_biolink_model.biolink_metamodel.includes.biolink_types import BooleanType, FileName, IdentifierType, LabelType, NarrativeText, UriType
from biolinkml.utils.metamodelcore import Bool, NCName, URIorCURIE, XSDDate
from includes.types import Boolean, Datetime, Ncname, String, Uri

metamodel_version = "1.0.2"

inherited_slots: List[str] = ["slots", "slot_class_range", "slot_relation_range", "definitional"]


# Types

# Class references
class ModelId(NamedThingId):
    pass


class PrefixLocalName(NCName):
    pass


@dataclass
class Model(NamedThing):

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
    id: Union[str, ModelId] = None
    category: List[Union[str, NamedThingId]] = empty_list()
    is_a: Optional[Union[str, NamedThingId]] = None
    mixins: List[Union[str, NamedThingId]] = empty_list()
    apply_to: List[Union[str, NamedThingId]] = empty_list()

    # === model ===
    license: Optional[str] = None
    prefixes: Union[dict, "Prefix"] = empty_dict()
    default_curi_maps: List[str] = empty_list()
    default_prefix: Optional[str] = None
    types: Dict[Union[str, TypeDefinitionId], Union[dict, TypeDefinition]] = empty_dict()
    subsets: Dict[Union[str, SubsetDefinitionId], Union[dict, SubsetDefinition]] = empty_dict()
    valuesets: Dict[Union[str, ValuesetDefinitionId], Union[dict, ValuesetDefinition]] = empty_dict()
    associations: Dict[Union[str, AssociationAssociationId], Union[dict, Association]] = empty_dict()
    nodes: Dict[Union[str, NodeTypeId], Union[dict, NodeType]] = empty_dict()
    relations: Dict[Union[str, RelationshipTypeId], Union[dict, RelationshipType]] = empty_dict()
    evidence: Dict[Union[str, EvidenceTypeId], Union[dict, EvidenceType]] = empty_dict()
    providers: Dict[Union[str, ProviderId], Union[dict, Provider]] = empty_dict()
    publications: Dict[Union[str, PublicationId], Union[dict, Publication]] = empty_dict()
    imports: List[Union[str, URIorCURIE]] = empty_list()

    def _fix_elements(self):
        super()._fix_elements()
        if not isinstance(self.id, ModelId):
            self.id = ModelId(self.id)
        for k, v in self.prefixes.items():
            if not isinstance(v, Prefix):
                self.prefixes[k] = Prefix(k, v)
        for k, v in self.types.items():
            if not isinstance(v, TypeDefinition):
                self.types[k] = TypeDefinition(id=k, **({} if v is None else v))
        for k, v in self.subsets.items():
            if not isinstance(v, SubsetDefinition):
                self.subsets[k] = SubsetDefinition(id=k, **({} if v is None else v))
        for k, v in self.valuesets.items():
            if not isinstance(v, ValuesetDefinition):
                self.valuesets[k] = ValuesetDefinition(id=k, **({} if v is None else v))
        for k, v in self.associations.items():
            if not isinstance(v, Association):
                self.associations[k] = Association(association_id=k, **({} if v is None else v))
        for k, v in self.nodes.items():
            if not isinstance(v, NodeType):
                self.nodes[k] = NodeType(id=k, **({} if v is None else v))
        for k, v in self.relations.items():
            if not isinstance(v, RelationshipType):
                self.relations[k] = RelationshipType(id=k, **({} if v is None else v))
        for k, v in self.evidence.items():
            if not isinstance(v, EvidenceType):
                self.evidence[k] = EvidenceType(id=k, **({} if v is None else v))
        for k, v in self.providers.items():
            if not isinstance(v, Provider):
                self.providers[k] = Provider(id=k, **({} if v is None else v))
        for k, v in self.publications.items():
            if not isinstance(v, Publication):
                self.publications[k] = Publication(id=k, **({} if v is None else v))
        self.imports = [v if isinstance(v, URIorCURIE)
                        else URIorCURIE(v) for v in self.imports]


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

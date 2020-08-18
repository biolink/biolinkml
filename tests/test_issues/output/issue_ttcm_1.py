# Auto generated from resourcedescription.yaml by pythongen.py version: 0.4.0
# Generation date: 2020-08-18 15:18
# Schema: resourcedescription
#
# id: https://hotecosystem.org/tccm/resourcedescription
# description: ResourceDescription represents the shared characteristics common to both abstract and resource
#              version descriptions. ResourceDescription is an abstract type and, as such, cannot be directly
#              created. Resource descriptions are Changeable, meaning that they have identity and can be created,
#              updated, and deleted.
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
from biolinkml.utils.metamodelcore import Bool, Curie, URIorCURIE, XSDDateTime
from datatypes import CURIE, DateAndTime, LocalIdentifier, URIorCurie
from includes.annotations import Annotation
from includes.extensions import Extension
from includes.types import Boolean, String
from references import CodeSystemReference, CodeSystemVersionReference, MapReference, MapVersionReference, NameAndMeaningReference, OntologyLanguageReference, OntologySyntaxReference, PredicateReference, RoleReference, SourceAndRoleReference
from uritypes import DocumentURI, ExternalURI, LocalURI, PersistentURI, RenderingURI

metamodel_version = "1.5.3"

# Overwrite dataclasses _init_fn to add **kwargs in __init__
dataclasses._init_fn = dataclasses_init_fn_with_kwargs

# Namespaces
BIOLINKML = CurieNamespace('biolinkml', 'https://w3id.org/biolink/biolinkml/')
TCCM = CurieNamespace('tccm', 'https://hotecosystem.org/tccm/')
DEFAULT_ = TCCM


# Types

# Class references



@dataclass
class ResourceDescription(YAMLRoot):
    """
    ResourceDescription represents the shared characteristics common to both abstract and resource version
    descriptions. ResourceDescription is an abstract type and, as such, cannot be directly created. Resource
    descriptions are Changeable, meaning that they have identity and can be created, updated, and deleted.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = TCCM.ResourceDescription
    class_class_curie: ClassVar[str] = "tccm:ResourceDescription"
    class_name: ClassVar[str] = "ResourceDescription"
    class_model_uri: ClassVar[URIRef] = TCCM.ResourceDescription

    about: Union[str, ExternalURI]
    resourceID: Union[str, LocalIdentifier]
    formalName: Optional[str] = None
    keyword: List[str] = empty_list()
    resourceSynopsis: Optional[str] = None
    additionalDocumentation: List[Union[str, PersistentURI]] = empty_list()
    rights: Optional[str] = None
    alternateID: Optional[str] = None
    extensions: List[Union[dict, Extension]] = empty_list()
    annotations: List[Union[dict, Annotation]] = empty_list()

    def __post_init__(self, **kwargs: Dict[str, Any]):
        if self.about is None:
            raise ValueError(f"about must be supplied")
        if not isinstance(self.about, ExternalURI):
            self.about = ExternalURI(self.about)
        if self.resourceID is None:
            raise ValueError(f"resourceID must be supplied")
        if not isinstance(self.resourceID, LocalIdentifier):
            self.resourceID = LocalIdentifier(self.resourceID)
        self.additionalDocumentation = [v if isinstance(v, PersistentURI)
                                        else PersistentURI(v) for v in ([self.additionalDocumentation] if isinstance(self.additionalDocumentation, str) else self.additionalDocumentation)]
        self.extensions = [Extension(*e) for e in self.extensions.items()] if isinstance(self.extensions, dict) \
                           else [v if isinstance(v, Extension) else Extension(**v)
                                 for v in ([self.extensions] if isinstance(self.extensions, str) else self.extensions)]
        self.annotations = [Annotation(*e) for e in self.annotations.items()] if isinstance(self.annotations, dict) \
                            else [v if isinstance(v, Annotation) else Annotation(**v)
                                  for v in ([self.annotations] if isinstance(self.annotations, str) else self.annotations)]
        super().__post_init__(**kwargs)


@dataclass
class SourceAndNotation(YAMLRoot):
    """
    Format and notation that some or all the releases (versions) of this resource are published in
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = TCCM.SourceAndNotation
    class_class_curie: ClassVar[str] = "tccm:SourceAndNotation"
    class_name: ClassVar[str] = "SourceAndNotation"
    class_model_uri: ClassVar[URIRef] = TCCM.SourceAndNotation

    sourceAndNotationDescription: Optional[str] = None
    sourceDocument: Optional[Union[str, PersistentURI]] = None
    sourceLanguage: Optional[Union[dict, OntologyLanguageReference]] = None
    sourceDocumentSyntax: Optional[Union[dict, OntologySyntaxReference]] = None

    def __post_init__(self, **kwargs: Dict[str, Any]):
        if self.sourceDocument is not None and not isinstance(self.sourceDocument, PersistentURI):
            self.sourceDocument = PersistentURI(self.sourceDocument)
        if self.sourceLanguage is not None and not isinstance(self.sourceLanguage, OntologyLanguageReference):
            self.sourceLanguage = OntologyLanguageReference(**self.sourceLanguage)
        if self.sourceDocumentSyntax is not None and not isinstance(self.sourceDocumentSyntax, OntologySyntaxReference):
            self.sourceDocumentSyntax = OntologySyntaxReference(**self.sourceDocumentSyntax)
        super().__post_init__(**kwargs)


@dataclass
class AbstractResourceDescription(ResourceDescription):
    """
    The description of the characteristics of a resource that are independent of the resource content.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = TCCM.AbstractResourceDescription
    class_class_curie: ClassVar[str] = "tccm:AbstractResourceDescription"
    class_name: ClassVar[str] = "AbstractResourceDescription"
    class_model_uri: ClassVar[URIRef] = TCCM.AbstractResourceDescription

    about: Union[str, ExternalURI] = None
    resourceID: Union[str, LocalIdentifier] = None
    releaseDocumentation: Optional[str] = None
    releaseFormat: List[Union[dict, SourceAndNotation]] = empty_list()

    def __post_init__(self, **kwargs: Dict[str, Any]):
        self.releaseFormat = [SourceAndNotation(*e) for e in self.releaseFormat.items()] if isinstance(self.releaseFormat, dict) \
                              else [v if isinstance(v, SourceAndNotation) else SourceAndNotation(**v)
                                    for v in ([self.releaseFormat] if isinstance(self.releaseFormat, str) else self.releaseFormat)]
        super().__post_init__(**kwargs)


@dataclass
class ResourceVersionDescription(ResourceDescription):
    """
    Information about the source, format, release date, version identifier, etc. of a specific version of an abstract
    resource.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = TCCM.ResourceVersionDescription
    class_class_curie: ClassVar[str] = "tccm:ResourceVersionDescription"
    class_name: ClassVar[str] = "ResourceVersionDescription"
    class_model_uri: ClassVar[URIRef] = TCCM.ResourceVersionDescription

    about: Union[str, ExternalURI] = None
    resourceID: Union[str, LocalIdentifier] = None
    documentURI: Optional[Union[str, DocumentURI]] = None
    sourceAndNotation: Optional[Union[dict, SourceAndNotation]] = None
    predecessor: Optional[Union[dict, NameAndMeaningReference]] = None
    officialResourceVersionID: Optional[str] = None
    officialReleaseDate: Optional[Union[str, XSDDateTime]] = None
    officialActivationDate: Optional[Union[str, XSDDateTime]] = None

    def __post_init__(self, **kwargs: Dict[str, Any]):
        if self.documentURI is not None and not isinstance(self.documentURI, DocumentURI):
            self.documentURI = DocumentURI(self.documentURI)
        if self.sourceAndNotation is not None and not isinstance(self.sourceAndNotation, SourceAndNotation):
            self.sourceAndNotation = SourceAndNotation(**self.sourceAndNotation)
        if self.predecessor is not None and not isinstance(self.predecessor, NameAndMeaningReference):
            self.predecessor = NameAndMeaningReference(**self.predecessor)
        if self.officialReleaseDate is not None and not isinstance(self.officialReleaseDate, XSDDateTime):
            self.officialReleaseDate = XSDDateTime(self.officialReleaseDate)
        if self.officialActivationDate is not None and not isinstance(self.officialActivationDate, XSDDateTime):
            self.officialActivationDate = XSDDateTime(self.officialActivationDate)
        super().__post_init__(**kwargs)



# Slots
class slots:
    pass

slots.about = Slot(uri=TCCM.about, name="about", curie=TCCM.curie('about'),
                      model_uri=TCCM.about, domain=None, range=Union[str, ExternalURI])

slots.resourceID = Slot(uri=TCCM.resourceID, name="resourceID", curie=TCCM.curie('resourceID'),
                      model_uri=TCCM.resourceID, domain=None, range=Union[str, LocalIdentifier])

slots.formalName = Slot(uri=TCCM.formalName, name="formalName", curie=TCCM.curie('formalName'),
                      model_uri=TCCM.formalName, domain=None, range=Optional[str])

slots.keyword = Slot(uri=TCCM.keyword, name="keyword", curie=TCCM.curie('keyword'),
                      model_uri=TCCM.keyword, domain=None, range=List[str])

slots.resourceSynopsis = Slot(uri=TCCM.resourceSynopsis, name="resourceSynopsis", curie=TCCM.curie('resourceSynopsis'),
                      model_uri=TCCM.resourceSynopsis, domain=None, range=Optional[str])

slots.additionalDocumentation = Slot(uri=TCCM.additionalDocumentation, name="additionalDocumentation", curie=TCCM.curie('additionalDocumentation'),
                      model_uri=TCCM.additionalDocumentation, domain=None, range=List[Union[str, PersistentURI]])

slots.rights = Slot(uri=TCCM.rights, name="rights", curie=TCCM.curie('rights'),
                      model_uri=TCCM.rights, domain=None, range=Optional[str])

slots.alternateID = Slot(uri=TCCM.alternateID, name="alternateID", curie=TCCM.curie('alternateID'),
                      model_uri=TCCM.alternateID, domain=None, range=Optional[str])

slots.sourceAndNotationDescription = Slot(uri=TCCM.sourceAndNotationDescription, name="sourceAndNotationDescription", curie=TCCM.curie('sourceAndNotationDescription'),
                      model_uri=TCCM.sourceAndNotationDescription, domain=None, range=Optional[str])

slots.sourceDocument = Slot(uri=TCCM.sourceDocument, name="sourceDocument", curie=TCCM.curie('sourceDocument'),
                      model_uri=TCCM.sourceDocument, domain=None, range=Optional[Union[str, PersistentURI]])

slots.sourceLanguage = Slot(uri=TCCM.sourceLanguage, name="sourceLanguage", curie=TCCM.curie('sourceLanguage'),
                      model_uri=TCCM.sourceLanguage, domain=None, range=Optional[Union[dict, OntologyLanguageReference]])

slots.sourceDocumentSyntax = Slot(uri=TCCM.sourceDocumentSyntax, name="sourceDocumentSyntax", curie=TCCM.curie('sourceDocumentSyntax'),
                      model_uri=TCCM.sourceDocumentSyntax, domain=None, range=Optional[Union[dict, OntologySyntaxReference]])

slots.releaseDocumentation = Slot(uri=TCCM.releaseDocumentation, name="releaseDocumentation", curie=TCCM.curie('releaseDocumentation'),
                      model_uri=TCCM.releaseDocumentation, domain=None, range=Optional[str])

slots.releaseFormat = Slot(uri=TCCM.releaseFormat, name="releaseFormat", curie=TCCM.curie('releaseFormat'),
                      model_uri=TCCM.releaseFormat, domain=None, range=List[Union[dict, SourceAndNotation]])

slots.documentURI = Slot(uri=TCCM.documentURI, name="documentURI", curie=TCCM.curie('documentURI'),
                      model_uri=TCCM.documentURI, domain=None, range=Optional[Union[str, DocumentURI]])

slots.sourceAndNotation = Slot(uri=TCCM.sourceAndNotation, name="sourceAndNotation", curie=TCCM.curie('sourceAndNotation'),
                      model_uri=TCCM.sourceAndNotation, domain=None, range=Optional[Union[dict, SourceAndNotation]])

slots.predecessor = Slot(uri=TCCM.predecessor, name="predecessor", curie=TCCM.curie('predecessor'),
                      model_uri=TCCM.predecessor, domain=None, range=Optional[Union[dict, NameAndMeaningReference]])

slots.officialResourceVersionID = Slot(uri=TCCM.officialResourceVersionID, name="officialResourceVersionID", curie=TCCM.curie('officialResourceVersionID'),
                      model_uri=TCCM.officialResourceVersionID, domain=None, range=Optional[str])

slots.officialReleaseDate = Slot(uri=TCCM.officialReleaseDate, name="officialReleaseDate", curie=TCCM.curie('officialReleaseDate'),
                      model_uri=TCCM.officialReleaseDate, domain=None, range=Optional[Union[str, XSDDateTime]])

slots.officialActivationDate = Slot(uri=TCCM.officialActivationDate, name="officialActivationDate", curie=TCCM.curie('officialActivationDate'),
                      model_uri=TCCM.officialActivationDate, domain=None, range=Optional[Union[str, XSDDateTime]])

slots.name = Slot(uri=TCCM.name, name="name", curie=TCCM.curie('name'),
                      model_uri=TCCM.name, domain=None, range=Union[str, LocalIdentifier])

slots.uri = Slot(uri=TCCM.uri, name="uri", curie=TCCM.curie('uri'),
                      model_uri=TCCM.uri, domain=None, range=Optional[Union[str, ExternalURI]])

slots.href = Slot(uri=TCCM.href, name="href", curie=TCCM.curie('href'),
                      model_uri=TCCM.href, domain=None, range=Optional[Union[str, RenderingURI]])

slots.codeSystem = Slot(uri=TCCM.codeSystem, name="codeSystem", curie=TCCM.curie('codeSystem'),
                      model_uri=TCCM.codeSystem, domain=None, range=Optional[Union[dict, CodeSystemReference]])

slots.map = Slot(uri=TCCM.map, name="map", curie=TCCM.curie('map'),
                      model_uri=TCCM.map, domain=None, range=Optional[Union[dict, MapReference]])

slots.designation = Slot(uri=TCCM.designation, name="designation", curie=TCCM.curie('designation'),
                      model_uri=TCCM.designation, domain=None, range=Optional[str])

slots.role = Slot(uri=TCCM.role, name="role", curie=TCCM.curie('role'),
                      model_uri=TCCM.role, domain=None, range=Optional[Union[dict, RoleReference]])

slots.ResourceDescription_about = Slot(uri=TCCM.about, name="ResourceDescription_about", curie=TCCM.curie('about'),
                      model_uri=TCCM.ResourceDescription_about, domain=ResourceDescription, range=Union[str, ExternalURI])

slots.ResourceDescription_resourceID = Slot(uri=TCCM.resourceID, name="ResourceDescription_resourceID", curie=TCCM.curie('resourceID'),
                      model_uri=TCCM.ResourceDescription_resourceID, domain=ResourceDescription, range=Union[str, LocalIdentifier])

slots.ResourceDescription_formalName = Slot(uri=TCCM.formalName, name="ResourceDescription_formalName", curie=TCCM.curie('formalName'),
                      model_uri=TCCM.ResourceDescription_formalName, domain=ResourceDescription, range=Optional[str])

slots.ResourceDescription_keyword = Slot(uri=TCCM.keyword, name="ResourceDescription_keyword", curie=TCCM.curie('keyword'),
                      model_uri=TCCM.ResourceDescription_keyword, domain=ResourceDescription, range=List[str])

slots.ResourceDescription_resourceSynopsis = Slot(uri=TCCM.resourceSynopsis, name="ResourceDescription_resourceSynopsis", curie=TCCM.curie('resourceSynopsis'),
                      model_uri=TCCM.ResourceDescription_resourceSynopsis, domain=ResourceDescription, range=Optional[str])

slots.ResourceDescription_additionalDocumentation = Slot(uri=TCCM.additionalDocumentation, name="ResourceDescription_additionalDocumentation", curie=TCCM.curie('additionalDocumentation'),
                      model_uri=TCCM.ResourceDescription_additionalDocumentation, domain=ResourceDescription, range=List[Union[str, PersistentURI]])

slots.ResourceDescription_rights = Slot(uri=TCCM.rights, name="ResourceDescription_rights", curie=TCCM.curie('rights'),
                      model_uri=TCCM.ResourceDescription_rights, domain=ResourceDescription, range=Optional[str])

slots.ResourceDescription_alternateID = Slot(uri=TCCM.alternateID, name="ResourceDescription_alternateID", curie=TCCM.curie('alternateID'),
                      model_uri=TCCM.ResourceDescription_alternateID, domain=ResourceDescription, range=Optional[str])

slots.SourceAndNotation_sourceAndNotationDescription = Slot(uri=TCCM.sourceAndNotationDescription, name="SourceAndNotation_sourceAndNotationDescription", curie=TCCM.curie('sourceAndNotationDescription'),
                      model_uri=TCCM.SourceAndNotation_sourceAndNotationDescription, domain=SourceAndNotation, range=Optional[str])

slots.SourceAndNotation_sourceDocument = Slot(uri=TCCM.sourceDocument, name="SourceAndNotation_sourceDocument", curie=TCCM.curie('sourceDocument'),
                      model_uri=TCCM.SourceAndNotation_sourceDocument, domain=SourceAndNotation, range=Optional[Union[str, PersistentURI]])

slots.SourceAndNotation_sourceLanguage = Slot(uri=TCCM.sourceLanguage, name="SourceAndNotation_sourceLanguage", curie=TCCM.curie('sourceLanguage'),
                      model_uri=TCCM.SourceAndNotation_sourceLanguage, domain=SourceAndNotation, range=Optional[Union[dict, OntologyLanguageReference]])

slots.SourceAndNotation_sourceDocumentSyntax = Slot(uri=TCCM.sourceDocumentSyntax, name="SourceAndNotation_sourceDocumentSyntax", curie=TCCM.curie('sourceDocumentSyntax'),
                      model_uri=TCCM.SourceAndNotation_sourceDocumentSyntax, domain=SourceAndNotation, range=Optional[Union[dict, OntologySyntaxReference]])

slots.AbstractResourceDescription_releaseDocumentation = Slot(uri=TCCM.releaseDocumentation, name="AbstractResourceDescription_releaseDocumentation", curie=TCCM.curie('releaseDocumentation'),
                      model_uri=TCCM.AbstractResourceDescription_releaseDocumentation, domain=AbstractResourceDescription, range=Optional[str])

slots.AbstractResourceDescription_releaseFormat = Slot(uri=TCCM.releaseFormat, name="AbstractResourceDescription_releaseFormat", curie=TCCM.curie('releaseFormat'),
                      model_uri=TCCM.AbstractResourceDescription_releaseFormat, domain=AbstractResourceDescription, range=List[Union[dict, SourceAndNotation]])

slots.ResourceVersionDescription_documentURI = Slot(uri=TCCM.documentURI, name="ResourceVersionDescription_documentURI", curie=TCCM.curie('documentURI'),
                      model_uri=TCCM.ResourceVersionDescription_documentURI, domain=ResourceVersionDescription, range=Optional[Union[str, DocumentURI]])

slots.ResourceVersionDescription_sourceAndNotation = Slot(uri=TCCM.sourceAndNotation, name="ResourceVersionDescription_sourceAndNotation", curie=TCCM.curie('sourceAndNotation'),
                      model_uri=TCCM.ResourceVersionDescription_sourceAndNotation, domain=ResourceVersionDescription, range=Optional[Union[dict, SourceAndNotation]])

slots.ResourceVersionDescription_predecessor = Slot(uri=TCCM.predecessor, name="ResourceVersionDescription_predecessor", curie=TCCM.curie('predecessor'),
                      model_uri=TCCM.ResourceVersionDescription_predecessor, domain=ResourceVersionDescription, range=Optional[Union[dict, NameAndMeaningReference]])

slots.ResourceVersionDescription_officialResourceVersionID = Slot(uri=TCCM.officialResourceVersionID, name="ResourceVersionDescription_officialResourceVersionID", curie=TCCM.curie('officialResourceVersionID'),
                      model_uri=TCCM.ResourceVersionDescription_officialResourceVersionID, domain=ResourceVersionDescription, range=Optional[str])

slots.ResourceVersionDescription_officialReleaseDate = Slot(uri=TCCM.officialReleaseDate, name="ResourceVersionDescription_officialReleaseDate", curie=TCCM.curie('officialReleaseDate'),
                      model_uri=TCCM.ResourceVersionDescription_officialReleaseDate, domain=ResourceVersionDescription, range=Optional[Union[str, XSDDateTime]])

slots.ResourceVersionDescription_officialActivationDate = Slot(uri=TCCM.officialActivationDate, name="ResourceVersionDescription_officialActivationDate", curie=TCCM.curie('officialActivationDate'),
                      model_uri=TCCM.ResourceVersionDescription_officialActivationDate, domain=ResourceVersionDescription, range=Optional[Union[str, XSDDateTime]])

slots.NameAndMeaningReference_name = Slot(uri=TCCM.name, name="NameAndMeaningReference_name", curie=TCCM.curie('name'),
                      model_uri=TCCM.NameAndMeaningReference_name, domain=NameAndMeaningReference, range=Union[str, LocalIdentifier])

slots.NameAndMeaningReference_uri = Slot(uri=TCCM.uri, name="NameAndMeaningReference_uri", curie=TCCM.curie('uri'),
                      model_uri=TCCM.NameAndMeaningReference_uri, domain=NameAndMeaningReference, range=Optional[Union[str, ExternalURI]])

slots.NameAndMeaningReference_href = Slot(uri=TCCM.href, name="NameAndMeaningReference_href", curie=TCCM.curie('href'),
                      model_uri=TCCM.NameAndMeaningReference_href, domain=NameAndMeaningReference, range=Optional[Union[str, RenderingURI]])

slots.CodeSystemVersionReference_codeSystem = Slot(uri=TCCM.codeSystem, name="CodeSystemVersionReference_codeSystem", curie=TCCM.curie('codeSystem'),
                      model_uri=TCCM.CodeSystemVersionReference_codeSystem, domain=CodeSystemVersionReference, range=Optional[Union[dict, CodeSystemReference]])

slots.MapVersionReference_map = Slot(uri=TCCM.map, name="MapVersionReference_map", curie=TCCM.curie('map'),
                      model_uri=TCCM.MapVersionReference_map, domain=MapVersionReference, range=Optional[Union[dict, MapReference]])

slots.PredicateReference_uri = Slot(uri=TCCM.uri, name="PredicateReference_uri", curie=TCCM.curie('uri'),
                      model_uri=TCCM.PredicateReference_uri, domain=PredicateReference, range=Union[str, ExternalURI])

slots.PredicateReference_name = Slot(uri=TCCM.name, name="PredicateReference_name", curie=TCCM.curie('name'),
                      model_uri=TCCM.PredicateReference_name, domain=PredicateReference, range=Curie)

slots.PredicateReference_href = Slot(uri=TCCM.href, name="PredicateReference_href", curie=TCCM.curie('href'),
                      model_uri=TCCM.PredicateReference_href, domain=PredicateReference, range=Optional[Union[str, RenderingURI]])

slots.PredicateReference_designation = Slot(uri=TCCM.designation, name="PredicateReference_designation", curie=TCCM.curie('designation'),
                      model_uri=TCCM.PredicateReference_designation, domain=PredicateReference, range=Optional[str])

slots.SourceAndRoleReference_role = Slot(uri=TCCM.role, name="SourceAndRoleReference_role", curie=TCCM.curie('role'),
                      model_uri=TCCM.SourceAndRoleReference_role, domain=SourceAndRoleReference, range=Optional[Union[dict, RoleReference]])

slots.annotation_extension_value = Slot(uri=TCCM.value, name="annotation_extension_value", curie=TCCM.curie('value'),
                      model_uri=TCCM.annotation_extension_value, domain=Annotation, range=Bool)
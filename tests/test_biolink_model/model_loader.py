import os
import sys
import time
from datetime import datetime
from io import StringIO
from typing import Union, TextIO, Optional, List, Set
from urllib.parse import urlparse
from urllib.request import Request, urlopen

import yaml

from tests.test_biolink_model.biolink_metamodel.biolink_association import SlotClassDescription, SlotDescription, \
    SlotRelationDescription
from tests.test_biolink_model.biolink_metamodel.biolink_metamodel import Model, metamodel_version
from biolinkml.utils.namespaces import Namespaces
from biolinkml.utils.yamlutils import DupCheckYamlLoader
from tests.test_biolink_model.biolink_metamodel.biolink_named_thing import Thing, NamedThing, OntologicalClass, \
    InformationContentEntity, AdministrativeEntity, PropertyDefinition, NamedThingId, TypeDefinition, TypeDefinitionId
from tests.test_biolink_model.model_merge_utils import merge_models


def load_raw_model(data: Union[str, TextIO],
                   source_file: Optional[str] = None,
                   source_file_date: Optional[str] = None,
                   source_file_size: Optional[int] = None,
                   base_dir: Optional[str] = None) -> Model:
    """ Load and flatten a Model definition from a file name, a URL or a block of text

    @param data: URL, file name or block of text
    @param source_file: Source file name for the model if data is type TextIO
    @param source_file_date: timestamp of source file if data is type TextIO
    @param source_file_size: size of source file if data is type TextIO
    @param base_dir: Working directory or base URL of sources

    @return: Map from model name to Model
    """

    def _name_from_url(url) -> str:
        return urlparse(url).path.rsplit('/', 1)[-1].rsplit('.', 1)[0]

    # Turn data into YAML
    if isinstance(data, str):
        if '\n' in data:
            # Actual data file being passed
            return load_raw_model(StringIO(data), source_file, source_file_date, source_file_size, base_dir)

        assert source_file is None, "source_file parameter not allowed if data is a file or URL"
        assert source_file_date is None, "source_file_date parameter not allowed if data is a file or URL"
        assert source_file_size is None, "source_file_size parameter not allowed if data is a file or URL"

        if '://' in data or (base_dir and '://' in base_dir):
            # URL being passed
            fname = Namespaces.join(base_dir, data) if '://' not in data else data
            req = Request(fname)
            req.add_header("Accept", "application/yaml, text/yaml;q=0.9")
            with urlopen(req) as response:
                return load_raw_model(response, fname, response.info()['Last-Modified'],
                                      response.info()['Content-Length'])
        else:
            # File name being passed
            if not base_dir:
                fname = os.path.abspath(data)
                base_dir = os.path.dirname(fname)
            else:
                fname = data if os.path.isabs(data) else os.path.join(base_dir, data)
            with open(fname) as f:
                return load_raw_model(f, fname, time.ctime(os.path.getmtime(fname)), os.path.getsize(fname), base_dir)
    else:
        # Process and normalize the YAML
        model = yaml.load(data, DupCheckYamlLoader)

        # Convert the schema into a "name: definition" form
        if not all(isinstance(e, dict) for e in model.values()):
            if 'name' in model:
                schemaname = model.pop('name')
            elif 'id' in model:
                schemaname = _name_from_url(model['id'])
            else:
                raise ValueError("Unable to determine schema name")
            model_body = [model]
            model = {schemaname: model}
        else:
            model_body = list(model.values())

        def check_is_dict(element: str) -> None:
            for modelname, modelbody in model.items():
                if element in modelbody and not isinstance(modelbody[element], dict):
                    raise ValueError(f'Model: {modelname} - {element} must be a dictionary')

        def fix_multiples(container: str, element: str) -> None:
            """ Convert strings to lists in common elements that have both single and multiple options """
            for mbody in model_body:
                if container in mbody:
                    for c in mbody[container].values():
                        if c and element in c and isinstance(c[element], str):
                            c[element] = [c[element]]

        for e in ['types', 'subsets', 'node_properties', 'assoc_properties', 'associations', 'nodes', 'relations',
                  'evidence', 'providers', 'publications']:
            check_is_dict(e)

        fix_multiples('comments', 'notes')
        for e in ['imports']:
            for body in model_body:
                if e in body:
                    if isinstance(body[e], str):
                        body[e] = [body[e]]

        schema: Model = None
        for sname, sdef in {k: Model(name=k, **v) for k, v in model.items()}.items():
            if schema is None:
                schema = sdef
                if source_file:
                    schema.source_file = source_file
                schema.source_file_date = source_file_date
                schema.source_file_size = source_file_size
                schema.generation_date = datetime.now().strftime("%Y-%m-%d %H:%M")
                schema.metamodel_version = metamodel_version
                # set_from_model(schema)
            else:
                # merge_models(schema, sdef)
                pass
        return schema


class ModelLoader:
    def __init__(self,
                 data: Union[str, TextIO, Model],
                 base_dir: Optional[str] = None,
                 namespaces: Optional[Namespaces] = None) \
            -> None:
        """ Constructor - load and process a YAML or pre-processed schema

        :param data: YAML schema text, URL, file name, open file or SchemaDefinition
        :param base_dir: base directory or URL where Schema came from
        :param namespaces: namespaces collector
        """
        if isinstance(data, Model):
            self.model = data
        else:
            self.model = load_raw_model(data, base_dir=base_dir)
        self.loaded: Set[str] = {self.model.name}
        self.base_dir = self._get_base_dir(base_dir)
        self.namespaces = namespaces if namespaces else Namespaces()

    def resolve(self) -> Model:
        """Reconcile a loaded model, applying is_a, mixins, apply_to's and other such things.  Also validate the
        content

        :return: Fully resolved definition
        """

        if not self.model.default_prefix:
            self.model.default_prefix = self.model.id
        self.namespaces._base = self.model.id

        # Process the namespace declarations
        for prefix in self.model.prefixes.values():
            self.namespaces[prefix.local_name] = prefix.prefix_uri
        for cmap in self.model.default_curi_maps:
            self.namespaces.add_prefixmap(cmap, include_defaults=False)
        if not self.namespaces._default:
            if '://' in self.model.default_prefix:
                self.namespaces._default = self.model.default_prefix
            elif self.model.default_prefix in self.namespaces:
                self.namespaces._default = self.namespaces[self.model.default_prefix]
            else:
                raise ValueError(f'Default prefix: {self.model.default_prefix} is not defined')

        # Process imports
        for mname in self.model.imports:
            if mname not in self.loaded:
                self.loaded.add(mname)
                merge_models(self.model, load_raw_model(mname + '.yaml', base_dir=self.base_dir), mname,
                              self.namespaces)


        # Massage initial set of slots
        for slot in self.model.slots.values():
            # Propagate domain to containing class
            if slot.domain and slot.domain in self.schema.classes:
                if slot.name not in self.schema.classes[slot.domain].slots:
                    self.schema.classes[slot.domain].slots.append(slot.name)
            elif slot.domain:
                self.raise_value_error(f"slot: {slot.name} - unrecognized domain ({slot.domain})")

            # Keys and identifiers must be present
            if bool(slot.key or slot.identifier):
                if slot.required is None:
                    slot.required = True
                elif not slot.required:
                    self.raise_value_error(f"slot: {slot.name} - key and identifier slots cannot be optional")

            # Add default ranges
            if slot.range is None:
                slot.range = self.schema.default_range
            elif slot.range not in self.schema.types and slot.range not in self.schema.classes \
                    and slot.range != self.schema.default_range:
                self.raise_value_error(f"slot: {slot.name} - unrecognized range ({slot.range})")

            # Assign missing predicates
            if slot.slot_uri is None:
                slot.slot_uri = self.namespaces.uri_or_curie_for(self.schema.default_prefix, self.slot_name_for(slot))

        # Massage classes, propagating class slots entries domain back to the target slots
        for cls in self.schema.classes.values():
            if not isinstance(cls, ClassDefinition):
                name = cls['name'] if 'name' in cls else 'Unknown'
                self.raise_value_error(f'Class "{name} (type: {type(cls)})" definition is not a class definition')
            if isinstance(cls.slots, str):
                print(f"File: {self.schema.source_file} Class: {cls.name} Slots are not an array", file=sys.stderr)
                cls.slots = [cls.slots]
            for slotname in cls.slots:
                if slotname in self.schema.slots:
                    slot = self.schema.slots[cast(SlotDefinitionName, slotname)]
                    if slot.domain is None:
                        slot.domain = cls.name
                    elif slot.domain != cls.name:
                        self.raise_value_error(f'Slot: {slot.name} domain ({slot.domain}) '
                                               f'does not match declaring class "({cls.name})"')
                else:
                    self.raise_value_error(f'Class "{cls.name}" - unknown slot: "{slotname}"')


        # apply to --> mixins
        for cls in self.schema.classes.values():
            for apply_to_cls in cls.apply_to:
                if apply_to_cls in self.schema.classes:
                    self.schema.classes[apply_to_cls].mixins.append(cls.name)
                else:
                    self.raise_value_error(f'Class "{cls.name}" unknown apply_to target: {apply_to_cls}')
            if cls.class_uri is None:
                cls.class_uri = self.namespaces.uri_or_curie_for(self.schema.default_prefix, camelcase(cls.name))

        # Update slots with parental information
        merged_slots: List[SlotDefinitionName] = []
        for slot in self.schema.slots.values():
            if not slot.from_schema:
                slot.from_schema = self.schema.id
            self.merge_slot(slot, merged_slots)

        # Update classes with parental information
        merged_classes: List[ClassDefinitionName] = []
        for cls in self.schema.classes.values():
            if not cls.from_schema:
                cls.from_schema = self.schema.id
            self.merge_class(cls, merged_classes)

        # Update types with parental information
        merged_types: List[TypeDefinitionName] = []
        for typ in self.schema.types.values():
            if not typ.base and not typ.typeof:
                self.raise_value_error(f'type "{typ.name}" must declare a type base or parent (typeof)')
            if not typ.typeof and not typ.uri:
                self.raise_value_error(f'type "{typ.name}" does not declare a URI')
            self.merge_type(typ, merged_types)
            if not typ.from_schema:
                typ.from_schema = self.schema.id

        # Update the subsets as needed
        for ss in self.schema.subsets.values():
            if not ss.from_schema:
                ss.from_schema = self.schema.id

        # Inline any class definitions that don't have keys
        for slot in self.schema.slots.values():
            if slot.range in self.schema.classes:
                range_class = self.schema.classes[cast(ClassDefinitionName, slot.range)]
                if not any([self.schema.slots[s].key for s in range_class.slots]):
                    slot.inlined = True

        # Check for duplicate class and type names
        def check_dups(s1: Set[ElementName], s2: Set[ElementName]) -> str:
            return ', '.join(sorted(s1.intersection(s2)))

        # Check for slots with both key and identifier
        for slot in self.schema.slots.values():
            if slot.key and slot.identifier:
                self.raise_value_error(f'slot: "{slot.name}" - key and identifier are mutually exclusive')

        classes = set(self.schema.classes.keys())
        slots = set(self.schema.slots.keys())
        types = set(self.schema.types.keys())
        subsets = set(self.schema.subsets.keys())

        # Check that the default range is valid
        if not self.schema.default_range:
            raise ValueError("Default range is not specified")
        if self.schema.default_range not in self.schema.types and self.schema.default_range not in self.schema.classes:
            raise ValueError(f'Unknown default range: "{self.schema.default_range}"')

        # We are currently limited to one key per class
        for cls in self.schema.classes.values():
            class_slots = []
            for sn in cls.slots:
                slot = self.schema.slots[sn]
                if slot.key:
                    class_slots.append(slot.name)
            if len(class_slots) > 1:
                self.raise_value_error(f'Class "{cls.name}" - multiple keys not allowed ({", ".join(class_slots)})')


        # Cannot have duplicate class or type keys
        dups = check_dups(classes, types)
        if dups:
            raise ValueError(f"Shared class and type names detected: {dups}")

        dups = check_dups(classes, slots)
        if dups:
            print(f"Warning: Shared class and slot names: {dups}", file=sys.stderr)
        dups = check_dups(classes, subsets)
        if dups:
            print(f"Warning: Shared class and subset names: {dups}", file=sys.stderr)
        dups = check_dups(slots, types)
        if dups:
            print(f"Warning: Shared type and slot names: {dups}", file=sys.stderr)
        dups = check_dups(slots, subsets)
        if dups:
            print(f"Warning: Shared slot and subset names: {dups}", file=sys.stderr)
        dups = check_dups(types, subsets)
        if dups:
            print(f"Warning: Shared type and subset names: {dups}", file=sys.stderr)

        # Make the source file relative if it is locally generated
        if self.schema.source_file and '://' not in self.schema.source_file:
            self.schema.source_file = os.path.basename(self.schema.source_file)

        self.synopsis = SchemaSynopsis(self.schema)
        return self.schema

    def merge_named_thing(self, thing: NamedThing, merged_things: List[NamedThingId], list_of_things: List[NamedThing],
                          inheritance_slot: str = 'is_a', slot_definitions_name: Optional[str] = None) -> None:
        """
        Merge parent thing information into target thing

        :param thing: target thing
        :param merged_things: list of thing names that have been merged.  Used to do a distal ancestor resolution
        :param list_of_things: List of all known things of given type
        :param inheritence_slot: parent slot name ('is_a', 'typeof', ...)
        """
        if thing.id not in merged_things:
            parent = thing[inheritance_slot]
            if parent:
                if parent in list_of_things:
                    self.merge_named_thing(list_of_things[parent], merged_things, list_of_things)
                    if slot_definitions_name:
                        merge_slots(thing, list_of_things[parent], slot_definitions_name)
                else:
                    unknown(thing, inheritance_slot, parent)
            for mixin in thing.mixins:
                if mixin in list_of_things:
                    self.merge_named_thing(list_of_things[mixin], merged_things, inheritance_slot)
                    if slot_definitions_name:
                        merge_slots(thing, list_of_things[mixin],slot_definitions_name)
                else:
                    unknown(thing, 'mixins', mixin)
            merged_things.append(thing.id)


    def slot_definition_for(self, slotname: SlotDefinitionName, cls: ClassDefinition) -> Optional[SlotDefinition]:
        """ Find the most proximal definition for slotname in the context of cls"""
        if cls.is_a:
            for sn in self.schema.classes[cls.is_a].slots:
                slot = self.schema.slots[sn]
                if slot.alias and slotname == slot.alias or slotname == slot.name:
                    return slot
        for mixin in cls.mixins:
            for sn in self.schema.classes[mixin].slots:
                slot = self.schema.slots[sn]
                if slot.alias and slotname == slot.alias or slotname == slot.name:
                    return slot
        if cls.is_a:
            defn = self.slot_definition_for(slotname, self.schema.classes[cls.is_a])
            if defn:
                return defn
        for mixin in cls.mixins:
            defn = self.slot_definition_for(slotname, self.schema.classes[mixin])
            if defn:
                return defn
        return None


    def _get_base_dir(self, stated_base: str) -> Optional[str]:
        if stated_base:
            return stated_base
        elif self.schema.source_file:
            if '://' in self.schema.source_file:
                parsed_url = urlparse(self.schema.source_file)
                self.schema.source_file = parsed_url.path.rsplit('/', 1)[-1]
                return parsed_url.path.split('/', 1)[0]
            else:
                rval = os.path.dirname(os.path.abspath(self.schema.source_file))
                self.schema.source_file = os.path.basename(self.schema.source_file)
                return rval
        else:
            return None


    def validate(self):
        """ Validate the contents of the model """
        def unknown(container: Thing, typ: str, inst: str) -> None:
            print(f"{type(container)}:{container.name} - unknown {typ} reference: {inst}", file=sys.stderr)

        def missing(container: Thing, typ: str) -> None:
            print(f"{type(container)}:{container.name} - missing required field: {typ}", file=sys.stderr)

        def process_thing(thing: Thing) -> None:
            for subset in thing.in_subset:
                if subset not in self.model.subsets:
                    unknown(thing, "subset", subset)

        def process_named_thing(nthing: NamedThing) -> None:
            process_thing(nthing)
            pass

        def process_ontological_class(oc: OntologicalClass) -> None:
            process_named_thing(oc)

        def process_information_content_entity(ice: InformationContentEntity) -> None:
            process_named_thing(ice)

        def process_administrative_entity(ae: AdministrativeEntity) -> None:
            process_named_thing(ae)

        def process_slot_description(sd: SlotDescription) -> None:
            process_thing(sd)

        def process_slot_class_description(scd: SlotClassDescription) -> None:
            process_slot_description(scd)
            if scd.range not in self.model.nodes:
                unknown(scd, "range", scd.range)

        def process_slot_relation_description(srd: SlotRelationDescription) -> None:
            process_slot_description(srd)
            if srd.range not in self.model.relations:
                unknown(srd, "range", srd.range)

        def process_property_definition(pd: PropertyDefinition) -> None:
            process_named_thing(pd)
            if not pd.domain:
                missing(pd, 'domain')
            if not pd.range:
                missing(pd, 'range')
            elif pd.range not in self.model.attributes:
                unknown(pd, 'range', pd.range)

        for typ in self.model.types.values():
            process_named_thing(typ)
            if typ.typeof and typ.typeof not in self.model.types:
                unknown(typ, "typeof", typ.typeof)
            # base
            # uri
            # repr

        for ss in self.model.subsets.values():
            process_named_thing(ss)

        for vs in self.model.valuesets.values():
            process_named_thing(vs)

        for assoc in self.model.associations.values():
            process_thing(assoc)
            if assoc.association_type and assoc.association_type not in self.model.relations:
                unknown(assoc, "association_type", assoc.association_type)
            if not assoc.subject:
                missing(assoc, "subject")
            else:
                process_slot_class_description(assoc.subject)
            if not assoc.relation:
                missing(assoc, "relation")
            else:
                process_slot_relation_description(assoc.relation)
            if not assoc.object:
                missing(assoc, "object")
            else:
                process_slot_class_description(assoc.object)
            if assoc.is_a and assoc.is_a not in self.model.associations:
                unknown(assoc, 'is_a', assoc.is_a)
            if assoc.has_confidence_level and assoc.has_confidence_level not in self.model.valuesets:
                unknown(assoc, 'has_confidence_level', assoc.has_confidence_level)
            for ev in assoc.has_evidence:
                if ev not in self.model.evidence:
                    unknown(assoc, 'evidence', ev)
            for prov in assoc.provided_by:
                if prov not in self.model.providers:
                    unknown(assoc, 'provided_by', prov)
            for q in assoc.qualifiers:
                if q not in self.model.valuesets:
                    unknown(assoc, 'qualifiers', q)
            for pub in assoc.publications:
                if pub not in self.model.publications:
                    unknown(assoc, 'publications', pub)
            for mixin in assoc.mixins:
                if mixin not in self.model.associations:
                    unknown(assoc, 'mixins', mixin)
            for apply_to in assoc.apply_to:
                if apply_to not in self.model.associations:
                    unknown(assoc, 'apply_to', apply_to)
            # for slot in assoc.slots:
            #     if slot not in self.model.association_slots:
            #         ???
            #         for ass_slot in assoc.association_slot:
            #             if ass_slot not in self.model.???

                for node in self.model.nodes.values():
                    process_ontological_class(node)
                    for uo in node.union_of:
                        if uo not in self.model.nodes:
                            unknown(node, "node", uo)

                for rel in self.model.relations.values():
                    process_ontological_class(rel)
                    if not rel.domain:
                        missing(rel, "domain")
                    if not rel.range:
                        missing(rel, "range")
                    if rel.domain not in self.model.nodes:
                        unknown(rel, "domain", rel.domain)
                    if rel.range not in self.model.nodes:
                        unknown(rel, "range", rel.range)

                for ev in self.model.evidence.values():
                    process_information_content_entity(ev)

                for prov in self.model.providers.values():
                    process_administrative_entity(prov)

                for pub in self.model.publications.values():
                    process_information_content_entity(pub)

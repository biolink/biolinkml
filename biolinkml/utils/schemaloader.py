import logging
import os
import sys
from collections import OrderedDict
from typing import Union, TextIO, Optional, Set, List, cast, Dict, Mapping, Tuple
from urllib.parse import urlparse

from biolinkml.meta import SchemaDefinition, SlotDefinition, SlotDefinitionName, ClassDefinition, \
    ClassDefinitionName, TypeDefinitionName, TypeDefinition, ElementName
from biolinkml.utils.context_utils import parse_import_map
from biolinkml.utils.formatutils import underscore, camelcase, sfx
from biolinkml.utils.mergeutils import merge_schemas, merge_slots, merge_classes, slot_usage_name
from biolinkml.utils.metamodelcore import Bool
from biolinkml.utils.namespaces import Namespaces
from biolinkml.utils.rawloader import load_raw_schema
from biolinkml.utils.schemasynopsis import SchemaSynopsis
from biolinkml.utils.yamlutils import TypedNode


class SchemaLoader:
    def __init__(self,
                 data: Union[str, TextIO, SchemaDefinition, dict],
                 base_dir: Optional[str] = None,
                 namespaces: Optional[Namespaces] = None,
                 useuris: Optional[bool] = None,
                 importmap: Optional[Mapping[str, str]] = None,
                 logger: Optional[logging.Logger] = None) \
            -> None:
        """ Constructor - load and process a YAML or pre-processed schema

        :param data: YAML schema text, python dict loaded from yaml,  URL, file name, open file or SchemaDefinition
        :param base_dir: base directory or URL where Schema came from
        :param namespaces: namespaces collector
        :param useuris: True means class_uri and slot_uri are identifiers.  False means they are mappings.
        :param importmap: A map from import entries to URI or file name.
        :param logger: Target Logger, if any
        """
        self.logger = logger if logger is not None else logging.getLogger(self.__class__.__name__)
        if isinstance(data, SchemaDefinition):
            self.schema = data
        else:
            self.schema = load_raw_schema(data, base_dir=base_dir)
        # Map from URI to source and version tuple
        self.loaded: OrderedDict[str, Tuple[str, str]] = {self.schema.id: (self.schema.source_file, self.schema.version)}
        self.base_dir = self._get_base_dir(base_dir)
        self.namespaces = namespaces if namespaces else Namespaces()
        self.useuris = useuris if useuris is not None else True
        self.importmap = parse_import_map(importmap, self.base_dir) if importmap is not None else dict()
        self.synopsis: Optional[SchemaSynopsis] = None
        self.schema_location: Optional[str] = None
        self.schema_defaults: Dict[str, str] = {}           # Map from schema URI to default namespace

    def resolve(self) -> SchemaDefinition:
        """Reconcile a loaded schema, applying is_a, mixins, apply_to's and other such things.  Also validate the
        content and load a SchemaSynopsis entry

        :return: Fully resolved definition
        """
        if not self.schema.default_range:
            self.schema.default_range = 'string'
            print(f"Warning: default_range not specified. Default set to '{self.schema.default_range}'",
                  file=sys.stderr)

        # Process the namespace declarations
        if not self.schema.default_prefix:
            self.schema.default_prefix = sfx(self.schema.id)
        self.schema_defaults[self.schema.id] = self.schema.default_prefix
        for prefix in self.schema.prefixes.values():
            self.namespaces[prefix.prefix_prefix] = prefix.prefix_reference
        for cmap in self.schema.default_curi_maps:
            self.namespaces.add_prefixmap(cmap, include_defaults=False)
        if not self.namespaces._default:
            if '://' in self.schema.default_prefix:
                self.namespaces._default = self.schema.default_prefix
            elif self.schema.default_prefix in self.namespaces:
                self.namespaces._default = self.namespaces[self.schema.default_prefix]
            else:
                self.raise_value_error(f'Default prefix: {self.schema.default_prefix} is not defined',
                                       self.schema.default_prefix)

        # Process imports
        for imp in self.schema.imports:
            sname = self.importmap.get(str(imp), imp)               # Import map may use CURIE
            sname = self.namespaces.uri_for(sname) if ':' in sname else sname
            sname = self.importmap.get(str(sname), sname)               # It may also use URI or other forms
            import_schemadefinition = \
                load_raw_schema(sname + '.yaml',
                                base_dir=os.path.dirname(self.schema.source_file) if self.schema.source_file else None)
            loaded_schema = (str(sname), import_schemadefinition.version)
            if import_schemadefinition.id in self.loaded:
                # If we've already loaded this, make sure that we've got the same version
                if self.loaded[import_schemadefinition.id][1] != loaded_schema[1]:
                    self.raise_value_error(f"Schema {import_schemadefinition.name} - version mismatch",
                                           import_schemadefinition.name)
                # Note: for debugging purposes we also check whether the version came from the same spot.  This should
                #       be loosened to version only once we're sure that everything is working
                if self.loaded[import_schemadefinition.id] != loaded_schema:
                    self.raise_value_error(f"Schema imported from different files: "
                                           f"{self.loaded[import_schemadefinition.id][0]} : {loaded_schema[0]}")
            else:
                self.loaded[import_schemadefinition.id] = loaded_schema
                merge_schemas(self.schema, import_schemadefinition, imp, self.namespaces)
                self.schema_defaults[import_schemadefinition.id] = import_schemadefinition.default_prefix

        self.namespaces._base = self.schema.default_prefix if ':' in self.schema.default_prefix else \
            self.namespaces[self.schema.default_prefix]

        # Assign class slot ownership
        for cls in self.schema.classes.values():
            if not isinstance(cls, ClassDefinition):
                name = cls['name'] if 'name' in cls else 'Unknown'
                self.raise_value_error(f'Class "{name} (type: {type(cls)})" definition is not a class definition', name)
            if isinstance(cls.slots, str):
                self.logger.warning(f"File: {self.schema.source_file} Class: {cls.name} Slots are not an array")
                cls.slots = [cls.slots]
            for slotname in cls.slots:
                if slotname in self.schema.slots:
                    slot = self.schema.slots[cast(SlotDefinitionName, slotname)]
                    slot.owner = cls.name
                else:
                    self.raise_value_error(f'Class "{cls.name}" - unknown slot: "{slotname}"', slotname)


        # Massage initial set of slots
        for slot in self.schema.slots.values():
            # Propagate domain to containing class
            if slot.domain and slot.domain in self.schema.classes:
                if slot.name not in self.schema.classes[slot.domain].slots:
                    slot.owner = slot.name
                    self.schema.classes[slot.domain].slots.append(slot.name)
            elif slot.domain:
                self.raise_value_error(f"slot: {slot.name} - unrecognized domain ({slot.domain})", slot.domain)

            # Keys and identifiers must be present
            if bool(slot.key or slot.identifier):
                if slot.required is None:
                    slot.required = True
                elif not slot.required:
                    self.raise_value_error(f"slot: {slot.name} - key and identifier slots cannot be optional", slot.name)

            # Validate the slot range
            if slot.range is not None and  slot.range not in self.schema.types and \
                    slot.range not in self.schema.classes:
                self.raise_value_error(f"slot: {slot.name} - unrecognized range ({slot.range})", slot.range)

        # apply to --> mixins
        for cls in self.schema.classes.values():
            for apply_to_cls in cls.apply_to:
                if apply_to_cls in self.schema.classes:
                    self.schema.classes[apply_to_cls].mixins.append(cls.name)
                else:
                    self.raise_value_error(f'Class "{cls.name}" unknown apply_to target: {apply_to_cls}', apply_to_cls)
            # Class URI's also count as (trivial) mappings
            if cls.class_uri is not None:
                cls.mappings.insert(0, cls.class_uri)
            if cls.class_uri is None or not self.useuris:
                cls.class_uri = \
                    self.namespaces.uri_or_curie_for(self.schema_defaults.get(cls.from_schema, sfx(cls.from_schema)),
                                                                 camelcase(cls.name))

        # Update slots with parental information
        merged_slots: List[SlotDefinitionName] = []
        for slot in self.schema.slots.values():
            if not slot.from_schema:
                slot.from_schema = self.schema.id
            self.merge_slot(slot, merged_slots)
            # Add default ranges
            if slot.range is None:
                slot.range = self.schema.default_range

        # Update classes with is_a and mixin information
        merged_classes: List[ClassDefinitionName] = []
        for cls in self.schema.classes.values():
            if not cls.from_schema:
                cls.from_schema = self.schema.id
            self.merge_class(cls, merged_classes)

        # Update types with parental information
        merged_types: List[TypeDefinitionName] = []
        for typ in self.schema.types.values():
            if not typ.base and not typ.typeof:
                self.raise_value_error(f'type "{typ.name}" must declare a type base or parent (typeof)', typ.name)
            if not typ.typeof and not typ.uri:
                self.raise_value_error(f'type "{typ.name}" does not declare a URI', typ.name)
            self.merge_type(typ, merged_types)
            if not typ.from_schema:
                typ.from_schema = self.schema.id

        # Update the subsets as needed
        for ss in self.schema.subsets.values():
            if not ss.from_schema:
                ss.from_schema = self.schema.id

        # Massage initial set of slots
        for slot in self.schema.slots.values():
            # Propagate domain to containing class
            if slot.domain and slot.domain in self.schema.classes:
                if slot.name not in self.schema.classes[slot.domain].slots and not slot.owner:
                    slot.owner = slot.name
                    self.schema.classes[slot.domain].slots.append(slot.name)
            elif slot.domain:
                self.raise_value_error(f"slot: {slot.name} - unrecognized domain ({slot.domain})", slot.domain)
            if slot.ifabsent:
                from biolinkml.utils.ifabsent_functions import isabsent_match
                if isabsent_match(slot.ifabsent) is None:
                    self.raise_value_error(f"Unrecognized ifabsent action for slot '{slot.name}': '{slot.ifabsent}'", slot.ifabsent)

            # Keys and identifiers must be present
            if bool(slot.key or slot.identifier):
                if slot.required is None:
                    slot.required = True
                elif not slot.required:
                    self.raise_value_error(f"slot: {slot.name} - key and identifier slots cannot be optional", slot.name)

            # Validate the slot range
            if slot.range is not None and  slot.range not in self.schema.types and \
                    slot.range not in self.schema.classes:
                self.raise_value_error(f"slot: {slot.name} - unrecognized range ({slot.range})", slot.range)

        # Massage classes, propagating class slots entries domain back to the target slots
        for cls in self.schema.classes.values():
            if not isinstance(cls, ClassDefinition):
                name = cls['name'] if 'name' in cls else 'Unknown'
                self.raise_value_error(f'Class "{name} (type: {type(cls)})" definition is not a class definition')
            if isinstance(cls.slots, str):
                self.logger.warning(f"File: {self.schema.source_file} Class: {cls.name} Slots are not an array")
                cls.slots = [cls.slots]
            for slotname in cls.slots:
                if slotname in self.schema.slots:
                    slot = self.schema.slots[cast(SlotDefinitionName, slotname)]
                else:
                    self.raise_value_error(f'Class "{cls.name}" - unknown slot: "{slotname}"', slotname)

        for slot in self.schema.slots.values():
            if slot.from_schema is None:
                slot.from_schema = self.schema.id
            # Inline any class definitions that don't have identifiers.  Note that keys ARE inlined
            if slot.range in self.schema.classes:
                range_class = self.schema.classes[cast(ClassDefinitionName, slot.range)]
                if not any([self.schema.slots[s].identifier for s in range_class.slots]):
                    slot.inlined = True

            if slot.slot_uri is not None:
                slot.mappings.insert(0, slot.slot_uri)
            # Assign missing predicates
            if slot.slot_uri is None or not self.useuris:
                slot.slot_uri = \
                    self.namespaces.uri_or_curie_for(self.schema_defaults.get(slot.from_schema, sfx(slot.from_schema)),
                                                                 self.slot_name_for(slot))

        # Check for duplicate class and type names
        def check_dups(s1: Set[ElementName], s2: Set[ElementName]) -> str:
            return ', '.join(sorted(s1.intersection(s2)))

        classes = set(self.schema.classes.keys())
        self.validate_item_names("class", classes)
        slots = set(self.schema.slots.keys())
        self.validate_item_names("slot", slots)
        types = set(self.schema.types.keys())
        self.validate_item_names("type", types)
        subsets = set(self.schema.subsets.keys())
        self.validate_item_names("subset", subsets)

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
                self.raise_value_error(f'Class "{cls.name}" - multiple keys not allowed ({", ".join(class_slots)})', class_slots[1])

        # Check out all the namespaces
        self.check_prefixes()

        # Cannot have duplicate class or type keys
        dups = check_dups(classes, types)
        if dups:
            raise ValueError(f"Shared class and type names detected: {dups}")

        dups = check_dups(classes, slots)
        if dups:
            self.logger.warning(f"Shared class and slot names: {dups}")
        dups = check_dups(classes, subsets)
        if dups:
            self.logger.warning(f"Shared class and subset names: {dups}")
        dups = check_dups(slots, types)
        if dups:
            self.logger.warning(f"Shared type and slot names: {dups}")
        dups = check_dups(slots, subsets)
        if dups:
            self.logger.warning(f"Shared slot and subset names: {dups}")
        dups = check_dups(types, subsets)
        if dups:
            self.logger.warning(f"Shared type and subset names: {dups}")

        # Make the source file relative if it is locally generated
        self.schema_location = self.schema.source_file
        if self.schema.source_file and '://' not in self.schema.source_file:
            self.schema.source_file = os.path.basename(self.schema.source_file)


        self.synopsis = SchemaSynopsis(self.schema)
        errs = self.synopsis.errors()
        if errs:
            print("Warning: The following errors were encountered in the schema")
            for errline in errs:
                print("\t" + errline)
            print()
        for subset, referees in self.synopsis.subsetrefs.items():
            if subset not in self.schema.subsets:
                self.raise_value_error(f"Subset: {subset} is not defined", subset)
        return self.schema


    def validate_item_names(self, typ: str, names: List[str]) -> None:
        # TODO: add a more rigorous syntax check for item names
        for name in names:
            if ':' in name:
                raise ValueError(f'{typ}: "{name}" - ":" not allowed in identifier')



    def merge_slot(self, slot: SlotDefinition, merged_slots: List[SlotDefinitionName]) -> None:
        """
        Merge parent slot information into target slot

        :param slot: target slot
        :param merged_slots: list of slot names that have been merged.  Used to do a distal ancestor resolution
        """
        if slot.name not in merged_slots:
            if slot.is_a:
                if slot.is_a in self.schema.slots:
                    self.merge_slot(self.schema.slots[slot.is_a], merged_slots)
                    merge_slots(slot, self.schema.slots[slot.is_a])
                else:
                    self.raise_value_error(f'Slot: "{slot.name}" - unknown is_a reference: {slot.is_a}', slot.is_a)
            for mixin in slot.mixins:
                if mixin in self.schema.slots:
                    self.merge_slot(self.schema.slots[mixin], merged_slots)
                    merge_slots(slot, self.schema.slots[mixin])
                else:
                    self.raise_value_error(f'Slot: "{slot.name}" - unknown mixin reference: {mixin}', mixin)
            merged_slots.append(slot.name)

    def merge_class(self, cls: ClassDefinition, merged_classes: List[ClassDefinitionName]) -> None:
        """
        Merge parent class information into target class

        :param cls: target class
        :param merged_classes: list of class names that have been merged. Used to do distal ancestor resolution
        """
        if cls.name not in merged_classes:
            merged_classes.append(cls.name)
            self.process_slot_usages(cls)
            if cls.is_a:
                if cls.is_a in self.schema.classes:
                    self.merge_class(self.schema.classes[cls.is_a], merged_classes)
                    merge_classes(self.schema, cls, self.schema.classes[cls.is_a], False)
                else:
                    self.raise_value_error(f'Class: "{cls.name}" - unknown is_a reference: {cls.is_a}', cls.is_a)
            for mixin in cls.mixins:
                # Note that apply_to has ben injected as a faux mixin so it gets covered here
                if mixin in self.schema.classes:
                    self.merge_class(self.schema.classes[mixin], merged_classes)
                    merge_classes(self.schema, cls, self.schema.classes[mixin], True)
                else:
                    self.raise_value_error(f'Class: "{cls.name}" - unknown mixin reference: {mixin}', mixin)

    def process_slot_usages(self, cls: ClassDefinition) -> None:
        """
        Connect any slot usage items

        :param cls: class to process
        :return: usage item
        """
        for slotname, slot_usage in cls.slot_usage.items():
            # Construct a new slot
            # Follow the ancestry of the class to get the most proximal parent
            parent_slot = self.slot_definition_for(slotname, cls)
            if not parent_slot and slotname in self.schema.slots:
                parent_slot = self.schema.slots[slotname]

            # If parent slot is still not defined, it means that we introduced a NEW slot in the slot usages
            if not parent_slot:
                self.logger.warning(f'class "{cls.name}" slot "{slotname}" does not reference an existing slot.  '
                                    f'New slot was created.')
                child_name = slotname
                slot_alias = None
            else:
                child_name = slot_usage_name(slotname, cls)
                slot_alias = slotname
            new_slot = SlotDefinition(name=child_name, alias=slot_alias, domain=cls.name, is_usage_slot=Bool(True),
                                      owner=cls.name)
            self.schema.slots[child_name] = new_slot
            merge_slots(new_slot, slot_usage)

            # Copy the parent definition.  If there is no parent definition, the slot is being defined
            # locally as a slot_usage
            if parent_slot is not None:
                new_slot.is_a = parent_slot.name
                merge_slots(new_slot, parent_slot)
                # This situation occurs when we are doing chained overrides.  Kludgy, but it works...
                if parent_slot.name in cls.slots:
                    if child_name in cls.slots:
                        del cls.slots[cls.slots.index(child_name)]
                    cls.slots[cls.slots.index(parent_slot.name)] = child_name

    def merge_type(self, typ: TypeDefinition, merged_types: List[TypeDefinitionName]) -> None:
        """
        Merge parent type information into target type
        :param typ: target type
        :param merged_types: list of type names that have bee merged.
        """
        if typ.name not in merged_types:
            if typ.typeof:
                if typ.typeof in self.schema.types:
                    reftyp = self.schema.types[cast(TypeDefinitionName, typ.typeof)]
                    self.merge_type(reftyp, merged_types)
                    merge_slots(typ, reftyp, [SlotDefinitionName('imported_from')])
                else:
                    self.raise_value_error(f'Type: "{typ.name}" - unknown typeof reference: {typ.typeof}', typ.typeof)
            merged_types.append(typ.name)

    def schema_errors(self) -> List[str]:
        return self.synopsis.errors() if self.synopsis else ["resolve() must be run before error check"]

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

    def check_prefixes(self) -> None:
        """
        Iterate over the entire schema checking all prefixes
        """
        self.check_prefix(self.schema.default_prefix)
        for prefix in self.schema.emit_prefixes:
            self.check_prefix(prefix)
        for typ in self.schema.types.values():
            self.check_prefix(typ.uri)
            for prefix in typ.mappings:
                self.check_prefix(prefix)
            for prefix in typ.id_prefixes:
                self.check_prefix(prefix)
        for slot in self.schema.slots.values():
            self.check_prefix(slot.slot_uri)
            for prefix in slot.mappings:
                self.check_prefix(prefix)
            for prefix in slot.id_prefixes:
                self.check_prefix(prefix)
        for cls in self.schema.classes.values():
            self.check_prefix(cls.class_uri)
            for prefix in cls.mappings:
                self.check_prefix(prefix)
            for prefix in cls.id_prefixes:
                self.check_prefix(prefix)

    def check_prefix(self, prefix: str) -> None:
        prefix = self.namespaces.prefix_for(prefix)
        if prefix and prefix not in self.namespaces:
            self.logger.warning(f"Unrecognized prefix: {prefix}")
            self.namespaces[prefix] = f"http://example.org/UNKNOWN/{prefix}/"

    @staticmethod
    def slot_name_for(slot: SlotDefinition) -> str:
        return underscore(slot.alias if slot.alias else slot.name)

    def raise_value_error(self, error: str, loc_str: Optional[Union[TypedNode, str]] = None) -> None:
        raise ValueError(f'{"" if loc_str is None or not getattr(loc_str, "loc") else (loc_str.loc() + " ")} {error}')

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
                return rval
        else:
            return None

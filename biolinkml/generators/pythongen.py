import os
import re
import sys
from typing import Optional, Tuple, List, Union, TextIO, Callable, Dict, Iterator, cast, Set

import click
from rdflib import URIRef

import biolinkml
from biolinkml.generators import PYTHON_GEN_VERSION
from biolinkml.meta import SchemaDefinition, SlotDefinition, ClassDefinition, ClassDefinitionName, \
    SlotDefinitionName, DefinitionName, Element, TypeDefinition, Definition
from biolinkml.utils.formatutils import camelcase, underscore, be, wrapped_annotation, split_line, sfx
from biolinkml.utils.generator import Generator, shared_arguments
from biolinkml.utils.ifabsent_functions import ifabsent_value_declaration, ifabsent_postinit_declaration, \
    default_curie_or_uri
from biolinkml.utils.metamodelcore import builtinnames
from includes import types


class PythonGenerator(Generator):
    generatorname = os.path.basename(__file__)
    generatorversion = PYTHON_GEN_VERSION
    valid_formats = ['py']
    visit_all_class_slots = False

    def __init__(self, schema: Union[str, TextIO, SchemaDefinition], format: str = valid_formats[0],
                 emit_metadata: bool = True, **kwargs) -> None:
        self.sourcefile = schema
        self.emit_prefixes: Set[str] = set()
        if format is None:
            format = self.valid_formats[0]
        super().__init__(schema, format, emit_metadata=emit_metadata, **kwargs)
        if not self.schema.source_file and isinstance(self.sourcefile, str) and '\n' not in self.sourcefile:
            self.schema.source_file = os.path.basename(self.sourcefile)

    def visit_schema(self, **kwargs) -> None:
        # Add explicitly declared prefixes
        self.emit_prefixes.update([p.prefix_prefix for p in self.schema.prefixes.values()])

        # Add all emit statements
        self.emit_prefixes.update(self.schema.emit_prefixes)

        # Add the default prefix
        if self.schema.default_prefix:
            self.emit_prefixes.add(self.namespaces.prefix_for(self.schema.default_prefix))

    def visit_class(self, cls: ClassDefinition) -> bool:
        if not cls.imported_from:
            cls_prefix = self.namespaces.prefix_for(cls.class_uri)
            if cls_prefix:
                self.emit_prefixes.add(cls_prefix)
            self.add_mappings(cls)
        return False

    def visit_slot(self, aliased_slot_name: str, slot: SlotDefinition) -> None:
        if not slot.imported_from:
            slot_prefix = self.namespaces.prefix_for(slot.slot_uri)
            if slot_prefix:
                self.emit_prefixes.add(slot_prefix)
            self.add_mappings(slot)

    def visit_type(self, typ: TypeDefinition) -> None:
        if not typ.imported_from:
            type_prefix = self.namespaces.prefix_for(typ.uri)
            if type_prefix:
                self.emit_prefixes.add(type_prefix)

    def add_mappings(self, defn: Definition) -> None:
        """
        Process any mappings in defn, adding all of the mappings prefixes to the namespace map
        :param defn: Class or Slot Definition
        """
        self.add_id_prefixes(defn)
        for mapping in defn.mappings:
            if '://' in mapping:
                mcurie = self.namespaces.curie_for(mapping)
                print(f"No namespace defined for URI: {mapping}", file=sys.stderr)
                if mcurie is None:
                    return        # Absolute path - no prefix/name
                else:
                    mapping = mcurie
            if ':' not in mapping or len(mapping.split(':')) != 2:
                raise ValueError(f"Definition {defn.name} - unrecognized mapping: {mapping}")
            ns = mapping.split(':')[0]
            self.emit_prefixes.add(ns)

    def add_id_prefixes(self, element: Element) -> None:
        self.emit_prefixes.update(element.id_prefixes)

    def gen_schema(self) -> str:
        split_descripton = '\n#              '.join(split_line(be(self.schema.description), split_len=100))
        head = f'''# Auto generated from {self.schema.source_file} by {self.generatorname} version: {self.generatorversion}
# Generation date: {self.schema.generation_date}
# Schema: {self.schema.name}
#''' if self.emit_metadata else ''

        return f'''{head}
# id: {self.schema.id}
# description: {split_descripton}
# license: {be(self.schema.license)}

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
{self.gen_imports()}

metamodel_version = "{self.schema.metamodel_version}"

# Overwrite dataclasses _init_fn to add **kwargs in __init__
dataclasses._init_fn = dataclasses_init_fn_with_kwargs

# Namespaces
{self.gen_namespaces()}


# Types
{self.gen_typedefs()}
# Class references
{self.gen_references()}

{self.gen_classdefs()}


# Slots
class slots:
    pass

{self.gen_slots()}'''

    def end_schema(self, **_):
        print(re.sub(r' +\n', '\n', self.gen_schema().replace('\t', '    ')).strip(' '), end='')

    def gen_imports(self) -> str:
        listents = [f"from {k} import {', '.join(v)}" for k, v in self.gen_import_list().items()]
        return '\n'.join(listents)

    def gen_import_list(self) -> Dict[str, List[str]]:
        """
        Generate a list of types to import

        :return: source file followed by elements to import
        """
        class ImportList:
            def __init__(self, schema_location: str):
                self.schema_location = schema_location
                self.v: Dict[str, Set[str]] = {}

            def add_element(self, e: Element) -> None:
                if e.imported_from:
                    if str(e.imported_from) == biolinkml.METATYPE_URI:
                        # TODO: figure out how to make this sort of stuff part of the model
                        self.v.setdefault(types.__name__, set()).add(camelcase(e.name))
                    elif str(e.imported_from) == biolinkml.BIOLINK_MODEL_URI:
                        self.v.setdefault(biolinkml.BIOLINK_MODEL_PYTHON_LOC, set()).add(camelcase(e.name))
                    elif e.imported_from.__contains__('://'):
                        raise ValueError(f"Cannot map {e.imported_from} into a python import statement")
                    else:
                        self.v.setdefault(types.__name__, set()).add(camelcase(e.name))

            def add_entry(self, path: Union[str, URIRef], name: str) -> None:
                path = str(path)
                if path == biolinkml.METATYPE_URI:
                    # TODO: figure out how to make this sort of stuff part of the model
                    self.v.setdefault(types.__name__, set()).add(name)
                elif path == biolinkml.BIOLINK_MODEL_URI:
                    self.v.setdefault(biolinkml.BIOLINK_MODEL_PYTHON_LOC, set()).add(name)
                elif path.__contains__('://'):
                    raise ValueError(f"Cannot map {path} into a python import statement")
                else:
                    self.v.setdefault(path.replace('/', '.'), set()).add(name)

            def values(self) -> Dict[str, List[str]]:
                return {k: sorted(self.v[k]) for k in sorted(self.v.keys())}

        def add_type_ref(typ: TypeDefinition) -> None:
            if not typ.typeof and typ.base and typ.base not in builtinnames:
                if '.' in typ.base:
                    rval.add_entry(*typ.base.rsplit('.'))
                else:
                    rval.add_entry('biolinkml.utils.metamodelcore', typ.base)
            if typ.typeof:
                add_type_ref(self.schema.types[typ.typeof])
            rval.add_element(typ)

        def add_slot_range(slot: SlotDefinition) -> None:
            if slot.range:
                if slot.range in self.schema.types:
                    add_type_ref(self.schema.types[slot.range])
                else:
                    cls = self.schema.classes[slot.range]
                    if cls.imported_from:
                        if self.class_identifier(cls):
                            rval.add_entry(cls.imported_from, self.class_identifier_path(cls, False)[-1])
                        if slot.inlined:
                            rval.add_element(cls)

        rval = ImportList(self.schema_location)
        for typ in self.schema.types.values():
            if not typ.imported_from:
                add_type_ref(typ)
        for slot in self.schema.slots.values():
            if not slot.imported_from:
                if slot.is_a:
                    parent = self.schema.slots[slot.is_a]
                    if parent.imported_from:
                        rval.add_element(self.schema.slots[slot.is_a])
                if slot.domain:
                    domain = self.schema.classes[slot.domain]
                    if domain.imported_from:
                        rval.add_element(self.schema.classes[slot.domain])
                add_slot_range(slot)
        for cls in self.schema.classes.values():
            if not cls.imported_from:
                if cls.is_a:
                    parent = self.schema.classes[cls.is_a]
                    if parent.imported_from:
                        rval.add_element(self.schema.classes[cls.is_a])
                        if self.class_identifier(parent):
                            rval.add_entry(parent.imported_from, self.class_identifier_path(parent, False)[-1])
                for slotname in cls.slots:
                    add_slot_range(self.schema.slots[slotname])

        return rval.values()

    def gen_namespaces(self) -> str:
        dflt_prefix = default_curie_or_uri(self)
        dflt = f"CurieNamespace('', '{sfx(dflt_prefix)}')" if ':/' in dflt_prefix else dflt_prefix.upper()
        return '\n'.join([
            f"{pfx.upper().replace('.', '_').replace('-', '_')} = CurieNamespace('{pfx.replace('.', '_')}', '{self.namespaces[pfx]}')"
            for pfx in sorted(self.emit_prefixes) if pfx in self.namespaces
        ] + [f"DEFAULT_ = {dflt}"])


    def gen_references(self) -> str:
        """ Generate python type declarations for all identifiers (primary keys)
        """
        rval = []
        for cls in self.schema.classes.values():
            if not cls.imported_from:
                pkeys = self.primary_keys_for(cls)
                if pkeys:
                    for pk in pkeys:
                        classname = camelcase(cls.name) + camelcase(self.aliased_slot_name(pk))
                        if cls.is_a and self.class_identifier(cls.is_a):
                            parents = self.class_identifier_path(cls.is_a, False)
                        else:
                            parents = self.slot_type_path(self.schema.slots[pk])
                        # TODO: check if parents[-1] is str, float, or int. changed it to extedned_
                        parent_cls = 'extended_' + parents[-1] if parents[-1] in ['str', 'float', 'int'] else parents[-1]
                        rval.append(f'class {classname}({parent_cls}):\n\tpass')
                        break       # We only do the first primary key
        return '\n\n\n'.join(rval)

    def gen_typedefs(self) -> str:
        """ Generate python type declarations for all defined types """
        rval = []
        for typ in self.schema.types.values():
            if not typ.imported_from:
                typname = camelcase(typ.name)
                desc = f'\n\t""" {typ.description} """' if typ.description else ''

                if typ.typeof:
                    parent_typename = camelcase(typ.typeof)
                    rval.append(f'class {typname}({parent_typename}):{desc}\n\t{self.gen_type_meta(typ)}\n\n')
                else:
                    base_base = typ.base.rsplit('.')[-1]
                    rval.append(f'class {typname}({base_base}):{desc}\n\t{self.gen_type_meta(typ)}\n\n')
        return '\n'.join(rval)

    def gen_classdefs(self) -> str:
        """ Create class definitions for all non-mixin classes in the model
            Note that apply_to classes are transformed to mixins
        """
        return '\n'.join([self.gen_classdef(v) for v in self.schema.classes.values()
                          if not v.mixin and not v.imported_from])

    def gen_classdef(self, cls: ClassDefinition) -> str:
        """ Generate python definition for class cls """

        parentref = f'({self.formatted_element_name(cls.is_a, True) if cls.is_a else "YAMLRoot"})'
        slotdefs = self.gen_class_variables(cls)
        postinits = self.gen_postinits(cls)

        wrapped_description = f'\n\t"""\n\t{wrapped_annotation(be(cls.description))}\n\t"""' if be(cls.description) else ''

        return ('\n@dataclass' if slotdefs else '') + \
               f'\nclass {self.class_or_type_name(cls.name)}{parentref}:{wrapped_description}' + \
               f'\n\t{self.gen_inherited_slots(cls)}\n' + \
               f'\n\t{self.gen_class_meta(cls)}\n' + \
               (f'\n\t{slotdefs}' if slotdefs else '') + \
               (f'\n{postinits}' if postinits else '')

    def gen_inherited_slots(self, cls: ClassDefinition) -> str:
        inherited_slots = []
        for slotname in cls.slots:
            slot = self.schema.slots[slotname]
            if slot.inherited:
                inherited_slots.append(slot.alias if slot.alias else slotname)
        inherited_slots_str = ", ".join([f'"{underscore(s)}"' for s in inherited_slots])
        return f"_inherited_slots: ClassVar[List[str]] = [{inherited_slots_str}]"

    def gen_class_meta(self, cls: ClassDefinition) -> str:
        class_class_uri = self.namespaces.uri_for(cls.class_uri)
        if class_class_uri:
            cls_python_uri = self.namespaces.curie_for(class_class_uri, default_ok=False, pythonform=True)
            class_class_curie = self.namespaces.curie_for(class_class_uri, default_ok=False, pythonform=False)
        else:
            cls_python_uri = None
            class_class_curie = None
        if class_class_curie:
            class_class_curie = f'"{class_class_curie}"'
        class_class_uri = cls_python_uri if cls_python_uri else f'URIRef("{class_class_uri}")'
        class_model_uri = self.namespaces.uri_or_curie_for(self.schema.default_prefix or "DEFAULT_", camelcase(cls.name))
        if ':/' in class_model_uri:
            class_model_uri = f'URIRef("{class_model_uri}")'
        else:
            ns, ln = class_model_uri.split(':', 1)
            class_model_uri = f"{ns.upper()}.{ln}"

        vars = [f'class_class_uri: ClassVar[URIRef] = {class_class_uri}',
                f'class_class_curie: ClassVar[str] = {class_class_curie}',
                f'class_name: ClassVar[str] = "{cls.name}"',
                f'class_model_uri: ClassVar[URIRef] = {class_model_uri}']
        return "\n\t".join(vars)

    def gen_type_meta(self, typ: TypeDefinition) -> str:
        type_class_uri = self.namespaces.uri_for(typ.uri)
        if type_class_uri:
            type_python_uri = self.namespaces.curie_for(type_class_uri, default_ok=False, pythonform=True)
            type_class_curie = self.namespaces.curie_for(type_class_uri, default_ok=False, pythonform=False)
        else:
            type_python_uri = None
            type_class_curie = None
        if type_class_curie:
            type_class_curie = f'"{type_class_curie}"'
        type_class_uri = type_python_uri if type_python_uri else f'URIRef("{type_class_uri}")'
        type_model_uri = self.namespaces.uri_or_curie_for(self.schema.default_prefix, camelcase(typ.name))
        if ':/' in type_model_uri:
            type_model_uri = f'URIRef("{type_model_uri}")'
        else:
            ns, ln = type_model_uri.split(':', 1)
            ln_suffix = f".{ln}" if ln.isidentifier() else f'["{ln}"]'
            type_model_uri = f"{ns.upper()}{ln_suffix}"
        vars = [f'type_class_uri = {type_class_uri}',
                f'type_class_curie = {type_class_curie}',
                f'type_name = "{typ.name}"',
                f'type_model_uri = {type_model_uri}']
        return "\n\t".join(vars)


    def gen_class_variables(self,
                            cls: ClassDefinition) -> str:
        """
        Generate the variable declarations for a dataclass.

        :param cls: class containing variables to be rendered in inheritence hierarchy
        :return: variable declarations for target class and its ancestors
        """
        def overridden_slot(slotname: SlotDefinitionName) -> bool:
            """ Determine whether slotname is overridden in any of the descendant classes """
            return False
            # return bool(set(ancestor_path)
            #             .intersection(set(self.synopsis.slotusages.get(self.aliased_slot_name(slotname), []))))

        initializers = []

        is_root = not cls.is_a
        domain_slots = self.domain_slots(cls)

        # Root keys and identifiers go first.  Note that even if a key or identifier is overridden it still
        # appears at the top of the list, as we need to keep the position
        slot_variables = self._slot_iter(cls, lambda slot: (slot.identifier or slot.key) and not slot.ifabsent,
                                         first_hit_only=True)
        initializers += [self.gen_class_variable(cls, slot, not is_root) for slot in slot_variables]

        # Required slots
        slot_variables = self._slot_iter(cls,
                                         lambda slot: slot.required and not slot.identifier and not slot.key and not slot.ifabsent)
        initializers += [self.gen_class_variable(cls, slot, not is_root) for slot in slot_variables]

        # Required or key slots with default values
        slot_variables = self._slot_iter(cls,
                                         lambda slot: slot.ifabsent and slot.required)
        initializers += [self.gen_class_variable(cls, slot, not is_root) for slot in slot_variables]

        # Followed by everything else
        slot_variables = self._slot_iter(cls, lambda slot: not slot.required and not overridden_slot(slot.name)
                                                           and slot in domain_slots)
        initializers += [self.gen_class_variable(cls, slot, True) for slot in slot_variables]

        return '\n\t'.join(initializers)

    def gen_class_variable(self, cls: ClassDefinition, slot: SlotDefinition, can_be_positional: bool) -> str:
        """
        Generate a class variable declaration for the supplied slot

        :param cls: Owning class
        :param slot: slot definition
        :param can_be_positional: True means that positional parameters are allowed
        :return: Initializer string
        """
        slotname = self.slot_name(slot.name)
        slot_range, default_val = self.range_cardinality(slot, cls, can_be_positional)
        ifabsent_text = ifabsent_value_declaration(slot.ifabsent, self, cls, slot) if slot.ifabsent is not None else None
        if ifabsent_text:
            default = f'= {ifabsent_text}'
        else:
            default = f'= {default_val}' if default_val else ''
        return f'''{slotname}: {slot_range} {default}'''

    def range_cardinality(self, slot: SlotDefinition, cls: Optional[ClassDefinition], positional_allowed: bool) \
            -> Tuple[str, Optional[str]]:
        """
        Return the range type including initializers, etc.

        :param slot: slot to generate type for
        :param cls: containing class -- used to render key slots correctly.  If absent, slot is an add-in
        :param positional_allowed: True Means that we are in the positional space
        :return: python property name and initializer (if any)
        """
        range_type, parent_type, _ = self.class_reference_type(slot, cls)

        if slot.multivalued:
            pkey = self.class_identifier(slot.range, keys_count=True)
            if self.is_key_value_class(cast(DefinitionName, slot.range)):
                return range_type, 'empty_dict()'
            elif slot.inlined and pkey:
                base_key = self.gen_class_reference(self.class_identifier_path(slot.range, False))
                return f'Dict[{base_key}, {range_type}]', 'empty_dict()'
            else:
                return f'List[{range_type}]', 'empty_list()'
        elif slot.required:
            return range_type, ('None' if positional_allowed else None)
        else:
            return f'Optional[{range_type}]', 'None'

    def class_reference_type(self, slot: SlotDefinition, cls: Optional[ClassDefinition]) \
            -> Tuple[str, str, str]:
        """
        Return the type of a slot referencing a class

        :param slot: slot to be typed
        :param cls: owning class.  Used for generating key references
        :return: Python class reference type, most proximal type, most proximal type name
        """
        assert not (slot.key or slot.identifier) or cls, "Key slots must have a domain"
        rangelist = self.class_identifier_path(cls, False) if slot.key or slot.identifier else self.slot_type_path(slot)
        prox_type = self.slot_type_path(slot)[-1].rsplit('.')[-1]
        prox_type_name = rangelist[-1]

        # Python version < 3.7 requires quoting forward references
        if cls and slot.inlined and slot.range in self.schema.classes and self.forward_reference(slot.range, cls.name):
            rangelist[-1] = f'"{rangelist[-1]}"'
        return f"{self.gen_class_reference(rangelist)}", prox_type, prox_type_name

    @staticmethod
    def gen_class_reference(rangelist: List[str]) -> str:
        """
        Return a basic or a union type depending on the number of elements in range list

        :param rangelist: List of types from distal to proximal
        :return:
        """
        base = rangelist[0].rsplit('.')[-1]
        return f"Union[{base}, {rangelist[-1]}]" if len(rangelist) > 1 else base

    def gen_postinits(self, cls: ClassDefinition) -> str:
        """ Generate all the typing and existence checks post initialize
        """
        post_inits_pre_super = []
        for slot in self.domain_slots(cls):
            if slot.ifabsent:
                dflt = ifabsent_postinit_declaration(slot.ifabsent, self, cls, slot)
                if dflt and dflt != "None":
                    post_inits_pre_super.append(f'if self.{self.slot_name(slot.name)} is None:')
                    post_inits_pre_super.append(f'\tself.{self.slot_name(slot.name)} = {dflt}')

        post_inits = []
        if not cls.abstract:
            pkeys = self.primary_keys_for(cls)
            for pkey in pkeys:
                slot = self.schema.slots[pkey]
                # TODO: Remove the bypass whenever we get default_range fixed
                if not slot.ifabsent or True:
                    post_inits.append(self.gen_postinit(cls, slot))
        else:
            pkeys = []
        for slot in self.domain_slots(cls):
            # TODO: Remove the bypass whenever we get default_range fixed
            if slot.name not in pkeys and (not slot.ifabsent or True):
                post_inits.append(self.gen_postinit(cls, slot))

        post_inits_pre_super_line = '\n\t\t'.join([p for p in post_inits_pre_super if p]) + \
                                    ('\n\t\t' if post_inits_pre_super else '')
        post_inits_line = '\n\t\t'.join([p for p in post_inits if p])
        return (f'''
    def __post_init__(self, **kwargs: Dict[str, Any]):
        {post_inits_pre_super_line}{post_inits_line}
        super().__post_init__(**kwargs)''' + '\n') if post_inits_line or post_inits_pre_super_line else ''

    def is_key_value_class(self, range_name: DefinitionName) -> bool:
        """
        Return True if range_name references a class with exactly one key and one value

        :param range_name: class definition (name)
        :return: True if meets the special case
        """
        rng = self.schema.classes.get(range_name)
        if rng:
            pkeys = self.primary_keys_for(rng)
            if pkeys:
                return len(rng.slots) - len(pkeys) == 1
        return False

    def gen_postinit(self, cls: ClassDefinition, slot: SlotDefinition) -> Optional[str]:
        """ Generate python post init rules for slot in class
        """
        rlines: List[str] = []
        slotname = self.slot_name(slot.name)
        range_type_name, base_type, base_type_name = self.class_reference_type(slot, cls)
        single_typed = range_type_name == base_type
        root_definition = not cls.is_a

        # Generate existence check for required slots.  Note that inherited classes have to check post-init because
        # named variables can't be mixed in the class signature
        if slot.required:
            # If we have a root class, the required part is set by the type.  If it is inherited, we have to add
            # the following
            if not slot.multivalued:
                rlines.append(f'if self.{slotname} is None:')
                rlines.append(f'\traise ValueError(f"{slotname} must be supplied")')
            else:
                rlines.append(f'if not isinstance(self.{slotname}, list) or len(self.{slotname}) == 0:')
                rlines.append(f'\traise ValueError(f"{slotname} must be a non-empty list")')
        if slot.range in self.schema.classes or slot.range in self.schema.types:
            indent = len(f'self.{slotname} = [') * ' '
            if not slot.multivalued:
                if not single_typed:
                    if slot.required:
                        rlines.append(f'if not isinstance(self.{slotname}, {base_type_name}):')
                    else:
                        rlines.append(f'if self.{slotname} is not None and '
                                      f'not isinstance(self.{slotname}, {base_type_name}):')
                    # Another really wierd case -- a class that has no properties
                    if slot.range in self.schema.classes and not self.schema.classes[slot.range].slots:
                        rlines.append(f'\tself.{slotname} = {base_type_name}()')
                    else:
                        if self.class_identifier(slot.range) or slot.range in self.schema.types:
                            rlines.append(f'\tself.{slotname} = {base_type_name}(self.{slotname})')
                        else:
                            rlines.append(f'\tself.{slotname} = {base_type_name}(**self.{slotname})')
            elif slot.inlined:
                slot_range_cls = self.schema.classes[slot.range]
                pkeys = self.primary_keys_for(slot_range_cls)
                if pkeys:
                    # Special situation -- if there are only two values: primary key and value,
                    # we load it is a list, not a dictionary
                    if self.is_key_value_class(cast(DefinitionName, slot.range)):
                        class_init = '(k, v)'
                    else:
                        pkey_name = self.formatted_element_name(pkeys[0])
                        class_init = f'({pkey_name}=k, **({{}} if v is None else v))'
                    rlines.append(f'for k, v in self.{slotname}.items():')
                    rlines.append(f'\tif not isinstance(v, {base_type_name}):')
                    rlines.append(f'\t\tself.{slotname}[k] = {base_type_name}{class_init}')
                elif not single_typed:
                    rlines.append(f'self.{slotname} = [v if isinstance(v, {base_type_name})')
                    rlines.append(f'{indent}else {base_type_name}(**v) for v in self.{slotname}]')
            elif not single_typed:
                rlines.append(f'self.{slotname} = [v if isinstance(v, {base_type_name})')
                rlines.append(f'{indent}else {base_type_name}(v) for v in self.{slotname}]')
        return '\n\t\t'.join(rlines)


    def _slot_iter(self, cls: ClassDefinition, test: Callable[[SlotDefinition], bool], first_hit_only: bool = False) \
            -> Iterator[SlotDefinition]:
        """ Return the representation for the set of own slots in cls that pass test

        :param cls: Class containing a set of slots
        :param test: Slot test function
        :param first_hit_only: True means stop on first match.  False means generate all
        :return: Set of slots that match
        """
        for slot in self.all_slots(cls):
            if test(slot):
                yield slot
                if first_hit_only:
                    break

    def primary_keys_for(self, cls: ClassDefinition) -> List[SlotDefinitionName]:
        """ Return the primary key for cls

        @param cls: class to get keys for
        @return: List of primary keys
        """
        return [slot_name for slot_name in cls.slots
                if self.schema.slots[slot_name].key or self.schema.slots[slot_name].identifier]

    def key_name_for(self, class_name: ClassDefinitionName) -> Optional[str]:
        for slot_name in self.primary_keys_for(self.schema.classes[class_name]):
            return self.formatted_element_name(class_name, True) + camelcase(slot_name)
        return None

    def range_type_name(self, slot: SlotDefinition) -> str:
        """ Generate the type name for the slot """
        cidpath = self.slot_type_path(slot)
        if len(cidpath) < 2:
            return cidpath[0]
        else:
            return f"Union[{cidpath[0]}, {cidpath[-1]}]"

    def forward_reference(self, slot_range: str, owning_class: str) -> bool:
        """ Determine whether slot_range is a forward reference """
        if slot_range in self.schema.classes and self.schema.classes[slot_range].imported_from:
            return False
        for cname in self.schema.classes:
            if cname == owning_class:
                return True             # Occurs on or after
            elif cname == slot_range:
                return False            # Occurs before
        return True

    def python_uri_for(self, uriorcurie: Union[str, URIRef]) -> Tuple[str, Optional[str]]:
        """ Return the python form of uriorcurie
        :param uriorcurie:
        :return: URI and CURIE form
        """
        ns, ln = self.namespaces.prefix_suffix(uriorcurie)
        if ns == '':
            ns = 'DEFAULT_'
        if ns is None:
            return f'"str(uriorcurie)"', None
        return ns.upper() + (f".{ln}" if ln.isidentifier() else f"['{ln}']"), ns.upper() + f".curie('{ln}')"


    def gen_slots(self) -> str:
        return '\n\n'.join([self.gen_slot(slot) for slot in self.schema.slots.values() if not slot.imported_from])

    def gen_slot(self, slot: SlotDefinition) -> str:
        python_slot_name = underscore(slot.name)
        slot_uri, slot_curie = self.python_uri_for(slot.slot_uri)
        slot_model_uri, slot_model_curie = \
            self.python_uri_for(self.namespaces.uri_or_curie_for(self.schema.default_prefix, python_slot_name))
        domain = camelcase(slot.domain) if slot.domain and not self.schema.classes[slot.domain].mixin else "None"
        # Going to omit the range on keys where the domain isn't specified (for now)
        if slot.domain is None and (slot.key or slot.identifier):
            rnge = "URIRef"
        else:
            rnge, _ = self.range_cardinality(slot, self.schema.classes[slot.domain] if slot.domain else None, True)
        if slot.mappings:
            map_texts = [self.namespaces.curie_for(self.namespaces.uri_for(m), default_ok=True, pythonform=True)
                         for m in slot.mappings if m != slot.slot_uri]
        else:
            map_texts = []
        if map_texts:
            mappings = ', mappings = [' + ', '.join(map_texts)+ ']'
        else:
            mappings = ''
        return f"""slots.{python_slot_name} = Slot(uri={slot_uri}, name="{slot.name}", curie={slot_curie},
                      model_uri={slot_model_uri}, domain={domain}, range={rnge}{mappings})"""


@shared_arguments(PythonGenerator)
@click.command()
@click.option("--head/--no-head", default=True, help="Emit metadata heading")
def cli(yamlfile, head=True, **args):
    """ Generate python classes to represent a biolink model """
    print(PythonGenerator(yamlfile, emit_metadata=head, **args).serialize(emit_metadata=head, **args))

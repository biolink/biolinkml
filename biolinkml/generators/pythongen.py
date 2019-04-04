import inspect
import os
import re
from typing import Optional, Tuple, List, Union, TextIO, Callable, Dict, Iterator, cast, Set

import click

import biolinkml
from biolinkml.generators import PYTHON_GEN_VERSION
from biolinkml.meta import SchemaDefinition, SlotDefinition, ClassDefinition, ClassDefinitionName, \
    SlotDefinitionName, DefinitionName, Element, TypeDefinition
from biolinkml.utils.formatutils import camelcase, underscore, be, wrapped_annotation, split_line
from biolinkml.utils.generator import Generator
from biolinkml.utils.metamodelcore import builtinnames
from includes import types


class PythonGenerator(Generator):
    generatorname = os.path.basename(__file__)
    generatorversion = PYTHON_GEN_VERSION
    valid_formats = ['py']
    visit_all_class_slots = False

    def __init__(self, schema: Union[str, TextIO, SchemaDefinition], fmt: str=valid_formats[0],
                 emit_metadata: bool=True) -> None:
        self.sourcefile = schema
        super().__init__(schema, fmt, emit_metadata)
        if not self.schema.source_file and isinstance(self.sourcefile, str) and '\n' not in self.sourcefile:
            self.schema.source_file = os.path.basename(self.sourcefile)

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

from typing import Optional, List, Union, Dict, ClassVar
from dataclasses import dataclass
from biolinkml.utils.metamodelcore import empty_list, empty_dict
from biolinkml.utils.yamlutils import YAMLRoot
{self.gen_imports()}

metamodel_version = "{self.schema.metamodel_version}"

# Types
{self.gen_typedefs()}
# Class references
{self.gen_references()}

{self.gen_classdefs()}'''

    def end_schema(self):
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
                    elif e.imported_from.__contains__('://'):
                        raise(NotImplementedError, f"Cannot map {e.imported_from} into a python import statement")
                    else:
                        anchor_path = os.path.dirname(self.schema_location)
                        abs_import_path = os.path.join(anchor_path, e.imported_from) \
                            if not os.path.isabs(e.imported_from) else e.imported_from
                        python_base_dir = os.path.dirname(os.path.dirname(inspect.getfile(biolinkml)))
                        python_import_dir = os.path.relpath(abs_import_path, python_base_dir)
                        self.v.setdefault(python_import_dir.replace('/', '.'), set()).add(camelcase(e.name))

            def add_entry(self, path: str, name: str) -> None:
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

        rval = ImportList(self.schema_location)
        for typ in self.schema.types.values():
            if not typ.imported_from:
                add_type_ref(typ)
        for cls in self.schema.classes.values():
            if not cls.imported_from:
                if cls.is_a:
                    parent = self.schema.classes[cls.is_a]
                    if parent.imported_from:
                        rval.add_element(self.schema.classes[cls.is_a])
                        if self.class_identifier(parent):
                            rval.add_entry(parent.imported_from, self.class_identifier_path(parent, False)[-1])
                for slotname in cls.slots:
                    slot = self.schema.slots[slotname]
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

        return rval.values()

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
                        rval.append(f'class {classname}({parents[-1]}):\n\tpass')
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
                    rval.append(f'class {typname}({parent_typename}):{desc}\n\tpass\n\n')
                else:
                    base_base = typ.base.rsplit('.')[-1]
                    rval.append(f'class {typname}({base_base}):{desc}\n\tpass\n\n')
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
        inheritedslots = self.gen_inherited_slots(cls)
        slotdefs = self.gen_class_variables(cls)
        postinits = self.gen_postinits(cls)
        if not slotdefs:
            slotdefs = 'pass'
        wrapped_description = f'''
    """
    {wrapped_annotation(be(cls.description))}
    """''' if be(cls.description) else ''
        return f'''
@dataclass
class {self.class_or_type_name(cls.name)}{parentref}:{wrapped_description}
    {inheritedslots}
    {slotdefs}
    {postinits}'''

    def gen_inherited_slots(self, cls: ClassDefinition) -> str:
        inherited_slots = []
        for slotname in cls.slots:
            slot = self.schema.slots[slotname]
            if slot.inherited:
                inherited_slots.append(slot.alias if slot.alias else slotname)
        inherited_slots_str = ", ".join([f'"{underscore(s)}"' for s in inherited_slots])
        return f"_inherited_slots: ClassVar[List[str]] = [{inherited_slots_str}]"

    def gen_class_variables(self,
                            cls: ClassDefinition,
                            target_class: ClassDefinition = None,
                            ancestor_path: List[ClassDefinitionName] = None) -> str:
        """
        Generate the variable declarations for a dataclass.

        :param cls: class containing variables to be rendered in inheritence hierarchy
        :param target_class: ultimate path being generated
        :param ancestor_path: class names from cls to target class -- used to strip slot_usage overrides
        :return: variable declarations for target class and its ancestors
        """
        def overridden_slot(slotname: SlotDefinitionName) -> bool:
            """ Determine whether slotname is overridden in any of the descendant classes """
            return bool(set(ancestor_path)
                        .intersection(set(self.synopsis.slotusages.get(self.aliased_slot_name(slotname), []))))

        if target_class is None:
            target_class = cls

        if ancestor_path is None:
            ancestor_path = []

        if cls.is_a:
            ancestor_path.append(cls.name)
            initializers = [self.gen_class_variables(self.schema.classes[cls.is_a], target_class, ancestor_path)]
        else:
            initializers = []

        is_root = not cls.is_a and not ancestor_path
        is_leaf = target_class == cls
        if cls.slots:
            initializers += ['', f"# === {cls.name} ==="]

            # Root keys and identifiers go first.  Note that even if a key or identifier is overridden it still
            # appears at the top of the list, as we want to keep the positionality...
            slot_variables = list(self._slot_iter(cls,
                                                  lambda slot: (slot.identifier or slot.key) and (
                                                               not overridden_slot(slot.name) or is_leaf),
                                                  first_hit_only=True))
            initializers += [self.gen_class_variable(target_class, slot, not is_root) for slot in slot_variables]


            # Required slots
            slot_variables = self._slot_iter(cls,
                                             lambda slot: slot.required and not slot.identifier and not slot.key
                                                          and not overridden_slot(slot.name))
            initializers +=  [self.gen_class_variable(target_class, slot, not is_root) for slot in slot_variables]

            # Followed by everything else
            slot_variables = self._slot_iter(cls, lambda slot: not slot.required and not overridden_slot(slot.name))
            initializers += [self.gen_class_variable(target_class, slot, True) for slot in slot_variables]

        if ancestor_path:
            ancestor_path.pop()
        if not ancestor_path and not initializers:
            initializers = ['pass']

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
        default = f'= {default_val}' if default_val else ''
        return f'''{slotname}: {slot_range} {default}'''

    def range_cardinality(self, slot: SlotDefinition, cls: ClassDefinition, positional_allowed: bool) \
            -> Tuple[str, Optional[str]]:
        """
        Return the range type including initializers, etc.

        :param slot: slot to generate type for
        :param cls: containing class -- used to render key slots correctly
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

    def class_reference_type(self, slot: SlotDefinition, cls: ClassDefinition) \
            -> Tuple[str, str, str]:
        """
        Return the type of a slot referencing a class

        :param slot: slot to be typed
        :param cls: owning class.  Used for generating key references
        :return: Python class reference type, most proximal type, most proximal type name
        """
        rangelist = self.class_identifier_path(cls, False) if slot.key or slot.identifier else self.slot_type_path(slot)
        prox_type = self.slot_type_path(slot)[-1].rsplit('.')[-1]
        prox_type_name = rangelist[-1]

        # Python version < 3.7 requires quoting forward references
        if slot.inlined and slot.range in self.schema.classes and self.forward_reference(slot.range, cls.name):
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
        post_inits = []
        if not cls.abstract:
            pkeys = self.primary_keys_for(cls)
            for pkey in pkeys:
                post_inits.append(self.gen_postinit(cls, self.schema.slots[pkey]))
        else:
            pkeys = []
        for slot in self.own_slots(cls):
            if slot.name not in pkeys:
                post_inits.append(self.gen_postinit(cls, slot))
        post_inits_line = '\n\t\t'.join([p for p in post_inits if p])
        return (f'''
    def _fix_elements(self):
        super()._fix_elements()
        {post_inits_line}''' + '\n') if post_inits_line else ''

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
        if slot.required and root_definition:
            if not root_definition:
                rlines.append(f'if self.{slotname} is None:')
                rlines.append(f'\traise ValueError(f"{slotname} must be supplied")')
            if not single_typed:
                rlines.append(f'if not isinstance(self.{slotname}, {base_type_name}):')
                rlines.append(f'\tself.{slotname} = {base_type_name}(self.{slotname})')
        elif slot.range in self.schema.classes or slot.range in self.schema.types:
            indent = len(f'self.{slotname} = [') * ' '
            if not slot.multivalued:
                if not single_typed:
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
        for slot in self.own_slots(cls):
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



@click.command()
@click.argument("yamlfile", type=click.Path(exists=True, dir_okay=False))
@click.option("--format", "-f", default='py', type=click.Choice(PythonGenerator.valid_formats), help="Output format")
@click.option("--head/--no-head", default=True, help="Emit metadata heading")
def cli(yamlfile, format, head):
    """ Generate python classes to represent a biolink model """
    print(PythonGenerator(yamlfile, format, head).serialize())

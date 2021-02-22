from dataclasses import dataclass, field
from typing import Dict, Set, List, Union, cast

from biolinkml.utils.generator import Generator
from biolinkml.generators.pythongen import PythonGenerator
from biolinkml.utils.schemaloader import SchemaLoader
from biolinkml.meta import SchemaDefinition, Element, Definition, ClassDefinition, SlotDefinition

@dataclass
class SqlTransformer():
    """
    Transforms from one SchemaDefinition to another.

    Note that this does not actually generate SQL DDL statements. This class is for
    pre-processing transformations in preparation such that the schema that can be directly exported.

    Examples of transforms:

     - rolling up or rolling down slots in the inheritance hierarchy
     - turning lists of primitives into their own tables

     Some of this may be useful for non-SQL formalisms. E.g. jsonschema does not have inheritance,
     so the roll up/down code may be useful here

     See: https://github.com/biolink/biolinkml/issues/288
    """
    source_schema: SchemaDefinition = None
    target_schema: SchemaDefinition = None
    source_generator: Generator = None
    target_generator: Generator = None

    def _asserted_slots(self, cls: ClassDefinition, schema: SchemaDefinition):
        # TODO: better way to determine asserted slots? use alias?
        return [schema.slots[sn] for sn in cls.slots if '__' not in sn]

    def transform_schema(self, src: SchemaDefinition) -> SchemaDefinition:
        """
        Transforms a native Schema into a Schema that conforms to a simpler SQLDDL profile
        :param src:
        :return:
        """
        self.source_schema = src

        # TODO: we only need methods from the base class, but we are forced to use a subclass
        self.source_generator = PythonGenerator(src)
        # todo: rename
        tgt = SchemaDefinition(id=src.id, name=src.name)
        self.target_generator = PythonGenerator(tgt)
        self.target_schema = tgt

        # TODO: clone vs reference?
        tgt.imports = src.imports
        tgt.prefixes = src.prefixes

        # clone classes
        for cn, c in src.classes.items():
            print(f'Cls: {cn}')
            # TODO: clone complete object
            tc = ClassDefinition(name=cn,
                                 is_a=c.is_a,
                                 mixins=c.mixins)
            tgt.classes[cn] = tc
            for ss in self.source_generator.own_slots(c):
                sn = ss.alias if ss.alias else ss.name
                print(f'  Slot: {sn} // {ss}')
                # TODO: clone complete object
                ts = SlotDefinition(name=sn,
                                    range=ss.range,
                                    multivalued=ss.multivalued)

                tgt.slots[sn] = ts
                tc.slots.append(sn)
        print(f'TGT: NC={len(tgt.classes.items())} NS={len(tgt.slots.items())}')
        for cn, c in dict(tgt.classes.items()).items():
            print(f'Tgt Cls: {cn} |S|={len(c.slots)}')
            for s in self.target_generator.own_slots(c):
                print(f'Checking: {s.name} in {cn} // {s}')
                if s.multivalued:
                    print(f'Transforming: {s.name} in {cn}')
                    self.transform_multivalued(s, c)

        # TODO: use schemaloader to unfold magic properties - not yet working
        sl = SchemaLoader(tgt)
        return tgt
        #return sl.resolve()

    def transform_multivalued(self, slot: SlotDefinition, base_class: ClassDefinition):
        """
        Transforms schema to account for a slot whose value may be a list/set/array

        There are two cases:

         - lists of primitives ("types" in linklml)
         - lists of objects

        In the former case, we create a name class '{cls}_to_{slot}'

        for example, in a schema with
        class Person and a multivalued slot aliases for a list of strings, we would make a fresh class:

        ```
           person_to_alias:
             attributes:
               person:
                 range: Person
               alias:
                 range: string
        ```

        (note that the `singular` metamodel slot is used to make singular names)

        In the second case, where the range of the multivalued slot is a class, we either inject a new slot
        {class} or we make a new linking table.

        Background:
        SQLDDL cannot typically represent lists (though some like postgresql may have bespoke extensions

        TODO: linking tables only need to be created if cardinality is many-to-many

        :param slot:
        :return:
        """
        tgt = self.target_schema
        base_cls_name = base_class.name
        slot_name = slot.name
        slot_name_singular = slot.singular_name if slot.singular_name is not None else slot.name
        if slot.multivalued != True:
            raise ValueError(f"slot should be multivalued: {slot}")
        else:
            linker_cls_name = f'{base_cls_name}_to_{slot_name_singular}'
            linker_cls = ClassDefinition(name=linker_cls_name)
            if linker_cls_name in tgt.classes:
                raise ValueError(f'linking class exists: {linker_cls_name}')
            tgt.classes[linker_cls_name] = linker_cls

            # create slots for linking table
            # TODO: these do not seem to show up in sqlddlgenarator
            new_slot = SlotDefinition(name=slot_name_singular,
                                      range=slot.range)
            linker_cls.slot_usage[slot_name_singular] = new_slot
            base_slot = SlotDefinition(name=base_cls_name,
                                       range=base_cls_name)
            linker_cls.slot_usage[base_cls_name] = base_slot
            base_class.slots.remove(slot_name)
            #if slot_name_singular not in tgt.slots:
            #    tgt.slots[slot_name_singular] = new_slot


    def rollup_slots_to_class(self, cls: ClassDefinition):
        """
        rolls up all slots to a common parent/ancestor class

        Background: standard SQLDDL does not allow for inheritance, so we need to 'flatten' the schema.
        See also rolldown_slots_to_class.

        :param cls:
        :return:
        """
        None # TODO

    def rolldown_slots_to_class(self, cls: ClassDefinition):
        """
        materializes all slots from ancestors to a descendant class

        Background: standard SQLDDL does not allow for inheritance, so we need to 'flatten' the schema.
        See also rolldown_slots_to_class.

        side effects: removes is_a and mixins from target class

        :param cls:
        :return:
        """
        None # TODO

    def suffix_foreign_key(self, slot: SlotDefinition, suffix: str = "_id"):
        """
        if slot has a range that is a class, rename the slot, suffixing an _id on the end
        :param slot:
        :return:
        """
        None # TODO

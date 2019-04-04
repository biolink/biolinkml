import os
from contextlib import redirect_stdout
from typing import Union, TextIO, Optional, Set

import click

from biolinkml.generators.yumlgen import YumlGenerator
from biolinkml.meta import SchemaDefinition, ClassDefinition, SlotDefinition, Element, ClassDefinitionName, \
    TypeDefinition
from biolinkml.utils.formatutils import camelcase, be, underscore
from biolinkml.utils.namespaces import Namespaces
from biolinkml.utils.generator import Generator
from biolinkml.utils.typereferences import References


class MarkdownGenerator(Generator):
    generatorname = os.path.basename(__file__)
    generatorversion = "0.0.3"
    valid_formats = ["md"]
    visit_all_class_slots = False

    def __init__(self, schema: Union[str, TextIO, SchemaDefinition], fmt: str=None) -> None:
        super().__init__(schema, fmt)
        self.directory: Optional[str] = None
        self.image_directory: Optional[str] = None
        self.noimages: bool = False
        self.gen_classes: Optional[Set[ClassDefinitionName]] = None
        self.gen_classes_neighborhood: Optional[References] = None
        self.BASE = None

    def visit_schema(self, directory: str=None, classes: Set[ClassDefinitionName]=None, image_dir: bool=False,
                     noimages: bool=False) -> None:
        self.gen_classes = classes if classes else []
        for cls in self.gen_classes:
            if cls not in self.schema.classes:
                raise ValueError("Unknown class name: {cls}")
        if self.gen_classes:
            self.gen_classes_neighborhood = self.neighborhood(list(self.gen_classes))

        self.directory = directory
        if directory:
            os.makedirs(directory, exist_ok=True)
        elif image_dir:
            raise ValueError(f"Image directory can only be used with '-d' option")
        if image_dir:
            self.image_directory = os.path.join(directory, 'images')
            if not noimages:
                os.makedirs(self.image_directory, exist_ok=True)
        self.noimages = noimages

        with open(os.path.join(directory, 'index.md'), 'w') as ixfile:
            with redirect_stdout(ixfile):
                self.frontmatter(f"{self.schema.name.title()} schema")
                self.para(be(self.schema.description))

                self.header(3, 'Classes')
                for cls in sorted(self.schema.classes.values(), key=lambda c: c.name):
                    if not cls.is_a and not cls.mixin and self.is_secondary_ref(cls.name):
                        self.class_hier(cls)

                self.header(3, 'Mixins')
                for cls in sorted(self.schema.classes.values(), key=lambda c: c.name):
                    if cls.mixin and self.is_secondary_ref(cls.name):
                        self.class_hier(cls)

                self.header(3, 'Slots')
                for slot in sorted(self.schema.slots.values(), key=lambda s: s.name):
                    if not slot.is_a and self.is_secondary_ref(slot.name):
                        self.pred_hier(slot)

                self.header(3, 'Types')
                self.header(4, 'Built in')
                for builtin_name in sorted(self.synopsis.typebases.keys()):
                    self.bullet(f'**{builtin_name}**')
                self.header(4, 'Defined')
                for typ in sorted(self.schema.types.values(), key=lambda t: t.name):
                    if self.is_secondary_ref(typ.name):
                        if typ.typeof:
                            typ_typ = self.type_link(typ.typeof)
                        else:
                            typ_typ = f'**{typ.base}**'

                        self.bullet(self.type_link(typ, after_link=f' ({typ_typ})', use_desc=True))

    def visit_class(self, cls: ClassDefinition) -> bool:
        if self.gen_classes and cls.name not in self.gen_classes:
            return False
        with open(self.dir_path(cls), 'w') as clsfile:
            with redirect_stdout(clsfile):
                self.frontmatter(f"Class: {cls.name}")
                self.para(be(cls.description))

                class_curi = self.namespaces.uri_or_curie_for(self.namespaces._base, camelcase(cls.name))
                class_uri = self.namespaces.uri_for(class_curi)
                print(f'URI: [{class_curi}]({class_uri})')
                print()
                if self.image_directory:
                    yg = YumlGenerator(self)
                    yg.serialize(classes=[cls.name], directory=self.image_directory, load_image=not self.noimages)
                    img_url = os.path.join('images', os.path.basename(yg.output_file_name))
                else:
                    yg = YumlGenerator(self)
                    img_url = yg.serialize(classes=[cls.name])\
                        .replace('[', '\\[').replace('?', '%3F').replace(' ', '%20')

                print(f'![img]({img_url})')
                self.mappings(cls)

                self.header(2, 'Inheritance')
                if cls.is_a is not None:
                    self.bullet(f' is_a: {self.class_link(cls.is_a, use_desc=True)}')
                for mixin in cls.mixins:
                    self.bullet(f' mixin: {self.class_link(mixin, use_desc=True)}')

                self.header(2, 'Children')
                if cls.name in self.synopsis.isarefs:
                    for child in sorted(self.synopsis.isarefs[cls.name].classrefs):
                        self.bullet(f'{self.class_link(child, use_desc=True)}')
                if cls.name in self.synopsis.mixinrefs:
                    for mixin in sorted(self.synopsis.mixinrefs[cls.name].classrefs):
                        self.bullet(f'{self.class_link(mixin, use_desc=True, after_link="(mixin)")}')

                if cls.name in self.synopsis.classrefs:
                    self.header(2, 'Used by')
                    for sn in sorted(self.synopsis.classrefs[cls.name].slotrefs):
                        slot = self.schema.slots[sn]
                        if slot.range == cls.name:
                            self.bullet(f' **{self.class_link(slot.domain)}** '
                                        f'*{self.slot_link(slot, add_subset=False)}*{self.predicate_cardinality(slot)}  '
                                        f'**{self.class_type_link(slot.range)}**')

                self.header(2, 'Fields')
                for sn in sorted(cls.slots):
                    self.slot_field(cls, self.schema.slots[sn])

                for slot in sorted(self.all_slots(cls), key=lambda s: s.name):
                    if slot.name not in cls.slots:
                        self.slot_field(cls, slot)

        return True

    def visit_class_slot(self, cls: ClassDefinition, aliased_slot_name: str, slot: SlotDefinition) -> None:
        with open(self.dir_path(slot), 'w') as slotfile:
            with redirect_stdout(slotfile):
                self.frontmatter(f"Slot: {aliased_slot_name}")
                self.para(be(slot.description))
                slot_curi = self.namespaces.uri_or_curie_for(self.namespaces._base, underscore(slot.name))
                slot_uri = self.namespaces.uri_for(slot_curi)
                print(f'URI: [{slot_curi}]({slot_uri})')
                self.mappings(slot)

                self.header(2, 'Domain and Range')
                print(f'{self.class_link(slot.domain)} ->{self.predicate_cardinality(slot)} '
                      f'{self.class_type_link(slot.range)}')

                self.header(2, 'Inheritance')
                if slot.is_a:
                    self.bullet(f' is_a: {self.slot_link(slot.is_a)}')

                self.header(2, 'Children')
                if slot.name in sorted(self.synopsis.isarefs):
                    for child in sorted(self.synopsis.isarefs[slot.name].slotrefs):
                        self.bullet(f' {self.slot_link(child)}')

                self.header(2, 'Used by')
                if slot.name in sorted(self.synopsis.slotrefs):
                    for rc in sorted(self.synopsis.slotrefs[slot.name].classrefs):
                        self.bullet(f'{self.class_link(rc)}')
                if aliased_slot_name == 'relation':
                    if slot.subproperty_of:
                        self.bullet(f' reifies: {self.slot_link(slot.subproperty_of)}')

    def class_hier(self, cls: ClassDefinition, level=0) -> None:
        self.bullet(self.class_link(cls, use_desc=True), level)
        if cls.name in sorted(self.synopsis.isarefs):
            for child in sorted(self.synopsis.isarefs[cls.name].classrefs):
                self.class_hier(self.schema.classes[child], level+1)
        
    def pred_hier(self, slot: SlotDefinition, level=0) -> None:
        self.bullet(self.slot_link(slot, use_desc=True), level)
        if slot.name in sorted(self.synopsis.isarefs):
            for child in sorted(self.synopsis.isarefs[slot.name].slotrefs):
                self.pred_hier(self.schema.slots[child], level+1)

    def dir_path(self, obj: Union[ClassDefinition, SlotDefinition]) -> str:
        filename = self.formatted_element_name(obj) if isinstance(obj, ClassDefinition) else underscore(obj.name)
        return f'{self.directory}/{filename}.md'

    def mappings(self, obj: [SlotDefinition, ClassDefinition]) -> None:
        # TODO: get rid of this?
        # self.header(2, 'Mappings')
        # for mapping in obj.mappings:
        #     self.bullet(f"{self.xlink(mapping)} {self.to_uri(mapping)}")
        # if obj.subclass_of:
        #     self.bullet(self.xlink(obj.subclass_of))
        pass

    def is_secondary_ref(self, en: str) -> bool:
        """ Determine whether 'en' is the name of something in the neighborhood of the requested classes

        @param en: element name
        @return: True if 'en' is the name of a slot, class or type in the immediate neighborhood of of what we are
        building
        """
        if not self.gen_classes:
            return True
        elif en in self.schema.classes:
            return en in self.gen_classes_neighborhood.classrefs
        elif en in self.schema.slots:
            return en in self.gen_classes_neighborhood.slotrefs
        elif en in self.schema.types:
            return en in self.gen_classes_neighborhood.typerefs
        else:
            return True

    def slot_field(self, cls: ClassDefinition, slot: SlotDefinition) -> None:
        self.bullet(f'{self.slot_link(slot)}{self.predicate_cardinality(slot)}')
        if slot.description:
            self.bullet(f'Description: {slot.description}', level=1)
        self.bullet(f'range: {self.class_type_link(slot.range)}', level=1)
        # if slot.subproperty_of:
        #     self.bullet(f'edge label: {self.slot_link(slot.subproperty_of)}', level=1)
        for example in slot.examples:
            self.bullet(f'Example: {example.value} {example.description}', level=1)
        if slot.name not in self.own_slot_names(cls):
            self.bullet(f'inherited from: {self.class_link(slot.domain)}', level=1)
        if slot.in_subset:
            ssl = ','.join(slot.in_subset)
            self.bullet(f'in subsets: ({ssl})', level=1)

    def to_uri(self, uri_or_curie: str) -> str:
        """ Return the URI for the slot if known """
        if ':/' in uri_or_curie:
            return uri_or_curie
        elif self.namespaces.prefix_for(uri_or_curie) in self.namespaces:
            return self.namespaces.uri_for(uri_or_curie)
        else:
            return "*(Unknown namespace)*"

    # --
    # FORMATTING
    # --
    @staticmethod
    def predicate_cardinality(slot: SlotDefinition) -> str:
        """ Emit cardinality for a suffix on a predicate"""
        if slot.multivalued:
            card_str = '1..*' if slot.required else '0..*'
        else:
            card_str = 'REQ' if slot.required else 'OPT'
        return f"  <sub>{card_str}</sub>"

    @staticmethod
    def range_cardinality(slot: SlotDefinition) -> str:
        """ Emits cardinality decorator at end of type """
        if slot.multivalued:
            card_str = '1..*' if slot.required else '0..*'
        else:
            card_str = '1..1' if slot.required else '0..1'
        return f"  <sub><b>{card_str}</b></sub>"

    @staticmethod
    def anchor(id_: str) -> None:
        print(f'<a name="{id_}">', end='')

    @staticmethod
    def anchorend() -> None:
        print('</a>')

    @staticmethod
    def header(level: int, txt: str) -> None:
        print(f'{"#" * level} {txt}\n')

    @staticmethod
    def para(txt: str) -> None:
        print(f'\n{txt}\n')

    @staticmethod
    def bullet(txt: str, level=0) -> None:
        print(f'{"   " * level} * {txt}')

    def frontmatter(self, thingtype: str, layout='default') -> None:
        self.header(1, thingtype)
        # print(f'---\nlayout: {layout}\n---\n')

    def bbin(self, obj: Element) -> str:
        """ Boldify built in types

        @param obj: object name or id
        @return:
        """
        return obj.name if isinstance(obj, Element ) else f'**{obj}**' if obj in self.synopsis.typebases else obj

    def desc_for(self, obj: Element, doing_descs: bool) -> str:
        """ Return a description for object if it is unique (different than its parent)

        @param obj: object to be described
        @param doing_descs: If false, always return an empty string
        @return: text or empty string
        """
        if obj.description and doing_descs:
            if isinstance(obj, SlotDefinition) and obj.is_a:
                parent = self.schema.slots[obj.is_a]
            elif isinstance(obj, ClassDefinition) and obj.is_a:
                parent = self.schema.classes[obj.is_a]
            else:
                parent = None
            return '' if parent and obj.description == parent.description else obj.description
        return ''

    def _link(self, obj: Optional[Element], *, after_link: str = None, use_desc: bool=False,
             add_subset: bool=True) -> str:
        """ Create a link to ref if appropriate.

        @param ref: the name or value of a class, slot, type or the name of a built in type.
        @param after_link: Text to put between link and description
        @param use_desc: True means append a description after the link if available
        @param add_subset: True means add any subset information that is available
        @return:
        """
        nl = '\n'
        if obj is None or not self.is_secondary_ref(obj.name):
            return self.bbin(obj)
        if isinstance(obj, SlotDefinition):
            link_name = ((be(obj.domain) + '.') if obj.alias else '') + self.aliased_slot_name(obj)
            link_ref = underscore(obj.name)
        else:
            link_name = camelcase(obj.name)
            link_ref = link_name
        desc = self.desc_for(obj, use_desc)
        return f'[{link_name}]' \
               f'({link_ref}.{self.format})' + \
                 (f' {after_link} ' if after_link else '') + (f' - {desc.split(nl)[0]}' if desc else '')

    def type_link(self, ref: Optional[Union[str, TypeDefinition]], *, after_link: str = None, use_desc: bool=False,
             add_subset: bool=True) -> str:
        return self._link(self.schema.types[ref] if isinstance(ref, str) else ref, after_link=after_link,
                         use_desc=use_desc, add_subset=add_subset)

    def slot_link(self, ref: Optional[Union[str, SlotDefinition]], *, after_link: str = None, use_desc: bool=False,
             add_subset: bool=True) -> str:
        return self._link(self.schema.slots[ref] if isinstance(ref, str) else ref, after_link=after_link,
                         use_desc=use_desc, add_subset=add_subset)

    def class_link(self, ref: Optional[Union[str, ClassDefinition]], *, after_link: str = None, use_desc: bool=False,
             add_subset: bool=True) -> str:
        return self._link(self.schema.classes[ref] if isinstance(ref, str) else ref, after_link=after_link,
                         use_desc=use_desc, add_subset=add_subset)

    def class_type_link(self, ref: Optional[Union[str, ClassDefinition, TypeDefinition]], *, after_link: str = None,
                        use_desc: bool=False, add_subset: bool=True) -> str:
        if isinstance(ref, ClassDefinition):
            return self.class_link(ref, after_link=after_link, use_desc=use_desc, add_subset=add_subset)
        elif isinstance(ref, TypeDefinition):
            return self.type_link(ref, after_link=after_link, use_desc=use_desc, add_subset=add_subset)
        elif ref in self.schema.classes:
            return self.class_link(ref, after_link=after_link, use_desc=use_desc, add_subset=add_subset)
        else:
            return self.type_link(ref, after_link=after_link, use_desc=use_desc, add_subset=add_subset)

    def xlink(self, id_: str) -> str:
        return f'[{id_}]({self.id_to_url(id_)})'


    @staticmethod
    def id_to_url(id_: str) -> str:
        uri = id_
        if ':' in id_:
            # TODO! use PC
            if id_.startswith('SIO:'):
                uri = id_.replace('SIO:', 'http://semanticscience.org/resource/SIO_')
            elif id_.startswith('HGNC:'):
                uri = 'https://monarchinitiative.org/gene/' + id_
            else:
                frag = id_.replace(':', '_')
                base = 'http://purl.obolibrary.org/obo/'
                uri = base+frag
        return uri


@click.command()
@click.argument("yamlfile", type=click.Path(exists=True, dir_okay=False))
@click.option("-d", "--dir", help="Output directory")
@click.option("-f", "--format", default='md', type=click.Choice(['md']), help="Output format")
@click.option("--classes", "-c", default=None, multiple=True, help="Class(es) to emit")
@click.option("-i", "--img", is_flag=True, help="Download YUML images to 'image' directory")
@click.option("--noimages", is_flag=True, help="Do not (re-)generate images")
def cli(yamlfile, format, dir, classes, img, noimages):
    """ Generate markdown documentation of a biolink model """
    MarkdownGenerator(yamlfile, format).serialize(classes=classes, directory=dir, image_dir=img, noimages=noimages)

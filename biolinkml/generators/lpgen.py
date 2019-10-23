import os
from typing import Union, TextIO, Optional

import click
from prologterms import Term, TermGenerator, PrologRenderer, SExpressionRenderer

from biolinkml.meta import SchemaDefinition, ClassDefinition, SlotDefinition
from biolinkml.utils.formatutils import camelcase, underscore
from biolinkml.utils.generator import Generator


class LogicProgramGenerator(Generator):
    generatorname = os.path.basename(__file__)
    generatorversion = "0.0.2"
    valid_formats = ['lp', 'sexpr']
    visit_all_class_slots = True

    def __init__(self, schema: Union[str, TextIO, SchemaDefinition], fmt: Optional[str] = None) -> None:
        super().__init__(schema, fmt)
        self.P = TermGenerator() 
        self.R = PrologRenderer() if fmt == 'lp' else SExpressionRenderer()

    def visit_class(self, cls: ClassDefinition) -> bool:
        cn = underscore(cls.name)
        
        self.emit('class', cn)
        for p in cls.mixins:
            self.emit('mixin', cn, underscore(p))
        if cls.is_a:
            is_a = underscore(cls.is_a)
            self.emit('is_a', cn, is_a)
            if cls.defining_slots:
                self.emit('defining_slots', is_a, [underscore(s) for s in cls.defining_slots])
        uri = f'http://w3id.org/biolink/vocab/{camelcase(cls.name)}'

        self.emit('has_uri', cn, uri)
        return True

    def visit_slot(self, slot_name: str, slot: SlotDefinition) -> None:
        """ Add a slot definition per slot

        @param slot_name:
        @param slot:
        @return:
        """
        sn = underscore(slot_name)
        self.emit('slot', sn)
        if slot.domain:
            self.emit('domain', sn, underscore(slot.domain))
        if slot.range:
            self.emit('range', sn, underscore(slot.range))
        for p in slot.mixins:
            self.emit('mixin', sn, underscore(p))
        if slot.is_a:
            is_a = underscore(slot.is_a)

        #uri = self.owlgen._prop_uri(slot.name)
        uri = f'http://w3id.org/biolink/vocab/{sn}'
        self.emit('has_uri', sn, uri)
        if slot.multivalued:
            self.emit('multivalued', sn)
        if slot.required:
            self.emit('required', sn)
            
        
    
    def visit_class_slot(self, cls: ClassDefinition, aliased_slot_name: str, slot: SlotDefinition) -> None:
        sn = underscore(aliased_slot_name)
        cn = underscore(cls.name)
        self.emit('class_slot', cn, sn)
        self.emit('required', sn)
        self.emit('slotrange', underscore(slot.range)) if slot.range in self.schema.classes or slot.range in self.schema.types else "String"
        if slot.multivalued:
            self.emit('multivalued_in', sn, cn)
        if slot.required:
            self.emit('required_in', sn, cn)
        if slot.range:
            self.emit('range_in', sn, underscore(slot.range), cn)


    def emit(self, p, *args):
        t = Term(p, *args)
        print(f'{self.R.render(t)}.')

        

@click.command()
@click.argument("yamlfile", type=click.Path(exists=True, dir_okay=False))
@click.option("--format", "-f", default='lp', type=click.Choice(['lp', 'sexpr']), help="Output format")
def cli(yamlfile, format):
    """ Generate logic program representation of a biolink model """
    print(LogicProgramGenerator(yamlfile, format).serialize())

if __name__ == "__main__":
    cli()

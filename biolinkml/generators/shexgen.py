"""Generate ShEx definition of a model

"""
import os
from typing import Union, TextIO, Optional, List, cast

import click
from ShExJSG import ShExC
from ShExJSG.SchemaWithContext import Schema
from ShExJSG.ShExJ import Shape, IRIREF, ShapeAnd, EachOf, TripleConstraint, NodeConstraint, ShapeOr
from jsonasobj import as_json
from rdflib import Graph, OWL, RDF, Namespace, XSD

from biolinkml import METAMODEL_LOCAL_NAME, METAMODEL_NAMESPACE
from biolinkml.meta import SchemaDefinition, ClassDefinition, SlotDefinition, ClassDefinitionName, \
    SlotDefinitionName, ElementName
from biolinkml.utils.formatutils import camelcase
from biolinkml.utils.generator import Generator


class ShExGenerator(Generator):
    generatorname = os.path.basename(__file__)
    generatorversion = "0.0.2"
    valid_formats = ['shex', 'json', 'rdf']
    visit_all_class_slots = False

    def __init__(self, schema: Union[str, TextIO, SchemaDefinition], fmt: str = 'shex') -> None:
        super().__init__(schema, fmt)
        self.shex: Schema = Schema()                # ShEx Schema being generated
        self.shapes = []
        self.shape: Shape = None                    # Current shape being defined
        self.list_shapes: List[IRIREF] = []         # Shapes that have been defined as lists

        if METAMODEL_LOCAL_NAME not in self.namespaces:
            self.namespaces[METAMODEL_LOCAL_NAME] = METAMODEL_NAMESPACE
        self.meta = Namespace(self.namespaces.join(self.namespaces[METAMODEL_LOCAL_NAME], ''))  # URI for the metamodel
        self.base = Namespace(self.namespaces.join(self.namespaces._base, ''))    # Base URI for what is being modeled

    def visit_schema(self, **_):
        # Adjust the schema context to include the base model URI
        context = self.shex['@context']
        self.shex['@context'] = [context, {'@base': self.namespaces._base}]
        # Emit all of the type definitions
        for typ in self.schema.types.values():
            if typ.uri:
                uri = self.namespaces.uri_for(typ.uri)
                if uri == XSD.anyURI:
                    self.shapes.append(NodeConstraint(id=self._shape_iri(typ.name), nodeKind="nonliteral"))
                else:
                    self.shapes.append(NodeConstraint(id=self._shape_iri(typ.name),
                                                      datatype=self.namespaces.uri_for(typ.uri)))
            else:
                self.shapes.append(Shape(id=self._shape_iri(typ.name), expression=self._shape_iri(typ.typeof)))

    def _shape_iri(self, name: ElementName) -> IRIREF:
        return IRIREF(self.base[camelcase(name)])

    def visit_class(self, cls: ClassDefinition) -> bool:
        self.shape = Shape()
        if not cls.mixin and not cls.name in self.synopsis.mixinrefs and not cls.abstract and self.class_identifier(cls):
            self.shape.closed = True
            self.shape.extra = [RDF.type]
            type_constraint = TripleConstraint()
            type_constraint.predicate = RDF.type
            type_constraint.valueExpr = NodeConstraint(values=[IRIREF(self.namespaces.uri_for(cls.class_uri))])
            self.shape.expression = type_constraint
        # # TODO: Add this when shex 2.1 is committed
        # if cls.abstract:
        #     self.shapeExpr.abstract = True
        # TODO: Figure out the semantics of union_of
        return True

    def end_class(self, cls: ClassDefinition) -> None:
        if cls.is_a or cls.mixins:
            shapeExpr = ShapeAnd(
                shapeExprs=([self._shape_iri(cast(ClassDefinitionName, cls.is_a))] if cls.is_a else []) +
                            [self._shape_iri(cast(ClassDefinitionName, mixin)) for mixin in cls.mixins] +
                            [self.shape])
        else:
            shapeExpr = self.shape
        shapeExpr.id = self._shape_iri(cls.name)
        self.shapes.append(shapeExpr)

    def visit_class_slot(self, cls: ClassDefinition, aliased_slot_name: SlotDefinitionName, slot: SlotDefinition) \
            -> None:
        if not (slot.identifier or slot.abstract):
            constraint = TripleConstraint()
            # Juggling to get the constraint to be either a single triple constraint or an eachof construct
            if not self.shape.expression:
                self.shape.expression = constraint
            elif isinstance(self.shape.expression, TripleConstraint):
                self.shape.expression = EachOf(expressions=[self.shape.expression, constraint])
            else:
                self.shape.expression.expressions.append(constraint)

            constraint.predicate = self.namespaces.uri_for(slot.slot_uri)
            constraint.min = int(bool(slot.required))
            constraint.max = 1 if not slot.multivalued else -1
            constraint.valueExpr = self._shape_iri(slot.range)

    def end_schema(self, output: Optional[str]=None, **_) -> None:
        self.shex.shapes = self.shapes
        shex = as_json(self.shex)
        if self.format == 'rdf':
            g = Graph()
            g.parse(data=shex, format="json-ld")
            g.bind('owl', OWL)
            # # TODO: Add bindings here
            # g.bind('biolink', BIOENTITY)
            # g.bind('meta', META)
            shex = g.serialize(format='turtle').decode()
        elif self.format == 'shex':
            shex = str(ShExC(self.shex))
        if output:
            with open(output, 'w') as outf:
                outf.write(shex)
        else:
            print(shex)



@click.command()
@click.argument("yamlfile", type=click.Path(exists=True, dir_okay=False))
@click.option("--format", "-f", default='shex', type=click.Choice(ShExGenerator.valid_formats),
              help="Output format")
@click.option("-o", "--output", help="Output file name")
def cli(yamlfile, format, output):
    """ Generate a ShEx Schema for a  biolink model """
    print(ShExGenerator(yamlfile, format).serialize(output=output))

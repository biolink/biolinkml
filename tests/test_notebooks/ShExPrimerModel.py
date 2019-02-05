from biolinkml.generators.shexgen import ShExGenerator

model = """
id: http://shex.io/shex-primer/issueshape
title: Issue Shape from ShEx primer
name: issue
version: 0.1.0

prefixes:
   issue: http://shex.io/shex-primer/issue/
   ex: http://ex.example/#
   xsd: http://www.w3.org/2001/XMLSchema#
   foaf: http://xmlns.com/foaf/0.1/

default_prefix: issue

default_range: str

types:
   str:
       biolinkml: str
       uri: xsd:string

   int:
      biolinkml: int
      uri: xsd:integer

classes:
    person:
    enrolee:
        is_a: person

slots:
    name:
        domain: person
        range: str
        key: true

    age:
        domain: enrolee
        range: int
        slot_uri: foaf:age

    hasGuardian:
        domain: enrolee
        range: person
        multivalued: true
        required: true

"""
MarkdownGenerator()
print(ShExGenerator(model).serialize())
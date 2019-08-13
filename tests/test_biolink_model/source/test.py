from jsonasobj import as_json

from biolinkml.meta import RDFS
from biolinkml.utils.strictness import lax, strict
from biolinkml.utils.yamlutils import as_rdf
from tests.test_biolink_model.source.model import Association, Gene, GeneToDiseaseAssociation, Disease, GO, HP

from rdflib import Namespace

LOINC = Namespace("http://loinc.org/")



g = Gene(HP.a1234)
d = Disease(HP.d17)

x = GeneToDiseaseAssociation(Gene(RDFS.Resource), HP['3345'], d, id=HP.abc)
print(as_json(x))
g = as_rdf(x, 'biolink-model.context.jsonld')
print(g.serialize(format="turtle").decode())

# This passes because we've turned off validation
lax()
y = GeneToDiseaseAssociation(d, HP['3345'], d)
strict()
try:
    y = GeneToDiseaseAssociation(d, HP['3345'], d)
except ValueError as e:
    print(f"Assignment failed as expected: \n{e}")
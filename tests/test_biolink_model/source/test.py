from jsonasobj import as_json

from tests.test_biolink_model.source.model import Association, Gene, GeneToDiseaseAssociation, Disease, GO, HP


g = Gene(HP.a1234)
d = Disease(HP.d17)
x = GeneToDiseaseAssociation(g.id, HP['3345'], d.id)
print(as_json(x))
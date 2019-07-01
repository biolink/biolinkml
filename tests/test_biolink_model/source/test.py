from jsonasobj import as_json

from tests.test_biolink_model.source.model import Association, Gene, GeneToDiseaseAssociation, Disease


g = Gene("HPO:1234")
d = Disease("HPO:11732")
x = GeneToDiseaseAssociation(g.id, "HP:3345", d.id)
print(as_json(x))
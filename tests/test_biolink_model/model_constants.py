""" Constants for biolink Model processing

* type - defines the range of a Literal target of a model_slot or association_slot
* valueset - defines a discrete set of possible values - either literals or URIs
* subset - used to classify and partition model elements through the "in_subset" attribute
* associations - a set of subject, relation, object entries with accompanying attribution and annotation
* nodes - a structured set of association subjects and/or objects
* relations - a structured set of association relations
* providers - providers used for association attribution
* publications - publications used for association attribution
"""

model_components = ['types', 'valusets', 'subsets', 'associations', 'nodes', 'relations', 'evidence', 'providers',
                    'publications']

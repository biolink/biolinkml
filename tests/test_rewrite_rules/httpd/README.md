# w3id.org rewrite rules
We use [w3id.org](https://github.com/perma-id/w3id.org) identifiers throughout the model. The current mappings are as
follows:

| http://w3id.org/biolink/biolinkml/... | http://biolink.github.io/biolinkml/... | Purpose | Example |
| :----------------------------------:  | :------------------------------------: | ------- | ------- |
| includes/types[.sfx] | includes/types[.sfx] | Language types (and other includes) (.sfx set by conneg if not already specified -- .ttl, .yaml, .owl, .shex, ...) | http://w3id.org/biolink/biolinkml/includes/types --> http://biolink.github.io/biolinkml/includes/types.yaml (Accept: text/yaml) |
| | | | http://w3id.org/biolink/biolinkml/includes/types --> http://biolink.github.io/biolinkml/includes/types (Accept: text/html) |
| type/[X][.sfx]  | docs/types/[X] | Access to metamodel type definitions w/ conneg | http://w3id.org/biolink/biolinkml/type/Bool --> http://biolink.github.io/biolinkml/docs/types/Bool |
| meta[.sfx] | meta[.sfx] | Access to Biolink meta models w/ conneg | http://w3id.org/biolink/biolinkml/meta --> http://biolink.github.io/biolinkml/meta.yaml (Accept: application/yaml) |
| | | |  http://w3id.org/biolink/biolinkml/meta.owl --> http://biolink.github.io/biolinkml/meta.owl (*What SHOULD we use for conneg for OWL/TTL?*) |
| meta/[X][.sfx] | docs/[X][.sfx] | Access to metamodel class and slot definitions w/ conneg | http://w3id.org/biolink/biolinkml/meta/Definition --> http://biolink.github.io/biolinkml/docs/Definition.jsonld (Accept: application/json) |
| context.jsonld | context.jsonld | metamodel context.jsonld for converting json instances to RDF | http://w3id.org/biolink/biolinkml/context.jsonld --> http://biolink.github.io/biolinkml/context.jsonld |

## Testing the rewrite rules

```bash
> cd httpd
> docker image build . -t http_test
> docker run --rm -d -p <port>:80 --name http_test http_test
> cd ../../..
> pipenv install
> pipenv shell
(biolinkml) > cd tests/test_rewrite_rules
(biolinkml) > export SERVER="http://localhost:<port>"
(biolinkml) > python test_rewrite_rules.py
ssssss
----------------------------------------------------------------------
Ran 6 tests in 0.000s

OK (skipped=6)
(biolinkml) > exit
> docker stop http_test
```

7. ** If necessary, make a pull request to w3id.org w/ changes **



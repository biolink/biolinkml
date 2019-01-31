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
1. **Fork or clone the w3id.org [perma-id](https://github.com/perma-id/w3id.org) repository to the tests/httpd directory **
```bash
# In a directory of your choice:
> git clone git@github.com:perma-id/w3id.org.git
> cd biolink/biolinkml/tests/httpd
> ln -s <path to>w3id.org
```
2. ** Copy the local rewrite rules across (Optional) **
```bash
> cp -R biolink w3id.org
```
3. **Build the local httpd server docker image**
```bash
> ./build.sh
```
4. ** Start the httpd server docker image, pointing the document root at the cloned repository **
```bash
> ./start.sh <port>
```
5. ** Run the `test_rewrite_rules.py` unit test **
```bash
> export SERVER="http://localhost:<port>"
$ pipenv run python ../test_rewrite_rules/test_rewrite_rules.py
......
----------------------------------------------------------------------
Ran 6 tests in 0.423s

OK
```
6. ** Teardown the docker server **
```bash
> docker stop httptest
```
7. ** If necessary, make a pull request to w3id.org w/ changes **



# JSON LD Contexts
This directory contains a variety of contexts for use with the JSON-LD module

## JSON LD 1.0 contexts
* [jsonld_10/termci_schema.context.jsonld]() - default context emitted by the current version (as of writing 1.7.0) of biolinkml

## JSON LD 1.1 contexts
* [jsonld_11/Package.context.jsonld]() - Package context (hand generated)
* [jsonld_11/ConceptSystem.context.jsonld]() - ConceptSystem context (hand generated)
* [jsonld_11/ConceptReference.context.jsonld]() - ConceptReference context (hand generated)
* [jsonld_11/termci_namespaces.context.jsonld]() - experimental module for separate namespaces, including explicit namespace
  identifier for namespaces that end with a '_' (hand generated)
* [tjsonld_11/ermci_schema_inlined.context.jsonld]() - Nested contexts inlined (generated using context_flattener.py starting
  with Package.context.jsonld)
  
## Starting the docker web server
```bash
> cd tests/test_loaders/dumpers/jsonld-context
> docker image build . -t context_server
> docker run -it --rm -d -p 8000:80 -p 8443:443 --name context_server -v `pwd`/:/usr/share/nginx/html context_server 
```
To test that the server is running:
```bash
> curl -k https://localhost:8443/jsonld_11/termci_schema.frame.jsonld
{
  "@context": "Package.context.json",
  "@omitGraph": true,
  "@type": "termci:Package",
  "system": {
    "@embed": "always",
    "contents": {
      "defined_in": {
        "@embed": "never"
      },
      "narrower_than": {
        "@embed": "never"
      }
    }
  }
}
> curl http://localhost:8000/jsonld_10/termci_schema.context.jsonld
{
   "_comments": "Auto generated from termci_schema.yaml by jsonldcontextgen.py version: 0.1.1\nGeneration date: 2021-02-12 11:24\nSchema: termci_schema\n\nid: https://w3id.org/termci_schema\ndescription: Terminology Code Index model\nlicense: https://creativecommons.org/publicdomain/zero/1.0/\n",
   "@context": {
    ...
>
```
The ports that you select for `http:` and `https:` can be assigned however you wish, but if you pick something the
ones above, you will need to edit [tests/test_loaders/__init__.py]() and change the lines:
```python
HTTP_TEST_PORT = 8000
HTTPS_TEST_PORT = 8443
```



# Type: prefix


prefix URI tuple

URI: [meta:Prefix](https://w3id.org/biolink/biolinkml/meta/Prefix)


![img](http://yuml.me/diagram/nofunky;dir:TB/class/\[SchemaDefinition]++-%20prefixes%200..*>\[Prefix|prefix_prefix(pk):ncname;prefix_reference:uri])

## Referenced by class

 *  **[schema_definition](schema_definition.md)** *[prefixes](prefixes.md)*  <sub>0..*</sub>  **[prefix](prefix.md)**

## Attributes


### Own

 * [prefix_prefix](prefix_prefix.md)  <sub>REQ</sub>
    * Description: the nsname (sans ':' for a given prefix)
    * range: [Ncname](type/Ncname.md)
 * [prefix_reference](prefix_reference.md)  <sub>REQ</sub>
    * Description: A URI associated with a given prefix
    * range: [Uri](type/Uri.md)

### Domain for slot:

 * [prefix_prefix](prefix_prefix.md)  <sub>REQ</sub>
    * Description: the nsname (sans ':' for a given prefix)
    * range: [Ncname](type/Ncname.md)
 * [prefix_reference](prefix_reference.md)  <sub>REQ</sub>
    * Description: A URI associated with a given prefix
    * range: [Uri](type/Uri.md)

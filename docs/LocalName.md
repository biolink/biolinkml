
# Type: local_name


an attributed label

URI: [meta:LocalName](https://w3id.org/biolink/biolinkml/meta/LocalName)


![img](http://yuml.me/diagram/nofunky;dir:TB/class/[Element]++-%20local_names%200..*>[LocalName&#124;local_name_source(pk):ncname;local_name_value:string])

## Referenced by class

 *  **[Element](Element.md)** *[local_names](local_names.md)*  <sub>0..*</sub>  **[LocalName](LocalName.md)**

## Attributes


### Own

 * [local_name_source](local_name_source.md)  <sub>REQ</sub>
    * Description: the ncname of the source of the name
    * range: [Ncname](types/Ncname.md)
 * [local_name_value](local_name_value.md)  <sub>REQ</sub>
    * Description: a name assigned to an element in a given ontology
    * range: [String](types/String.md)

### Domain for slot:

 * [local_name_source](local_name_source.md)  <sub>REQ</sub>
    * Description: the ncname of the source of the name
    * range: [Ncname](types/Ncname.md)
 * [local_name_value](local_name_value.md)  <sub>REQ</sub>
    * Description: a name assigned to an element in a given ontology
    * range: [String](types/String.md)

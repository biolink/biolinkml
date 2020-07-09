
# Type: alt_description


an attributed description

URI: [meta:AltDescription](https://w3id.org/biolink/biolinkml/meta/AltDescription)


![img](http://yuml.me/diagram/nofunky;dir:TB/class/[Element],[Element]++-%20alt_descriptions%200..*>[AltDescription&#124;source(pk):ncname;description:string])

## Referenced by class

 *  **[Element](Element.md)** *[alt_descriptions](alt_descriptions.md)*  <sub>0..*</sub>  **[AltDescription](AltDescription.md)**

## Attributes


### Own

 * [alt_description➞source](alt_description_source.md)  <sub>REQ</sub>
    * Description: the source of an attributed description
    * range: [Ncname](types/Ncname.md)
 * [alt_description➞description](alt_description_text.md)  <sub>REQ</sub>
    * Description: text of an attributed description
    * range: [String](types/String.md)

# Class: alt_description


an attributed description

URI: [meta:AltDescription](https://w3id.org/biolink/biolinkml/meta/AltDescription)

![img](http://yuml.me/diagram/nofunky;dir:TB/class/\[Element]++-%20alt_descriptions%200..*>\[AltDescription|source(pk):ncname;description:string])
## Inheritance

## Children

## Used by

 *  **[Element](Element.md)** *[alt_descriptions](alt_descriptions.md)*  <sub>0..*</sub>  **[AltDescription](AltDescription.md)**
## Fields

 * [alt_description.source](alt_description_source.md)  <sub>REQ</sub>
    * Description: the source of an attributed description
    * range: [Ncname](Ncname.md)
 * [alt_description.description](alt_description_text.md)  <sub>REQ</sub>
    * Description: text of an attributed description
    * range: [String](String.md)

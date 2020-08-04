
# Type: annotation


a tag/value pair with the semantics of OWL Annotation

URI: [meta:Annotation](https://w3id.org/biolink/biolinkml/meta/Annotation)


![img](http://yuml.me/diagram/nofunky;dir:TB/class/[Extension],[Annotation]<annotations%200..*-++[Annotation&#124;value:boolean;tag(i):uriorcurie],[Extension]^-[Annotation],[Annotatable])

## Parents

 *  is_a: [Extension](Extension.md) - a tag/value pair used to add non-model information to an entry

## Referenced by class

 *  **[Annotatable](Annotatable.md)** *[annotations](annotations.md)*  <sub>0..*</sub>  **[Annotation](Annotation.md)**

## Attributes


### Own

 * [annotation➞value](annotation_extension_value.md)  <sub>REQ</sub>
    * range: [Boolean](types/Boolean.md)
 * [annotations](annotations.md)  <sub>0..*</sub>
    * Description: a collection of tag/text tuples with the semantics of OWL Annotation
    * range: [Annotation](Annotation.md)

### Inherited from extension:

 * [extension➞tag](extension_tag.md)  <sub>REQ</sub>
    * Description: a tag associated with an extension
    * range: [Uriorcurie](types/Uriorcurie.md)
 * [extensions](extensions.md)  <sub>0..*</sub>
    * Description: a tag/text tuple attached to an arbitrary element
    * range: [Extension](Extension.md)

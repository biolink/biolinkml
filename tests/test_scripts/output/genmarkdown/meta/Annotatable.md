
# Type: annotatable


mixin for classes that support annotations

URI: [meta:Annotatable](https://w3id.org/biolink/biolinkml/meta/Annotatable)


![img](http://yuml.me/diagram/nofunky;dir:TB/class/[Annotation],[Annotation]<annotations%200..*-++[Annotatable],[Element]uses%20-.->[Annotatable],[Element])

## Mixin for

 * [Element](Element.md) (mixin)  - a named element in the model

## Referenced by class


## Attributes


### Own

 * [annotations](annotations.md)  <sub>0..*</sub>
    * Description: a collection of tag/text tuples with the semantics of OWL Annotation
    * range: [Annotation](Annotation.md)

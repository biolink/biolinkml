# Types For Use In The Biolink Model schema


Type definitions for the biolink model definitions

### Classes

### Mixins

### Slots

### Types

#### Built in

 * **Bool**
 * **NCName**
 * **URIorCURIE**
 * **XSDDate**
 * **XSDDateTime**
 * **XSDTime**
 * **float**
 * **int**
 * **str**
#### Defined

 * [BiologicalSequence](BiologicalSequence.md)  ([String](String.md)) 
 * [Boolean](Boolean.md)  (**Bool**)  - A binary (true or false) value
 * [BooleanType](BooleanType.md)  ([Boolean](Boolean.md))  - A true/false value with absent (None) meaning not specified
 * [ChemicalFormulaType](ChemicalFormulaType.md)  ([String](String.md)) 
 * [Date](Date.md)  (**XSDDateTime**)  - a date (year, month and day) in an idealized calendar
 * [Datetime](Datetime.md)  (**XSDDate**) 
 * [Double](Double.md)  (**float**) 
 * [FileName](FileName.md)  ([String](String.md)) 
 * [Float](Float.md)  (**float**) 
 * [FrequencyValue](FrequencyValue.md)  ([String](String.md)) 
 * [IdentifierType](IdentifierType.md)  ([Uri](Uri.md))  - A URI or CURIE that uniquely identifies the named thing
 * [Integer](Integer.md)  (**int**) 
 * [LabelType](LabelType.md)  ([String](String.md))  - A string that provides a human-readable name for a thing
 * [NarrativeText](NarrativeText.md)  ([String](String.md))  - A string that provides a human-readable description of something
 * [Ncname](Ncname.md)  (**NCName**)  - Prefix part of CURIE
 * [PerecentageFrequencyValue](PerecentageFrequencyValue.md)  ([Double](Double.md)) 
 * [Quotient](Quotient.md)  ([Double](Double.md)) 
 * [String](String.md)  (**str**) 
 * [SymbolType](SymbolType.md)  ([String](String.md)) 
 * [Time](Time.md)  (**XSDTime**)  - A time object represents a (local) time of day, independent of any particular day
 * [TimeType](TimeType.md)  ([Time](Time.md)) 
 * [Unit](Unit.md)  ([String](String.md)) 
 * [Uri](Uri.md)  (**URIorCURIE**)  - a URI or a CURIE
 * [UriType](UriType.md)  ([Uri](Uri.md))  - The URI that uniquely identifies the named thing

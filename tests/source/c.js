function jsonToRdf (obj, baseURL, resourceType) {
  // return Promise.resolve(_showSource(new N3.Store(), obj))
  const rootNode = baseURL + resourceType + '/' + obj.id // top-level resource node., e.g. http://.../Observation/123
  return new Promise(function (resolve, reject) {
    // Load the appropriate @context.
    if (!Contexts[obj.resourceType])
      Contexts[obj.resourceType] = JSON.parse(
        Fs.readFileSync(
          ContextPath.replace(/RESOURCE/, obj.resourceType), // e.g. s/RESOURCE/Patienbt/
          {encoding: 'utf-8'}
        )
      ) // @@ make async
    resolve(Contexts[obj.resourceType])
  }).then(context => {
    // Convert to (invented) FHIR/JSON-LD.
    const copy = JSON.parse(JSON.stringify(obj))
    addReferenceLinks(copy, "")
    copy['@context'] = context
    copy['@id'] = rootNode
    return copy
  }).then(copy => {
    // Parse the JSON-LD.
    return parseJsonld(copy, baseURL)
  }).then(nquads => {
    // console.log(`${resourceType + '/' + obj.id} VVV\n`, nquads, `\n^^^`)
    // Parse the resulting Turtle.
    return parseTurtle(nquads, baseURL, resourceType + '/' + obj.id)
  }).then(graph => {
    const bareStrings = [NS_fhir + "Narrative.div", NS_fhir + "Extension.url", NS_fhir + "Bundle.link.relation", NS_fhir + "value"]
    const ret = new N3.Store()
    ret.addQuad(quad(namedNode(rootNode), namedNode(NS_fhir + 'nodeRole'), namedNode(NS_fhir + 'treeRoot')))

    graph.getQuads().forEach(q => {
      if (q.predicate.value === RDF_type && q.object.value.indexOf(baseURL) === 0) {
        // rewrite type arc baseURL+X to fhir:X
        q.object = namedNode(NS_fhir + q.object.value.substr(baseURL.length))
        ret.addQuad(q)
      } else if (q.object.termType === "Literal" && bareStrings.indexOf(q.predicate.value) === -1) {
        // add in intermediate bnode a la: { ?s ?p ?x && ?x a Literal } => { ?s ?p [ fhir:value ?x ] }
        const bnode = blankNode('lit' + bnodeId++)
        ret.addQuad(quad(q.subject, q.predicate, bnode))
        ret.addQuad(quad(bnode, fhirValue, q.object))
      } else {
        ret.addQuad(q)
      }
    })
    return ret
  })
}


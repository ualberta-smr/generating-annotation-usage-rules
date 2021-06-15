from eulxml import xpath

input = """src:class[(src:annotation[src:name[text()='Path']] and src:annotation[src:name[text()='RegisterRestClient']] and descendant-or-self::src:decl_stmt/src:decl[(src:annotation[src:name[text()='Inject']] and src:annotation[src:name[text()='Claim']])] and src:block/src:function[(src:annotation[src:name[text()='Path']] and src:annotation[src:name[text()='Produces']] and src:annotation[src:name[text()='GET']] and src:annotation[src:name[text()='Traced']])])]"""

ast = xpath.parse(input)

def extractConditions(node, collection):
    if isinstance(node, xpath.ast.Step):
        name = node.node_test.name
        collection.append(xpath.serialize(node))
    elif isinstance(node, xpath.ast.BinaryExpression):
        op = node.op
        if op in ["and", "or"]:
            l, r = node.left, node.right
            extractConditions(l, collection)
            extractConditions(r, collection)
        else:
            collection.append(node)
    else:
        print("unknown node : %s" % str(node))


container = list()
extractConditions(ast.predicates[0], container)

for e in container:
    print(str(e), end='\n\n')
from utils import *
from eulxml import xpath

def find_violations(xml_dict, rules):
    for k, v in xml_dict.items():
        for rule in rules:
            pre_match = match_xpath(v, rule.precondition)
            if len(pre_match) > 0:
                post_match = match_xpath(v, rule.postcondition)
                if len(post_match) == 0:
                    yield {
                        "candidate-rule-id": rule.id,
                        "file": k,
                        "precondition": rule.precondition,
                        "postcondition": rule.postcondition,
                        "grammar": rule.grammar,
                        "elements": pre_match
                    }

def extractConditions(node, collection):
    if isinstance(node, xpath.ast.Step):
        collection.append(node)
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


def find_positions_of_violations(violations):
    for found in violations:
        clazz = found["elements"][0]
        xpath_ast_root = xpath.parse(found["postcondition"])
        aList = []
        extractConditions(xpath_ast_root.predicates[0], aList)

        failed = []
        for cond in aList:
            re = run_xpath_query(clazz, xpath.serialize(cond))
            if len(re) == 0:
                failed.append(cond)
        
        # class/interface level violations
        final_results = []
        for fail in failed:
            if isinstance(fail, xpath.ast.BinaryExpression):
                violation_positions = find_positions_in_binary_expression(fail, clazz) # assumes there's only one class
                final_results += violation_positions
            else:
                # can be:
                # - annotations
                # - extends/implements
                final_results.append({
                    "element": xpath.serialize(xpath_ast_root.node_test),
                    "violation": xpath.serialize(fail)
                })
        del found["elements"]
        found["details"] = final_results


def find_positions_in_binary_expression(be: xpath.ast.BinaryExpression, clazz):
    violations = []
    
    element = be.left
    matches = run_xpath_query(clazz, xpath.serialize(element))
    
    node_name = xpath.serialize(be.right.node_test)
    # assumes: be.right is always a 'xpath.ast.Step'
    for i, match in enumerate(matches):
        node_name_matches = run_xpath_query(match, node_name)
        for node_name_match in node_name_matches:
            predicates = be.right.predicates[0]
            aList = []
            extractConditions(predicates, aList)
            
            results = find_violations_in_function(node_name_match, aList)
            if results:
                for result in results:
                    violations.append({
                        "element": f"{xpath.serialize(element)}[{i+1}]",
                        "violation": xpath.serialize(result)
                    })
    return violations


def find_violations_in_function(function_element, predicates):
    """
    intended to work with src:function[PREDICATES]

    assumes all the predicates operations are 'AND's
    """
    results = [False] * len(predicates)
    for i, predicate in enumerate(predicates):
        r = function_element.xpath(xpath.serialize(predicate), namespaces=ns)
        results[i] = len(r) > 0
    # if above 40%
    isAbove50Percent = (sum(results) / len(results)) >= 0.4
    if isAbove50Percent:
        return list(map(lambda r: r[1], filter(lambda r: r[0] is False, zip(results, predicates))))
    return None
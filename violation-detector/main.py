# idea is the following
# 0. Given a project, generate xml files from the files using srcML
# 1. Take the rules.json file, and check the rules against any project.
# 2. Report on the violations.

from re import sub
import sys
import json
import glob
import os
from subprocess import Popen, PIPE
from lxml import etree
from typing import *
from dataclasses import *
from eulxml import xpath


@dataclass
class Rule:
    id: str
    """
    pre-condition
    """
    precondition: str
    """
    post-condition
    """
    postcondition: str
    grammar: str


def main(args: List[str]):
    rules_file, path_to_project, violations_output = args
    rules = list(get_rules(rules_file))
    print("Rules available: %d" % len(rules))

    filenames = get_files(path_to_project, 'java')
    print("Files available: %d" % len(filenames))
    
    file_xml_dict = execute_srcml(filenames)

    d = list(find_violations(file_xml_dict, rules))

    print("found: " + str(len(d)))

    # find_positions_of_violations(d)

    with open(violations_output, "w+") as f:
        json.dump(list(d), f, indent=4)

def extractConditions(node, collection):
    if isinstance(node, xpath.ast.Step):
        name = node.node_test.name
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


ns = {"src": "http://www.srcML.org/srcML/src",
      "pos": "http://www.srcML.org/srcML/position"}


def run_xpath_query(element, xpath_query):
    return element.xpath(xpath_query, namespaces=ns)

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
                position = get_positions(clazz)
                final_results.append({
                    "element": xpath.serialize(xpath_ast_root.node_test),
                    "violation": xpath.serialize(fail),
                    "position": position
                })
        del found["elements"]
        found["details"] = final_results

def get_positions(node):
    specifier = node.find("src:specifier", namespaces=ns)
    line_num = str(run_xpath_query(specifier, "@pos:line")[0])
    col_num = str(run_xpath_query(specifier, "@pos:column")[0])
    return (line_num, col_num)

def find_positions_in_binary_expression(be: xpath.ast.BinaryExpression, clazz):
    violations = []
    
    element = be.left
    matches = run_xpath_query(clazz, xpath.serialize(element))
    node_name = xpath.serialize(be.right.node_test)
    # assumes: be.right is always a 'xpath.ast.Step'
    for match in matches:
        # node_name_matches = match.xpath(node_name, namespaces=ns)
        node_name_matches = run_xpath_query(match, node_name)
        for node_name_match in node_name_matches:
            predicates = be.right.predicates[0]
            aList = []
            extractConditions(predicates, aList)
            results = find_violations_in_function(node_name_match, aList)
            if results:
                position = get_positions(node_name_match)
                for result in results:
                    violations.append({
                        "element": node_name,
                        "violation": xpath.serialize(result),
                        "position": position
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
    # if above 50%
    isAbove50Percent = (sum(results) / len(results)) > 0.5
    if isAbove50Percent:
        return list(map(lambda r: r[1], filter(lambda r: r[0] is False, zip(results, predicates))))
    return None

def match_xpath(xml_string, xpath):
    ns = {"src": "http://www.srcML.org/srcML/src"}
    tree = etree.fromstring(xml_string.encode("UTF-8"))
    return tree.xpath(xpath, namespaces=ns)


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
                        # "elements": pre_match
                    }


def get_rules(rules_path: str):
    with open(rules_path) as f:
        rules = json.load(f)
        for rule in rules:
            _id = rule["candidate_id"]
            pre = rule["quantifier"]
            pos = rule["constraint"]
            g = rule["grammar"]
            yield Rule(_id, pre, pos, g)


def get_files(path, lang):
    # windows specific for now
    if not path.endswith(os.path.sep):
        path = path + os.path.sep
    path = path + "**"
    raw_files = glob.glob(path, recursive=True)
    return list(filter(lambda x: x.endswith("." + lang), raw_files))


def execute_srcml(filenames):
    results = dict()
    for filename in filenames:
        r1 = Popen(f"java -jar ../type-resolution/type-resolver.jar \"{filename}\" ../type-resolution/lib", stdout=PIPE)
        r2 = Popen(f"srcml --language Java --position", stdin=r1.stdout, stdout=PIPE)
        result = r2.communicate()
        if r2.returncode == 0:
            xml = result[0].decode('UTF-8')
            results[filename] = xml
    return results


# 3 args:
# <rules path> <project path> <violations output>
if __name__ == '__main__':
    main(sys.argv[1:])

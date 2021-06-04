# idea is the following
# 0. Given a project, generate xml files from the files using srcML
# 1. Take the rules.json file, and check the rules against any project.
# 2. Report on the violations.

import sys
import json
import glob
import os
import subprocess
from lxml import etree
from typing import *
from dataclasses import *


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
    rules = list(get_rules())
    print("Rules available: %d" % len(rules))

    path = args[0]
    violations_output = args[1]
    
    filenames = get_files(path, 'java')
    print("Files available: %d" % len(filenames))
    
    file_xml_dict = execute_srcml(filenames)

    d = find_violations(file_xml_dict, rules)
    with open(violations_output, "w+") as f:
        json.dump(list(d), f, indent=4)


def match_xpath(xml_string, xpath):
    ns = {"src": "http://www.srcML.org/srcML/src"}
    tree = etree.fromstring(xml_string.encode("UTF-8"))
    return tree.xpath(xpath, namespaces=ns)


def find_violations(xml_dict, rules):
    for k, v in xml_dict.items():
        for rule in rules:
            a = match_xpath(v, rule.precondition)
            if len(a) > 0:
                a = match_xpath(v, rule.postcondition)
                if len(a) == 0:
                    yield {
                        "candidate-rule-id": rule.id,
                        "file": k,
                        "precondition": rule.precondition,
                        "postcondition": rule.postcondition,
                        "grammar": rule.grammar
                    }


def get_rules():
    with open("rules.json") as f:
        rules = json.load(f)
        for rule in rules:
            _id = rule["candidate-id"]
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
        result = subprocess.run(["srcml", filename], capture_output=True)
        if result.returncode == 0:
            xml = result.stdout.decode('UTF-8')
            results[filename] = xml
    return results


if __name__ == '__main__':
    main(sys.argv[1:])

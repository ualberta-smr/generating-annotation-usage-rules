from typing import *
from dataclasses import *
import json
import os
import glob
from lxml import etree

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

ns = {"src": "http://www.srcML.org/srcML/src",
      "pos": "http://www.srcML.org/srcML/position"}


def run_xpath_query(element, xpath_query):
    return element.xpath(xpath_query, namespaces=ns)

def match_xpath(xml_string, xpath_query):
    tree = etree.fromstring(xml_string.encode("UTF-8"))
    return run_xpath_query(tree, xpath_query)
from utils import *
from lxml import etree

def get_positions(element_str, xml):
    results = match_xpath(xml, element_str)
    if (len(results) > 0):
        return get_positions_of_node(results[0])
    return None

def get_positions_of_node(node):
    specifier = run_xpath_query(node, "descendant::src:specifier")[0]
    line_num = str(run_xpath_query(specifier, "@pos:line")[0])
    col_num = str(run_xpath_query(specifier, "@pos:column")[0])
    return (line_num, col_num)

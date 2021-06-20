import json
import sys
from typing import List
from dataclasses import *
from model import *

def fqnToSimpleName(fully_qualified_name: str)-> str:
    return fully_qualified_name#.split(".")[-1]

def annotationsToGrammar(annos: List[Annotation]) -> str:
    return " and ".join(map(lambda anno: f"annotation \"{fqnToSimpleName(anno.name)}\"", annos))


def fieldToGrammar(field: Field) -> str:
    final_string = []
    a = field.annotations
    if len(a) > 0:
        final_string.append(annotationsToGrammar(a))

    if field.type:
        final_string.append(f"type \"{fqnToSimpleName(field.type.name)}\"")

    if len(final_string) > 0:
        return "declaration statement with (" + " and ".join(final_string) + " )"
    return ""


def methodToGrammar(function: Function) -> str:
    final_string = []
    a = function.annotations
    if len(a) > 0:
        final_string.append(annotationsToGrammar(a))

    if function.type:
        final_string.append(f"type \"{fqnToSimpleName(function.type.name)}\"")

    if len(final_string) > 0:
        return "function with (" + " and ".join(final_string)+" )"
    return ""


def toAntecedent(clazz: Class) -> str:
    final_string = []
    a = clazz.annotations
    if len(a) > 0:
        final_string.append(annotationsToGrammar(a))

    if clazz.field:
        final_string.append(fieldToGrammar(clazz.field))

    if clazz.function:
        final_string.append(methodToGrammar(clazz.function))

    return "class with (" + " and ".join(final_string) + " )"


def toConsequent(clazz: Class) -> str:
    final_string = []
    a = clazz.annotations
    if len(a) > 0:
        final_string.append(annotationsToGrammar(a))

    if clazz.field:
        final_string.append(fieldToGrammar(clazz.field))

    if clazz.function:
        final_string.append(methodToGrammar(clazz.function))

    return "(" + " and ".join(final_string) + " )"


def toRuleWithNoAntecedent(clazz: Class) -> str:
    final_string = []
    a = clazz.annotations
    if len(a) > 0:
        final_string.append(annotationsToGrammar(a))

    if clazz.field:
        final_string.append(fieldToGrammar(clazz.field))

    if clazz.function:
        final_string.append(methodToGrammar(clazz.function))

    return "class must have (" + " and ".join(final_string) + " )"


def toGrammar(rule: Rule) -> str:
    a = toAntecedent(rule.antecedent)
    c = toConsequent(rule.consequent)
    r = toRuleWithNoAntecedent(mergeClasses(rule.antecedent, rule.consequent))
    return {
        "id": rule.id,
        "rule": r,
        "antecedent_origin": "%s must have %s " % (a, c)
    }


def toGrammarAll(candidatesFile: str) -> List[str]:
    return list(
        filter(lambda x: not x["rule"].endswith("must have ( ) ") and \
            not x["antecedent_origin"].endswith("must have ( ) "),
               map(toGrammar, makeRulesList(candidatesFile))
        )
    )

# candidates file and grammar output file need to be json files
if __name__ == "__main__":
    _, candidatesFile, grammarRulesOutput = sys.argv
    # candidatesFile = "./rules.json"
    # grammarRulesOutput = "./out.json"
    with open(grammarRulesOutput, "w+") as f:
        json.dump(toGrammarAll(candidatesFile), f, indent=4)
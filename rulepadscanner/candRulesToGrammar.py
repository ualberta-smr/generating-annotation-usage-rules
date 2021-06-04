from typing import List
from dataclasses import *
from model import *

def annotationsToGrammar(annos: List[Annotation]) -> str:
    return " and ".join(map(lambda anno: f"annotation \"{anno.name}\"", annos))


def fieldToGrammar(field: Field) -> str:
    final_string = []
    a = field.annotations
    if len(a) > 0:
        final_string.append(annotationsToGrammar(a))

    if field.type:
        final_string.append("type " + field.type.name)

    if len(final_string) > 0:
        return "declaration statement with (" + " and ".join(final_string) + " )"
    return ""

def methodToGrammar(function: Function) -> str:
    final_string = []
    a = function.annotations
    if len(a) > 0:
        final_string.append(annotationsToGrammar(a))

    if function.type:
        final_string.append("type " + function.type.name)

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


def toGrammar(rule: Rule) -> str:
    format = "%s must have %s "
    a = toAntecedent(rule.antecedent)
    c = toConsequent(rule.consequent)
    return format % (a, c)


def toGrammarAll() -> List[str]:
    return list(
            filter(lambda x: not x.endswith("must have ( ) "), 
                map(toGrammar, makeRulesList())
            )
    )

with open("results.txt", "w+") as f:
    f.write("\n".join(toGrammarAll()).strip())
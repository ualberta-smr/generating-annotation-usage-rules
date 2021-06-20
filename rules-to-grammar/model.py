from dataclasses import *
from typing import *
import json


@dataclass
class Annotation:
    name: str
    param_name: str = None
    param_type: Type = None


@dataclass
class Type:
    name: str


@dataclass
class Function:
    annotations: List[Annotation] = field(default_factory=list)
    type: Type = None


@dataclass
class Field:
    annotations: List[Annotation] = field(default_factory=list)
    type: Type = None


@dataclass
class Class:
    annotations: List[Annotation] = field(default_factory=list)
    function: Function = None
    field: Field = None


@dataclass
class Rule:
    id: int
    antecedent: Class
    consequent: Class


@dataclass
class CandidateRule:
    id: int
    antecedent: List[str]
    consequent: List[str]
    label: str


def mergeFields(a: Field, b: Field) -> Field:
    if not (a or b):
        return a
    elif not a:
        return b
    elif not b:
        return a
    return Field(a.annotations + b.annotations, a.type if a.type else b.type)


def mergeFunctions(a: Function, b: Function) -> Function:
    if not (a or b):
        return a
    elif not a:
        return b
    elif not b:
        return a
    return Function(a.annotations + b.annotations, a.type if a.type else b.type)


def mergeClasses(a: Class, b: Class) -> Class:
    annotations = a.annotations + b.annotations
    field = mergeFields(a.field, b.field)
    function = mergeFunctions(a.function, b.function)
    return Class(annotations, function, field)


def loadRulesFromFile(candidatesFile:str) -> List[CandidateRule]:
    with open(candidatesFile) as f:
        rules = json.load(f)
        return list(
            map(lambda r: CandidateRule(r["id"], r["antecedent"], r["consequent"], r["label"]),
                filter(lambda r: r["label"] != "not a rule", rules)))


def makeRule(d: CandidateRule) -> Rule:
    a = partialToClass(d.antecedent)
    c = partialToClass(d.consequent)
    return Rule(d.id, a, c)


def makeRulesList(candidatesFile:str) -> List[Rule]:
    candidates = loadRulesFromFile(candidatesFile)
    return list(map(makeRule, candidates))


def partialToClass(facts: List[str]) -> Class:
    class_anno = []
    method_anno = []
    field_anno = []

    class_ext_impl = []

    field_type = None

    method_type = None
    method_param = []

    anno_info = {}
    for ant in facts:
        if "Class --" in ant:
            clazz = ant.split()[-1].split("_")[-1]
            if "annotatedWith" in ant:
                class_anno.append(clazz)
            elif "extends/implements" in ant:
                class_ext_impl.append(clazz)
        elif "Field --" in ant:
            if "annotatedWith" in ant:
                field_anno.append(ant.split()[-1].split("_")[-1])
            elif "hasType":
                field_type = ant.split()[-1]
        elif "Method --" in ant:
            if "annotatedWith" in ant:
                method_anno.append(ant.split()[-1].split("_")[-1])
            elif "hasType" in ant or "hasReturnType" in ant:
                method_type = ant.split()[-1]
            elif "hasParam" in ant:
                method_param.append(ant.split()[-1].split("_")[-1])
        elif ant.startswith("Annotation_"):
            f, s, t = ant.split()
            if "hasParam" in ant:
                anno_type = f.split("_")[-1]
                a, b = t.split(":")
                a = a.split("_")[-1]
                anno_info[anno_type] = (a, b)

    def makeAnnotation(full_path_anno: str) -> Annotation:
        canonical_name = full_path_anno
        param_name, param_type = None, None
        if full_path_anno in anno_info:
            param_name, param_type = anno_info[full_path_anno]
        return Annotation(canonical_name, param_name, param_type)

    class_annotations = list(map(makeAnnotation, class_anno))
    method_annotations = list(map(makeAnnotation, method_anno))
    field_annotations = list(map(makeAnnotation, field_anno))

    method_type = Type(method_type) if method_type else None
    field_type = Type(field_type) if field_type else None

    method = Function(
        method_annotations, method_type) if method_annotations or method_type else None
    field = Field(field_annotations,
                  field_type) if field_annotations or field_type else None

    return Class(class_annotations, method, field)
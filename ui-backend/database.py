from enum import Enum
from dataclasses import dataclass
import json
from typing import Any, Dict

import rulepadFormat as rf


def getDataFromSourceConfirmed():
    with open("data_confirmed.json") as j:
        values = json.load(j)
        return map(lambda x: rf.JsonRule(x["id"], x["antecedent"], x["consequent"]), values)


def getDataFromMinedSource():
    with open("data_mined.json") as j:
        values = json.load(j)

        def toJsonRule(x):
            ant = x["antecedent"]
            con = x["consequent"]

            new_ant = []
            cand = []

            for a in ant:
                if "(definedIn)" in a or (a.startswith("Annotation_") and "(hasParam)" in a):
                    cand.append(a)
                else:
                    new_ant.append(a)

            con = cand if cand else [ant.pop()]
            ant = new_ant if cand else ant
            return rf.JsonRule(x["id"], ant, con)

        return map(toJsonRule, values)

@dataclass
class RuleDTO:
    data: Any
    hasPrev: bool
    hasNext: bool
    label: str

class RuleLabels(Enum):
    CORRECT = 1
    NOT_A_RULE = 2

class Database:
    def __init__(self) -> None:
        self.__data = []
        # id -> label
        self.__labeledRules: Dict[int, str] = {}

    def initialize(self):
        data = getDataFromMinedSource()
        self.__data = list(map(lambda jf: {"id": jf.id,
                                           "ruleString": rf.toShortRulePad(jf)},
                               data))

    def data(self):
        return self.__data

    def __findNextInDatabase(self, id: int) -> RuleDTO:
        for i, rule in enumerate(self.__data):
            if id == rule["id"]:
                l = len(self.__data)
                hasNext = i < l - 2
                datum = self.__data[i + 1] if i < l - 1 else None
                return RuleDTO(datum, True, hasNext, self.__getRuleLabel(datum["id"]))
        return RuleDTO(None, False, False, False)

    def __findPrevInDatabase(self, id: int) -> RuleDTO:
        for i in range(len(self.__data) - 1, -1, -1):
            rule = self.__data[i]
            if id == rule["id"]:
                hasPrev = i > 1
                datum = self.__data[i - 1] if i > 0 else None
                return RuleDTO(datum, hasPrev, True, self.__getRuleLabel(datum["id"]))
        return RuleDTO(None, False, False, False)

    def getNext(self, id: int) -> RuleDTO:
        if id is None:
            e = self.__data[0]
            return RuleDTO(e, False, True, self.__getRuleLabel(e["id"])) # TODO: prev or next might be false when there's only 1 element
        return self.__findNextInDatabase(id)

    def getPrev(self, id: int) -> RuleDTO:
        if id is None:
            e = self.__data[0]
            return RuleDTO(e, False, True, self.__getRuleLabel(e["id"])) # TODO: prev or next might be false when there's only 1 element
        return self.__findPrevInDatabase(id)

    def labelRuleCorrect(self, id: int, rulePadString: str):
        # update the rule
        for rule in self.__data:
            if rule["id"] == id:
                rule["ruleString"] = rulePadString
        self.__labeledRules[id] = RuleLabels.CORRECT
    
    def labelNotARule(self, id: int):
        self.__labeledRules[id] = RuleLabels.NOT_A_RULE

    def unlabel(self, id: int):
        del self.__labeledRules[id]

    def __getRuleLabel(self, id):
        if id in self.__labeledRules:
            return "correct" if self.__labeledRules[id] == RuleLabels.CORRECT else "not_a_rule"
        return "unlabeled"
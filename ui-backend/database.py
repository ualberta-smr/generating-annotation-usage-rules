from enum import Enum
from dataclasses import dataclass
import json
from typing import Any, Dict, Iterator

import rulepadFormat as rf


def getDataFromSourceConfirmed() -> Iterator[rf.JsonRule]:
    with open("./data/data_confirmed.json") as j:
        values = json.load(j)
        return map(lambda x: rf.JsonRule(x["id"], x["antecedent"], x["consequent"]), values)

def getDataFromSourceMicroProfile() -> Iterator[rf.JsonRule]:
    with open("./data/data_final_mp.json") as j:
        values = json.load(j)
        return map(lambda x: rf.JsonRule(x["id"], x["antecedent"], x["consequent"]), values)

def getDataFromMinedSource() -> Iterator[rf.JsonRule]:
    with open("./data/data_mined_no_consequent.json") as j:
        values = json.load(j)

        def toJsonRule(x):
            antecedents = x["antecedent"]

            annotations_hasParam = set(
                map(
                    lambda x: x.split()[0].split("_")[-1],
                    filter(lambda x: x.startswith("Annotation_") and "hasParam" in x, antecedents))
            )

            consequent_candidate = None
            for a in antecedents:
                if "(definedIn)" in a:
                    consequent_candidate = a
                    break
                if "(annotatedWith)" in a:
                    simpleName = a.split()[-1].split("_")[-1]
                    if simpleName not in annotations_hasParam:
                        consequent_candidate = a
                        break

            # handling special case where there are only 2 elements and 1 of them is hasParam on annotation
            if len(antecedents) == 2:
                ll = list(filter(lambda x: x.startswith(
                    "Annotation_") and "hasParam" in x, antecedents))
                if len(ll) != 0:
                    consequents = ll
                    antecedents = [item for item in antecedents if item not in consequents]
                    return rf.JsonRule(x["id"], antecedents, consequents)

            consequents = [consequent_candidate] if consequent_candidate else [antecedents.pop(-1)]
            antecedents = [item for item in antecedents if item not in consequent_candidate]
            return rf.JsonRule(x["id"], antecedents, consequents)

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
        data = getDataFromSourceMicroProfile()
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
            # TODO: prev or next might be false when there's only 1 element
            return RuleDTO(e, False, True, self.__getRuleLabel(e["id"]))
        return self.__findNextInDatabase(id)

    def getPrev(self, id: int) -> RuleDTO:
        if id is None:
            e = self.__data[0]
            # TODO: prev or next might be false when there's only 1 element
            return RuleDTO(e, False, True, self.__getRuleLabel(e["id"]))
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

from dataclasses import dataclass
import json
from typing import Any

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
class Triplet:
    data: Any
    hasPrev: bool
    hasNext: bool

class Database:
    def __init__(self) -> None:
        self.__data = []

    def initialize(self):
        data = getDataFromMinedSource()
        self.__data = list(map(lambda jf: {"id": jf.id,
                                           "ruleString": rf.toShortRulePad(jf)},
                               data))

    def data(self):
        return self.__data

    def __findNextInDatabase(self, id: int) -> Triplet:
        for i, rule in enumerate(self.__data):
            if id == rule["id"]:
                l = len(self.__data)
                hasNext = i < l - 2
                datum = self.__data[i + 1] if i < l - 1 else None
                return Triplet(datum, True, hasNext)
        return Triplet(None, False, False)

    def __findPrevInDatabase(self, id: int) -> Triplet:
        for i in range(len(self.__data) - 1, -1, -1):
            rule = self.__data[i]
            if id == rule["id"]:
                hasPrev = i > 1
                datum = self.__data[i - 1] if i > 0 else None
                return Triplet(datum, hasPrev, True)
        return Triplet(None, False, False)

    def getNext(self, id: int) -> Triplet:
        if id is None:
            return Triplet(self.__data[0], False, True) # TODO: might be false when there's only 1 element
        return self.__findNextInDatabase(id)

    def getPrev(self, id: int) -> Triplet:
        if id is None:
            return Triplet(self.__data[0], False, True) # TODO: might be false when there's only 1 element
        return self.__findPrevInDatabase(id)

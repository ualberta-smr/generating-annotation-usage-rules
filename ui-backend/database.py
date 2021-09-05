import json
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
            con.append(ant.pop())
            return rf.JsonRule(x["id"], ant, con)

        return map(toJsonRule, values)


class Database:
    def __init__(self) -> None:
        self.__data = []

    def initialize(self):
        data = getDataFromMinedSource()
        self.__data = list(map(lambda jf: {"id": jf.id,
                                           "rule_string": rf.toShortRulePad(jf)},
                               data))

    def data(self):
        return self.__data

    def __findNextInDatabase(self, id: int):
        for i, rule in enumerate(self.__data):
            if id == rule["id"]:
                hasNext = i < len(self.__data) - 2
                datum = self.__data[i +
                                    1] if i < len(self.__data) - 1 else None
                return datum, hasNext
        return None, False

    def getNext(self, id: int):
        if id is None:
            return {
                "data": self.__data[0],
                "hasNext": True  # TODO: might be false
            }
        datum, hasNext = self.__findNextInDatabase(id)
        return {
            "data": datum,
            "hasNext": hasNext
        }

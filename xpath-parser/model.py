from dataclasses import *
from typing import *
from enum import Enum

class Operation(Enum):
    AND = 1
    OR = 2
    NO_OP = 0


class Node:
    previous_result: bool = True
    next_operation: Operation
    next_node: Node

    # abstract method
    def evaluate(self, xml):
        pass

@dataclass
class SimpleNode(Node):
    xpath_query: str

    def evaluate(self, xml):
        pass


@dataclass
class ComplexNode(Node):
    chain: Node

    def evaluate(self, xml):
        copy_chain = self.chain
        result = copy_chain.previous_result
        op = copy_chain.next_operation
        next = copy_chain.next_node
        eval_result = next.evaluate(xml)

        if op is Operation.AND and (result and eval_result):
            pass

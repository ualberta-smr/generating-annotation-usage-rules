# Generated from RulepadGrammar.g4 by ANTLR 4.9.2
from typing import List
from dataclasses import *

@dataclass
class Part:
    is_antecedent: bool = field(default=None, init=False)

@dataclass
class Param(Part):
    type: str
    name: str

@dataclass
class Annotation(Part):
    type: str
    param: Param = field(default=None)

@dataclass
class Field(Part):
    type: str = "Object"
    annotations: List[Annotation] = field(default_factory=[])

@dataclass
class Method(Part):
    returnType: str = "void"
    parameters: List[Param] = field(default_factory=[])
    annotations: List[Annotation] = field(default_factory=[])

@dataclass
class JavaClass(Part):
    annotations: List[Annotation] = field(default_factory=[])
    extendedClass: str = None
    implementedInterfaces: List[str] = field(default_factory=[])
    field: Field = None
    method: Method = None
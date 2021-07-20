# Generated from RulepadGrammar.g4 by ANTLR 4.9.2
from typing import List
from dataclasses import *

@dataclass
class Annotation:
    type: str
    # param: str

@dataclass
class Field:
    type: str = "Object"
    annotations: List[Annotation] = field(default_factory=[])

@dataclass
class Param:
    type: str
    name: str

@dataclass
class Method:
    returnType: str = "void"
    parameters: List[Param] = field(default_factory=[])
    annotations: List[Annotation] = field(default_factory=[])

@dataclass
class JavaClass:
    annotations: List[Annotation] = field(default_factory=[])
    extendedClass: str = None
    implementedInterfaces: List[str] = field(default_factory=[])
    field: Field = None
    method: Method = None
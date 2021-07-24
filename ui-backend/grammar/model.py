# Generated from RulepadGrammar.g4 by ANTLR 4.9.2
from re import L
from typing import List
from dataclasses import *

@dataclass
class Part:
    is_antecedent: bool = field(default=None, init=False)

@dataclass
class Type(Part):
    name: str

@dataclass
class ConfigurationProperty(Part):
    name: str
    type: Type

@dataclass
class ConfigurationFile(Part):
    name: str
    properties: List[ConfigurationProperty] = field(default_factory=[])

@dataclass
class Param(Part):
    type: Type
    name: str

@dataclass
class Annotation(Part):
    type: Type
    param: Param = field(default=None)

@dataclass
class Field(Part):
    type: Type = field(default=Type("Object"))
    annotations: List[Annotation] = field(default_factory=[])

@dataclass
class Method(Part):
    returnType: Type = field(default=Type("void"))
    parameters: List[Param] = field(default_factory=[])
    annotations: List[Annotation] = field(default_factory=[])

@dataclass
class JavaClass(Part):
    annotations: List[Annotation] = field(default_factory=[])
    extendedClass: Type = None
    implementedInterfaces: List[Type] = field(default_factory=[])
    field: Field = None
    method: Method = None
    configurationFile: ConfigurationFile = None
from __future__ import annotations
from typing import List
from dataclasses import *

class AntecedentOrConsequent:
    is_antecedent: bool = None

@dataclass
class Type(AntecedentOrConsequent):
    name: str

@dataclass
class ConfigurationProperty(AntecedentOrConsequent):
    name: str
    type: Type

@dataclass
class ConfigurationFile(AntecedentOrConsequent):
    name: str
    properties: List[ConfigurationProperty] = field(default_factory=[])

@dataclass
class Param(AntecedentOrConsequent):
    type: Type
    name: str
    annotations: List[Annotation] = field(default_factory=[])

@dataclass
class Annotation(AntecedentOrConsequent):
    type: Type
    parameters: List[Param] = field(default_factory=[])

@dataclass
class Field(AntecedentOrConsequent):
    type: Type = field(default=Type("Object"))
    annotations: List[Annotation] = field(default_factory=[])

@dataclass
class Method(AntecedentOrConsequent):
    returnType: Type
    parameters: List[Param] = field(default_factory=[])
    annotations: List[Annotation] = field(default_factory=[])

@dataclass
class JavaClass(AntecedentOrConsequent):
    annotations: List[Annotation] = field(default_factory=[])
    extendedClass: Type = None
    implementedInterfaces: List[Type] = field(default_factory=[])
    field: Field = None
    method: Method = None
    configurationFile: ConfigurationFile = None
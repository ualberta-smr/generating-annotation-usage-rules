from typing import List
from dataclasses import *

class Part:
    is_antecedent: bool = None

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
    parameters: List[Param] = field(default_factory=[])

@dataclass
class Field(Part):
    type: Type = field(default=Type("Object"))
    annotations: List[Annotation] = field(default_factory=[])

@dataclass
class Method(Part):
    returnType: Type
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
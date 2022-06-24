from __future__ import annotations
from typing import List
from dataclasses import *

@dataclass
class Type:
    name: str

@dataclass
class ConfigurationProperty:
    name: str
    type: Type
    value: str

@dataclass
class ConfigurationFile:
    name: str
    properties: List[ConfigurationProperty] = field(default_factory=[])

@dataclass
class BeanDeclaration:
    name: str
    declared: bool = field(default=False)

@dataclass
class Param:
    type: Type
    name: str
    annotations: List[Annotation] = field(default_factory=[])

@dataclass
class AnnotationParam:
    type: Type
    name: str
    value: str

@dataclass
class Annotation:
    type: Type
    parameters: List[AnnotationParam] = field(default_factory=[])

@dataclass
class Field:
    type: Type = field(default=Type("Object"))
    annotations: List[Annotation] = field(default_factory=[])
    configurationFile: ConfigurationFile = None

@dataclass
class Method:
    returnType: Type
    parameters: List[Param] = field(default_factory=[])
    annotations: List[Annotation] = field(default_factory=[])
    configurationFile: ConfigurationFile = None

@dataclass
class JavaClass:
    annotations: List[Annotation] = field(default_factory=[])
    extendedClass: Type = None
    implementedInterfaces: List[Type] = field(default_factory=[])
    field: Field = None
    method: Method = None
    configurationFile: ConfigurationFile = None
    declaredInBeans: BeanDeclaration = None
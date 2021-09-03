from typing import List, Tuple
import re

if __name__ is not None and "." in __name__:
    from .model import *
else:
    from model import *

ANTECEDENT_SIGN_START = """<span class="antecedent">"""
ANTECEDENT_SIGN_END = "</span>"
CONSEQUENT_SIGN_START = """<span class="consequent">"""
CONSEQUENT_SIGN_END = "</span>"

TEMPLATE = '''
<ClassAnnotations>
class Foo <ExtendsTemplate> <ImplementsTemplate> {
<FieldDeclaration>
<MethodDeclaration>
}'''

def addSigns(obj: Part, string) -> str:
    if obj.is_antecedent is None:
        return string
    start, end = (ANTECEDENT_SIGN_START, ANTECEDENT_SIGN_END) if obj.is_antecedent else (CONSEQUENT_SIGN_START, CONSEQUENT_SIGN_END)
    return f"{start}{string}{end}"

def field(field: Field):
    if field is None:
        return ""
    t = "\t<FieldAnnotations>\n\tprivate <ReturnType> field;"
    annos = annotations(field.annotations, ch="\t").strip()
    return t.replace("<FieldAnnotations>", annos).replace("<ReturnType>", addSigns(field.type, field.type.name))

def functionParameters(function: Method):
    if len(function.parameters) == 0:
        return ""
    
    def functionParameter(p: Tuple[int, Param]) -> str:
        param = p[1]
        type_name = param.type.name 
        name = param.name if param.name else f"p{p[0]}"
        return addSigns(param, f"{type_name} {name}")

    return map(functionParameter, enumerate(function.parameters, start=1))

def function(function: Method):
    if function is None: 
        return ""
    t = "\t<MethodAnnotations>\n\tpublic <ReturnType> method(<FunctionParameters>) {}"
    annos = annotations(function.annotations, ch="\t").strip()
    params = ", ".join(functionParameters(function))
    return t.replace("<MethodAnnotations>", annos)\
            .replace("<ReturnType>", addSigns(function.returnType, function.returnType.name))\
            .replace("<FunctionParameters>", params)

def extends(extendedClass: Type):
    return "" if extendedClass is None else f"extends {addSigns(extendedClass, extendedClass.name)}"

def implements(interfaces: List[Type]):
    def interface(interface: Type) -> str:
        return addSigns(interface, interface.name)
    return "" if len(interfaces) == 0 else "implements " + ", ".join(map(interface, interfaces))

def annotations(annotations: List[Annotation], ch = "") -> str:
    def annotation(a: Annotation) -> str:
        result = f"@{a.type.name}"
        if a.parameters != []:
            params = ",".join(map(lambda p: addSigns(p, f"{'='.join(filter(lambda x: x is not None, [p.name, p.type.name]))}"), a.parameters))
            result = f"{result}({params})"
        return addSigns(a, result)
    return f"\n{ch}".join(map(annotation, annotations))

def javaClass(clazz: JavaClass):
    return TEMPLATE\
            .replace("<ClassAnnotations>", annotations(clazz.annotations))\
            .replace("<FieldDeclaration>", field(clazz.field))\
            .replace("<MethodDeclaration>", function(clazz.method))\
            .replace("<ExtendsTemplate>", extends(clazz.extendedClass))\
            .replace("<ImplementsTemplate>", implements(clazz.implementedInterfaces))

def configFiles(cf: ConfigurationFile) -> Tuple[str, str]:
    if cf is None:
        return None
    lines = "\n".join(
        map(lambda t: f"{t[0]}={t[1]}", map(lambda x: (x.name, x.type.name), cf.properties)))
    return cf.name, lines 
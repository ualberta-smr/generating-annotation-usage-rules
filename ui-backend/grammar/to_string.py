from typing import List, Tuple
import re

if __name__ is not None and "." in __name__:
    from .model import *
else:
    from model import *

ANTECEDENT_SIGN_START = """<span class="antecedent" title="Antecedent">"""
ANTECEDENT_SIGN_END = "</span>"
CONSEQUENT_SIGN_START = """<span class="consequent" title="Consequent">"""
CONSEQUENT_SIGN_END = "</span>"

TEMPLATE = '''
<ClassAnnotations>
class Foo <ExtendsTemplate> <ImplementsTemplate> {
<FieldDeclaration>
<MethodDeclaration>
}'''


def shortenTypeName(type: Type) -> str:
    if type is None or type.name is None:
        return None
    pieces = type.name.split(".")
    if len(pieces) > 1:
        simpleName = pieces[-1]
        pieces = pieces[:-1]
        if len(pieces) == 2 and ".".join(pieces) == "java.lang":
            return simpleName
        return ".".join(map(lambda x: x[0], pieces))+"."+simpleName
    else:
        return type.name


def addSigns(obj: AntecedentOrConsequent, string) -> str:
    if obj.is_antecedent is None:
        return string
    start, end = (ANTECEDENT_SIGN_START, ANTECEDENT_SIGN_END) if obj.is_antecedent else (
        CONSEQUENT_SIGN_START, CONSEQUENT_SIGN_END)
    return f"{start}{string}{end}"


def field(field: Field):
    if field is None:
        return ""
    t = "\t<FieldAnnotations>\n\tprivate <ReturnType> field;"
    annos = handleAnnotations(field.annotations, ch="\t").strip()
    return t.replace("<FieldAnnotations>", annos).replace("<ReturnType>", addSigns(field.type, shortenTypeName(field.type)))


def functionParameters(function: Method):
    if len(function.parameters) == 0:
        return ""

    def functionParameter(p: Tuple[int, Param]) -> str:
        # @A @B @C String value
        param = p[1]
        anno_str = " ".join(handleAnnotations(param.annotations).splitlines()) + " " if param.annotations else ""
        type_name = shortenTypeName(param.type)
        name = param.name if param.name else f"p{p[0]}"
        return addSigns(param, f"{anno_str}{type_name} {name}")

    return map(functionParameter, enumerate(function.parameters, start=1))


def function(function: Method):
    if function is None:
        return ""
    t = "\t<MethodAnnotations>\n\tpublic <ReturnType> method(<FunctionParameters>) {}"
    annos = handleAnnotations(function.annotations, ch="\t").strip()
    params = ", ".join(functionParameters(function))
    return t.replace("<MethodAnnotations>", annos)\
            .replace("<ReturnType>", addSigns(function.returnType, shortenTypeName(function.returnType)))\
            .replace("<FunctionParameters>", params)


def extends(extendedClass: Type):
    return "" if extendedClass is None else f"extends {addSigns(extendedClass, shortenTypeName(extendedClass))}"


def implements(interfaces: List[Type]):
    def interface(interface: Type) -> str:
        return addSigns(interface, shortenTypeName(interface))
    return "" if len(interfaces) == 0 else "implements " + ", ".join(map(interface, interfaces))


def handleAnnotations(annotations: List[Annotation], ch="") -> str:
    def annotation(a: Annotation) -> str:
        result = f"@{shortenTypeName(a.type)}"
        if a.parameters != []:
            params = ",".join(map(lambda p: addSigns(
                p, f"{'='.join(filter(lambda x: x is not None, [p.name, shortenTypeName(p.type)]))}"), a.parameters))
            result = f"{result}({params})"
        return addSigns(a, result)
    return f"\n{ch}".join(map(annotation, annotations))


def javaClass(clazz: JavaClass):
    return TEMPLATE\
        .replace("<ClassAnnotations>", handleAnnotations(clazz.annotations))\
        .replace("<FieldDeclaration>", field(clazz.field))\
        .replace("<MethodDeclaration>", function(clazz.method))\
        .replace("<ExtendsTemplate>", extends(clazz.extendedClass))\
        .replace("<ImplementsTemplate>", implements(clazz.implementedInterfaces))


def configFiles(cf: ConfigurationFile) -> Tuple[str, str]:
    if cf is None:
        return None
    lines = "\n".join(
        map(lambda t: f"{t[0]}={t[1]}", map(lambda x: (x.name, shortenTypeName(x.type)), cf.properties)))
    return cf.name, lines

from typing import List, Optional, Tuple, Dict, Union
from .model import *
import inspect

ANTECEDENT_SIGN_START = """<span class="antecedent" title="Antecedent">"""
ANTECEDENT_SIGN_END = "</span>"
CONSEQUENT_SIGN_START = """<span class="consequent" title="Consequent">"""
CONSEQUENT_SIGN_END = "</span>"

TEMPLATE = '''
<ClassAnnotations>
class Foo <ExtendsTemplate><ImplementsTemplate> {
<FieldDeclaration><MethodDeclaration>
}'''


def shortenTypeName(type: Type) -> str:
    if type is None or type.name is None:
        return None
    pieces = type.name.split(".")
    if len(pieces) > 1:
        # assumes that the package names will be all lowercase
        # a.b.c.A => A
        # a.b.c.D.A => D.A
        simpleName = ".".join(filter(lambda x: x[0].isupper(), pieces))
        return simpleName
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
    t = "\n\t<FieldAnnotations>\n\tprivate <ReturnType> field;"
    annos = handleAnnotations(field.annotations, ch="\t").strip()
    return t.replace("<FieldAnnotations>", annos).replace("<ReturnType>", addSigns(field.type, shortenTypeName(field.type)))


def functionParameters(function: Method):
    if len(function.parameters) == 0:
        return ""

    def functionParameter(p: Tuple[int, Param]) -> str:
        # @A @B @C String value
        param = p[1]
        anno_str = " ".join(handleAnnotations(
            param.annotations).splitlines()) + " " if param.annotations else ""
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


def paramToString(p: Union[ConfigurationProperty, AnnotationParam]) -> str:
    name_ = "?"
    if name_:
        name_ = p.name
    if p.value is None:
        if p.type is None or p.type.name is None:
            value_ = "?"
        else:
            value_ = shortenTypeName(p.type)
    else:
        value_ = p.value.strip()
    return f"{name_}={value_}"


def handleAnnotations(annotations: List[Annotation], ch="") -> str:
    def annotation(a: Annotation) -> str:
        result = f"@{shortenTypeName(a.type)}"
        if a.parameters != []:
            params = ",".join(map(lambda p: addSigns(
                p, paramToString(p)), a.parameters))
            result = f"{result}({params})"
        return addSigns(a, result)
    return f"\n{ch}".join(map(annotation, annotations))


def javaClass(clazz: JavaClass) -> str:
    return TEMPLATE\
        .replace("<ClassAnnotations>", handleAnnotations(clazz.annotations))\
        .replace("<FieldDeclaration>", field(clazz.field))\
        .replace("<MethodDeclaration>", function(clazz.method))\
        .replace("<ExtendsTemplate>", extends(clazz.extendedClass))\
        .replace("<ImplementsTemplate>", implements(clazz.implementedInterfaces))


def beanDeclaration(bd: BeanDeclaration) -> Tuple[str, str]:
    if bd is None:
        return None


    if bd.declared:
        body = """&lt;bean id="..." class="Foo" /&gt;"""
    else:
        body = """&lt;!--empty--&gt;"""

    lines = inspect.cleandoc("""
    &lt;beans&gt;
      BODY
    &lt;/beans&gt;
    """).lstrip().replace("BODY", body)
    return bd.name, lines


def configFiles(cf: ConfigurationFile) -> Tuple[str, str]:
    if cf is None:
        return None

    lines = "\n".join(
        map(paramToString, cf.properties))
    return cf.name, lines


def configurationFiles(jc: JavaClass) -> List[Dict[str, str]]:
    configuredObj = __extractConfigurationObj(jc)
    bd = beanDeclaration(jc.declaredInBeans)
    if configuredObj:
        cf = configFiles(configuredObj.configurationFile)
        configs = [cf, bd]
    else:
        configs = [bd]
    
    return list(map(lambda x: {
        "filename": x[0],
        "code": x[1]
    }, filter(lambda x: x is not None, configs)))

def __extractConfigurationObj(obj: JavaClass) -> Optional[Union[JavaClass, Method, Field]]:
    """
        returns the object that has a config file
    """
    if obj.configurationFile:
        return obj
    elif obj.field and obj.field.configurationFile:
        return obj.field
    elif obj.method and obj.method.configurationFile:
        return obj.method
    return None
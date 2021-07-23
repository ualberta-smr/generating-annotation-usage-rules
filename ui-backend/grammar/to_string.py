if __name__ is not None and "." in __name__:
    from .model import *
else:
    from model import *

def field(field: Field):
    if field is None:
        return ""
    t = "\t<FieldAnnotations>\n\tprivate <ReturnType> field;"
    annos = annotations(field.annotations, ch="\t").strip()
    return t.replace("<FieldAnnotations>", annos).replace("<ReturnType>", field.type.name)

def functionParameters(function: Method):
    if len(function.parameters) == 0:
        return ""
    return map(lambda p: f"{p[1].type.name} p{p[0]}", enumerate(function.parameters, start=1))

def function(function: Method):
    if function is None: 
        return ""
    t = "\t<MethodAnnotations>\n\tpublic <ReturnType> method(<FunctionParameters>) {}"
    annos = annotations(function.annotations, ch="\t").strip()
    params = ", ".join(functionParameters(function))
    return t.replace("<MethodAnnotations>", annos)\
            .replace("<ReturnType>", function.returnType.name)\
            .replace("<FunctionParameters>", params)

def extends(extendedClass: Type):
    return "" if extendedClass is None else f"extends {extendedClass.name}"

def implements(interfaces: List[Type]):
    return "" if len(interfaces) == 0 else "implements " + ", ".join(map(lambda t: t.name, interfaces))

def annotations(annotations: List[Annotation], ch = "") -> str:
    def annotation(a: Annotation) -> str:
        result = f"@{a.type.name}"
        if a.param is not None:
            result += f"({'='.join(filter(lambda x: x is not None, [a.param.name, a.param.type.name]))})"
        return result
    return f"\n{ch}".join(map(annotation, annotations))

def javaClass(clazz: JavaClass):
    template = '''
<ClassAnnotations>
class Foo <ExtendsTemplate> <ImplementsTemplate> {

<FieldDeclaration>
<MethodDeclaration>

}'''

    annos = annotations(clazz.annotations)

    return template\
            .replace("<ClassAnnotations>", annos)\
            .replace("<FieldDeclaration>", field(clazz.field))\
            .replace("<MethodDeclaration>", function(clazz.method))\
            .replace("<ExtendsTemplate>", extends(clazz.extendedClass))\
            .replace("<ImplementsTemplate>", implements(clazz.implementedInterfaces))

from antlr4 import *

if __name__ is not None and "." in __name__:
    from .RulepadGrammarLexer import RulepadGrammarLexer
    from .RulepadGrammarParser import RulepadGrammarParser
    from .RulepadGrammarListener import *
else:
    from RulepadGrammarLexer import RulepadGrammarLexer
    from RulepadGrammarParser import RulepadGrammarParser
    from RulepadGrammarListener import *

def toStringField(field: Field):
    if field is None:
        return ""
    t = "\t<FieldAnnotations>\n\tprivate <ReturnType> field;"
    annos = "\n\t".join(map(lambda x: f"@{x.type}", field.annotations)).strip()
    return t.replace("<FieldAnnotations>", annos).replace("<ReturnType>", field.type)

def toStringFunctionParameters(function: Method):
    if len(function.parameters) == 0:
        return ""
    return map(lambda p: f"{p[1].type} p{p[0]}", enumerate(function.parameters, start=1))

def toStringFunction(function: Method):
    if function is None: 
        return ""
    t = "\t<MethodAnnotations>\n\tpublic <ReturnType> method(<FunctionParameters>) {}"
    annos = "\n\t".join(map(lambda x: f"@{x.type}", function.annotations)).strip()
    params = ", ".join(toStringFunctionParameters(function))
    return t.replace("<MethodAnnotations>", annos)\
            .replace("<ReturnType>", function.returnType)\
            .replace("<FunctionParameters>", params)

def toStringExtends(extendedClass: str):
    return "" if extendedClass is None else f"extends {extendedClass}"

def toStringImplements(interfaces: List[str]):
    return "" if len(interfaces) == 0 else "implements " + ", ".join(interfaces)

def toStringJavaClass(clazz: JavaClass):
    template = '''
<ClassAnnotations>
class Demo <ExtendsTemplate> <ImplementsTemplate> {

<FieldDeclaration>
<MethodDeclaration>

}'''

    annos = "\n".join(map(lambda x: f"@{x.type}", clazz.annotations))

    return template\
            .replace("<ClassAnnotations>", annos)\
            .replace("<FieldDeclaration>", toStringField(clazz.field))\
            .replace("<MethodDeclaration>", toStringFunction(clazz.method))\
            .replace("<ExtendsTemplate>", toStringExtends(clazz.extendedClass))\
            .replace("<ImplementsTemplate>", toStringImplements(clazz.implementedInterfaces))


def convert(input):
    parser = RulepadGrammarParser(CommonTokenStream(RulepadGrammarLexer(InputStream(input))))
    tree = parser.inputSentence()

    listener = RulepadGrammarListener()
    walker = ParseTreeWalker()
    walker.walk(listener, tree)

    return toStringJavaClass(listener.getJavaClass()).strip()

# print(convert('class with annotation "Demo" must have extension of "SomeOtherClass" and (implementation of "IInterface" and implementation of "BInterface" )'))
# print(convert('class must have function with (parameter with type "HelloWorldItsAMe" and parameter with type "RequestObject" ) '))
print(convert("class with (function with (annotation \"org.eclipse.microprofile.reactive.messaging.<Outgoing Incoming>\" ) ) must have (annotation \"javax.enterprise.context.<ApplicationScoped Dependent>\" ) "))
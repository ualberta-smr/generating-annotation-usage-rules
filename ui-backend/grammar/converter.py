from antlr4 import *

if __name__ is not None and "." in __name__:
    from .RulepadGrammarLexer import RulepadGrammarLexer
    from .RulepadGrammarParser import RulepadGrammarParser
    from .RulepadGrammarListener import *
    from .listener import *
else:
    from RulepadGrammarLexer import RulepadGrammarLexer
    from RulepadGrammarParser import RulepadGrammarParser
    from RulepadGrammarListener import *
    from listener import *

def toStringField(field: Field):
    if field is None:
        return ""
    t = "\t<FieldAnnotations>\n\tprivate <ReturnType> field;"
    annos = toStringAnnotations(field.annotations, ch="\t").strip()
    return t.replace("<FieldAnnotations>", annos).replace("<ReturnType>", field.type)

def toStringFunctionParameters(function: Method):
    if len(function.parameters) == 0:
        return ""
    return map(lambda p: f"{p[1].type} p{p[0]}", enumerate(function.parameters, start=1))

def toStringFunction(function: Method):
    if function is None: 
        return ""
    t = "\t<MethodAnnotations>\n\tpublic <ReturnType> method(<FunctionParameters>) {}"
    annos = toStringAnnotations(function.annotations, ch="\t").strip()
    params = ", ".join(toStringFunctionParameters(function))
    return t.replace("<MethodAnnotations>", annos)\
            .replace("<ReturnType>", function.returnType)\
            .replace("<FunctionParameters>", params)

def toStringExtends(extendedClass: str):
    return "" if extendedClass is None else f"extends {extendedClass}"

def toStringImplements(interfaces: List[str]):
    return "" if len(interfaces) == 0 else "implements " + ", ".join(interfaces)

def toStringAnnotations(annotations: List[Annotation], ch = "") -> str:
    def toStringAnnotation(a: Annotation) -> str:
        result = f"@{a.type}"
        if a.param is not None:
            result += f"({'='.join(filter(lambda x: x is not None, [a.param.name, a.param.type]))})"
        return result
    return f"\n{ch}".join(map(toStringAnnotation, annotations))

def toStringJavaClass(clazz: JavaClass):
    template = '''
<ClassAnnotations>
class Foo <ExtendsTemplate> <ImplementsTemplate> {

<FieldDeclaration>
<MethodDeclaration>

}'''

    annos = toStringAnnotations(clazz.annotations)

    return template\
            .replace("<ClassAnnotations>", annos)\
            .replace("<FieldDeclaration>", toStringField(clazz.field))\
            .replace("<MethodDeclaration>", toStringFunction(clazz.method))\
            .replace("<ExtendsTemplate>", toStringExtends(clazz.extendedClass))\
            .replace("<ImplementsTemplate>", toStringImplements(clazz.implementedInterfaces))


def convert(input):
    lexer = RulepadGrammarLexer(InputStream(input))
    parser = RulepadGrammarParser(CommonTokenStream(lexer))
    parser.setTrace(not True)
    tree = parser.inputSentence()

    listener = ConcreteRulepadGrammarListener()
    walker = ParseTreeWalker()
    walker.walk(listener, tree)
    j = listener.getJavaClass()
    return toStringJavaClass(j).strip()

# print(convert('class with annotation "Demo" must have extension of "SomeOtherClass" and (implementation of "IInterface" and implementation of "BInterface" )'))
# print(convert('class must have function with (parameter with type "HelloWorldItsAMe" and parameter with type "RequestObject" ) '))
# print(convert("class with (function with (annotation \"org.eclipse.microprofile.reactive.messaging.<Outgoing Incoming>\" ) ) must have (annotation \"javax.enterprise.context.<ApplicationScoped Dependent>\" ) "))

# convert('class must have annotation "Hello" ')
# convert('class must have annotation with parameter with type "String" ')
# print(convert('class must have (annotation "Hello" with parameter with (type "String" and name "targetClassName" ) ) '))

a = """class with declaration statement with (annotation "Autowired" with parameter with (name "name" and type "String" ) ) must have annotation "Demo" """

# a = 'class with annotation "A" with parameter with type "String" must have annotation "A" with parameter with name "className" '

print(convert(a))

from antlr4 import *

if __name__ is not None and "." in __name__:
    from .RulepadGrammarLexer import RulepadGrammarLexer
    from .RulepadGrammarParser import RulepadGrammarParser
    from .RulepadGrammarListener import *
    from .listener import *
    from .to_string import *
else:
    from RulepadGrammarLexer import RulepadGrammarLexer
    from RulepadGrammarParser import RulepadGrammarParser
    from RulepadGrammarListener import *
    from listener import *
    from to_string import *


def convert(input):
    lexer = RulepadGrammarLexer(InputStream(input))
    parser = RulepadGrammarParser(CommonTokenStream(lexer))
    parser.setTrace(not True)
    tree = parser.inputSentence()

    listener = ConcreteRulepadGrammarListener()
    walker = ParseTreeWalker()
    walker.walk(listener, tree)
    j = listener.getJavaClass()
    return javaClass(j).strip(), configurationFiles(j)

def check(input):
    lexer = RulepadGrammarLexer(InputStream(input))
    parser = RulepadGrammarParser(CommonTokenStream(lexer))
    # parser.setTrace(True)
    tree = parser.inputSentence()

    listener = ConcreteRulepadGrammarListener()
    walker = ParseTreeWalker()
    walker.walk(listener, tree)
    j = listener.getJavaClass()
    import json
    print(json.dumps(j, default=lambda x: x.__dict__, indent=4))
    return None

# check(
#     """function with annotation "a.b.c.[A|B|C]" must have annotation "a.b.c.D" """
# )

# check(
#     """function with parameter "String value" with (annotation "Hello" and annotation "Bello" ) must have type "String" """
# )

# check(
#     """class with (function with parameter "java.lang.String" with annotation "PathParam" ) and annotation "org.eclipse.microprofile.rest.client.inject.RegisterRestClient" must have function with annotation "javax.ws.rs.Path" """
# )

# check(
#     """function with parameter with (type "String" and name "value" and annotation "a.b.c.Hello" ) must have type "String" """
# )

# check(
#     """class with (function with (annotation "org.eclipse.microprofile.reactive.messaging.Incoming" and annotation "org.eclipse.microprofile.reactive.messaging.Outgoing" with parameter "java.lang.String value" ) ) and annotation "javax.enterprise.context.ApplicationScoped" must have (function with annotation "org.eclipse.microprofile.reactive.messaging.Incoming" with parameter "java.lang.String value" ) """
# )

# check(
#     """class with annotation "Config" must have configuration file with property with (name "name" and type "String" ) """
# )

# check(
    # """class with annotation "Config" must have configuration file with property "List<String> name" """
# )

# check(
#     """function with annotation "ABC" must have type "String" and annotation "Hello" """
# )

# check (
#     """field with annotation "ABC" must have type "WebToken" """
# )

# check(
#     """function with annotation "Bulkhead" with parameter "int waitingTaskQueue" must have annotation "Asynchronous" """
# )

# check(
#     """function with annotation "A" must have type "B" """
# )

# check(
#     """class must have configuration file with property "String hello" """
# )

# check(
#     """class with function with annotation "RolesAllowed" must have (annotation "LoginConfig" and extension of "Application" ) or configuration file with property "String login-config" """
# )

# print(convert('class with annotation "Demo" must have extension of "SomeOtherClass" and (implementation of "IInterface" and implementation of "BInterface" )'))
# print(convert('class must have function with (parameter with type "HelloWorldItsAMe" and parameter with type "RequestObject" ) '))
# print(convert("class with (function with (annotation \"org.eclipse.microprofile.reactive.messaging.<Outgoing Incoming>\" ) ) must have (annotation \"javax.enterprise.context.<ApplicationScoped Dependent>\" ) "))

# convert('class must have annotation "Hello" ')
# convert('class must have annotation with parameter with type "String" ')
# print(convert('class must have (annotation "Hello" with parameter with (type "String" and name "targetClassName" ) ) '))

# a = """class with declaration statement with (annotation "Autowired" with parameter with (name "name" and type "String" ) ) must have annotation "Demo" and extension of "Hello" and (implementation of "IInterface" and implementation of "BInterface" ) """

# a = 'class with annotation "A" with parameter with type "String" must have annotation "A" with parameter with name "className" '

# print(convert(a))

# a = """class with function with (parameter with type "String" and annotation "AnnoA" ) must have declaration statement with (type "Bean" and annotation "AnnoB" ) """

# a = """class with function with annotation "Fallback" must have function with annotation "Fallback" with parameter with (name "fallbackMethod" and type "String" ) """

# print(convert(a))



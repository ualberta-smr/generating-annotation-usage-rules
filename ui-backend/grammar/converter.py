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
    import json
    # print(json.dumps(j, default=lambda x: x.__dict__, indent=4))
    return findRanges(javaClass(j).strip())

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

# print(convert(a))

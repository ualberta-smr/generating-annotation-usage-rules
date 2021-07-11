from antlr4 import *
from .RulepadGrammarLexer import RulepadGrammarLexer
from .RulepadGrammarParser import RulepadGrammarParser
from .RulepadGrammarListener import *

def convert(input):
    parser = RulepadGrammarParser(CommonTokenStream(RulepadGrammarLexer(InputStream(input))))
    tree = parser.inputSentence()

    listener = RulepadGrammarListener()
    walker = ParseTreeWalker()
    walker.walk(listener, tree)

    return toStringJavaClass(listener.getJavaClass())
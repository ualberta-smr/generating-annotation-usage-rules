from antlr4 import *

from .RulepadGrammarLexer import RulepadGrammarLexer
from .RulepadGrammarParser import RulepadGrammarParser
from .RulepadGrammarListener import *
from .listener import *
from .toString import *
from typing import Tuple, List, Dict

def rulepadToJavaCode(input) -> Tuple[str, List[Dict[str, str]]]:
    """
        Given Rulepad string (:input), the function returns a tuple:
            (java code preview, potential configuration file content preview)
    """
    lexer = RulepadGrammarLexer(InputStream(input))
    parser = RulepadGrammarParser(CommonTokenStream(lexer))
    tree = parser.start()

    listener = ConcreteRulepadGrammarListener()
    walker = ParseTreeWalker()
    walker.walk(listener, tree)
    j = listener.getJavaClass()
    return javaClass(j).strip(), configurationFiles(j)
from dataclasses import *
from antlr4 import *

if __name__ is not None and "." in __name__:
    from .RulepadGrammarParser import RulepadGrammarParser
    from .RulepadGrammarListener import RulepadGrammarListener
    from .model import *
else:
    from RulepadGrammarParser import RulepadGrammarParser
    from RulepadGrammarListener import RulepadGrammarListener
    from model import *


class ConcreteRulepadGrammarListener(RulepadGrammarListener):
    def __init__(self) -> None:
        super().__init__()
        self.annotations = []
        self.field = None
        self.function = None
        self.extendedClass = None
        self.implementedInterfaces = []
        self.clazz = JavaClass([], None, [], None, None)
        self.stack = [{
            'comingFrom': 'class',
            'node': self.clazz
        }]

    def getJavaClass(self) -> JavaClass:
        return self.clazz

    def enterAnnotations(self, ctx: RulepadGrammarParser.AnnotationsContext):
        try:
            annotationName = ctx.annotationCondition().combinatorialWords().getText().replace("\"", "")
        except:
            annotationName = None
        
        a = Annotation(annotationName)

        prev = self.stack[-1]
        if prev['comingFrom'] in ['class', 'function', 'field']:
            prev['node'].annotations.append(a)

        self.stack.append({
            'comingFrom': 'annotation',
            'node': a
        })
    
    def exitAnnotations(self, ctx:RulepadGrammarParser.AnnotationsContext):
        self.stack.pop()
    
    def enterExtensions(self, ctx:RulepadGrammarParser.ExtensionsContext):
        '''there can be multiple extensions'''
        extendedClass = ctx.extensionCondition().words().getText().replace('"', "")

        prev = self.stack[-1]
        if prev['comingFrom'] == 'class':
            prev['node'].extendedClass = extendedClass
    
    def enterImplementations(self, ctx:RulepadGrammarParser.ImplementationsContext):
        '''there can be multiple extensions'''
        prev = self.stack[-1]
        if prev['comingFrom'] == 'class':
            prev['node'].implementedInterfaces.append(ctx.implementationCondition().words().getText().replace('"', ""))

    def enterTypes(self, ctx:RulepadGrammarParser.TypesContext):
        try:
            type = ctx.typeCondition().combinatorialWords().getText().replace("\"", "")
        except:
            type = ctx.typeCondition().words().getText().replace("\"", "")

        prev = self.stack[-1]
        if prev['comingFrom'] == 'parameter':
            prev['node'].type = type
        elif prev['comingFrom'] == 'function':
            prev['node'].returnType = type
        elif prev['comingFrom'] == 'field':
            prev['node'].type = type
    
    def enterParameters(self, ctx:RulepadGrammarParser.ParametersContext):
        prev = self.stack[-1]
        p = Param(None, None)
        if prev['comingFrom'] == 'annotation':
            prev['node'].param = p
        elif prev['comingFrom'] == 'function':
            prev['node'].parameters.append(p)
        
        self.stack.append({
            'comingFrom': 'parameter',
            'node': p
        })

    def exitParameters(self, ctx:RulepadGrammarParser.ParametersContext):
        self.stack.pop()

    # Enter a parse tree produced by RulepadGrammarParser#functions.
    def enterFunctions(self, ctx:RulepadGrammarParser.FunctionsContext):
        method = Method("void", [], [])

        prev = self.stack[-1]
        if prev['comingFrom'] == 'class':
            prev['node'].method = method

        self.stack.append({
            'comingFrom': 'function',
            'node': method
        })


    # Exit a parse tree produced by RulepadGrammarParser#functions.
    def exitFunctions(self, ctx:RulepadGrammarParser.FunctionsContext):
        self.stack.pop()

    # Enter a parse tree produced by RulepadGrammarParser#declarationStatements.
    def enterDeclarationStatements(self, ctx:RulepadGrammarParser.DeclarationStatementsContext):
        field = Field("Object", [])
        prev = self.stack[-1]
        if prev['comingFrom'] == 'class':
            prev['node'].field = field

        self.stack.append({
            'comingFrom': 'field',
            'node': field
        })

    # Exit a parse tree produced by RulepadGrammarParser#declarationStatements.
    def exitDeclarationStatements(self, ctx:RulepadGrammarParser.DeclarationStatementsContext):
        self.stack.pop()

    # Enter a parse tree produced by RulepadGrammarParser#names.
    def enterNames(self, ctx:RulepadGrammarParser.NamesContext):
        name = ctx.nameCondition().words().getText().replace("\"", "")
        prev = self.stack[-1]
        if prev['comingFrom'] == 'parameter':
            prev['node'].name = name




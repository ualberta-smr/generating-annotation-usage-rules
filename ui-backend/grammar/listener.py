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
        self.__clazz = JavaClass([], None, [], None, None)
        self.__stack = [{
            'comingFrom': 'class',
            'node': self.__clazz
        }]
        self.__is_antecedent = True

    def getJavaClass(self) -> JavaClass:
        return self.__clazz

    # Enter a parse tree produced by RulepadGrammarParser#must.
    def enterMust(self, ctx:RulepadGrammarParser.MustContext):
        self.__is_antecedent = False

    def enterAnnotations(self, ctx: RulepadGrammarParser.AnnotationsContext):
        try:
            annotationType = self.initObj(
                Type(ctx.annotationCondition().combinatorialWords().getText().replace("\"", ""))
            )
        except:
            annotationType = None

        annotation = self.initObj(Annotation(annotationType))

        prev = self.__stack[-1]
        if prev['comingFrom'] in ['class', 'function', 'field']:
            prev['node'].annotations.append(annotation)

        self.__stack.append({
            'comingFrom': 'annotation',
            'node': annotation
        })
    
    def exitAnnotations(self, ctx:RulepadGrammarParser.AnnotationsContext):
        self.__stack.pop()
    
    def enterExtensions(self, ctx:RulepadGrammarParser.ExtensionsContext):
        '''there can be multiple extensions'''
        extendedClass = ctx.extensionCondition().words().getText().replace('"', "")

        prev = self.__stack[-1]
        if prev['comingFrom'] == 'class':
            prev['node'].extendedClass = self.initObj(Type(extendedClass))
    
    def enterImplementations(self, ctx:RulepadGrammarParser.ImplementationsContext):
        '''there can be multiple extensions'''
        prev = self.__stack[-1]
        if prev['comingFrom'] == 'class':
            className = ctx.implementationCondition().words().getText().replace('"', "")
            prev['node'].implementedInterfaces.append(self.initObj(Type(className)))

    def enterTypes(self, ctx:RulepadGrammarParser.TypesContext):
        try:
            type = ctx.typeCondition().combinatorialWords()
        except:
            type = ctx.typeCondition().words()

        type = self.initObj(Type(type.getText().replace("\"", "")))

        prev = self.__stack[-1]
        if prev['comingFrom'] == 'parameter':
            prev['node'].type = type
        elif prev['comingFrom'] == 'function':
            prev['node'].returnType = type
        elif prev['comingFrom'] == 'field':
            prev['node'].type = type
    
    def enterParameters(self, ctx:RulepadGrammarParser.ParametersContext):
        prev = self.__stack[-1]
        param = self.initObj(Param(None, None))
        if prev['comingFrom'] == 'annotation':
            prev['node'].param = param
        elif prev['comingFrom'] == 'function':
            prev['node'].parameters.append(param)
        
        self.__stack.append({
            'comingFrom': 'parameter',
            'node': param
        })

    def exitParameters(self, ctx:RulepadGrammarParser.ParametersContext):
        self.__stack.pop()

    # Enter a parse tree produced by RulepadGrammarParser#functions.
    def enterFunctions(self, ctx:RulepadGrammarParser.FunctionsContext):
        method = self.initObj(Method(self.initObj(Type("void")), [], []))

        prev = self.__stack[-1]
        if prev['comingFrom'] == 'class':
            prev['node'].method = method

        self.__stack.append({
            'comingFrom': 'function',
            'node': method
        })


    # Exit a parse tree produced by RulepadGrammarParser#functions.
    def exitFunctions(self, ctx:RulepadGrammarParser.FunctionsContext):
        self.__stack.pop()

    # Enter a parse tree produced by RulepadGrammarParser#declarationStatements.
    def enterDeclarationStatements(self, ctx:RulepadGrammarParser.DeclarationStatementsContext):
        field = self.initObj(Field(Type("Object"), []))
        
        prev = self.__stack[-1]
        if prev['comingFrom'] == 'class':
            prev['node'].field = field

        self.__stack.append({
            'comingFrom': 'field',
            'node': field
        })

    # Exit a parse tree produced by RulepadGrammarParser#declarationStatements.
    def exitDeclarationStatements(self, ctx:RulepadGrammarParser.DeclarationStatementsContext):
        self.__stack.pop()

    # Enter a parse tree produced by RulepadGrammarParser#names.
    def enterNames(self, ctx:RulepadGrammarParser.NamesContext):
        name = ctx.nameCondition().words().getText().replace("\"", "")
        prev = self.__stack[-1]
        if prev['comingFrom'] == 'parameter':
            prev['node'].name = name

    def initObj(self, obj):
        obj.is_antecedent = self.__is_antecedent
        return obj



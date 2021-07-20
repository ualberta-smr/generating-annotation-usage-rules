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

    def getJavaClass(self) -> JavaClass:
        return JavaClass(
            self.annotations, self.extendedClass, self.implementedInterfaces, self.field, self.function
        )

    def enterAnnotations(self, ctx: RulepadGrammarParser.AnnotationsContext):
        annotation = ctx.annotationCondition().combinatorialWords().getText().replace("\"", "")
        annotation = Annotation(annotation)
        comingFrom = ctx.parentCtx.__class__.__name__
        if comingFrom == 'ClassExpressionContext':
            self.annotations.append(annotation)
        elif comingFrom == 'DeclarationStatementExpressionContext':
            if self.field is None:
                self.field = Field('Object', [])
            self.field.annotations.append(annotation)
        elif comingFrom == 'FunctionExpressionContext':
            if self.function is None:
                self.function = Method('void', [], [])
            self.function.annotations.append(annotation)
    
    def enterExtensions(self, ctx:RulepadGrammarParser.ExtensionsContext):
        extendedClass = ctx.extensionCondition().words().getText().replace('"', "")
        if self.extendedClass is None:
            self.extendedClass = extendedClass
    
    def enterImplementations(self, ctx:RulepadGrammarParser.ImplementationsContext):
        self.implementedInterfaces.append(ctx.implementationCondition().words().getText().replace('"', ""))

    def enterTypes(self, ctx:RulepadGrammarParser.TypesContext):
        type = ctx.typeCondition().combinatorialWords().getText().replace("\"", "")
        comingFrom = ctx.parentCtx.__class__.__name__
        if comingFrom == 'DeclarationStatementExpressionContext':
            if self.field is None:
                self.field = Field(None, [])
            self.field.type = type
        elif comingFrom == 'FunctionExpressionContext':
            if self.function is None:
                self.function = Method('void', [], [])
            self.function.returnType = type
        elif comingFrom == "ParameterExpressionContext":
            if self.function is None:
                self.function = Method('void', [], [])
            self.function.parameters.append(Param(type, None))
# Generated from RulepadGrammar.g4 by ANTLR 4.9.2
from dataclasses import *
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .RulepadGrammarParser import RulepadGrammarParser
    from .model import *
else:
    from RulepadGrammarParser import RulepadGrammarParser
    from model import *

# This class defines a complete listener for a parse tree produced by RulepadGrammarParser.
class RulepadGrammarListener(ParseTreeListener):

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

    # Enter a parse tree produced by RulepadGrammarParser#inputSentence.
    def enterInputSentence(self, ctx:RulepadGrammarParser.InputSentenceContext):
        pass

    # Exit a parse tree produced by RulepadGrammarParser#inputSentence.
    def exitInputSentence(self, ctx:RulepadGrammarParser.InputSentenceContext):
        pass


    # Enter a parse tree produced by RulepadGrammarParser#mustClause.
    def enterMustClause(self, ctx:RulepadGrammarParser.MustClauseContext):
        classes = ctx.classes()
        # help(classes.classCondition().classExpression())
        # expr = ctx.classExpression()

    # Exit a parse tree produced by RulepadGrammarParser#mustClause.
    def exitMustClause(self, ctx:RulepadGrammarParser.MustClauseContext):
        pass


    # Enter a parse tree produced by RulepadGrammarParser#words.
    def enterWords(self, ctx:RulepadGrammarParser.WordsContext):
        pass

    # Exit a parse tree produced by RulepadGrammarParser#words.
    def exitWords(self, ctx:RulepadGrammarParser.WordsContext):
        pass


    # Enter a parse tree produced by RulepadGrammarParser#word.
    def enterWord(self, ctx:RulepadGrammarParser.WordContext):
        pass

    # Exit a parse tree produced by RulepadGrammarParser#word.
    def exitWord(self, ctx:RulepadGrammarParser.WordContext):
        pass


    # Enter a parse tree produced by RulepadGrammarParser#combinatorialWords.
    def enterCombinatorialWords(self, ctx:RulepadGrammarParser.CombinatorialWordsContext):
        pass

    # Exit a parse tree produced by RulepadGrammarParser#combinatorialWords.
    def exitCombinatorialWords(self, ctx:RulepadGrammarParser.CombinatorialWordsContext):
        pass


    # Enter a parse tree produced by RulepadGrammarParser#symbols.
    def enterSymbols(self, ctx:RulepadGrammarParser.SymbolsContext):
        pass

    # Exit a parse tree produced by RulepadGrammarParser#symbols.
    def exitSymbols(self, ctx:RulepadGrammarParser.SymbolsContext):
        pass


    # Enter a parse tree produced by RulepadGrammarParser#end.
    def enterEnd(self, ctx:RulepadGrammarParser.EndContext):
        pass

    # Exit a parse tree produced by RulepadGrammarParser#end.
    def exitEnd(self, ctx:RulepadGrammarParser.EndContext):
        pass


    # Enter a parse tree produced by RulepadGrammarParser#emptyLine.
    def enterEmptyLine(self, ctx:RulepadGrammarParser.EmptyLineContext):
        pass

    # Exit a parse tree produced by RulepadGrammarParser#emptyLine.
    def exitEmptyLine(self, ctx:RulepadGrammarParser.EmptyLineContext):
        pass


    # Enter a parse tree produced by RulepadGrammarParser#comments.
    def enterComments(self, ctx:RulepadGrammarParser.CommentsContext):
        pass

    # Exit a parse tree produced by RulepadGrammarParser#comments.
    def exitComments(self, ctx:RulepadGrammarParser.CommentsContext):
        pass


    # Enter a parse tree produced by RulepadGrammarParser#must.
    def enterMust(self, ctx:RulepadGrammarParser.MustContext):
        pass

    # Exit a parse tree produced by RulepadGrammarParser#must.
    def exitMust(self, ctx:RulepadGrammarParser.MustContext):
        pass


    # Enter a parse tree produced by RulepadGrammarParser#of.
    def enterOf(self, ctx:RulepadGrammarParser.OfContext):
        pass

    # Exit a parse tree produced by RulepadGrammarParser#of.
    def exitOf(self, ctx:RulepadGrammarParser.OfContext):
        pass


    # Enter a parse tree produced by RulepadGrammarParser#and_.
    def enterAnd_(self, ctx:RulepadGrammarParser.And_Context):
        pass

    # Exit a parse tree produced by RulepadGrammarParser#and_.
    def exitAnd_(self, ctx:RulepadGrammarParser.And_Context):
        pass


    # Enter a parse tree produced by RulepadGrammarParser#or_.
    def enterOr_(self, ctx:RulepadGrammarParser.Or_Context):
        pass

    # Exit a parse tree produced by RulepadGrammarParser#or_.
    def exitOr_(self, ctx:RulepadGrammarParser.Or_Context):
        pass


    # Enter a parse tree produced by RulepadGrammarParser#have.
    def enterHave(self, ctx:RulepadGrammarParser.HaveContext):
        pass

    # Exit a parse tree produced by RulepadGrammarParser#have.
    def exitHave(self, ctx:RulepadGrammarParser.HaveContext):
        pass


    # Enter a parse tree produced by RulepadGrammarParser#withWord.
    def enterWithWord(self, ctx:RulepadGrammarParser.WithWordContext):
        pass

    # Exit a parse tree produced by RulepadGrammarParser#withWord.
    def exitWithWord(self, ctx:RulepadGrammarParser.WithWordContext):
        pass


    # Enter a parse tree produced by RulepadGrammarParser#binary.
    def enterBinary(self, ctx:RulepadGrammarParser.BinaryContext):
        pass

    # Exit a parse tree produced by RulepadGrammarParser#binary.
    def exitBinary(self, ctx:RulepadGrammarParser.BinaryContext):
        pass


    # Enter a parse tree produced by RulepadGrammarParser#names.
    def enterNames(self, ctx:RulepadGrammarParser.NamesContext):
        pass

    # Exit a parse tree produced by RulepadGrammarParser#names.
    def exitNames(self, ctx:RulepadGrammarParser.NamesContext):
        pass


    # Enter a parse tree produced by RulepadGrammarParser#nameCondition.
    def enterNameCondition(self, ctx:RulepadGrammarParser.NameConditionContext):
        pass

    # Exit a parse tree produced by RulepadGrammarParser#nameCondition.
    def exitNameCondition(self, ctx:RulepadGrammarParser.NameConditionContext):
        pass


    # Enter a parse tree produced by RulepadGrammarParser#annotations.
    def enterAnnotations(self, ctx:RulepadGrammarParser.AnnotationsContext):
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


    # Exit a parse tree produced by RulepadGrammarParser#annotations.
    def exitAnnotations(self, ctx:RulepadGrammarParser.AnnotationsContext):
        pass


    # Enter a parse tree produced by RulepadGrammarParser#annotationCondition.
    def enterAnnotationCondition(self, ctx:RulepadGrammarParser.AnnotationConditionContext):
        pass

    # Exit a parse tree produced by RulepadGrammarParser#annotationCondition.
    def exitAnnotationCondition(self, ctx:RulepadGrammarParser.AnnotationConditionContext):
        pass


    # Enter a parse tree produced by RulepadGrammarParser#extensions.
    def enterExtensions(self, ctx:RulepadGrammarParser.ExtensionsContext):
        extendedClass = ctx.extensionCondition().words().getText().replace('"', "")
        if self.extendedClass is None:
            self.extendedClass = extendedClass

    # Exit a parse tree produced by RulepadGrammarParser#extensions.
    def exitExtensions(self, ctx:RulepadGrammarParser.ExtensionsContext):
        pass


    # Enter a parse tree produced by RulepadGrammarParser#extensionCondition.
    def enterExtensionCondition(self, ctx:RulepadGrammarParser.ExtensionConditionContext):
        pass

    # Exit a parse tree produced by RulepadGrammarParser#extensionCondition.
    def exitExtensionCondition(self, ctx:RulepadGrammarParser.ExtensionConditionContext):
        pass


    # Enter a parse tree produced by RulepadGrammarParser#implementations.
    def enterImplementations(self, ctx:RulepadGrammarParser.ImplementationsContext):
        self.implementedInterfaces.append(ctx.implementationCondition().words().getText().replace('"', ""))

    # Exit a parse tree produced by RulepadGrammarParser#implementations.
    def exitImplementations(self, ctx:RulepadGrammarParser.ImplementationsContext):
        pass


    # Enter a parse tree produced by RulepadGrammarParser#implementationCondition.
    def enterImplementationCondition(self, ctx:RulepadGrammarParser.ImplementationConditionContext):
        pass

    # Exit a parse tree produced by RulepadGrammarParser#implementationCondition.
    def exitImplementationCondition(self, ctx:RulepadGrammarParser.ImplementationConditionContext):
        pass


    # Enter a parse tree produced by RulepadGrammarParser#functions.
    def enterFunctions(self, ctx:RulepadGrammarParser.FunctionsContext):
        pass

    # Exit a parse tree produced by RulepadGrammarParser#functions.
    def exitFunctions(self, ctx:RulepadGrammarParser.FunctionsContext):
        pass


    # Enter a parse tree produced by RulepadGrammarParser#functionOf.
    def enterFunctionOf(self, ctx:RulepadGrammarParser.FunctionOfContext):
        pass

    # Exit a parse tree produced by RulepadGrammarParser#functionOf.
    def exitFunctionOf(self, ctx:RulepadGrammarParser.FunctionOfContext):
        pass


    # Enter a parse tree produced by RulepadGrammarParser#functionCondition.
    def enterFunctionCondition(self, ctx:RulepadGrammarParser.FunctionConditionContext):
        pass

    # Exit a parse tree produced by RulepadGrammarParser#functionCondition.
    def exitFunctionCondition(self, ctx:RulepadGrammarParser.FunctionConditionContext):
        pass


    # Enter a parse tree produced by RulepadGrammarParser#functionExpression.
    def enterFunctionExpression(self, ctx:RulepadGrammarParser.FunctionExpressionContext):
        pass

    # Exit a parse tree produced by RulepadGrammarParser#functionExpression.
    def exitFunctionExpression(self, ctx:RulepadGrammarParser.FunctionExpressionContext):
        pass


    # Enter a parse tree produced by RulepadGrammarParser#abstractFunctions.
    def enterAbstractFunctions(self, ctx:RulepadGrammarParser.AbstractFunctionsContext):
        pass

    # Exit a parse tree produced by RulepadGrammarParser#abstractFunctions.
    def exitAbstractFunctions(self, ctx:RulepadGrammarParser.AbstractFunctionsContext):
        pass


    # Enter a parse tree produced by RulepadGrammarParser#abstractFunctionOf.
    def enterAbstractFunctionOf(self, ctx:RulepadGrammarParser.AbstractFunctionOfContext):
        pass

    # Exit a parse tree produced by RulepadGrammarParser#abstractFunctionOf.
    def exitAbstractFunctionOf(self, ctx:RulepadGrammarParser.AbstractFunctionOfContext):
        pass


    # Enter a parse tree produced by RulepadGrammarParser#abstractFunctionCondition.
    def enterAbstractFunctionCondition(self, ctx:RulepadGrammarParser.AbstractFunctionConditionContext):
        pass

    # Exit a parse tree produced by RulepadGrammarParser#abstractFunctionCondition.
    def exitAbstractFunctionCondition(self, ctx:RulepadGrammarParser.AbstractFunctionConditionContext):
        pass


    # Enter a parse tree produced by RulepadGrammarParser#abstractFunctionExpression.
    def enterAbstractFunctionExpression(self, ctx:RulepadGrammarParser.AbstractFunctionExpressionContext):
        pass

    # Exit a parse tree produced by RulepadGrammarParser#abstractFunctionExpression.
    def exitAbstractFunctionExpression(self, ctx:RulepadGrammarParser.AbstractFunctionExpressionContext):
        pass


    # Enter a parse tree produced by RulepadGrammarParser#constructors.
    def enterConstructors(self, ctx:RulepadGrammarParser.ConstructorsContext):
        pass

    # Exit a parse tree produced by RulepadGrammarParser#constructors.
    def exitConstructors(self, ctx:RulepadGrammarParser.ConstructorsContext):
        pass


    # Enter a parse tree produced by RulepadGrammarParser#constructorOf.
    def enterConstructorOf(self, ctx:RulepadGrammarParser.ConstructorOfContext):
        pass

    # Exit a parse tree produced by RulepadGrammarParser#constructorOf.
    def exitConstructorOf(self, ctx:RulepadGrammarParser.ConstructorOfContext):
        pass


    # Enter a parse tree produced by RulepadGrammarParser#constructorCondition.
    def enterConstructorCondition(self, ctx:RulepadGrammarParser.ConstructorConditionContext):
        pass

    # Exit a parse tree produced by RulepadGrammarParser#constructorCondition.
    def exitConstructorCondition(self, ctx:RulepadGrammarParser.ConstructorConditionContext):
        pass


    # Enter a parse tree produced by RulepadGrammarParser#constructorExpression.
    def enterConstructorExpression(self, ctx:RulepadGrammarParser.ConstructorExpressionContext):
        pass

    # Exit a parse tree produced by RulepadGrammarParser#constructorExpression.
    def exitConstructorExpression(self, ctx:RulepadGrammarParser.ConstructorExpressionContext):
        pass


    # Enter a parse tree produced by RulepadGrammarParser#parameters.
    def enterParameters(self, ctx:RulepadGrammarParser.ParametersContext):
        pass

    # Exit a parse tree produced by RulepadGrammarParser#parameters.
    def exitParameters(self, ctx:RulepadGrammarParser.ParametersContext):
        pass


    # Enter a parse tree produced by RulepadGrammarParser#parameterCondition.
    def enterParameterCondition(self, ctx:RulepadGrammarParser.ParameterConditionContext):
        pass

    # Exit a parse tree produced by RulepadGrammarParser#parameterCondition.
    def exitParameterCondition(self, ctx:RulepadGrammarParser.ParameterConditionContext):
        pass


    # Enter a parse tree produced by RulepadGrammarParser#parameterExpression.
    def enterParameterExpression(self, ctx:RulepadGrammarParser.ParameterExpressionContext):
        pass

    # Exit a parse tree produced by RulepadGrammarParser#parameterExpression.
    def exitParameterExpression(self, ctx:RulepadGrammarParser.ParameterExpressionContext):
        pass


    # Enter a parse tree produced by RulepadGrammarParser#types.
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

    # Exit a parse tree produced by RulepadGrammarParser#types.
    def exitTypes(self, ctx:RulepadGrammarParser.TypesContext):
        pass


    # Enter a parse tree produced by RulepadGrammarParser#typeCondition.
    def enterTypeCondition(self, ctx:RulepadGrammarParser.TypeConditionContext):
        pass

    # Exit a parse tree produced by RulepadGrammarParser#typeCondition.
    def exitTypeCondition(self, ctx:RulepadGrammarParser.TypeConditionContext):
        pass


    # Enter a parse tree produced by RulepadGrammarParser#specifiers.
    def enterSpecifiers(self, ctx:RulepadGrammarParser.SpecifiersContext):
        pass

    # Exit a parse tree produced by RulepadGrammarParser#specifiers.
    def exitSpecifiers(self, ctx:RulepadGrammarParser.SpecifiersContext):
        pass


    # Enter a parse tree produced by RulepadGrammarParser#specifierCondition.
    def enterSpecifierCondition(self, ctx:RulepadGrammarParser.SpecifierConditionContext):
        pass

    # Exit a parse tree produced by RulepadGrammarParser#specifierCondition.
    def exitSpecifierCondition(self, ctx:RulepadGrammarParser.SpecifierConditionContext):
        pass


    # Enter a parse tree produced by RulepadGrammarParser#visibilities.
    def enterVisibilities(self, ctx:RulepadGrammarParser.VisibilitiesContext):
        pass

    # Exit a parse tree produced by RulepadGrammarParser#visibilities.
    def exitVisibilities(self, ctx:RulepadGrammarParser.VisibilitiesContext):
        pass


    # Enter a parse tree produced by RulepadGrammarParser#visibilityCondition.
    def enterVisibilityCondition(self, ctx:RulepadGrammarParser.VisibilityConditionContext):
        pass

    # Exit a parse tree produced by RulepadGrammarParser#visibilityCondition.
    def exitVisibilityCondition(self, ctx:RulepadGrammarParser.VisibilityConditionContext):
        pass


    # Enter a parse tree produced by RulepadGrammarParser#returnValues.
    def enterReturnValues(self, ctx:RulepadGrammarParser.ReturnValuesContext):
        pass

    # Exit a parse tree produced by RulepadGrammarParser#returnValues.
    def exitReturnValues(self, ctx:RulepadGrammarParser.ReturnValuesContext):
        pass


    # Enter a parse tree produced by RulepadGrammarParser#returnValueCondition.
    def enterReturnValueCondition(self, ctx:RulepadGrammarParser.ReturnValueConditionContext):
        pass

    # Exit a parse tree produced by RulepadGrammarParser#returnValueCondition.
    def exitReturnValueCondition(self, ctx:RulepadGrammarParser.ReturnValueConditionContext):
        pass


    # Enter a parse tree produced by RulepadGrammarParser#declarationStatements.
    def enterDeclarationStatements(self, ctx:RulepadGrammarParser.DeclarationStatementsContext):
        pass
        

    # Exit a parse tree produced by RulepadGrammarParser#declarationStatements.
    def exitDeclarationStatements(self, ctx:RulepadGrammarParser.DeclarationStatementsContext):
        pass


    # Enter a parse tree produced by RulepadGrammarParser#declarationStatementOf.
    def enterDeclarationStatementOf(self, ctx:RulepadGrammarParser.DeclarationStatementOfContext):
        pass

    # Exit a parse tree produced by RulepadGrammarParser#declarationStatementOf.
    def exitDeclarationStatementOf(self, ctx:RulepadGrammarParser.DeclarationStatementOfContext):
        pass


    # Enter a parse tree produced by RulepadGrammarParser#declarationStatementCondition.
    def enterDeclarationStatementCondition(self, ctx:RulepadGrammarParser.DeclarationStatementConditionContext):
        pass

    # Exit a parse tree produced by RulepadGrammarParser#declarationStatementCondition.
    def exitDeclarationStatementCondition(self, ctx:RulepadGrammarParser.DeclarationStatementConditionContext):
        pass


    # Enter a parse tree produced by RulepadGrammarParser#declarationStatementExpression.
    def enterDeclarationStatementExpression(self, ctx:RulepadGrammarParser.DeclarationStatementExpressionContext):
        pass

    # Exit a parse tree produced by RulepadGrammarParser#declarationStatementExpression.
    def exitDeclarationStatementExpression(self, ctx:RulepadGrammarParser.DeclarationStatementExpressionContext):
        pass


    # Enter a parse tree produced by RulepadGrammarParser#expressionStatements.
    def enterExpressionStatements(self, ctx:RulepadGrammarParser.ExpressionStatementsContext):
        pass

    # Exit a parse tree produced by RulepadGrammarParser#expressionStatements.
    def exitExpressionStatements(self, ctx:RulepadGrammarParser.ExpressionStatementsContext):
        pass


    # Enter a parse tree produced by RulepadGrammarParser#expressionStatementOf.
    def enterExpressionStatementOf(self, ctx:RulepadGrammarParser.ExpressionStatementOfContext):
        pass

    # Exit a parse tree produced by RulepadGrammarParser#expressionStatementOf.
    def exitExpressionStatementOf(self, ctx:RulepadGrammarParser.ExpressionStatementOfContext):
        pass


    # Enter a parse tree produced by RulepadGrammarParser#expressionStatementCondition.
    def enterExpressionStatementCondition(self, ctx:RulepadGrammarParser.ExpressionStatementConditionContext):
        pass

    # Exit a parse tree produced by RulepadGrammarParser#expressionStatementCondition.
    def exitExpressionStatementCondition(self, ctx:RulepadGrammarParser.ExpressionStatementConditionContext):
        pass


    # Enter a parse tree produced by RulepadGrammarParser#expressionStatementExpression.
    def enterExpressionStatementExpression(self, ctx:RulepadGrammarParser.ExpressionStatementExpressionContext):
        pass

    # Exit a parse tree produced by RulepadGrammarParser#expressionStatementExpression.
    def exitExpressionStatementExpression(self, ctx:RulepadGrammarParser.ExpressionStatementExpressionContext):
        pass


    # Enter a parse tree produced by RulepadGrammarParser#value.
    def enterValue(self, ctx:RulepadGrammarParser.ValueContext):
        pass

    # Exit a parse tree produced by RulepadGrammarParser#value.
    def exitValue(self, ctx:RulepadGrammarParser.ValueContext):
        pass


    # Enter a parse tree produced by RulepadGrammarParser#valueCondition.
    def enterValueCondition(self, ctx:RulepadGrammarParser.ValueConditionContext):
        pass

    # Exit a parse tree produced by RulepadGrammarParser#valueCondition.
    def exitValueCondition(self, ctx:RulepadGrammarParser.ValueConditionContext):
        pass


    # Enter a parse tree produced by RulepadGrammarParser#initialValues.
    def enterInitialValues(self, ctx:RulepadGrammarParser.InitialValuesContext):
        pass

    # Exit a parse tree produced by RulepadGrammarParser#initialValues.
    def exitInitialValues(self, ctx:RulepadGrammarParser.InitialValuesContext):
        pass


    # Enter a parse tree produced by RulepadGrammarParser#initialValueOf.
    def enterInitialValueOf(self, ctx:RulepadGrammarParser.InitialValueOfContext):
        pass

    # Exit a parse tree produced by RulepadGrammarParser#initialValueOf.
    def exitInitialValueOf(self, ctx:RulepadGrammarParser.InitialValueOfContext):
        pass


    # Enter a parse tree produced by RulepadGrammarParser#initialValueCondition.
    def enterInitialValueCondition(self, ctx:RulepadGrammarParser.InitialValueConditionContext):
        pass

    # Exit a parse tree produced by RulepadGrammarParser#initialValueCondition.
    def exitInitialValueCondition(self, ctx:RulepadGrammarParser.InitialValueConditionContext):
        pass


    # Enter a parse tree produced by RulepadGrammarParser#classes.
    def enterClasses(self, ctx:RulepadGrammarParser.ClassesContext):
        pass

    # Exit a parse tree produced by RulepadGrammarParser#classes.
    def exitClasses(self, ctx:RulepadGrammarParser.ClassesContext):
        pass


    # Enter a parse tree produced by RulepadGrammarParser#classCondition.
    def enterClassCondition(self, ctx:RulepadGrammarParser.ClassConditionContext):
        pass

    # Exit a parse tree produced by RulepadGrammarParser#classCondition.
    def exitClassCondition(self, ctx:RulepadGrammarParser.ClassConditionContext):
        pass


    # Enter a parse tree produced by RulepadGrammarParser#classExpression.
    def enterClassExpression(self, ctx:RulepadGrammarParser.ClassExpressionContext):
        pass

    # Exit a parse tree produced by RulepadGrammarParser#classExpression.
    def exitClassExpression(self, ctx:RulepadGrammarParser.ClassExpressionContext):
        pass


    # Enter a parse tree produced by RulepadGrammarParser#subclasses.
    def enterSubclasses(self, ctx:RulepadGrammarParser.SubclassesContext):
        pass

    # Exit a parse tree produced by RulepadGrammarParser#subclasses.
    def exitSubclasses(self, ctx:RulepadGrammarParser.SubclassesContext):
        pass


    # Enter a parse tree produced by RulepadGrammarParser#subclassOf.
    def enterSubclassOf(self, ctx:RulepadGrammarParser.SubclassOfContext):
        pass

    # Exit a parse tree produced by RulepadGrammarParser#subclassOf.
    def exitSubclassOf(self, ctx:RulepadGrammarParser.SubclassOfContext):
        pass


    # Enter a parse tree produced by RulepadGrammarParser#subclassCondition.
    def enterSubclassCondition(self, ctx:RulepadGrammarParser.SubclassConditionContext):
        pass

    # Exit a parse tree produced by RulepadGrammarParser#subclassCondition.
    def exitSubclassCondition(self, ctx:RulepadGrammarParser.SubclassConditionContext):
        pass


    # Enter a parse tree produced by RulepadGrammarParser#subclassExpression.
    def enterSubclassExpression(self, ctx:RulepadGrammarParser.SubclassExpressionContext):
        pass

    # Exit a parse tree produced by RulepadGrammarParser#subclassExpression.
    def exitSubclassExpression(self, ctx:RulepadGrammarParser.SubclassExpressionContext):
        pass



del RulepadGrammarParser
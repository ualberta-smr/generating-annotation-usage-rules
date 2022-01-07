package ca.ualberta.smr.grammar;

import ca.ualberta.grammar.RulepadGrammarListener;
import ca.ualberta.grammar.RulepadGrammarParser;
import org.antlr.v4.runtime.ParserRuleContext;
import org.antlr.v4.runtime.tree.ErrorNode;
import org.antlr.v4.runtime.tree.ParseTree;
import org.antlr.v4.runtime.tree.TerminalNode;

public class AbstractRulePadGrammarListener implements RulepadGrammarListener {
    @Override
    public void enterInputSentence(RulepadGrammarParser.InputSentenceContext ctx) {

    }

    @Override
    public void exitInputSentence(RulepadGrammarParser.InputSentenceContext ctx) {

    }

    @Override
    public void enterMustClause(RulepadGrammarParser.MustClauseContext ctx) {

    }

    @Override
    public void exitMustClause(RulepadGrammarParser.MustClauseContext ctx) {

    }

    @Override
    public void enterWords(RulepadGrammarParser.WordsContext ctx) {

    }

    @Override
    public void exitWords(RulepadGrammarParser.WordsContext ctx) {

    }

    @Override
    public void enterWord(RulepadGrammarParser.WordContext ctx) {

    }

    @Override
    public void exitWord(RulepadGrammarParser.WordContext ctx) {

    }

    @Override
    public void enterCombinatorialWords(RulepadGrammarParser.CombinatorialWordsContext ctx) {

    }

    @Override
    public void exitCombinatorialWords(RulepadGrammarParser.CombinatorialWordsContext ctx) {

    }

    @Override
    public void enterSymbols(RulepadGrammarParser.SymbolsContext ctx) {

    }

    @Override
    public void exitSymbols(RulepadGrammarParser.SymbolsContext ctx) {

    }

    @Override
    public void enterEnd(RulepadGrammarParser.EndContext ctx) {

    }

    @Override
    public void exitEnd(RulepadGrammarParser.EndContext ctx) {

    }

    @Override
    public void enterEmptyLine(RulepadGrammarParser.EmptyLineContext ctx) {

    }

    @Override
    public void exitEmptyLine(RulepadGrammarParser.EmptyLineContext ctx) {

    }

    @Override
    public void enterComments(RulepadGrammarParser.CommentsContext ctx) {

    }

    @Override
    public void exitComments(RulepadGrammarParser.CommentsContext ctx) {

    }

    @Override
    public void enterMust(RulepadGrammarParser.MustContext ctx) {

    }

    @Override
    public void exitMust(RulepadGrammarParser.MustContext ctx) {

    }

    @Override
    public void enterOf(RulepadGrammarParser.OfContext ctx) {

    }

    @Override
    public void exitOf(RulepadGrammarParser.OfContext ctx) {

    }

    @Override
    public void enterAnd_(RulepadGrammarParser.And_Context ctx) {

    }

    @Override
    public void exitAnd_(RulepadGrammarParser.And_Context ctx) {

    }

    @Override
    public void enterOr_(RulepadGrammarParser.Or_Context ctx) {

    }

    @Override
    public void exitOr_(RulepadGrammarParser.Or_Context ctx) {

    }

    @Override
    public void enterHave(RulepadGrammarParser.HaveContext ctx) {

    }

    @Override
    public void exitHave(RulepadGrammarParser.HaveContext ctx) {

    }

    @Override
    public void enterWithWord(RulepadGrammarParser.WithWordContext ctx) {

    }

    @Override
    public void exitWithWord(RulepadGrammarParser.WithWordContext ctx) {

    }

    @Override
    public void enterBinary(RulepadGrammarParser.BinaryContext ctx) {

    }

    @Override
    public void exitBinary(RulepadGrammarParser.BinaryContext ctx) {

    }

    @Override
    public void enterNames(RulepadGrammarParser.NamesContext ctx) {

    }

    @Override
    public void exitNames(RulepadGrammarParser.NamesContext ctx) {

    }

    @Override
    public void enterNameCondition(RulepadGrammarParser.NameConditionContext ctx) {

    }

    @Override
    public void exitNameCondition(RulepadGrammarParser.NameConditionContext ctx) {

    }

    @Override
    public void enterAnnotations(RulepadGrammarParser.AnnotationsContext ctx) {

    }

    @Override
    public void exitAnnotations(RulepadGrammarParser.AnnotationsContext ctx) {

    }

    @Override
    public void enterAnnotationCondition(RulepadGrammarParser.AnnotationConditionContext ctx) {

    }

    @Override
    public void exitAnnotationCondition(RulepadGrammarParser.AnnotationConditionContext ctx) {

    }

    @Override
    public void enterAnnotationConditionTransition(RulepadGrammarParser.AnnotationConditionTransitionContext ctx) {

    }

    @Override
    public void exitAnnotationConditionTransition(RulepadGrammarParser.AnnotationConditionTransitionContext ctx) {

    }

    @Override
    public void enterAnnotationExpression(RulepadGrammarParser.AnnotationExpressionContext ctx) {

    }

    @Override
    public void exitAnnotationExpression(RulepadGrammarParser.AnnotationExpressionContext ctx) {

    }

    @Override
    public void enterExtensions(RulepadGrammarParser.ExtensionsContext ctx) {

    }

    @Override
    public void exitExtensions(RulepadGrammarParser.ExtensionsContext ctx) {

    }

    @Override
    public void enterExtensionCondition(RulepadGrammarParser.ExtensionConditionContext ctx) {

    }

    @Override
    public void exitExtensionCondition(RulepadGrammarParser.ExtensionConditionContext ctx) {

    }

    @Override
    public void enterImplementations(RulepadGrammarParser.ImplementationsContext ctx) {

    }

    @Override
    public void exitImplementations(RulepadGrammarParser.ImplementationsContext ctx) {

    }

    @Override
    public void enterImplementationCondition(RulepadGrammarParser.ImplementationConditionContext ctx) {

    }

    @Override
    public void exitImplementationCondition(RulepadGrammarParser.ImplementationConditionContext ctx) {

    }

    @Override
    public void enterFunctions(RulepadGrammarParser.FunctionsContext ctx) {

    }

    @Override
    public void exitFunctions(RulepadGrammarParser.FunctionsContext ctx) {

    }

    @Override
    public void enterFunctionOf(RulepadGrammarParser.FunctionOfContext ctx) {

    }

    @Override
    public void exitFunctionOf(RulepadGrammarParser.FunctionOfContext ctx) {

    }

    @Override
    public void enterFunctionCondition(RulepadGrammarParser.FunctionConditionContext ctx) {

    }

    @Override
    public void exitFunctionCondition(RulepadGrammarParser.FunctionConditionContext ctx) {

    }

    @Override
    public void enterFunctionExpression(RulepadGrammarParser.FunctionExpressionContext ctx) {

    }

    @Override
    public void exitFunctionExpression(RulepadGrammarParser.FunctionExpressionContext ctx) {

    }

    @Override
    public void enterAbstractFunctions(RulepadGrammarParser.AbstractFunctionsContext ctx) {

    }

    @Override
    public void exitAbstractFunctions(RulepadGrammarParser.AbstractFunctionsContext ctx) {

    }

    @Override
    public void enterAbstractFunctionOf(RulepadGrammarParser.AbstractFunctionOfContext ctx) {

    }

    @Override
    public void exitAbstractFunctionOf(RulepadGrammarParser.AbstractFunctionOfContext ctx) {

    }

    @Override
    public void enterAbstractFunctionCondition(RulepadGrammarParser.AbstractFunctionConditionContext ctx) {

    }

    @Override
    public void exitAbstractFunctionCondition(RulepadGrammarParser.AbstractFunctionConditionContext ctx) {

    }

    @Override
    public void enterAbstractFunctionExpression(RulepadGrammarParser.AbstractFunctionExpressionContext ctx) {

    }

    @Override
    public void exitAbstractFunctionExpression(RulepadGrammarParser.AbstractFunctionExpressionContext ctx) {

    }

    @Override
    public void enterConstructors(RulepadGrammarParser.ConstructorsContext ctx) {

    }

    @Override
    public void exitConstructors(RulepadGrammarParser.ConstructorsContext ctx) {

    }

    @Override
    public void enterConstructorOf(RulepadGrammarParser.ConstructorOfContext ctx) {

    }

    @Override
    public void exitConstructorOf(RulepadGrammarParser.ConstructorOfContext ctx) {

    }

    @Override
    public void enterConstructorCondition(RulepadGrammarParser.ConstructorConditionContext ctx) {

    }

    @Override
    public void exitConstructorCondition(RulepadGrammarParser.ConstructorConditionContext ctx) {

    }

    @Override
    public void enterConstructorExpression(RulepadGrammarParser.ConstructorExpressionContext ctx) {

    }

    @Override
    public void exitConstructorExpression(RulepadGrammarParser.ConstructorExpressionContext ctx) {

    }

    @Override
    public void enterParameters(RulepadGrammarParser.ParametersContext ctx) {

    }

    @Override
    public void exitParameters(RulepadGrammarParser.ParametersContext ctx) {

    }

    @Override
    public void enterParameterCondition(RulepadGrammarParser.ParameterConditionContext ctx) {

    }

    @Override
    public void exitParameterCondition(RulepadGrammarParser.ParameterConditionContext ctx) {

    }

    @Override
    public void enterParameterExpression(RulepadGrammarParser.ParameterExpressionContext ctx) {

    }

    @Override
    public void exitParameterExpression(RulepadGrammarParser.ParameterExpressionContext ctx) {

    }

    @Override
    public void enterFunctionParameters(RulepadGrammarParser.FunctionParametersContext ctx) {

    }

    @Override
    public void exitFunctionParameters(RulepadGrammarParser.FunctionParametersContext ctx) {

    }

    @Override
    public void enterFunctionParameterCondition(RulepadGrammarParser.FunctionParameterConditionContext ctx) {

    }

    @Override
    public void exitFunctionParameterCondition(RulepadGrammarParser.FunctionParameterConditionContext ctx) {

    }

    @Override
    public void enterFunctionParameterConditionTransition(RulepadGrammarParser.FunctionParameterConditionTransitionContext ctx) {

    }

    @Override
    public void exitFunctionParameterConditionTransition(RulepadGrammarParser.FunctionParameterConditionTransitionContext ctx) {

    }

    @Override
    public void enterFunctionParameterExpression(RulepadGrammarParser.FunctionParameterExpressionContext ctx) {

    }

    @Override
    public void exitFunctionParameterExpression(RulepadGrammarParser.FunctionParameterExpressionContext ctx) {

    }

    @Override
    public void enterTypes(RulepadGrammarParser.TypesContext ctx) {

    }

    @Override
    public void exitTypes(RulepadGrammarParser.TypesContext ctx) {

    }

    @Override
    public void enterTypeCondition(RulepadGrammarParser.TypeConditionContext ctx) {

    }

    @Override
    public void exitTypeCondition(RulepadGrammarParser.TypeConditionContext ctx) {

    }

    @Override
    public void enterSpecifiers(RulepadGrammarParser.SpecifiersContext ctx) {

    }

    @Override
    public void exitSpecifiers(RulepadGrammarParser.SpecifiersContext ctx) {

    }

    @Override
    public void enterSpecifierCondition(RulepadGrammarParser.SpecifierConditionContext ctx) {

    }

    @Override
    public void exitSpecifierCondition(RulepadGrammarParser.SpecifierConditionContext ctx) {

    }

    @Override
    public void enterVisibilities(RulepadGrammarParser.VisibilitiesContext ctx) {

    }

    @Override
    public void exitVisibilities(RulepadGrammarParser.VisibilitiesContext ctx) {

    }

    @Override
    public void enterVisibilityCondition(RulepadGrammarParser.VisibilityConditionContext ctx) {

    }

    @Override
    public void exitVisibilityCondition(RulepadGrammarParser.VisibilityConditionContext ctx) {

    }

    @Override
    public void enterReturnValues(RulepadGrammarParser.ReturnValuesContext ctx) {

    }

    @Override
    public void exitReturnValues(RulepadGrammarParser.ReturnValuesContext ctx) {

    }

    @Override
    public void enterReturnValueCondition(RulepadGrammarParser.ReturnValueConditionContext ctx) {

    }

    @Override
    public void exitReturnValueCondition(RulepadGrammarParser.ReturnValueConditionContext ctx) {

    }

    @Override
    public void enterDeclarationStatements(RulepadGrammarParser.DeclarationStatementsContext ctx) {

    }

    @Override
    public void exitDeclarationStatements(RulepadGrammarParser.DeclarationStatementsContext ctx) {

    }

    @Override
    public void enterDeclarationStatementOf(RulepadGrammarParser.DeclarationStatementOfContext ctx) {

    }

    @Override
    public void exitDeclarationStatementOf(RulepadGrammarParser.DeclarationStatementOfContext ctx) {

    }

    @Override
    public void enterDeclarationStatementCondition(RulepadGrammarParser.DeclarationStatementConditionContext ctx) {

    }

    @Override
    public void exitDeclarationStatementCondition(RulepadGrammarParser.DeclarationStatementConditionContext ctx) {

    }

    @Override
    public void enterDeclarationStatementExpression(RulepadGrammarParser.DeclarationStatementExpressionContext ctx) {

    }

    @Override
    public void exitDeclarationStatementExpression(RulepadGrammarParser.DeclarationStatementExpressionContext ctx) {

    }

    @Override
    public void enterConfigurationFiles(RulepadGrammarParser.ConfigurationFilesContext ctx) {

    }

    @Override
    public void exitConfigurationFiles(RulepadGrammarParser.ConfigurationFilesContext ctx) {

    }

    @Override
    public void enterConfigurationFileCondition(RulepadGrammarParser.ConfigurationFileConditionContext ctx) {

    }

    @Override
    public void exitConfigurationFileCondition(RulepadGrammarParser.ConfigurationFileConditionContext ctx) {

    }

    @Override
    public void enterConfigurationFileExpression(RulepadGrammarParser.ConfigurationFileExpressionContext ctx) {

    }

    @Override
    public void exitConfigurationFileExpression(RulepadGrammarParser.ConfigurationFileExpressionContext ctx) {

    }

    @Override
    public void enterConfigurationProperties(RulepadGrammarParser.ConfigurationPropertiesContext ctx) {

    }

    @Override
    public void exitConfigurationProperties(RulepadGrammarParser.ConfigurationPropertiesContext ctx) {

    }

    @Override
    public void enterConfigurationPropertyCondition(RulepadGrammarParser.ConfigurationPropertyConditionContext ctx) {

    }

    @Override
    public void exitConfigurationPropertyCondition(RulepadGrammarParser.ConfigurationPropertyConditionContext ctx) {

    }

    @Override
    public void enterConfigurationPropertyExpression(RulepadGrammarParser.ConfigurationPropertyExpressionContext ctx) {

    }

    @Override
    public void exitConfigurationPropertyExpression(RulepadGrammarParser.ConfigurationPropertyExpressionContext ctx) {

    }

    @Override
    public void enterExpressionStatements(RulepadGrammarParser.ExpressionStatementsContext ctx) {

    }

    @Override
    public void exitExpressionStatements(RulepadGrammarParser.ExpressionStatementsContext ctx) {

    }

    @Override
    public void enterExpressionStatementOf(RulepadGrammarParser.ExpressionStatementOfContext ctx) {

    }

    @Override
    public void exitExpressionStatementOf(RulepadGrammarParser.ExpressionStatementOfContext ctx) {

    }

    @Override
    public void enterExpressionStatementCondition(RulepadGrammarParser.ExpressionStatementConditionContext ctx) {

    }

    @Override
    public void exitExpressionStatementCondition(RulepadGrammarParser.ExpressionStatementConditionContext ctx) {

    }

    @Override
    public void enterExpressionStatementExpression(RulepadGrammarParser.ExpressionStatementExpressionContext ctx) {

    }

    @Override
    public void exitExpressionStatementExpression(RulepadGrammarParser.ExpressionStatementExpressionContext ctx) {

    }

    @Override
    public void enterValue(RulepadGrammarParser.ValueContext ctx) {

    }

    @Override
    public void exitValue(RulepadGrammarParser.ValueContext ctx) {

    }

    @Override
    public void enterValueCondition(RulepadGrammarParser.ValueConditionContext ctx) {

    }

    @Override
    public void exitValueCondition(RulepadGrammarParser.ValueConditionContext ctx) {

    }

    @Override
    public void enterInitialValues(RulepadGrammarParser.InitialValuesContext ctx) {

    }

    @Override
    public void exitInitialValues(RulepadGrammarParser.InitialValuesContext ctx) {

    }

    @Override
    public void enterInitialValueOf(RulepadGrammarParser.InitialValueOfContext ctx) {

    }

    @Override
    public void exitInitialValueOf(RulepadGrammarParser.InitialValueOfContext ctx) {

    }

    @Override
    public void enterInitialValueCondition(RulepadGrammarParser.InitialValueConditionContext ctx) {

    }

    @Override
    public void exitInitialValueCondition(RulepadGrammarParser.InitialValueConditionContext ctx) {

    }

    @Override
    public void enterClasses(RulepadGrammarParser.ClassesContext ctx) {

    }

    @Override
    public void exitClasses(RulepadGrammarParser.ClassesContext ctx) {

    }

    @Override
    public void enterClassCondition(RulepadGrammarParser.ClassConditionContext ctx) {

    }

    @Override
    public void exitClassCondition(RulepadGrammarParser.ClassConditionContext ctx) {

    }

    @Override
    public void enterClassExpression(RulepadGrammarParser.ClassExpressionContext ctx) {

    }

    @Override
    public void exitClassExpression(RulepadGrammarParser.ClassExpressionContext ctx) {

    }

    @Override
    public void enterSubclasses(RulepadGrammarParser.SubclassesContext ctx) {

    }

    @Override
    public void exitSubclasses(RulepadGrammarParser.SubclassesContext ctx) {

    }

    @Override
    public void enterSubclassOf(RulepadGrammarParser.SubclassOfContext ctx) {

    }

    @Override
    public void exitSubclassOf(RulepadGrammarParser.SubclassOfContext ctx) {

    }

    @Override
    public void enterSubclassCondition(RulepadGrammarParser.SubclassConditionContext ctx) {

    }

    @Override
    public void exitSubclassCondition(RulepadGrammarParser.SubclassConditionContext ctx) {

    }

    @Override
    public void enterSubclassExpression(RulepadGrammarParser.SubclassExpressionContext ctx) {

    }

    @Override
    public void exitSubclassExpression(RulepadGrammarParser.SubclassExpressionContext ctx) {

    }

    @Override
    public void visitTerminal(TerminalNode terminalNode) {

    }

    @Override
    public void visitErrorNode(ErrorNode errorNode) {

    }

    @Override
    public void enterEveryRule(ParserRuleContext parserRuleContext) {

    }

    @Override
    public void exitEveryRule(ParserRuleContext parserRuleContext) {

    }
}
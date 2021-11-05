package ca.ualberta.smr.visualize;

import ca.ualberta.grammar.RulepadGrammarListener;
import ca.ualberta.grammar.RulepadGrammarParser;
import org.antlr.v4.runtime.ParserRuleContext;
import org.antlr.v4.runtime.tree.ErrorNode;
import org.antlr.v4.runtime.tree.TerminalNode;

public class DummyListener implements RulepadGrammarListener {

    @Override
    public void enterInputSentence(RulepadGrammarParser.InputSentenceContext ctx) {
        System.out.println("enterInputSentence");
    }

    @Override
    public void exitInputSentence(RulepadGrammarParser.InputSentenceContext ctx) {
        System.out.println("exitInputSentence");
    }

    @Override
    public void enterMustClause(RulepadGrammarParser.MustClauseContext ctx) {
        System.out.println("enterMustClause");
    }

    @Override
    public void exitMustClause(RulepadGrammarParser.MustClauseContext ctx) {
        System.out.println("exitMustClause");
    }

    @Override
    public void enterWords(RulepadGrammarParser.WordsContext ctx) {
        System.out.println("enterWords");
    }

    @Override
    public void exitWords(RulepadGrammarParser.WordsContext ctx) {
        System.out.println("exitWords");
    }

    @Override
    public void enterWord(RulepadGrammarParser.WordContext ctx) {
        System.out.println("enterWord");
    }

    @Override
    public void exitWord(RulepadGrammarParser.WordContext ctx) {
        System.out.println("exitWord");
    }

    @Override
    public void enterCombinatorialWords(RulepadGrammarParser.CombinatorialWordsContext ctx) {
        System.out.println("enterCombinatorialWords");
    }

    @Override
    public void exitCombinatorialWords(RulepadGrammarParser.CombinatorialWordsContext ctx) {
        System.out.println("exitCombinatorialWords");
    }

    @Override
    public void enterSymbols(RulepadGrammarParser.SymbolsContext ctx) {
        System.out.println("enterSymbols");
    }

    @Override
    public void exitSymbols(RulepadGrammarParser.SymbolsContext ctx) {
        System.out.println("exitSymbols");
    }

    @Override
    public void enterEnd(RulepadGrammarParser.EndContext ctx) {
        System.out.println("enterEnd");
    }

    @Override
    public void exitEnd(RulepadGrammarParser.EndContext ctx) {
        System.out.println("exitEnd");
    }

    @Override
    public void enterEmptyLine(RulepadGrammarParser.EmptyLineContext ctx) {
        System.out.println("enterEmptyLine");
    }

    @Override
    public void exitEmptyLine(RulepadGrammarParser.EmptyLineContext ctx) {
        System.out.println("exitEmptyLine");
    }

    @Override
    public void enterComments(RulepadGrammarParser.CommentsContext ctx) {
        System.out.println("enterComments");
    }

    @Override
    public void exitComments(RulepadGrammarParser.CommentsContext ctx) {
        System.out.println("exitComments");
    }

    @Override
    public void enterMust(RulepadGrammarParser.MustContext ctx) {
        System.out.println("enterMust");
    }

    @Override
    public void exitMust(RulepadGrammarParser.MustContext ctx) {
        System.out.println("exitMust");
    }

    @Override
    public void enterOf(RulepadGrammarParser.OfContext ctx) {
        System.out.println("enterOf");
    }

    @Override
    public void exitOf(RulepadGrammarParser.OfContext ctx) {
        System.out.println("exitOf");
    }

    @Override
    public void enterAnd_(RulepadGrammarParser.And_Context ctx) {
        System.out.println("enterAnd_");
    }

    @Override
    public void exitAnd_(RulepadGrammarParser.And_Context ctx) {
        System.out.println("exitAnd_");
    }

    @Override
    public void enterOr_(RulepadGrammarParser.Or_Context ctx) {
        System.out.println("enterOr_");
    }

    @Override
    public void exitOr_(RulepadGrammarParser.Or_Context ctx) {
        System.out.println("exitOr_");
    }

    @Override
    public void enterHave(RulepadGrammarParser.HaveContext ctx) {
        System.out.println("enterHave");
    }

    @Override
    public void exitHave(RulepadGrammarParser.HaveContext ctx) {
        System.out.println("exitHave");
    }

    @Override
    public void enterWithWord(RulepadGrammarParser.WithWordContext ctx) {
        System.out.println("enterWithWord");
    }

    @Override
    public void exitWithWord(RulepadGrammarParser.WithWordContext ctx) {
        System.out.println("exitWithWord");
    }

    @Override
    public void enterBinary(RulepadGrammarParser.BinaryContext ctx) {
        System.out.println("enterBinary");
    }

    @Override
    public void exitBinary(RulepadGrammarParser.BinaryContext ctx) {
        System.out.println("exitBinary");
    }

    @Override
    public void enterNames(RulepadGrammarParser.NamesContext ctx) {
        System.out.println("enterNames");
    }

    @Override
    public void exitNames(RulepadGrammarParser.NamesContext ctx) {
        System.out.println("exitNames");
    }

    @Override
    public void enterNameCondition(RulepadGrammarParser.NameConditionContext ctx) {
        System.out.println("enterNameCondition");
    }

    @Override
    public void exitNameCondition(RulepadGrammarParser.NameConditionContext ctx) {
        System.out.println("exitNameCondition");
    }

    @Override
    public void enterAnnotations(RulepadGrammarParser.AnnotationsContext ctx) {
        System.out.println("enterAnnotations");
    }

    @Override
    public void exitAnnotations(RulepadGrammarParser.AnnotationsContext ctx) {
        System.out.println("exitAnnotations");
    }

    @Override
    public void enterAnnotationCondition(RulepadGrammarParser.AnnotationConditionContext ctx) {
        System.out.println("enterAnnotationCondition");
    }

    @Override
    public void exitAnnotationCondition(RulepadGrammarParser.AnnotationConditionContext ctx) {
        System.out.println("exitAnnotationCondition");
    }

    @Override
    public void enterAnnotationConditionTransition(RulepadGrammarParser.AnnotationConditionTransitionContext ctx) {
        System.out.println("enterAnnotationConditionTransition");
    }

    @Override
    public void exitAnnotationConditionTransition(RulepadGrammarParser.AnnotationConditionTransitionContext ctx) {
        System.out.println("exitAnnotationConditionTransition");
    }

    @Override
    public void enterAnnotationExpression(RulepadGrammarParser.AnnotationExpressionContext ctx) {
        System.out.println("enterAnnotationExpression");
    }

    @Override
    public void exitAnnotationExpression(RulepadGrammarParser.AnnotationExpressionContext ctx) {
        System.out.println("exitAnnotationExpression");
    }

    @Override
    public void enterExtensions(RulepadGrammarParser.ExtensionsContext ctx) {
        System.out.println("enterExtensions");
    }

    @Override
    public void exitExtensions(RulepadGrammarParser.ExtensionsContext ctx) {
        System.out.println("exitExtensions");
    }

    @Override
    public void enterExtensionCondition(RulepadGrammarParser.ExtensionConditionContext ctx) {
        System.out.println("enterExtensionCondition");
    }

    @Override
    public void exitExtensionCondition(RulepadGrammarParser.ExtensionConditionContext ctx) {
        System.out.println("exitExtensionCondition");
    }

    @Override
    public void enterImplementations(RulepadGrammarParser.ImplementationsContext ctx) {
        System.out.println("enterImplementations");
    }

    @Override
    public void exitImplementations(RulepadGrammarParser.ImplementationsContext ctx) {
        System.out.println("exitImplementations");
    }

    @Override
    public void enterImplementationCondition(RulepadGrammarParser.ImplementationConditionContext ctx) {
        System.out.println("enterImplementationCondition");
    }

    @Override
    public void exitImplementationCondition(RulepadGrammarParser.ImplementationConditionContext ctx) {
        System.out.println("exitImplementationCondition");
    }

    @Override
    public void enterFunctions(RulepadGrammarParser.FunctionsContext ctx) {
        System.out.println("enterFunctions");
    }

    @Override
    public void exitFunctions(RulepadGrammarParser.FunctionsContext ctx) {
        System.out.println("exitFunctions");
    }

    @Override
    public void enterFunctionOf(RulepadGrammarParser.FunctionOfContext ctx) {
        System.out.println("enterFunctionOf");
    }

    @Override
    public void exitFunctionOf(RulepadGrammarParser.FunctionOfContext ctx) {
        System.out.println("exitFunctionOf");
    }

    @Override
    public void enterFunctionCondition(RulepadGrammarParser.FunctionConditionContext ctx) {
        System.out.println("enterFunctionCondition");
    }

    @Override
    public void exitFunctionCondition(RulepadGrammarParser.FunctionConditionContext ctx) {
        System.out.println("exitFunctionCondition");
    }

    @Override
    public void enterFunctionExpression(RulepadGrammarParser.FunctionExpressionContext ctx) {
        System.out.println("enterFunctionExpression");
    }

    @Override
    public void exitFunctionExpression(RulepadGrammarParser.FunctionExpressionContext ctx) {
        System.out.println("exitFunctionExpression");
    }

    @Override
    public void enterAbstractFunctions(RulepadGrammarParser.AbstractFunctionsContext ctx) {
        System.out.println("enterAbstractFunctions");
    }

    @Override
    public void exitAbstractFunctions(RulepadGrammarParser.AbstractFunctionsContext ctx) {
        System.out.println("exitAbstractFunctions");
    }

    @Override
    public void enterAbstractFunctionOf(RulepadGrammarParser.AbstractFunctionOfContext ctx) {
        System.out.println("enterAbstractFunctionOf");
    }

    @Override
    public void exitAbstractFunctionOf(RulepadGrammarParser.AbstractFunctionOfContext ctx) {
        System.out.println("exitAbstractFunctionOf");
    }

    @Override
    public void enterAbstractFunctionCondition(RulepadGrammarParser.AbstractFunctionConditionContext ctx) {
        System.out.println("enterAbstractFunctionCondition");
    }

    @Override
    public void exitAbstractFunctionCondition(RulepadGrammarParser.AbstractFunctionConditionContext ctx) {
        System.out.println("exitAbstractFunctionCondition");
    }

    @Override
    public void enterAbstractFunctionExpression(RulepadGrammarParser.AbstractFunctionExpressionContext ctx) {
        System.out.println("enterAbstractFunctionExpression");
    }

    @Override
    public void exitAbstractFunctionExpression(RulepadGrammarParser.AbstractFunctionExpressionContext ctx) {
        System.out.println("exitAbstractFunctionExpression");
    }

    @Override
    public void enterConstructors(RulepadGrammarParser.ConstructorsContext ctx) {
        System.out.println("enterConstructors");
    }

    @Override
    public void exitConstructors(RulepadGrammarParser.ConstructorsContext ctx) {
        System.out.println("exitConstructors");
    }

    @Override
    public void enterConstructorOf(RulepadGrammarParser.ConstructorOfContext ctx) {
        System.out.println("enterConstructorOf");
    }

    @Override
    public void exitConstructorOf(RulepadGrammarParser.ConstructorOfContext ctx) {
        System.out.println("exitConstructorOf");
    }

    @Override
    public void enterConstructorCondition(RulepadGrammarParser.ConstructorConditionContext ctx) {
        System.out.println("enterConstructorCondition");
    }

    @Override
    public void exitConstructorCondition(RulepadGrammarParser.ConstructorConditionContext ctx) {
        System.out.println("exitConstructorCondition");
    }

    @Override
    public void enterConstructorExpression(RulepadGrammarParser.ConstructorExpressionContext ctx) {
        System.out.println("enterConstructorExpression");
    }

    @Override
    public void exitConstructorExpression(RulepadGrammarParser.ConstructorExpressionContext ctx) {
        System.out.println("exitConstructorExpression");
    }

    @Override
    public void enterParameters(RulepadGrammarParser.ParametersContext ctx) {
        System.out.println("enterParameters");
    }

    @Override
    public void exitParameters(RulepadGrammarParser.ParametersContext ctx) {
        System.out.println("exitParameters");
    }

    @Override
    public void enterParameterCondition(RulepadGrammarParser.ParameterConditionContext ctx) {
        System.out.println("enterParameterCondition");
    }

    @Override
    public void exitParameterCondition(RulepadGrammarParser.ParameterConditionContext ctx) {
        System.out.println("exitParameterCondition");
    }

    @Override
    public void enterParameterExpression(RulepadGrammarParser.ParameterExpressionContext ctx) {
        System.out.println("enterParameterExpression");
    }

    @Override
    public void exitParameterExpression(RulepadGrammarParser.ParameterExpressionContext ctx) {
        System.out.println("exitParameterExpression");
    }

    @Override
    public void enterFunctionParameters(RulepadGrammarParser.FunctionParametersContext ctx) {
        System.out.println("enterFunctionParameters");
    }

    @Override
    public void exitFunctionParameters(RulepadGrammarParser.FunctionParametersContext ctx) {
        System.out.println("exitFunctionParameters");
    }

    @Override
    public void enterFunctionParameterCondition(RulepadGrammarParser.FunctionParameterConditionContext ctx) {
        System.out.println("enterFunctionParameterCondition");
    }

    @Override
    public void exitFunctionParameterCondition(RulepadGrammarParser.FunctionParameterConditionContext ctx) {
        System.out.println("exitFunctionParameterCondition");
    }

    @Override
    public void enterFunctionParameterConditionTransition(RulepadGrammarParser.FunctionParameterConditionTransitionContext ctx) {
        System.out.println("enterFunctionParameterConditionTransition");
    }

    @Override
    public void exitFunctionParameterConditionTransition(RulepadGrammarParser.FunctionParameterConditionTransitionContext ctx) {
        System.out.println("exitFunctionParameterConditionTransition");
    }

    @Override
    public void enterFunctionParameterExpression(RulepadGrammarParser.FunctionParameterExpressionContext ctx) {
        System.out.println("enterFunctionParameterExpression");
    }

    @Override
    public void exitFunctionParameterExpression(RulepadGrammarParser.FunctionParameterExpressionContext ctx) {
        System.out.println("exitFunctionParameterExpression");
    }

    @Override
    public void enterTypes(RulepadGrammarParser.TypesContext ctx) {
        System.out.println("enterTypes");
    }

    @Override
    public void exitTypes(RulepadGrammarParser.TypesContext ctx) {
        System.out.println("exitTypes");
    }

    @Override
    public void enterTypeCondition(RulepadGrammarParser.TypeConditionContext ctx) {
        System.out.println("enterTypeCondition");
    }

    @Override
    public void exitTypeCondition(RulepadGrammarParser.TypeConditionContext ctx) {
        System.out.println("exitTypeCondition");
    }

    @Override
    public void enterSpecifiers(RulepadGrammarParser.SpecifiersContext ctx) {
        System.out.println("enterSpecifiers");
    }

    @Override
    public void exitSpecifiers(RulepadGrammarParser.SpecifiersContext ctx) {
        System.out.println("exitSpecifiers");
    }

    @Override
    public void enterSpecifierCondition(RulepadGrammarParser.SpecifierConditionContext ctx) {
        System.out.println("enterSpecifierCondition");
    }

    @Override
    public void exitSpecifierCondition(RulepadGrammarParser.SpecifierConditionContext ctx) {
        System.out.println("exitSpecifierCondition");
    }

    @Override
    public void enterVisibilities(RulepadGrammarParser.VisibilitiesContext ctx) {
        System.out.println("enterVisibilities");
    }

    @Override
    public void exitVisibilities(RulepadGrammarParser.VisibilitiesContext ctx) {
        System.out.println("exitVisibilities");
    }

    @Override
    public void enterVisibilityCondition(RulepadGrammarParser.VisibilityConditionContext ctx) {
        System.out.println("enterVisibilityCondition");
    }

    @Override
    public void exitVisibilityCondition(RulepadGrammarParser.VisibilityConditionContext ctx) {
        System.out.println("exitVisibilityCondition");
    }

    @Override
    public void enterReturnValues(RulepadGrammarParser.ReturnValuesContext ctx) {
        System.out.println("enterReturnValues");
    }

    @Override
    public void exitReturnValues(RulepadGrammarParser.ReturnValuesContext ctx) {
        System.out.println("exitReturnValues");
    }

    @Override
    public void enterReturnValueCondition(RulepadGrammarParser.ReturnValueConditionContext ctx) {
        System.out.println("enterReturnValueCondition");
    }

    @Override
    public void exitReturnValueCondition(RulepadGrammarParser.ReturnValueConditionContext ctx) {
        System.out.println("exitReturnValueCondition");
    }

    @Override
    public void enterDeclarationStatements(RulepadGrammarParser.DeclarationStatementsContext ctx) {
        System.out.println("enterDeclarationStatements");
    }

    @Override
    public void exitDeclarationStatements(RulepadGrammarParser.DeclarationStatementsContext ctx) {
        System.out.println("exitDeclarationStatements");
    }

    @Override
    public void enterDeclarationStatementOf(RulepadGrammarParser.DeclarationStatementOfContext ctx) {
        System.out.println("enterDeclarationStatementOf");
    }

    @Override
    public void exitDeclarationStatementOf(RulepadGrammarParser.DeclarationStatementOfContext ctx) {
        System.out.println("exitDeclarationStatementOf");
    }

    @Override
    public void enterDeclarationStatementCondition(RulepadGrammarParser.DeclarationStatementConditionContext ctx) {
        System.out.println("enterDeclarationStatementCondition");
    }

    @Override
    public void exitDeclarationStatementCondition(RulepadGrammarParser.DeclarationStatementConditionContext ctx) {
        System.out.println("exitDeclarationStatementCondition");
    }

    @Override
    public void enterDeclarationStatementExpression(RulepadGrammarParser.DeclarationStatementExpressionContext ctx) {
        System.out.println("enterDeclarationStatementExpression");
    }

    @Override
    public void exitDeclarationStatementExpression(RulepadGrammarParser.DeclarationStatementExpressionContext ctx) {
        System.out.println("exitDeclarationStatementExpression");
    }

    @Override
    public void enterConfigurationFiles(RulepadGrammarParser.ConfigurationFilesContext ctx) {
        System.out.println("enterConfigurationFiles");
    }

    @Override
    public void exitConfigurationFiles(RulepadGrammarParser.ConfigurationFilesContext ctx) {
        System.out.println("exitConfigurationFiles");
    }

    @Override
    public void enterConfigurationFileCondition(RulepadGrammarParser.ConfigurationFileConditionContext ctx) {
        System.out.println("enterConfigurationFileCondition");
    }

    @Override
    public void exitConfigurationFileCondition(RulepadGrammarParser.ConfigurationFileConditionContext ctx) {
        System.out.println("exitConfigurationFileCondition");
    }

    @Override
    public void enterConfigurationFileExpression(RulepadGrammarParser.ConfigurationFileExpressionContext ctx) {
        System.out.println("enterConfigurationFileExpression");
    }

    @Override
    public void exitConfigurationFileExpression(RulepadGrammarParser.ConfigurationFileExpressionContext ctx) {
        System.out.println("exitConfigurationFileExpression");
    }

    @Override
    public void enterConfigurationProperties(RulepadGrammarParser.ConfigurationPropertiesContext ctx) {
        System.out.println("enterConfigurationProperties");
    }

    @Override
    public void exitConfigurationProperties(RulepadGrammarParser.ConfigurationPropertiesContext ctx) {
        System.out.println("exitConfigurationProperties");
    }

    @Override
    public void enterConfigurationPropertyCondition(RulepadGrammarParser.ConfigurationPropertyConditionContext ctx) {
        System.out.println("enterConfigurationPropertyCondition");
    }

    @Override
    public void exitConfigurationPropertyCondition(RulepadGrammarParser.ConfigurationPropertyConditionContext ctx) {
        System.out.println("exitConfigurationPropertyCondition");
    }

    @Override
    public void enterConfigurationPropertyExpression(RulepadGrammarParser.ConfigurationPropertyExpressionContext ctx) {
        System.out.println("enterConfigurationPropertyExpression");
    }

    @Override
    public void exitConfigurationPropertyExpression(RulepadGrammarParser.ConfigurationPropertyExpressionContext ctx) {
        System.out.println("exitConfigurationPropertyExpression");
    }

    @Override
    public void enterExpressionStatements(RulepadGrammarParser.ExpressionStatementsContext ctx) {
        System.out.println("enterExpressionStatements");
    }

    @Override
    public void exitExpressionStatements(RulepadGrammarParser.ExpressionStatementsContext ctx) {
        System.out.println("exitExpressionStatements");
    }

    @Override
    public void enterExpressionStatementOf(RulepadGrammarParser.ExpressionStatementOfContext ctx) {
        System.out.println("enterExpressionStatementOf");
    }

    @Override
    public void exitExpressionStatementOf(RulepadGrammarParser.ExpressionStatementOfContext ctx) {
        System.out.println("exitExpressionStatementOf");
    }

    @Override
    public void enterExpressionStatementCondition(RulepadGrammarParser.ExpressionStatementConditionContext ctx) {
        System.out.println("enterExpressionStatementCondition");
    }

    @Override
    public void exitExpressionStatementCondition(RulepadGrammarParser.ExpressionStatementConditionContext ctx) {
        System.out.println("exitExpressionStatementCondition");
    }

    @Override
    public void enterExpressionStatementExpression(RulepadGrammarParser.ExpressionStatementExpressionContext ctx) {
        System.out.println("enterExpressionStatementExpression");
    }

    @Override
    public void exitExpressionStatementExpression(RulepadGrammarParser.ExpressionStatementExpressionContext ctx) {
        System.out.println("exitExpressionStatementExpression");
    }

    @Override
    public void enterValue(RulepadGrammarParser.ValueContext ctx) {
        System.out.println("enterValue");
    }

    @Override
    public void exitValue(RulepadGrammarParser.ValueContext ctx) {
        System.out.println("exitValue");
    }

    @Override
    public void enterValueCondition(RulepadGrammarParser.ValueConditionContext ctx) {
        System.out.println("enterValueCondition");
    }

    @Override
    public void exitValueCondition(RulepadGrammarParser.ValueConditionContext ctx) {
        System.out.println("exitValueCondition");
    }

    @Override
    public void enterInitialValues(RulepadGrammarParser.InitialValuesContext ctx) {
        System.out.println("enterInitialValues");
    }

    @Override
    public void exitInitialValues(RulepadGrammarParser.InitialValuesContext ctx) {
        System.out.println("exitInitialValues");
    }

    @Override
    public void enterInitialValueOf(RulepadGrammarParser.InitialValueOfContext ctx) {
        System.out.println("enterInitialValueOf");
    }

    @Override
    public void exitInitialValueOf(RulepadGrammarParser.InitialValueOfContext ctx) {
        System.out.println("exitInitialValueOf");
    }

    @Override
    public void enterInitialValueCondition(RulepadGrammarParser.InitialValueConditionContext ctx) {
        System.out.println("enterInitialValueCondition");
    }

    @Override
    public void exitInitialValueCondition(RulepadGrammarParser.InitialValueConditionContext ctx) {
        System.out.println("exitInitialValueCondition");
    }

    @Override
    public void enterClasses(RulepadGrammarParser.ClassesContext ctx) {
        System.out.println("enterClasses");
    }

    @Override
    public void exitClasses(RulepadGrammarParser.ClassesContext ctx) {
        System.out.println("exitClasses");
    }

    @Override
    public void enterClassCondition(RulepadGrammarParser.ClassConditionContext ctx) {
        System.out.println("enterClassCondition");
    }

    @Override
    public void exitClassCondition(RulepadGrammarParser.ClassConditionContext ctx) {
        System.out.println("exitClassCondition");
    }

    @Override
    public void enterClassExpression(RulepadGrammarParser.ClassExpressionContext ctx) {
        System.out.println("enterClassExpression");
        final RulepadGrammarParser.BinaryContext op = ctx.op;
        System.out.println("Operation: " + (op == null ? "NULL" : op.getText().toString()));
    }

    @Override
    public void exitClassExpression(RulepadGrammarParser.ClassExpressionContext ctx) {
        System.out.println("exitClassExpression");
    }

    @Override
    public void enterSubclasses(RulepadGrammarParser.SubclassesContext ctx) {
        System.out.println("enterSubclasses");
    }

    @Override
    public void exitSubclasses(RulepadGrammarParser.SubclassesContext ctx) {
        System.out.println("exitSubclasses");
    }

    @Override
    public void enterSubclassOf(RulepadGrammarParser.SubclassOfContext ctx) {
        System.out.println("enterSubclassOf");
    }

    @Override
    public void exitSubclassOf(RulepadGrammarParser.SubclassOfContext ctx) {
        System.out.println("exitSubclassOf");
    }

    @Override
    public void enterSubclassCondition(RulepadGrammarParser.SubclassConditionContext ctx) {
        System.out.println("enterSubclassCondition");
    }

    @Override
    public void exitSubclassCondition(RulepadGrammarParser.SubclassConditionContext ctx) {
        System.out.println("exitSubclassCondition");
    }

    @Override
    public void enterSubclassExpression(RulepadGrammarParser.SubclassExpressionContext ctx) {
        System.out.println("enterSubclassExpression");
    }

    @Override
    public void exitSubclassExpression(RulepadGrammarParser.SubclassExpressionContext ctx) {
        System.out.println("exitSubclassExpression");
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

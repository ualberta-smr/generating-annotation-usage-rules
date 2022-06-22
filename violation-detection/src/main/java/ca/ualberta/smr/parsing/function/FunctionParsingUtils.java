package ca.ualberta.smr.parsing.function;

import ca.ualberta.grammar.RulepadGrammarParser;
import ca.ualberta.smr.model.javaelements.Method;
import ca.ualberta.smr.parsing.annotation.AnnotationVisitor;
import lombok.val;
import org.antlr.v4.runtime.ParserRuleContext;

import static ca.ualberta.smr.parsing.utils.CombinatorialWordsExtractorUtility.extractEnclosingClass;
import static ca.ualberta.smr.parsing.utils.CombinatorialWordsExtractorUtility.extractReturnType;
import static ca.ualberta.smr.parsing.utils.GeneralUtility.acceptIfAvailable;

public class FunctionParsingUtils {

    public static Method createMethodFromCtx(ParserRuleContext generalContext) {
        final RulepadGrammarParser.ReturnTypesContext returnTypesContext;
        final RulepadGrammarParser.AnnotationsContext annotationsContext;
        final RulepadGrammarParser.FunctionParametersContext parametersContext;
        final RulepadGrammarParser.EnclosingClassContext enclosingClassContext;

        if (generalContext instanceof RulepadGrammarParser.FunctionExpressionContext) {
            val ctx = (RulepadGrammarParser.FunctionExpressionContext) generalContext;
            returnTypesContext = ctx.returnTypes();
            annotationsContext = ctx.annotations();
            parametersContext = ctx.functionParameters();
            enclosingClassContext = ctx.enclosingClass();
        } else if (generalContext instanceof RulepadGrammarParser.FunctionExpressionAggregateContentsContext) {
            val ctx = (RulepadGrammarParser.FunctionExpressionAggregateContentsContext) generalContext;
            returnTypesContext = ctx.returnTypes();
            annotationsContext = ctx.annotations();
            parametersContext = ctx.functionParameters();
            enclosingClassContext = ctx.enclosingClass();
        } else {
            // generalContext instanceof RulepadGrammarParser.FunctionExpressionNoContext
            val ctx = (RulepadGrammarParser.FunctionExpressionNoContext) generalContext;
            returnTypesContext = ctx.returnTypes();
            annotationsContext = ctx.annotations();
            parametersContext = ctx.functionParameters();
            enclosingClassContext = ctx.enclosingClass();
        }

        val returnType = extractReturnType(returnTypesContext);
        val annotations = acceptIfAvailable(annotationsContext, new AnnotationVisitor());
        val parameters = acceptIfAvailable(parametersContext, new FunctionParameterVisitor());
        extractEnclosingClass(enclosingClassContext);

        return new Method(returnType, annotations, parameters);
    }

}

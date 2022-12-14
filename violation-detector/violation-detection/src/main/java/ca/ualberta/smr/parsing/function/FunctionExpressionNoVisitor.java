package ca.ualberta.smr.parsing.function;

import ca.ualberta.grammar.RulepadGrammarBaseVisitor;
import ca.ualberta.grammar.RulepadGrammarParser;
import ca.ualberta.smr.parsing.utils.CombinatorialWordsExtractorUtility;
import ca.ualberta.smr.parsing.annotation.AnnotationVisitor;
import ca.ualberta.smr.model.javaelements.AggregateCondition;
import ca.ualberta.smr.model.javaelements.Method;
import lombok.val;

import static ca.ualberta.smr.parsing.function.FunctionParsingUtils.createMethodFromCtx;
import static ca.ualberta.smr.parsing.utils.GeneralUtility.acceptIfAvailable;

class FunctionExpressionNoVisitor extends RulepadGrammarBaseVisitor<AggregateCondition> {
    @Override
    public AggregateCondition visitFunctionExpressionNo(RulepadGrammarParser.FunctionExpressionNoContext ctx) {
        val method = createMethodFromCtx(ctx);
        return AggregateCondition.not(method);
    }
}

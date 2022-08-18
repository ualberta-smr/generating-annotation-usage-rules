package ca.ualberta.smr.parsing.function;

import ca.ualberta.grammar.RulepadGrammarBaseVisitor;
import ca.ualberta.grammar.RulepadGrammarParser;
import ca.ualberta.smr.parsing.utils.CombinatorialWordsExtractorUtility;
import ca.ualberta.smr.parsing.annotation.AnnotationVisitor;
import ca.ualberta.smr.model.javaelements.AggregateCondition;
import ca.ualberta.smr.model.javaelements.AggregateConditionOperation;
import ca.ualberta.smr.model.javaelements.Method;
import ca.ualberta.smr.model.javaelements.ProgramElement;
import lombok.val;

import static ca.ualberta.smr.parsing.function.FunctionParsingUtils.createMethodFromCtx;
import static ca.ualberta.smr.parsing.utils.GeneralUtility.acceptIfAvailable;

class FunctionExpressionNoneOfVisitor extends RulepadGrammarBaseVisitor<AggregateCondition> {

    @Override
    public AggregateCondition visitFunctionExpressionNoneOf(RulepadGrammarParser.FunctionExpressionNoneOfContext ctx) {
        return ctx.functionExpressionAggregateContents().accept(this);
    }

    @Override
    public AggregateCondition visitFunctionExpressionAggregateContents(RulepadGrammarParser.FunctionExpressionAggregateContentsContext ctx) {
        if (ctx.op == null) {
            val method = createMethodFromCtx(ctx);
            return AggregateCondition.not(method);
        }
        val op = AggregateConditionOperation.AND;
        val left = this.visitFunctionExpressionAggregateContents(ctx.left);
        val right = this.visitFunctionExpressionAggregateContents(ctx.right);
        return new AggregateCondition(left, right, op, ProgramElement.ProgramElementType.METHOD);
    }
}

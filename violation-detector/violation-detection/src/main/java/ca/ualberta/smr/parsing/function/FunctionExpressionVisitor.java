package ca.ualberta.smr.parsing.function;

import ca.ualberta.grammar.RulepadGrammarBaseVisitor;
import ca.ualberta.grammar.RulepadGrammarParser;
import ca.ualberta.smr.parsing.utils.CombinatorialWordsExtractorUtility;
import ca.ualberta.smr.parsing.annotation.AnnotationVisitor;
import ca.ualberta.smr.model.javaelements.AggregateCondition;
import ca.ualberta.smr.model.javaelements.Method;
import ca.ualberta.smr.model.javaelements.ProgramElement;
import lombok.val;

import static ca.ualberta.smr.parsing.function.FunctionParsingUtils.createMethodFromCtx;
import static ca.ualberta.smr.parsing.utils.GeneralUtility.acceptIfAvailable;
import static ca.ualberta.smr.parsing.utils.GeneralUtility.getOperation;
import static ca.ualberta.smr.parsing.utils.GeneralUtility.unwrapIfSingle;
import static ca.ualberta.smr.parsing.utils.GeneralUtility.listOf;

public class FunctionExpressionVisitor extends RulepadGrammarBaseVisitor<AggregateCondition> {

    @Override
    public AggregateCondition visitFunctionExpression(RulepadGrammarParser.FunctionExpressionContext ctx) {
        if (ctx.op == null) {
            if (ctx.functionExpression().isEmpty()) {
                val method = createMethodFromCtx(ctx);

                // these can be Method aggregate condition objects
                val no = acceptIfAvailable(ctx.functionExpressionNo(), new FunctionExpressionNoVisitor());
                val noneOf = acceptIfAvailable(ctx.functionExpressionNoneOf(), new FunctionExpressionNoneOfVisitor());
                val oneOf = acceptIfAvailable(ctx.functionExpressionOneOf(), new FunctionExpressionOneOfVisitor());

                return listOf(no, noneOf, oneOf)
                        .stream()
                        .filter(a -> !a.isEmpty())
                        .findFirst()
                        .orElseGet(() -> AggregateCondition.single(method));
            }
            return this.visitFunctionExpression(ctx.functionExpression(0));
        }
        val op = getOperation(ctx.op);
        val left = unwrapIfSingle(this.visitFunctionExpression(ctx.left));
        val right = unwrapIfSingle(this.visitFunctionExpression(ctx.right));
        return new AggregateCondition(left, right, op, ProgramElement.ProgramElementType.METHOD);
    }

}
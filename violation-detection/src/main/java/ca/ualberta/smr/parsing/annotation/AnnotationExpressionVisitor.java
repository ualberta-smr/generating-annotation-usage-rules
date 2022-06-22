package ca.ualberta.smr.parsing.annotation;

import ca.ualberta.grammar.RulepadGrammarBaseVisitor;
import ca.ualberta.grammar.RulepadGrammarParser;
import ca.ualberta.smr.model.javaelements.AggregateCondition;
import lombok.val;

import static ca.ualberta.smr.parsing.utils.GeneralUtility.getOperation;
import static ca.ualberta.smr.parsing.utils.GeneralUtility.unwrapIfSingle;

public class AnnotationExpressionVisitor extends RulepadGrammarBaseVisitor<AggregateCondition> {

    @Override
    public AggregateCondition visitAnnotationExpression(RulepadGrammarParser.AnnotationExpressionContext ctx) {
        if (ctx.op == null) {
            if (ctx.annotationExpression().isEmpty()) {
                return ctx.parameters().accept(new AnnotationParameterVisitor());
            }
            return this.visitAnnotationExpression(ctx.annotationExpression(0));
        } else {
            val op = getOperation(ctx.op);
            val left = unwrapIfSingle(this.visitAnnotationExpression(ctx.left));
            val right = unwrapIfSingle(this.visitAnnotationExpression(ctx.right));

            return new AggregateCondition(left, right, op);
        }
    }
}

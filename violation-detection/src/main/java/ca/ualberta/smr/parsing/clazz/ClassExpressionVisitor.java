package ca.ualberta.smr.parsing.clazz;

import ca.ualberta.grammar.RulepadGrammarBaseVisitor;
import ca.ualberta.grammar.RulepadGrammarParser;
import ca.ualberta.smr.model.javaelements.AggregateCondition;
import ca.ualberta.smr.model.javaelements.ProgramElement;
import lombok.val;

import static ca.ualberta.smr.model.javaelements.AggregateCondition.single;
import static ca.ualberta.smr.parsing.clazz.ClassParsingUtils.createClassFromCtx;
import static ca.ualberta.smr.parsing.utils.GeneralUtility.*;

public class ClassExpressionVisitor extends RulepadGrammarBaseVisitor<AggregateCondition> {

    @Override
    public AggregateCondition visitClassExpression(RulepadGrammarParser.ClassExpressionContext ctx) {
        if (ctx.op == null) {
            if (ctx.classExpression().isEmpty()) {
                val javaClass = createClassFromCtx(ctx);

                val no = acceptIfAvailable(ctx.classExpressionNo(), new ClassExpressionNoVisitor());
                val noneOf = acceptIfAvailable(ctx.classExpressionNoneOf(), new ClassExpressionNoneOfVisitor());
                val oneOf = acceptIfAvailable(ctx.classExpressionOneOf(), new ClassExpressionOneOfVisitor());

                return listOf(no, noneOf, oneOf)
                        .stream()
                        .filter(a -> !a.isEmpty())
                        .findFirst()
                        .orElseGet(() -> single(javaClass));
            }
            return this.visitClassExpression(ctx.classExpression(0));
        }
        val op = getOperation(ctx.op);
        val left = unwrapIfSingle(this.visitClassExpression(ctx.left));
        val right = unwrapIfSingle(this.visitClassExpression(ctx.right));
        return new AggregateCondition(left, right, op, ProgramElement.ProgramElementType.CLASS);
    }
}


package ca.ualberta.smr.parsing.clazz;

import ca.ualberta.grammar.RulepadGrammarBaseVisitor;
import ca.ualberta.grammar.RulepadGrammarParser;
import ca.ualberta.smr.model.javaelements.AggregateCondition;
import ca.ualberta.smr.model.javaelements.AggregateConditionOperation;
import ca.ualberta.smr.model.javaelements.ProgramElement;
import lombok.val;

import static ca.ualberta.smr.parsing.clazz.ClassParsingUtils.createClassFromCtx;

class ClassExpressionNoneOfVisitor extends RulepadGrammarBaseVisitor<AggregateCondition> {

    @Override
    public AggregateCondition visitClassExpressionNoneOf(RulepadGrammarParser.ClassExpressionNoneOfContext ctx) {
        return ctx.classExpressionAggregateContents().accept(this);
    }

    @Override
    public AggregateCondition visitClassExpressionAggregateContents(RulepadGrammarParser.ClassExpressionAggregateContentsContext ctx) {
        if (ctx.op == null) {
            val javaClass = createClassFromCtx(ctx);
            return AggregateCondition.not(javaClass);
        }
        val op = AggregateConditionOperation.AND;
        val left = this.visitClassExpressionAggregateContents(ctx.left);
        val right = this.visitClassExpressionAggregateContents(ctx.right);
        return new AggregateCondition(left, right, op, ProgramElement.ProgramElementType.CLASS);
    }

}

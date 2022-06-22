package ca.ualberta.smr.parsing.clazz;

import ca.ualberta.grammar.RulepadGrammarBaseVisitor;
import ca.ualberta.grammar.RulepadGrammarParser;
import ca.ualberta.smr.model.javaelements.AggregateCondition;
import lombok.val;

import static ca.ualberta.smr.parsing.clazz.ClassParsingUtils.createClassFromCtx;

class ClassExpressionNoVisitor extends RulepadGrammarBaseVisitor<AggregateCondition> {

    @Override
    public AggregateCondition visitClassExpressionNo(RulepadGrammarParser.ClassExpressionNoContext ctx) {
        val javaClass = createClassFromCtx(ctx);
        return AggregateCondition.single(javaClass);
    }

}

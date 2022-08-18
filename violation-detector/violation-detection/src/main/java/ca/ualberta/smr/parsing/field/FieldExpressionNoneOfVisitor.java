package ca.ualberta.smr.parsing.field;

import ca.ualberta.grammar.RulepadGrammarBaseVisitor;
import ca.ualberta.grammar.RulepadGrammarParser;
import ca.ualberta.smr.model.javaelements.AggregateCondition;
import ca.ualberta.smr.model.javaelements.AggregateConditionOperation;
import ca.ualberta.smr.model.javaelements.ProgramElement;
import lombok.val;

import static ca.ualberta.smr.parsing.field.FieldParsingUtils.createFieldFromCtx;

class FieldExpressionNoneOfVisitor extends RulepadGrammarBaseVisitor<AggregateCondition> {

    @Override
    public AggregateCondition visitDeclarationStatementExpressionNoneOf(RulepadGrammarParser.DeclarationStatementExpressionNoneOfContext ctx) {
        return ctx.declarationStatementExpressionAggregateContents().accept(this);
    }

    @Override
    public AggregateCondition visitDeclarationStatementExpressionAggregateContents(RulepadGrammarParser.DeclarationStatementExpressionAggregateContentsContext ctx) {
        if (ctx.op == null) {
            val field = createFieldFromCtx(ctx);
            return AggregateCondition.not(field);
        }
        val op = AggregateConditionOperation.AND;
        val left = this.visitDeclarationStatementExpressionAggregateContents(ctx.left);
        val right = this.visitDeclarationStatementExpressionAggregateContents(ctx.right);
        return new AggregateCondition(left, right, op, ProgramElement.ProgramElementType.FIELD);
    }

}

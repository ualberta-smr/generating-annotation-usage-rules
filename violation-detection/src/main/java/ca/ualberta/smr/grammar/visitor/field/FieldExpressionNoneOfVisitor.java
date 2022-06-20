package ca.ualberta.smr.grammar.visitor.field;

import ca.ualberta.grammar.RulepadGrammarBaseVisitor;
import ca.ualberta.grammar.RulepadGrammarParser;
import ca.ualberta.smr.grammar.visitor.CombinatorialWordsExtractorUtility;
import ca.ualberta.smr.grammar.visitor.annotation.AnnotationVisitor;
import ca.ualberta.smr.newmodel.javaelements.AggregateCondition;
import ca.ualberta.smr.newmodel.javaelements.AggregateConditionOperation;
import ca.ualberta.smr.newmodel.javaelements.Field;
import lombok.val;

import static ca.ualberta.smr.grammar.visitor.GeneralUtility.acceptIfAvailable;

class FieldExpressionNoneOfVisitor extends RulepadGrammarBaseVisitor<AggregateCondition> {

    @Override
    public AggregateCondition visitDeclarationStatementExpressionNoneOf(RulepadGrammarParser.DeclarationStatementExpressionNoneOfContext ctx) {
        return ctx.declarationStatementExpressionAggregateContents().accept(this);
    }

    @Override
    public AggregateCondition visitDeclarationStatementExpressionAggregateContents(RulepadGrammarParser.DeclarationStatementExpressionAggregateContentsContext ctx) {
        if (ctx.op == null) {
            val types = CombinatorialWordsExtractorUtility.extractType(ctx.types());
            val annotations = acceptIfAvailable(ctx.annotations(), new AnnotationVisitor());
            return AggregateCondition.not(
                    new Field(types, annotations)
            );
        }
        val op = AggregateConditionOperation.AND;
        val left = this.visitDeclarationStatementExpressionAggregateContents(ctx.left);
        val right = this.visitDeclarationStatementExpressionAggregateContents(ctx.right);
        return new AggregateCondition(left, right, op);
    }

}

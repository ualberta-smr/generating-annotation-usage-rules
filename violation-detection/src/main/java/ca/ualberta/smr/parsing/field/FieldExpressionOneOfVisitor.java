package ca.ualberta.smr.parsing.field;

import ca.ualberta.grammar.RulepadGrammarBaseVisitor;
import ca.ualberta.grammar.RulepadGrammarParser;
import ca.ualberta.smr.parsing.utils.CombinatorialWordsExtractorUtility;
import ca.ualberta.smr.parsing.annotation.AnnotationVisitor;
import ca.ualberta.smr.model.javaelements.AggregateCondition;
import ca.ualberta.smr.model.javaelements.AggregateConditionOperation;
import ca.ualberta.smr.model.javaelements.Field;
import ca.ualberta.smr.model.javaelements.ProgramElement;
import lombok.val;

import static ca.ualberta.smr.parsing.field.FieldParsingUtils.createFieldFromCtx;
import static ca.ualberta.smr.parsing.utils.GeneralUtility.acceptIfAvailable;

class FieldExpressionOneOfVisitor extends RulepadGrammarBaseVisitor<AggregateCondition> {

    @Override
    public AggregateCondition visitDeclarationStatementExpressionOneOf(RulepadGrammarParser.DeclarationStatementExpressionOneOfContext ctx) {
        return ctx.declarationStatementExpressionAggregateContents().accept(this);
    }

    @Override
    public AggregateCondition visitDeclarationStatementExpressionAggregateContents(RulepadGrammarParser.DeclarationStatementExpressionAggregateContentsContext ctx) {
        if (ctx.op == null) {
            val field = createFieldFromCtx(ctx);
            return AggregateCondition.single(field);
        }
        // when evaluating XOR, if two processed nodes produce True and True, then stop the evaluation
        // because one of implies only one element from the bunch
        val op = AggregateConditionOperation.XOR;
        val left = this.visitDeclarationStatementExpressionAggregateContents(ctx.left);
        val right = this.visitDeclarationStatementExpressionAggregateContents(ctx.right);
        return new AggregateCondition(left, right, op, ProgramElement.ProgramElementType.FIELD);
    }

}

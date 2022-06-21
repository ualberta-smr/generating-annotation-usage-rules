package ca.ualberta.smr.grammar.visitor.field;

import ca.ualberta.grammar.RulepadGrammarBaseVisitor;
import ca.ualberta.grammar.RulepadGrammarParser;
import ca.ualberta.smr.grammar.visitor.CombinatorialWordsExtractorUtility;
import ca.ualberta.smr.grammar.visitor.annotation.AnnotationVisitor;
import ca.ualberta.smr.newmodel.javaelements.AggregateCondition;
import ca.ualberta.smr.newmodel.javaelements.AggregateConditionOperation;
import ca.ualberta.smr.newmodel.javaelements.Field;
import ca.ualberta.smr.newmodel.javaelements.ProgramElement;
import lombok.val;

import static ca.ualberta.smr.grammar.visitor.GeneralUtility.acceptIfAvailable;

class FieldExpressionOneOfVisitor extends RulepadGrammarBaseVisitor<AggregateCondition> {

    @Override
    public AggregateCondition visitDeclarationStatementExpressionOneOf(RulepadGrammarParser.DeclarationStatementExpressionOneOfContext ctx) {
        return ctx.declarationStatementExpressionAggregateContents().accept(this);
    }

    @Override
    public AggregateCondition visitDeclarationStatementExpressionAggregateContents(RulepadGrammarParser.DeclarationStatementExpressionAggregateContentsContext ctx) {
        if (ctx.op == null) {
            val types = CombinatorialWordsExtractorUtility.extractType(ctx.types());
            val annotations = acceptIfAvailable(ctx.annotations(), new AnnotationVisitor());
            return AggregateCondition.single(
                    new Field(types, annotations), ProgramElement.ProgramElementType.FIELD
            );
        }
        // when evaluating XOR, if two processed nodes produce True and True, then stop the evaluation
        // because one of implies only one element from the bunch
        val op = AggregateConditionOperation.XOR;
        val left = this.visitDeclarationStatementExpressionAggregateContents(ctx.left);
        val right = this.visitDeclarationStatementExpressionAggregateContents(ctx.right);
        return new AggregateCondition(left, right, op, ProgramElement.ProgramElementType.FIELD);
    }

}

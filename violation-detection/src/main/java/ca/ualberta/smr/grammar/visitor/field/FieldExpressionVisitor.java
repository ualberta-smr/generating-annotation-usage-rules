package ca.ualberta.smr.grammar.visitor.field;

import ca.ualberta.grammar.RulepadGrammarBaseVisitor;
import ca.ualberta.grammar.RulepadGrammarParser;
import ca.ualberta.smr.grammar.visitor.CombinatorialWordsExtractorUtility;
import ca.ualberta.smr.grammar.visitor.annotation.AnnotationVisitor;
import ca.ualberta.smr.newmodel.javaelements.AggregateCondition;
import ca.ualberta.smr.newmodel.javaelements.Field;
import ca.ualberta.smr.newmodel.javaelements.ProgramElement;
import lombok.val;

import static ca.ualberta.smr.grammar.visitor.GeneralUtility.acceptIfAvailable;
import static ca.ualberta.smr.grammar.visitor.GeneralUtility.getOperation;
import static ca.ualberta.smr.grammar.visitor.GeneralUtility.unwrapIfSingle;
import static ca.ualberta.smr.utils.Utils.listOf;

public class FieldExpressionVisitor extends RulepadGrammarBaseVisitor<AggregateCondition> {

    @Override
    public AggregateCondition visitDeclarationStatementExpression(RulepadGrammarParser.DeclarationStatementExpressionContext ctx) {
        if (ctx.op == null) {
            if (ctx.declarationStatementExpression().isEmpty()) {
                // these are properties of Field objects
                val types = CombinatorialWordsExtractorUtility.extractType(ctx.types());
                val annotations = acceptIfAvailable(ctx.annotations(), new AnnotationVisitor());

                // these can be Field aggregate condition objects
                val no = acceptIfAvailable(ctx.declarationStatementExpressionNo(), new FieldExpressionNoVisitor());
                val noneOf = acceptIfAvailable(ctx.declarationStatementExpressionNoneOf(), new FieldExpressionNoneOfVisitor());
                val oneOf = acceptIfAvailable(ctx.declarationStatementExpressionOneOf(), new FieldExpressionOneOfVisitor());

                return listOf(no, noneOf, oneOf)
                        .stream()
                        .filter(a -> !a.isEmpty())
                        .findFirst()
                        .orElseGet(() -> AggregateCondition.single(
                                new Field(types, annotations), ProgramElement.ProgramElementType.FIELD
                        ));
            }
            return this.visitDeclarationStatementExpression(ctx.declarationStatementExpression(0));
        }
        val op = getOperation(ctx.op);
        val left = unwrapIfSingle(this.visitDeclarationStatementExpression(ctx.left));
        val right = unwrapIfSingle(this.visitDeclarationStatementExpression(ctx.right));
        return new AggregateCondition(left, right, op, ProgramElement.ProgramElementType.FIELD);
    }
}


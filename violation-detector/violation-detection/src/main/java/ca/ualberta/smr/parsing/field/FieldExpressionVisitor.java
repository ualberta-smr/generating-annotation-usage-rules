package ca.ualberta.smr.parsing.field;

import ca.ualberta.grammar.RulepadGrammarBaseVisitor;
import ca.ualberta.grammar.RulepadGrammarParser;
import ca.ualberta.smr.model.javaelements.AggregateCondition;
import ca.ualberta.smr.model.javaelements.ProgramElement;
import lombok.val;

import static ca.ualberta.smr.parsing.field.FieldParsingUtils.createFieldFromCtx;
import static ca.ualberta.smr.parsing.utils.GeneralUtility.*;

public class FieldExpressionVisitor extends RulepadGrammarBaseVisitor<AggregateCondition> {

    @Override
    public AggregateCondition visitDeclarationStatementExpression(RulepadGrammarParser.DeclarationStatementExpressionContext ctx) {
        if (ctx.op == null) {
            if (ctx.declarationStatementExpression().isEmpty()) {
                val field = createFieldFromCtx(ctx);
                // these can be Field aggregate condition objects
                val no = acceptIfAvailable(ctx.declarationStatementExpressionNo(), new FieldExpressionNoVisitor());
                val noneOf = acceptIfAvailable(ctx.declarationStatementExpressionNoneOf(), new FieldExpressionNoneOfVisitor());
                val oneOf = acceptIfAvailable(ctx.declarationStatementExpressionOneOf(), new FieldExpressionOneOfVisitor());

                return listOf(no, noneOf, oneOf)
                        .stream()
                        .filter(a -> !a.isEmpty())
                        .findFirst()
                        .orElseGet(() -> AggregateCondition.single(
                                field, ProgramElement.ProgramElementType.FIELD
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


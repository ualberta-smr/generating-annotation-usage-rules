package ca.ualberta.smr.grammar.visitor.function;

import ca.ualberta.grammar.RulepadGrammarBaseVisitor;
import ca.ualberta.grammar.RulepadGrammarParser;
import ca.ualberta.smr.grammar.visitor.CombinatorialWordsExtractorUtility;
import ca.ualberta.smr.grammar.visitor.annotation.AnnotationVisitor;
import ca.ualberta.smr.newmodel.javaelements.AggregateCondition;
import ca.ualberta.smr.newmodel.javaelements.Method;
import lombok.val;

import static ca.ualberta.smr.grammar.visitor.GeneralUtility.acceptIfAvailable;
import static ca.ualberta.smr.grammar.visitor.GeneralUtility.getOperation;
import static ca.ualberta.smr.grammar.visitor.GeneralUtility.unwrapIfSingle;
import static ca.ualberta.smr.utils.Utils.listOf;

public class FunctionExpressionVisitor extends RulepadGrammarBaseVisitor<AggregateCondition> {

    @Override
    public AggregateCondition visitFunctionExpression(RulepadGrammarParser.FunctionExpressionContext ctx) {
        if (ctx.op == null) {
            if (ctx.functionExpression().isEmpty()) {
                // these can be parts of a Method object
                val returnType = CombinatorialWordsExtractorUtility.extractReturnType(ctx.returnTypes());
                val annotations = acceptIfAvailable(ctx.annotations(), new AnnotationVisitor());
                val parameters = acceptIfAvailable(ctx.functionParameters(), new FunctionParameterVisitor());

                // these can be Method aggregate condition objects
                val no = acceptIfAvailable(ctx.functionExpressionNo(), new FunctionExpressionNoVisitor());
                val noneOf = acceptIfAvailable(ctx.functionExpressionNoneOf(), new FunctionExpressionNoneOfVisitor());
                val oneOf = acceptIfAvailable(ctx.functionExpressionOneOf(), new FunctionExpressionOneOfVisitor());

                return listOf(no, noneOf, oneOf)
                        .stream()
                        .filter(a -> !a.isEmpty())
                        .findFirst()
                        .orElseGet(() -> AggregateCondition.single(
                                new Method(returnType, annotations, parameters)
                        ));
            }
            return this.visitFunctionExpression(ctx.functionExpression(0));
        }
        val op = getOperation(ctx.op);
        val left = unwrapIfSingle(this.visitFunctionExpression(ctx.left));
        val right = unwrapIfSingle(this.visitFunctionExpression(ctx.right));
        return new AggregateCondition(left, right, op);
    }

}
package ca.ualberta.smr.parsing.function;

import ca.ualberta.grammar.RulepadGrammarBaseVisitor;
import ca.ualberta.grammar.RulepadGrammarParser;
import ca.ualberta.smr.parsing.utils.CombinatorialWordsExtractorUtility;
import ca.ualberta.smr.parsing.utils.GeneralUtility;
import ca.ualberta.smr.parsing.annotation.AnnotationVisitor;
import ca.ualberta.smr.model.javaelements.AggregateCondition;
import ca.ualberta.smr.model.javaelements.MethodParameter;
import ca.ualberta.smr.model.javaelements.Type;
import lombok.val;
import lombok.var;

import static ca.ualberta.smr.parsing.utils.GeneralUtility.getText;
import static ca.ualberta.smr.parsing.utils.GeneralUtility.unwrapIfSingle;

public class FunctionParameterVisitor extends RulepadGrammarBaseVisitor<AggregateCondition> {

    @Override
    public AggregateCondition visitFunctionParameterCondition(RulepadGrammarParser.FunctionParameterConditionContext ctx) {
        // TODO: need to work on this because type can also be specified in the param combWords
        var defaultType = AggregateCondition.empty();

        val combWords = ctx.combinatorialWords();
        if (combWords != null) {
            val text = getText(combWords);
            val pieces = text.split("\\s+");
            if (pieces.length >= 1) {
                defaultType = Type.of(pieces[0].trim());
            }
        }

        val transitionContext = ctx.functionParameterConditionTransition();
        if (transitionContext != null) {
            return this.visitFunctionParameterExpression(transitionContext.functionParameterExpression(), defaultType);
        }

        if (defaultType.isEmpty()) {
            throw new RuntimeException("Method parameter needs to have a type or an annotation");
        }

        return AggregateCondition.single(
                new MethodParameter(defaultType, AggregateCondition.empty())
        );
    }

    public AggregateCondition visitFunctionParameterExpression(RulepadGrammarParser.FunctionParameterExpressionContext ctx,
                                                               AggregateCondition defaultType) {
        if (ctx.op == null) {
            if (ctx.functionParameterExpression().isEmpty()) {
                val types = CombinatorialWordsExtractorUtility.extractType(ctx.types());
                // actually irrelevant, maybe should be replaced with position?
                val names = CombinatorialWordsExtractorUtility.extractName(ctx.names());
                val annotations = ctx.annotations().accept(new AnnotationVisitor());

                return AggregateCondition.single(
                        new MethodParameter(types.isEmpty() ? defaultType : types, annotations)
                );
            }
            return this.visitFunctionParameterExpression(ctx.functionParameterExpression(0), defaultType);
        } else {
            val op = GeneralUtility.getOperation(ctx.op);
            val left = unwrapIfSingle(this.visitFunctionParameterExpression(ctx.left, defaultType));
            val right = unwrapIfSingle(this.visitFunctionParameterExpression(ctx.right, defaultType));

            return new AggregateCondition(left, right, op);
        }
    }

}

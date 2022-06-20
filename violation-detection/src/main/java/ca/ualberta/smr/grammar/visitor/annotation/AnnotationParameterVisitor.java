package ca.ualberta.smr.grammar.visitor.annotation;

import ca.ualberta.grammar.RulepadGrammarBaseVisitor;
import ca.ualberta.grammar.RulepadGrammarParser;
import ca.ualberta.smr.grammar.visitor.CombinatorialWordsExtractorUtility;
import ca.ualberta.smr.grammar.visitor.GeneralUtility;
import ca.ualberta.smr.newmodel.javaelements.AggregateCondition;
import ca.ualberta.smr.newmodel.javaelements.AnnotationParameter;
import ca.ualberta.smr.newmodel.javaelements.Name;
import ca.ualberta.smr.newmodel.javaelements.Type;
import lombok.val;
import lombok.var;

import static ca.ualberta.smr.grammar.visitor.GeneralUtility.*;

public class AnnotationParameterVisitor extends RulepadGrammarBaseVisitor<AggregateCondition> {
    @Override
    public AggregateCondition visitParameterCondition(RulepadGrammarParser.ParameterConditionContext ctx) {
        // TODO: need to work on this because type can also be specified in the param combWords
        var defaultType = AggregateCondition.empty();
        var defaultName = AggregateCondition.empty();

        val combWords = ctx.combinatorialWords();
        if (combWords != null) {
            val pieces = getText(combWords).split("\\s+");
            if (pieces.length == 1) {
                defaultName = AggregateCondition.single(new Name(pieces[0]));
            } else if (pieces.length > 1) {
                defaultType = AggregateCondition.single(new Type(pieces[0]));
                defaultName = AggregateCondition.single(new Name(pieces[1]));
            }
        }

        val transitionContext = ctx.parameterConditionTransition();
        if (transitionContext != null) {
            return this.visitParameterExpression(transitionContext.parameterExpression(), defaultType, defaultName);
        }

        if (defaultName.isEmpty() && defaultType.isEmpty()) {
            throw new RuntimeException("Annotation parameter is missing both combWords and conditionalTransition");
        }

        return AggregateCondition.single(
                new AnnotationParameter(
                        defaultType,
                        defaultName,
                        AggregateCondition.empty())
        );
    }

    public AggregateCondition visitParameterExpression(RulepadGrammarParser.ParameterExpressionContext ctx,
                                                       AggregateCondition defaultType,
                                                       AggregateCondition defaultName) {
        if (ctx.op == null) {
            if (ctx.parameterExpression().isEmpty()) {
                val types = CombinatorialWordsExtractorUtility.extractType(ctx.types());
                val names = CombinatorialWordsExtractorUtility.extractName(ctx.names());
                val values = CombinatorialWordsExtractorUtility.extractValue(ctx.values());

                return AggregateCondition.single(
                        new AnnotationParameter(
                                types.isEmpty() ? defaultType : types,
                                names.isEmpty() ? defaultName : names,
                                values)
                );
            }
            // it's not a binary context, so we'll only have 1 parameter expression
            return this.visitParameterExpression(ctx.parameterExpression(0), defaultType, defaultName);
        } else {
            val op = getOperation(ctx.op);
            val left = unwrapIfSingle(this.visitParameterExpression(ctx.left, defaultType, defaultName));
            val right = unwrapIfSingle(this.visitParameterExpression(ctx.right, defaultType, defaultName));

            return new AggregateCondition(left, right, op);
        }
    }
}

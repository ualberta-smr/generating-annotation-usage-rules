package ca.ualberta.smr.parsing.annotation;

import ca.ualberta.grammar.RulepadGrammarBaseVisitor;
import ca.ualberta.grammar.RulepadGrammarParser;
import ca.ualberta.smr.model.javaelements.AggregateCondition;
import ca.ualberta.smr.model.javaelements.AggregateConditionOperation;
import ca.ualberta.smr.model.javaelements.Annotation;
import ca.ualberta.smr.model.javaelements.Type;
import lombok.val;

import java.util.Arrays;
import java.util.function.BinaryOperator;

import static ca.ualberta.smr.parsing.utils.GeneralUtility.getText;
import static ca.ualberta.smr.model.javaelements.AggregateCondition.*;
import static ca.ualberta.smr.parsing.utils.GeneralUtility.unwrapIfSingle;

public class AnnotationVisitor extends RulepadGrammarBaseVisitor<AggregateCondition> {
    @Override
    public AggregateCondition visitAnnotations(RulepadGrammarParser.AnnotationsContext ctx) {
        val annotationType = getAnnotationType(ctx);

        val txCtx = ctx.annotationCondition().annotationConditionTransition();
        if (txCtx != null) {
            val annotationParameters = txCtx.annotationExpression()
                    .accept(new AnnotationExpressionVisitor());
            return single(new Annotation(annotationType, annotationParameters));
        }
        return single(new Annotation(annotationType, empty()));
    }

    private AggregateCondition getAnnotationType(RulepadGrammarParser.AnnotationsContext ctx) {
        val words = ctx.annotationCondition().combinatorialWords();
        if (words != null) {
            val annotationTypeString = getText(words);
            val lparenPos = annotationTypeString.indexOf("[");
            if (lparenPos != -1) {
                val rparenPos = annotationTypeString.indexOf("]");
                if (rparenPos != -1) {
                    // a.b.c.[X|Y|Z]
                    val packageName = annotationTypeString.substring(0, lparenPos);
                    val expr = annotationTypeString.substring(lparenPos + 1, rparenPos).trim().split("\\|");
                    return Arrays.stream(expr)
                            .map(String::trim)
                            .map(s -> packageName + s)
                            .map(Type::of)
                            .reduce((type1, type2) -> {
                                val t1 = unwrapIfSingle(type1);
                                val t2 = unwrapIfSingle(type2);
                                return new AggregateCondition(t1, t2, AggregateConditionOperation.OR);
                            }).orElseGet(AggregateCondition::empty);
                }
                // error
            }

            return Type.of(annotationTypeString);
        }
        return empty();
    }
}

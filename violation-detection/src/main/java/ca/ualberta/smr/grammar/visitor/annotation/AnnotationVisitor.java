package ca.ualberta.smr.grammar.visitor.annotation;

import ca.ualberta.grammar.RulepadGrammarBaseVisitor;
import ca.ualberta.grammar.RulepadGrammarParser;
import ca.ualberta.smr.newmodel.javaelements.AggregateCondition;
import ca.ualberta.smr.newmodel.javaelements.Annotation;
import ca.ualberta.smr.newmodel.javaelements.Type;
import lombok.val;

import static ca.ualberta.smr.grammar.visitor.GeneralUtility.getText;
import static ca.ualberta.smr.newmodel.javaelements.AggregateCondition.*;

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
            return Type.of(getText(words));
        }
        return empty();
    }
}

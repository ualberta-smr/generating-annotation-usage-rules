package ca.ualberta.smr.grammar.visitor.clazz;

import ca.ualberta.grammar.RulepadGrammarBaseVisitor;
import ca.ualberta.grammar.RulepadGrammarParser;
import ca.ualberta.smr.grammar.visitor.GeneralUtility;
import ca.ualberta.smr.grammar.visitor.annotation.AnnotationVisitor;
import ca.ualberta.smr.grammar.visitor.field.FieldExpressionVisitor;
import ca.ualberta.smr.grammar.visitor.function.FunctionExpressionVisitor;
import ca.ualberta.smr.newmodel.javaelements.AggregateCondition;
import ca.ualberta.smr.newmodel.javaelements.AggregateConditionOperation;
import ca.ualberta.smr.newmodel.javaelements.JavaClass;
import lombok.val;

import static ca.ualberta.smr.grammar.visitor.CombinatorialWordsExtractorUtility.*;

class ClassExpressionNoneOfVisitor extends RulepadGrammarBaseVisitor<AggregateCondition> {

    @Override
    public AggregateCondition visitClassExpressionNoneOf(RulepadGrammarParser.ClassExpressionNoneOfContext ctx) {
        return ctx.classExpressionAggregateContents().accept(this);
    }

    @Override
    public AggregateCondition visitClassExpressionAggregateContents(RulepadGrammarParser.ClassExpressionAggregateContentsContext ctx) {
        if (ctx.op == null) {
            val annotations = GeneralUtility.acceptIfAvailable(ctx.annotations(), new AnnotationVisitor());
            val extension = extractExtension(ctx.extensions());
            val implementation = extractImplementations(ctx.implementations());
            val methods = GeneralUtility.acceptIfAvailable(ctx.functions(), new FunctionExpressionVisitor());
            val fields = GeneralUtility.acceptIfAvailable(ctx.declarationStatements(), new FieldExpressionVisitor());
            // TODO: -- constructors
            // TODO:beans
            // TODO:beansFile
            // TODO:config

            return AggregateCondition.not(
                    new JavaClass(
                            annotations,
                            fields,
                            methods,
                            extension,
                            implementation
                    )
            );
        }
        val op = AggregateConditionOperation.AND;
        val left = this.visitClassExpressionAggregateContents(ctx.left);
        val right = this.visitClassExpressionAggregateContents(ctx.right);
        return new AggregateCondition(left, right, op);
    }

}

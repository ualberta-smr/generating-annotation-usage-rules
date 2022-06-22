package ca.ualberta.smr.parsing.clazz;

import ca.ualberta.grammar.RulepadGrammarBaseVisitor;
import ca.ualberta.grammar.RulepadGrammarParser;
import ca.ualberta.smr.parsing.utils.GeneralUtility;
import ca.ualberta.smr.parsing.annotation.AnnotationVisitor;
import ca.ualberta.smr.parsing.field.FieldExpressionVisitor;
import ca.ualberta.smr.parsing.function.FunctionExpressionVisitor;
import ca.ualberta.smr.model.javaelements.AggregateCondition;
import ca.ualberta.smr.model.javaelements.AggregateConditionOperation;
import ca.ualberta.smr.model.javaelements.JavaClass;
import ca.ualberta.smr.model.javaelements.ProgramElement;
import lombok.val;

import static ca.ualberta.smr.parsing.clazz.ClassExpressionVisitor.extractOverriddenFunctions;
import static ca.ualberta.smr.parsing.utils.CombinatorialWordsExtractorUtility.*;
import static ca.ualberta.smr.parsing.utils.GeneralUtility.acceptIfAvailable;

class ClassExpressionNoneOfVisitor extends RulepadGrammarBaseVisitor<AggregateCondition> {

    @Override
    public AggregateCondition visitClassExpressionNoneOf(RulepadGrammarParser.ClassExpressionNoneOfContext ctx) {
        return ctx.classExpressionAggregateContents().accept(this);
    }

    @Override
    public AggregateCondition visitClassExpressionAggregateContents(RulepadGrammarParser.ClassExpressionAggregateContentsContext ctx) {
        if (ctx.op == null) {
            val annotations = acceptIfAvailable(ctx.annotations(), new AnnotationVisitor());
            val extension = extractExtension(ctx.extensions());
            val implementation = extractImplementations(ctx.implementations());
            val overriddenMethods = extractOverriddenFunctions(ctx.overriddenFunctions());
            val methods = acceptIfAvailable(ctx.functions(), new FunctionExpressionVisitor());
            val fields = acceptIfAvailable(ctx.declarationStatements(), new FieldExpressionVisitor());
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
                            implementation,
                            overriddenMethods
                    )
            );
        }
        val op = AggregateConditionOperation.AND;
        val left = this.visitClassExpressionAggregateContents(ctx.left);
        val right = this.visitClassExpressionAggregateContents(ctx.right);
        return new AggregateCondition(left, right, op, ProgramElement.ProgramElementType.CLASS);
    }

}

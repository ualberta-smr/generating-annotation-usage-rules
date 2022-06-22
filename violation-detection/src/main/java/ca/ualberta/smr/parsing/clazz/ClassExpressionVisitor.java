package ca.ualberta.smr.parsing.clazz;

import ca.ualberta.grammar.RulepadGrammarBaseVisitor;
import ca.ualberta.grammar.RulepadGrammarParser;
import ca.ualberta.smr.parsing.utils.GeneralUtility;
import ca.ualberta.smr.parsing.annotation.AnnotationVisitor;
import ca.ualberta.smr.parsing.field.FieldExpressionVisitor;
import ca.ualberta.smr.parsing.function.FunctionExpressionVisitor;
import ca.ualberta.smr.model.javaelements.AggregateCondition;
import ca.ualberta.smr.model.javaelements.JavaClass;
import ca.ualberta.smr.model.javaelements.ProgramElement;
import lombok.val;

import static ca.ualberta.smr.parsing.utils.CombinatorialWordsExtractorUtility.*;
import static ca.ualberta.smr.parsing.utils.GeneralUtility.*;

public class ClassExpressionVisitor extends RulepadGrammarBaseVisitor<AggregateCondition> {

    @Override
    public AggregateCondition visitClassExpression(RulepadGrammarParser.ClassExpressionContext ctx) {
        if (ctx.op == null) {
            if (ctx.classExpression().isEmpty()) {
                val annotations = acceptIfAvailable(ctx.annotations(), new AnnotationVisitor());
                val extension = extractExtension(ctx.extensions());
                val implementation = extractImplementations(ctx.implementations());
                val methods = acceptIfAvailable(ctx.functions(), new FunctionExpressionVisitor());
                val fields = acceptIfAvailable(ctx.declarationStatements(), new FieldExpressionVisitor());
                // TODO: -- constructors
                // TODO:beans
                // TODO:beansFile
                // TODO:config

                val no = acceptIfAvailable(ctx.classExpressionNo(), new ClassExpressionNoVisitor());
                val noneOf = acceptIfAvailable(ctx.classExpressionNoneOf(), new ClassExpressionNoneOfVisitor());
                val oneOf = acceptIfAvailable(ctx.classExpressionOneOf(), new ClassExpressionOneOfVisitor());

                return listOf(no, noneOf, oneOf)
                        .stream()
                        .filter(a -> !a.isEmpty())
                        .findFirst()
                        .orElseGet(() -> AggregateCondition.single(
                                new JavaClass(
                                        annotations,
                                        fields,
                                        methods,
                                        extension,
                                        implementation
                                ), ProgramElement.ProgramElementType.CLASS
                        ));
            }
            return this.visitClassExpression(ctx.classExpression(0));
        }
        val op = getOperation(ctx.op);
        val left = unwrapIfSingle(this.visitClassExpression(ctx.left));
        val right = unwrapIfSingle(this.visitClassExpression(ctx.right));
        return new AggregateCondition(left, right, op, ProgramElement.ProgramElementType.CLASS);
    }
}


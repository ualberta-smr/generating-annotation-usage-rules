package ca.ualberta.smr.grammar.visitor.clazz;

import ca.ualberta.grammar.RulepadGrammarBaseVisitor;
import ca.ualberta.grammar.RulepadGrammarParser;
import ca.ualberta.smr.grammar.visitor.GeneralUtility;
import ca.ualberta.smr.grammar.visitor.annotation.AnnotationVisitor;
import ca.ualberta.smr.grammar.visitor.field.FieldExpressionVisitor;
import ca.ualberta.smr.grammar.visitor.function.FunctionExpressionVisitor;
import ca.ualberta.smr.newmodel.javaelements.AggregateCondition;
import ca.ualberta.smr.newmodel.javaelements.JavaClass;
import lombok.val;

import static ca.ualberta.smr.grammar.visitor.CombinatorialWordsExtractorUtility.*;
import static ca.ualberta.smr.grammar.visitor.GeneralUtility.getOperation;
import static ca.ualberta.smr.grammar.visitor.GeneralUtility.unwrapIfSingle;
import static ca.ualberta.smr.utils.Utils.listOf;

public class ClassExpressionVisitor extends RulepadGrammarBaseVisitor<AggregateCondition> {

    @Override
    public AggregateCondition visitClassExpression(RulepadGrammarParser.ClassExpressionContext ctx) {
        if (ctx.op == null) {
            if (ctx.classExpression().isEmpty()) {
                val annotations = GeneralUtility.acceptIfAvailable(ctx.annotations(), new AnnotationVisitor());
                val extension = extractExtension(ctx.extensions());
                val implementation = extractImplementations(ctx.implementations());
                val methods = GeneralUtility.acceptIfAvailable(ctx.functions(), new FunctionExpressionVisitor());
                val fields = GeneralUtility.acceptIfAvailable(ctx.declarationStatements(), new FieldExpressionVisitor());
                // TODO: -- constructors
                // TODO:beans
                // TODO:beansFile
                // TODO:config

                val no = GeneralUtility.acceptIfAvailable(ctx.classExpressionNo(), new ClassExpressionNoVisitor());
                val noneOf = GeneralUtility.acceptIfAvailable(ctx.classExpressionNoneOf(), new ClassExpressionNoneOfVisitor());
                val oneOf = GeneralUtility.acceptIfAvailable(ctx.classExpressionOneOf(), new ClassExpressionOneOfVisitor());

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
                                )
                        ));
            }
            return this.visitClassExpression(ctx.classExpression(0));
        }
        val op = getOperation(ctx.op);
        val left = unwrapIfSingle(this.visitClassExpression(ctx.left));
        val right = unwrapIfSingle(this.visitClassExpression(ctx.right));
        return new AggregateCondition(left, right, op);
    }
}


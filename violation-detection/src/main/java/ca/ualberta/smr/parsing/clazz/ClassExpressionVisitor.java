package ca.ualberta.smr.parsing.clazz;

import ca.ualberta.grammar.RulepadGrammarBaseVisitor;
import ca.ualberta.grammar.RulepadGrammarParser;
import ca.ualberta.smr.model.javaelements.*;
import ca.ualberta.smr.parsing.annotation.AnnotationVisitor;
import ca.ualberta.smr.parsing.field.FieldExpressionVisitor;
import ca.ualberta.smr.parsing.function.FunctionExpressionVisitor;
import lombok.val;

import java.util.Arrays;
import java.util.Collections;
import java.util.stream.Collectors;

import static ca.ualberta.smr.model.javaelements.AggregateCondition.empty;
import static ca.ualberta.smr.model.javaelements.AggregateCondition.single;
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
                val overriddenMethods = extractOverriddenFunctions(ctx.overriddenFunctions());
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
                        .orElseGet(() -> single(
                                new JavaClass(
                                        annotations,
                                        fields,
                                        methods,
                                        extension,
                                        implementation,
                                        overriddenMethods
                                )
                        ));
            }
            return this.visitClassExpression(ctx.classExpression(0));
        }
        val op = getOperation(ctx.op);
        val left = unwrapIfSingle(this.visitClassExpression(ctx.left));
        val right = unwrapIfSingle(this.visitClassExpression(ctx.right));
        return new AggregateCondition(left, right, op, ProgramElement.ProgramElementType.CLASS);
    }

    static AggregateCondition extractOverriddenFunctions(RulepadGrammarParser.OverriddenFunctionsContext ctx) {
        if (ctx == null) return empty();

        val expr = getText(ctx.combinatorialWords());

        val lparenIx = expr.indexOf('(');
        val rparenIx = expr.lastIndexOf(')');

        // ...overridden method "foobar"
        boolean noParenthesisAvailable = lparenIx == rparenIx && lparenIx == -1;
        if (noParenthesisAvailable) return single(new JavaClass.OverriddenMethod(expr.trim(), Collections.emptyList()));

        // ...overridden method "foobar(...)"
        val methodName = expr.substring(0, lparenIx);
        val paramsString = expr.substring(lparenIx + 1, rparenIx);

        // ...overridden method "foobar()"
        // ...overridden method "foobar(a)"
        // ...overridden method "foobar(a,b,...)"
        val params = Arrays.stream(paramsString.trim().split(","))
                .map(String::trim)
                .filter(s -> !s.isEmpty())
                .map(paramType -> new MethodParameter(Type.of(paramType), empty()))
                .collect(Collectors.toList());

        return single(new JavaClass.OverriddenMethod(methodName, params));
    }
}


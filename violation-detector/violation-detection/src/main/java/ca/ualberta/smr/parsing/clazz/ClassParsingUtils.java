package ca.ualberta.smr.parsing.clazz;

import ca.ualberta.grammar.RulepadGrammarParser;
import ca.ualberta.smr.model.javaelements.AggregateCondition;
import ca.ualberta.smr.model.javaelements.JavaClass;
import ca.ualberta.smr.model.javaelements.MethodParameter;
import ca.ualberta.smr.model.javaelements.Type;
import ca.ualberta.smr.parsing.annotation.AnnotationVisitor;
import ca.ualberta.smr.parsing.field.FieldExpressionVisitor;
import ca.ualberta.smr.parsing.function.FunctionExpressionVisitor;
import lombok.val;
import org.antlr.v4.runtime.ParserRuleContext;

import java.util.Arrays;
import java.util.Collections;
import java.util.stream.Collectors;

import static ca.ualberta.smr.model.javaelements.AggregateCondition.*;
import static ca.ualberta.smr.parsing.utils.CombinatorialWordsExtractorUtility.*;
import static ca.ualberta.smr.parsing.utils.GeneralUtility.*;

public class ClassParsingUtils {

    public static JavaClass createClassFromCtx(ParserRuleContext generalContext) {
        final RulepadGrammarParser.AnnotationsContext annotationsContext;
        final RulepadGrammarParser.ExtensionsContext extensionsContext;
        final RulepadGrammarParser.ImplementationsContext implementationsContext;
        final RulepadGrammarParser.OverriddenFunctionsContext overriddenFunctionsContext;
        final RulepadGrammarParser.FunctionsContext functionsContext;
        final RulepadGrammarParser.DeclarationStatementsContext declarationStatementsContext;
        final RulepadGrammarParser.BeansContext beansContext;

        if (generalContext instanceof RulepadGrammarParser.ClassExpressionContext) {
            val ctx = (RulepadGrammarParser.ClassExpressionContext) generalContext;
            annotationsContext = ctx.annotations();
            extensionsContext = ctx.extensions();
            implementationsContext = ctx.implementations();
            overriddenFunctionsContext = ctx.overriddenFunctions();
            functionsContext = ctx.functions();
            declarationStatementsContext = ctx.declarationStatements();
            beansContext = ctx.beans();
        } else if (generalContext instanceof RulepadGrammarParser.ClassExpressionAggregateContentsContext) {
            val ctx = (RulepadGrammarParser.ClassExpressionAggregateContentsContext) generalContext;
            annotationsContext = ctx.annotations();
            extensionsContext = ctx.extensions();
            implementationsContext = ctx.implementations();
            overriddenFunctionsContext = ctx.overriddenFunctions();
            functionsContext = ctx.functions();
            declarationStatementsContext = ctx.declarationStatements();
            beansContext = ctx.beans();
        } else {
            val ctx = (RulepadGrammarParser.ClassExpressionNoContext) generalContext;
            annotationsContext = ctx.annotations();
            extensionsContext = ctx.extensions();
            implementationsContext = ctx.implementations();
            overriddenFunctionsContext = ctx.overriddenFunctions();
            functionsContext = ctx.functions();
            declarationStatementsContext = ctx.declarationStatements();
            beansContext = ctx.beans();
        }

        val annotations = acceptIfAvailable(annotationsContext, new AnnotationVisitor());
        val extension = extractExtension(extensionsContext);
        val implementation = extractImplementations(implementationsContext);
        val overriddenMethods = extractOverriddenFunctions(overriddenFunctionsContext);
        val beans = extractBeanDeclaration(beansContext);
        val methods = acceptIfAvailable(functionsContext, new FunctionExpressionVisitor());
        val fields = acceptIfAvailable(declarationStatementsContext, new FieldExpressionVisitor());
        // TODO: -- constructors
        // TODO:beansFile
        // TODO:config

        return new JavaClass(
                annotations,
                fields,
                methods,
                extension,
                implementation,
                overriddenMethods,
                beans
        );
    }

    private static AggregateCondition extractOverriddenFunctions(RulepadGrammarParser.OverriddenFunctionsContext ctx) {
        if (ctx == null) return empty();

        val expr = getText(ctx.combinatorialWords());

        val lparenIx = expr.indexOf('(');
        val rparenIx = expr.lastIndexOf(')');

        // ...overridden method "foobar"
        boolean noParenthesisAvailable = lparenIx == rparenIx && lparenIx == -1;
        if (noParenthesisAvailable)
            return single(new JavaClass.OverriddenMethod(expr.trim(), Collections.emptyList()));

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

    private static AggregateCondition extractBeanDeclaration(RulepadGrammarParser.BeansContext ctx) {
        if (ctx == null) return empty();
        return single(new JavaClass.BeanDeclaration());
    }

}

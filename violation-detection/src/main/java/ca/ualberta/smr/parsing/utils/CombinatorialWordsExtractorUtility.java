package ca.ualberta.smr.parsing.utils;

import ca.ualberta.grammar.RulepadGrammarParser;
import ca.ualberta.smr.model.javaelements.AggregateCondition;
import ca.ualberta.smr.model.javaelements.Name;
import ca.ualberta.smr.model.javaelements.Type;
import ca.ualberta.smr.model.javaelements.Value;
import ca.ualberta.smr.parsing.clazz.ClassExpressionVisitor;
import lombok.val;

import java.util.Optional;

import static ca.ualberta.smr.parsing.utils.GeneralUtility.getText;
import static ca.ualberta.smr.model.javaelements.AggregateCondition.empty;

public class CombinatorialWordsExtractorUtility {

    public static AggregateCondition extractReturnType(RulepadGrammarParser.ReturnTypesContext ctx) {
        if (ctx == null) return empty();
        val combWords = ctx.returnTypeCondition().combinatorialWords();
        val typeString = getText(combWords);
        return Type.of(typeString);
    }

    public static AggregateCondition extractType(RulepadGrammarParser.TypesContext ctx) {
        if (ctx == null) return empty();
        val combWords = ctx.typeCondition().combinatorialWords();
        val typeString = getText(combWords);
        return Type.of(typeString);
    }

    public static AggregateCondition extractName(RulepadGrammarParser.NamesContext ctx) {
        if (ctx == null) return empty();
        val combWords = ctx.nameCondition().combinatorialWords();
        val nameString = getText(combWords);
        return Name.of(nameString);
    }

    public static AggregateCondition extractValue(RulepadGrammarParser.ValuesContext ctx) {
        if (ctx == null) return empty();
        val combWords = ctx.valueCondition().combinatorialWords();
        val valueString = getText(combWords);
        return Value.of(valueString);
    }

    public static AggregateCondition extractExtension(RulepadGrammarParser.ExtensionsContext ctx) {
        if (ctx == null) return empty();
        val combWords = ctx.extensionCondition().combinatorialWords();
        val extendedClass = getText(combWords);
        return Type.of(extendedClass);
    }

    public static AggregateCondition extractImplementations(RulepadGrammarParser.ImplementationsContext ctx) {
        if (ctx == null) return empty();
        val combWords = ctx.implementationCondition().combinatorialWords();
        val implementedInterface = getText(combWords);
        return Type.of(implementedInterface);
    }

    public static AggregateCondition extractEnclosingClass(RulepadGrammarParser.EnclosingClassContext ctx) {
        return Optional.ofNullable(ctx)
                .map(RulepadGrammarParser.EnclosingClassContext::classCondition)
                .map(RulepadGrammarParser.ClassConditionContext::classExpression)
                .map(expr -> expr.accept(new ClassExpressionVisitor()))
                .orElseGet(AggregateCondition::empty);
    }

}

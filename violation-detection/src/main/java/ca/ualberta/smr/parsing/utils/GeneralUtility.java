package ca.ualberta.smr.parsing.utils;

import ca.ualberta.grammar.RulepadGrammarParser;
import ca.ualberta.grammar.RulepadGrammarVisitor;
import ca.ualberta.smr.model.javaelements.AggregateCondition;
import ca.ualberta.smr.model.javaelements.AggregateConditionOperation;
import ca.ualberta.smr.model.javaelements.ProgramElement;
import org.antlr.v4.runtime.tree.ParseTree;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import java.util.Map;

import static ca.ualberta.smr.model.javaelements.AggregateCondition.empty;
import static java.lang.String.format;
import static java.util.stream.Collectors.joining;

public class GeneralUtility {

    public static AggregateConditionOperation getOperation(RulepadGrammarParser.BinaryContext ctx) {
        if (ctx.getText().trim().equals("or")) {
            return AggregateConditionOperation.OR;
        }
        return AggregateConditionOperation.AND;
    }

    public static String getText(RulepadGrammarParser.CombinatorialWordsContext words) {
        return words.getText().replace("\"", "").trim();
    }

    public static ProgramElement unwrapIfSingle(AggregateCondition condition) {
        if (condition.isSingle()) {
            return condition.getLeft(); // left and right are the same anyway
        }
        return condition;
    }

    public static AggregateCondition acceptIfAvailable(ParseTree parseTree,
                                                       RulepadGrammarVisitor<AggregateCondition> visitor) {
        if (parseTree == null) return empty();
        return parseTree.accept(visitor);
    }

    @SafeVarargs
    public static <T> List<T> listOf(T...args) {
        return new ArrayList<>(Arrays.asList(args));
    }

    public static String describe(String prefix, Map<String, AggregateCondition> keyValues) {
        return keyValues.entrySet().stream()
                .filter(entry -> !entry.getValue().isEmpty())
                .map(entry -> format("%s=[%s]", entry.getKey(), entry.getValue()))
                .collect(joining(", ", prefix + " {", "}"));
    }
}
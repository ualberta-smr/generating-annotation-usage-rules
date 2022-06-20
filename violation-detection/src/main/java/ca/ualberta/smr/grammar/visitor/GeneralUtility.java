package ca.ualberta.smr.grammar.visitor;

import ca.ualberta.grammar.RulepadGrammarParser;
import ca.ualberta.grammar.RulepadGrammarVisitor;
import ca.ualberta.smr.newmodel.javaelements.AggregateCondition;
import ca.ualberta.smr.newmodel.javaelements.AggregateConditionOperation;
import ca.ualberta.smr.newmodel.javaelements.ProgramElement;
import org.antlr.v4.runtime.tree.ParseTree;

import static ca.ualberta.smr.newmodel.javaelements.AggregateCondition.empty;

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
            return condition.getLeft(); // left and right are the same anyways
        }
        return condition;
    }

    public static AggregateCondition acceptIfAvailable(ParseTree parseTree,
                                                       RulepadGrammarVisitor<AggregateCondition> visitor) {
        if (parseTree == null) return empty();
        return parseTree.accept(visitor);
    }
}
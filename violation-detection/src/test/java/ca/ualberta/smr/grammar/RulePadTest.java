package ca.ualberta.smr.grammar;

import ca.ualberta.grammar.RulepadGrammarLexer;
import ca.ualberta.grammar.RulepadGrammarParser;
import org.antlr.v4.runtime.CharStreams;
import org.antlr.v4.runtime.CommonTokenStream;
import org.antlr.v4.runtime.tree.*;
import org.junit.jupiter.api.Test;

public class RulePadTest {

    @Test
    void hello() {
        final String rule = "field must have annotation \"Demo\" and annotation \"Hello\" ";
        final RulepadGrammarLexer lexer = new RulepadGrammarLexer(CharStreams.fromString(rule));
        final RulepadGrammarParser parser = new RulepadGrammarParser(new CommonTokenStream(lexer));
        final ParseTree tree = parser.inputSentence();

        final ParseTreeWalker walker = new ParseTreeWalker();
        final AbstractRulePadGrammarListener listener = new AbstractRulePadGrammarListener();
        walker.walk(listener, tree);
    }



}

package ca.ualberta.smr.visualize;

import ca.ualberta.grammar.RulepadGrammarLexer;
import ca.ualberta.grammar.RulepadGrammarParser;
import ca.ualberta.smr.grammar.DefaultRulePadGrammarListener;
import ca.ualberta.smr.model.StaticAnalysisRule;
import ca.ualberta.smr.rules.Rule;
import org.antlr.v4.runtime.CharStreams;
import org.antlr.v4.runtime.CommonTokenStream;
import org.antlr.v4.runtime.tree.ParseTree;
import org.antlr.v4.runtime.tree.ParseTreeWalker;
import org.junit.jupiter.api.Test;

public class DummyListenerTest {

    @Test
    void test1() {
        String input = "class with function with parameter with annotation \"PathParam\" must have annotation \"Path\" or function with annotation \"Path\" ";
        final RulepadGrammarLexer lexer = new RulepadGrammarLexer(CharStreams.fromString(input));
        final RulepadGrammarParser parser = new RulepadGrammarParser(new CommonTokenStream(lexer));
//        parser.setTrace(true);
        ParseTree tree = parser.inputSentence();
        final ParseTreeWalker walker = new ParseTreeWalker();
        final DefaultRulePadGrammarListener dasdas = new DefaultRulePadGrammarListener(new Rule());
        walker.walk(dasdas, tree);
        final StaticAnalysisRule rule = dasdas.getRule();
        System.out.println("final");
    }
}

package ca.ualberta.smr.visualize;

import ca.ualberta.grammar.RulepadGrammarLexer;
import ca.ualberta.grammar.RulepadGrammarParser;
import org.antlr.v4.gui.TreeViewer;
import org.antlr.v4.runtime.*;
import org.antlr.v4.runtime.tree.ParseTree;

import java.util.Arrays;

public class HelloTest {
    public static void main(String[] args) {
        String input = "class with (function with parameter with annotation \"PathParam\" ) must have annotation \"Path\" or function with annotation \"Path\" ";
//        String input = "function must have annotation \"A\" or annotation \"B\" ";
        final RulepadGrammarLexer lexer = new RulepadGrammarLexer(CharStreams.fromString(input));
        final RulepadGrammarParser parser = new RulepadGrammarParser(new CommonTokenStream(lexer));
//        parser.setTrace(true);
        final ParseTree tree = parser.inputSentence();

        System.out.println(tree.toStringTree(parser));
        //show AST in GUI
        TreeViewer viewr = new TreeViewer(Arrays.asList(
                parser.getRuleNames()),tree);
        viewr.open();
    }
}
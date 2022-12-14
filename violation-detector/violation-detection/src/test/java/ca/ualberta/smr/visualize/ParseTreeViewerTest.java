package ca.ualberta.smr.visualize;

import ca.ualberta.grammar.RulepadGrammarLexer;
import ca.ualberta.grammar.RulepadGrammarParser;
import org.antlr.v4.gui.TreeViewer;
import org.antlr.v4.runtime.*;
import org.antlr.v4.runtime.tree.ParseTree;

import java.util.Arrays;

/**
 * The whole purpose of this "test" is to visualize the parse tree of a RulePad rule
 */
public class ParseTreeViewerTest {

    public static void main(String[] args) {
        String input = "class with annotation \"A\" must have none of (annotation \"B\" or annotation \"C\" ) ";
        final RulepadGrammarLexer lexer = new RulepadGrammarLexer(CharStreams.fromString(input));
        final RulepadGrammarParser parser = new RulepadGrammarParser(new CommonTokenStream(lexer));
//        parser.setTrace(true);
        final ParseTree tree = parser.start();
        System.out.println(tree.toStringTree(parser));
        //show AST in GUI
        TreeViewer viewr = new TreeViewer(Arrays.asList(parser.getRuleNames()),tree);
        viewr.open();
    }

}


















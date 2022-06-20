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
//        String input = "class with (function with parameter with annotation \"PathParam\" ) must have annotation \"Path\" or function with annotation \"Path\" ";
//        String input = "function must have annotation \"A\" or annotation \"B\" ";
//        String input = "class with annotation \"A\" must have function with annotation \"B\" or annotation \"C\" ";
//        String input = "class with annotation \"A\" must have function with (annotation \"B\" or annotation \"C\" ) ";

//        String input = "class with annotation \"A\" must have (function with annotation \"B\" or annotation \"C\" " +
//                "or annotation \"D\" ) or (field with type \"X\" or type \"Y\" ) or (annotation \"M\" or annotation \"L\" ) ";

//        String input = "class with annotation \"A\" must have function with annotation \"B\" or annotation \"C\" or annotation \"D\" ";
//        String input = "class with function with annotation \"O\" or annotation \"I\" must have annotation \"A\" or annotation \"D\" ";
//        String input = "class with annotation \"A\" must have function with (annotation \"B\" or annotation \"C\" ) or annotation \"D\" ";
        String input = "field with type \"B\" or annotation \"D\" must have annotation \"B\" or annotation \"C\" or annotation \"D\" ";
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


















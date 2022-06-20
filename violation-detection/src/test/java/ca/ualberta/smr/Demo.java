package ca.ualberta.smr;


import ca.ualberta.grammar.RulepadGrammarLexer;
import ca.ualberta.grammar.RulepadGrammarParser;
import ca.ualberta.smr.grammar.visitor.DefaultRulePadGrammarVisitor;
import ca.ualberta.smr.newmodel.StaticAnalysisRule;
import org.antlr.v4.runtime.CharStream;
import org.antlr.v4.runtime.CharStreams;
import org.antlr.v4.runtime.CommonTokenStream;

import java.io.IOException;

public class Demo {

    public static void main(String[] args) throws IOException {
        String input = "method with annotation \"D\" must have annotation \"B\" or annotation \"C\" or annotation \"Z\" ";
        input = "field with annotation \"A\" and none of (annotation \"B\" or annotation \"C\" or annotation \"D\" ) must have annotation \"E\" ";
//        input = "method with annotation \"A\" and one of (annotation \"B\" or annotation \"C\" or annotation \"D\" ) must have annotation \"E\" ";
//        input = "method with annotation \"A\" and no annotation \"B\" must have annotation \"E\" ";
        CharStream stream = CharStreams.fromString(input);
        RulepadGrammarLexer lexer = new RulepadGrammarLexer(stream);
        CommonTokenStream commonTokenStream = new CommonTokenStream(lexer);
        RulepadGrammarParser rulepadGrammarParser = new RulepadGrammarParser(commonTokenStream);

        DefaultRulePadGrammarVisitor v = new DefaultRulePadGrammarVisitor("dasda", "dasdasd");

        StaticAnalysisRule visit = v.visitMustClause(rulepadGrammarParser.inputSentence().mustClause());

        System.out.println(visit);
    }

}



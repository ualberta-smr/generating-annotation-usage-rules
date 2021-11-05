package ca.ualberta.smr.rules;

import ca.ualberta.grammar.RulepadGrammarLexer;
import ca.ualberta.grammar.RulepadGrammarParser;
import ca.ualberta.smr.grammar.DefaultRulePadGrammarListener;
import ca.ualberta.smr.model.StaticAnalysisRule;
import com.fasterxml.jackson.databind.ObjectMapper;
import org.antlr.v4.runtime.CharStreams;
import org.antlr.v4.runtime.CommonTokenStream;
import org.antlr.v4.runtime.tree.ParseTree;
import org.antlr.v4.runtime.tree.ParseTreeWalker;

import java.io.IOException;
import java.io.InputStream;
import java.util.Collection;
import java.util.stream.Collectors;

public class RuleParser {

    public static Collection<StaticAnalysisRule> parseRules(InputStream stream) throws IOException {
        return doParseRules(stream).getRules()
                .stream()
                .map(r -> {
                    final RulepadGrammarLexer lexer = new RulepadGrammarLexer(CharStreams.fromString(r.getSpecification()));
                    final RulepadGrammarParser parser = new RulepadGrammarParser(new CommonTokenStream(lexer));
                    final ParseTree tree = parser.inputSentence();

                    final ParseTreeWalker walker = new ParseTreeWalker();
//                    final ConcreteRulePadGrammarListener listener = new ConcreteRulePadGrammarListener(r);
                    final DefaultRulePadGrammarListener listener = new DefaultRulePadGrammarListener(r);

                    walker.walk(listener, tree);

                    return listener.getRule();
                }).collect(Collectors.toList());
    }

    private static Rules doParseRules(InputStream stream) throws IOException {
        final ObjectMapper objectMapper = new ObjectMapper();
        return objectMapper.readValue(stream, Rules.class);
    }

}

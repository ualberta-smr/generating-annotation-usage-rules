package ca.ualberta.smr.parsing.rules;

import ca.ualberta.grammar.RulepadGrammarLexer;
import ca.ualberta.grammar.RulepadGrammarParser;
import ca.ualberta.smr.parsing.DefaultRulePadGrammarVisitor;
import ca.ualberta.smr.model.StaticAnalysisRule;
import com.fasterxml.jackson.databind.ObjectMapper;
import lombok.val;
import org.antlr.v4.runtime.CharStreams;
import org.antlr.v4.runtime.CommonTokenStream;

import java.io.IOException;
import java.io.InputStream;
import java.util.Collection;

import static java.util.stream.Collectors.toList;

public class RuleParser {

    /**
     * Given an input stream of a correct json file with a collection of RulePad rules, this function returns <br>
     * a collection of rules that are represented in the internal representation.
     * @param stream InputStream of a correct json file
     * @return a collection of rules in the internal format.
     * @throws IOException when the input stream is invalid.
     */
    public static Collection<StaticAnalysisRule> parseRules(InputStream stream) throws IOException {
        return doParseRules(stream).getRules().stream()
                .map(RuleParser::parseRule)
                .collect(toList());
    }

    private static Rules doParseRules(InputStream stream) throws IOException {
        return OBJECT_MAPPER.readValue(stream, Rules.class);
    }

    public static StaticAnalysisRule parseRule(Rule rule) {
        val lexer = new RulepadGrammarLexer(CharStreams.fromString(rule.getSpecification()));
        val parser = new RulepadGrammarParser(new CommonTokenStream(lexer));
        val tree = parser.start();
        val visitor = new DefaultRulePadGrammarVisitor(rule.getId(), rule.getSpecification());
        return visitor.visit(tree);
    }

    private static final ObjectMapper OBJECT_MAPPER = new ObjectMapper();

}

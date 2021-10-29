package ca.ualberta.smr.rules;

import ca.ualberta.smr.model.StaticAnalysisRule;
import org.junit.jupiter.api.Test;

import java.io.IOException;
import java.io.InputStream;
import java.util.Collection;

class RuleParserTest {
    @Test
    void test() throws IOException {
        final InputStream is = RuleParserTest.class.getResourceAsStream("/rules.json");
        final Collection<StaticAnalysisRule> vvv = RuleParser.parseRules(is);
        System.out.println(vvv);
    }
}
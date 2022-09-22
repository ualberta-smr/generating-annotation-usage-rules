package ca.ualberta;

import ca.ualberta.smr.model.StaticAnalysisRule;
import ca.ualberta.smr.parsing.rules.RuleParser;
import lombok.SneakyThrows;

import java.util.Collection;

public class RuleProvider {

    private final String rulesFile;

    public RuleProvider(String rulesFile) {
        this.rulesFile = rulesFile;
    }

    @SneakyThrows
    public Collection<StaticAnalysisRule> getRules() {
        return RuleParser.parseRules(
                RuleProvider.class.getResourceAsStream(this.rulesFile));
    }
}

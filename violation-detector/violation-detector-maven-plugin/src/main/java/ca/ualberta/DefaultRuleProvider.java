package ca.ualberta;

import ca.ualberta.smr.model.StaticAnalysisRule;
import ca.ualberta.smr.parsing.rules.RuleParser;
import lombok.SneakyThrows;

import javax.inject.Named;
import javax.inject.Singleton;
import java.util.Collection;

@Named
@Singleton
public class DefaultRuleProvider implements RuleProvider {

    @Override
    @SneakyThrows
    public Collection<StaticAnalysisRule> getRules() {
        return RuleParser.parseRules(
                DefaultRuleProvider.class.getResourceAsStream("/rules.json"));
    }
}

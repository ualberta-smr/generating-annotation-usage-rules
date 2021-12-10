package ca.ualberta;

import ca.ualberta.smr.model.StaticAnalysisRule;

import java.util.Collection;

public interface RuleProvider {

    Collection<StaticAnalysisRule> getRules();

}

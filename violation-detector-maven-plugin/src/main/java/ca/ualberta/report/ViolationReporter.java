package ca.ualberta.report;

import ca.ualberta.smr.model.StaticAnalysisRule;
import ca.ualberta.smr.model.violationreport.ViolationCombination;

import java.util.Collection;
import java.util.function.Consumer;

public interface ViolationReporter {

    void report(StaticAnalysisRule rule, Collection<ViolationCombination> violation, Consumer<String> logger);

}

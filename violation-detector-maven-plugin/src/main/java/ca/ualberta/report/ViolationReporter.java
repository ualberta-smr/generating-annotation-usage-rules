package ca.ualberta.report;

import ca.ualberta.FileStaticAnalysisRulePair;
import ca.ualberta.smr.model.StaticAnalysisRule;

import java.util.Collection;
import java.util.function.Consumer;

public interface ViolationReporter {

    void report(StaticAnalysisRule rule, Collection<FileStaticAnalysisRulePair> violations, Consumer<String> logger);

}

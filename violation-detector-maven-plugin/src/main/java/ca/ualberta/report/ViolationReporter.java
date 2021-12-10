package ca.ualberta.report;

import ca.ualberta.smr.model.StaticAnalysisRule;
import ca.ualberta.smr.model.ViolationInfo;

import java.util.Collection;

public interface ViolationReporter {

    void report(StaticAnalysisRule rule, Collection<ViolationInfo> violation);

}

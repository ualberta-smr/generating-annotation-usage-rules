package ca.ualberta.report;

import ca.ualberta.smr.model.ViolationInfo;

public interface ViolationReporter {

    void report(ViolationInfo violation);

}

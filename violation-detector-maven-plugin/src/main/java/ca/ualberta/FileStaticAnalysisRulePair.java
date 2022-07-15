package ca.ualberta;

import ca.ualberta.smr.model.StaticAnalysisRule;
import ca.ualberta.smr.model.violationreport.ViolationCombination;
import lombok.AllArgsConstructor;

import java.util.Collection;

@AllArgsConstructor
public class FileStaticAnalysisRulePair {
    public String path;
    public StaticAnalysisRule rule;
    public Collection<ViolationCombination> misuses;
}

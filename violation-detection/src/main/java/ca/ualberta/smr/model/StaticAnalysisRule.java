package ca.ualberta.smr.model;

import ca.ualberta.smr.model.javaelements.AnalysisItem;
import lombok.Getter;
import lombok.RequiredArgsConstructor;
import lombok.experimental.Accessors;

@RequiredArgsConstructor
@Getter
@Accessors(fluent = true)
public class StaticAnalysisRule {

    private final AnalysisItem antecedent;
    private final AnalysisItem consequent;

}

package ca.ualberta.smr.model;

import ca.ualberta.smr.model.javaelements.*;
import lombok.Getter;
import lombok.RequiredArgsConstructor;
import lombok.experimental.Accessors;

@RequiredArgsConstructor
@Accessors(fluent = true)
@Getter
public class StaticAnalysisRule {
    private final String name;
    private final AnalysisItem antecedent;
    private final Condition<? extends AnalysisItem> consequent;

    @Override
    public String toString() {
        return name;
    }
}

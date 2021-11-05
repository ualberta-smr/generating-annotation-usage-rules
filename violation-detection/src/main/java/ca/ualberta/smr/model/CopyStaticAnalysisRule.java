package ca.ualberta.smr.model;

import ca.ualberta.smr.model.javaelements.AnalysisItem;
import ca.ualberta.smr.model.javaelements.Condition;
import lombok.EqualsAndHashCode;
import lombok.Getter;
import lombok.RequiredArgsConstructor;
import lombok.experimental.Accessors;

@RequiredArgsConstructor
@Accessors(fluent = true)
@Getter
@EqualsAndHashCode
public class CopyStaticAnalysisRule {
    private final String name;
    private final Condition<? extends AnalysisItem> antecedent;
    private final Condition<? extends AnalysisItem> consequent;
    private final String description;

    @Override
    public String toString() {
        return name;
    }
}

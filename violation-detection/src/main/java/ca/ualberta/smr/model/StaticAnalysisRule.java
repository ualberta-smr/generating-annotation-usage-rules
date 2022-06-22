package ca.ualberta.smr.model;

import ca.ualberta.smr.model.javaelements.AggregateCondition;
import lombok.EqualsAndHashCode;
import lombok.Getter;
import lombok.RequiredArgsConstructor;
import lombok.experimental.Accessors;

@RequiredArgsConstructor
@Accessors(fluent = true)
@Getter
@EqualsAndHashCode
public class StaticAnalysisRule {
    private final String name;
    private final AggregateCondition antecedent;
    private final AggregateCondition consequent;
    private final String description;

    @Override
    public String toString() {
        return name;
    }
}

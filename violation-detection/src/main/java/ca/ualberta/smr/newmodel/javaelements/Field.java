package ca.ualberta.smr.newmodel.javaelements;

import lombok.EqualsAndHashCode;
import lombok.Getter;
import lombok.RequiredArgsConstructor;
import lombok.experimental.Accessors;

@Getter
@RequiredArgsConstructor
@Accessors(fluent = true)
@EqualsAndHashCode
public final class Field implements AnalysisItem, ProgramElement {
    private final AggregateCondition type;
    private final AggregateCondition annotations;

    @Override
    public String toString() {
        return "Field{" +
                "type=" + type.toString() +
                ", annotations=" + annotations.toString() +
                '}';
    }
}
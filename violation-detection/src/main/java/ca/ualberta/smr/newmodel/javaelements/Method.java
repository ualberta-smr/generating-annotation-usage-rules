package ca.ualberta.smr.newmodel.javaelements;

import lombok.*;
import lombok.experimental.Accessors;

import java.util.ArrayList;
import java.util.Collection;

@Getter
@RequiredArgsConstructor
@Accessors(fluent = true)
@EqualsAndHashCode
public final class Method implements AnalysisItem, ProgramElement {
    private final AggregateCondition returnType;
    private final AggregateCondition annotations;
    private final AggregateCondition parameters;

    @Override
    public String toString() {
        return "Method{" +
                "returnType=" + returnType.toString() +
                ", annotations=" + annotations.toString() +
                ", parameters=" + parameters.toString() +
                '}';
    }
}
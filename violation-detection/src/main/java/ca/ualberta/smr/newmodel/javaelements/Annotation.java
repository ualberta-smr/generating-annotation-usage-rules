package ca.ualberta.smr.newmodel.javaelements;

import lombok.EqualsAndHashCode;
import lombok.Getter;
import lombok.RequiredArgsConstructor;
import lombok.experimental.Accessors;

@Getter
@Accessors(fluent = true)
@EqualsAndHashCode
@RequiredArgsConstructor
public class Annotation implements ProgramElement {
    private final AggregateCondition type;
    private final AggregateCondition parameters;

    @Override
    public String toString() {
        String minimal = String.format("@%s", type.toString());
        if (parameters.isEmpty()) {
            return minimal;
        }
        return minimal + "(" + parameters.toString() + ")";
    }
}
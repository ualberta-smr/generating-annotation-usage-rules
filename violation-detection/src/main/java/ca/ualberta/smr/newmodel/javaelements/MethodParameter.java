package ca.ualberta.smr.newmodel.javaelements;

import lombok.EqualsAndHashCode;
import lombok.Getter;
import lombok.RequiredArgsConstructor;
import lombok.experimental.Accessors;

@Getter
@RequiredArgsConstructor
@Accessors(fluent = true)
@EqualsAndHashCode
public class MethodParameter implements ProgramElement {
    private final AggregateCondition type;
    private final AggregateCondition annotations;

    @Override
    public String toString() {
        return "MethodParameter{" +
                "type=" + type.toString() +
                ", annotations=" + annotations.toString() +
                '}';
    }
}
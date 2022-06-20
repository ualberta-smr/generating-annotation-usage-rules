package ca.ualberta.smr.newmodel.javaelements;

import lombok.EqualsAndHashCode;
import lombok.Getter;
import lombok.RequiredArgsConstructor;
import lombok.experimental.Accessors;

@RequiredArgsConstructor
@Getter
@Accessors(fluent = true)
@EqualsAndHashCode
public class Value implements ProgramElement {
    private final String name;

    public static AggregateCondition of(String name) {
        return AggregateCondition.single(new Value(name));
    }

    @Override
    public String toString() {
        return name;
    }

}

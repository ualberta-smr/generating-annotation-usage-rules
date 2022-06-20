package ca.ualberta.smr.model.javaelements;

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

    public static Condition<Value> of(String name) {
        return Condition.single(new Value(name));
    }

    public boolean equalsValueString(String name) {
        return this.name.equals(name);
    }

    public boolean isEmpty() {
        return this == EMPTY_VALUE;
    }

    @Override
    public String toString() {
        return name;
    }

    public static final Value EMPTY_VALUE = new Value("__VALUE__");
}

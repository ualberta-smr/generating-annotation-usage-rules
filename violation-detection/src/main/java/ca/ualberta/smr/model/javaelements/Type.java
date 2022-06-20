package ca.ualberta.smr.model.javaelements;

import lombok.EqualsAndHashCode;
import lombok.Getter;
import lombok.RequiredArgsConstructor;
import lombok.experimental.Accessors;

@RequiredArgsConstructor
@Getter
@Accessors(fluent = true)
@EqualsAndHashCode
public class Type implements ProgramElement {
    private final String name;

    public static Condition<Type> type(String name) {
        return Condition.single(new Type(name));
    }

    public static Condition<Type> of(String name) {
        return Condition.single(new Type(name));
    }

    public boolean equalsTypeString(String typeString) {
        return typeString.equals(name);
    }

    public boolean isEmpty() {
        return this == EMPTY_TYPE;
    }

    @Override
    public String toString() {
        return name;
    }

    public static final Type EMPTY_TYPE = new Type("__EMPTY__");
}
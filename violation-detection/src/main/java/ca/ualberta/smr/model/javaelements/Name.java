package ca.ualberta.smr.model.javaelements;

import lombok.EqualsAndHashCode;
import lombok.Getter;
import lombok.RequiredArgsConstructor;
import lombok.experimental.Accessors;

@RequiredArgsConstructor
@Getter
@Accessors(fluent = true)
@EqualsAndHashCode
public class Name implements ProgramElement {
    private final String name;

    public static Condition<Name> of(String name) {
        return Condition.single(new Name(name));
    }

    public boolean equalsNameString(String name) {
        return this.name.equals(name);
    }

    public boolean isEmpty() {
        return this == EMPTY_NAME;
    }

    @Override
    public String toString() {
        return name;
    }

    public static final Name EMPTY_NAME = new Name("__NAME__");
}

package ca.ualberta.smr.model.javaelements;

import lombok.Getter;
import lombok.RequiredArgsConstructor;
import lombok.experimental.Accessors;

@RequiredArgsConstructor
@Getter
@Accessors(fluent = true)
public class Type {
    private final String name;

    public static Condition<Type> type(String name) {
        return Condition.single(new Type(name));
    }

    public boolean equalsTypeString(String typeString) {
        return typeString.equals(name);
    }

    @Override
    public String toString() {
        return name;
    }
}
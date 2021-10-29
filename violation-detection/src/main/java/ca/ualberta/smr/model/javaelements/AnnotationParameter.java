package ca.ualberta.smr.model.javaelements;

import lombok.EqualsAndHashCode;
import lombok.Getter;
import lombok.RequiredArgsConstructor;
import lombok.experimental.Accessors;

import static ca.ualberta.smr.utils.Utils.listOf;

@Getter
@Accessors(fluent = true)
@RequiredArgsConstructor
@EqualsAndHashCode
public class AnnotationParameter implements ProgramElement{

    private final Condition<Type> type = Condition.empty(Type.class);
    private final String name;

    @Override
    public String toString() {
        String t = type.toString();
        String n = name == null ? "" : name;
        return String.join(" ", listOf(t, n));
    }

}

package ca.ualberta.smr.model.javaelements;

import lombok.Getter;
import lombok.RequiredArgsConstructor;
import lombok.experimental.Accessors;

import static ca.ualberta.smr.utils.Utils.listOf;

@Getter
@Accessors(fluent = true)
@RequiredArgsConstructor
public class AnnotationParameter implements ProgramElement{

    private final Type type;
    private final String name;

    @Override
    public String toString() {
        String t = type.name();
        String n = name == null ? "" : name;
        return String.join(" ", listOf(t, n));
    }

}

package ca.ualberta.smr.model.javaelements;

import lombok.Builder;
import lombok.Getter;
import lombok.experimental.Accessors;

import static ca.ualberta.smr.utils.Utils.listOf;

@Builder
@Getter
@Accessors(fluent = true)
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

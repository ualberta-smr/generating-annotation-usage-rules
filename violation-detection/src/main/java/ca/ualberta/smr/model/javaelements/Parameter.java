package ca.ualberta.smr.model.javaelements;

import lombok.Builder;
import lombok.Getter;
import lombok.experimental.Accessors;

import java.util.ArrayList;
import java.util.Collection;
import java.util.List;

import static ca.ualberta.smr.utils.Utils.listOf;

@Builder
@Getter
@Accessors(fluent = true)
public class Parameter implements ProgramElement{
    private final Type type;
    private final String name;
    @Builder.Default
    private final Collection<Condition<Annotation>> annotations = new ArrayList<>();

    @Override
    public String toString() {
        String t = type.name();
        String n = name == null ? "" : name;
        return String.join(" ", listOf(t, n));
    }
}
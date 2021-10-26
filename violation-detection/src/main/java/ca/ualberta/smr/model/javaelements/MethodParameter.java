package ca.ualberta.smr.model.javaelements;

import lombok.Getter;
import lombok.Setter;
import lombok.experimental.Accessors;

import java.util.ArrayList;
import java.util.Collection;
import java.util.stream.Collectors;

import static ca.ualberta.smr.utils.Utils.listOf;

@Getter
@Setter
@Accessors(fluent = true)
public class MethodParameter implements ProgramElement{
    private Type type = Type.EMPTY_TYPE;
    private final Collection<Condition<Annotation>> annotations = new ArrayList<>();

    @Override
    public String toString() {
        String typeString = type == Type.EMPTY_TYPE ? "__" : type.name();
        String annotationString = annotations.stream()
                .map(Condition::toString)
                .collect(Collectors.joining(", "));
        return String.join(" ", listOf(annotationString, typeString));
    }
}
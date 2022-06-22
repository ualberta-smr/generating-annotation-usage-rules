package ca.ualberta.smr.deprecated.model.javaelements;

import lombok.EqualsAndHashCode;
import lombok.Getter;
import lombok.Setter;
import lombok.experimental.Accessors;

import java.util.ArrayList;
import java.util.Collection;
import java.util.stream.Collectors;

import static ca.ualberta.smr.parsing.utils.GeneralUtility.listOf;

@Getter
@Setter
@Accessors(fluent = true)
@EqualsAndHashCode
public class MethodParameter implements ProgramElement, WithAnnotation, WithType {
    private Condition<Type> type = Condition.empty(Type.class);
    private final Collection<Condition<Annotation>> annotations = new ArrayList<>();

    public void type(Condition<Type> type) {
        this.type = type;
    }

    @Override
    public String toString() {
        String typeString = type.isNotEmpty() ? type.toString() : "__";
        String annotationString = annotations.stream()
                .map(Condition::toString)
                .collect(Collectors.joining(", "));
        return String.join(" ", listOf(annotationString, typeString));
    }
}
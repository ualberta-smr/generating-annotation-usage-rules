package ca.ualberta.smr.model.javaelements;

import lombok.EqualsAndHashCode;
import lombok.Getter;
import lombok.Setter;
import lombok.experimental.Accessors;

import java.util.ArrayList;
import java.util.Collection;

@Getter
@Setter
@Accessors(fluent = true)
@EqualsAndHashCode
public class Annotation implements ProgramElement {
    private Condition<Type> type = Condition.empty(Type.class);
    private Collection<Condition<AnnotationParameter>> parameters = new ArrayList<>();

    public static Annotation annotation(String typeName) {
        final Annotation annotation = new Annotation();
        annotation.type(Type.type(typeName));
        return annotation;
    }

    @Override
    public String toString() {
        return String.format("@%s", type.toString());
    }
}

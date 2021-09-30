package ca.ualberta.smr.model.javaelements;

import lombok.Builder;
import lombok.Getter;
import lombok.experimental.Accessors;

import java.util.ArrayList;
import java.util.Collection;

@Builder
@Getter
@Accessors(fluent = true)
public class Annotation {
    @Builder.Default
    private final Condition<Type> type = Condition.empty();
    @Builder.Default
    private final Collection<Condition<AnnotationParameter>> parameters = new ArrayList<>();

    public static Annotation annotation(String typeName) {
        return Annotation.builder()
                .type(Type.type(typeName))
                .build();
    }

    @Override
    public String toString() {
        return String.format("@%s", type.toString());
    }
}

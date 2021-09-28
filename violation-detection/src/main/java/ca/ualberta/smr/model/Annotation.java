package ca.ualberta.smr.model;

import lombok.Builder;
import lombok.Getter;
import lombok.experimental.Accessors;

import java.util.ArrayList;
import java.util.Collection;

@Builder
@Getter
@Accessors(fluent = true)
public class Annotation {
    private final Type type;
    private final Collection<AnnotationParameter> parameters = new ArrayList<>();

    public static Annotation annotation(String type) {
        return Annotation.builder()
                .type(new Type(type)).build();
    }

    @Override
    public String toString() {
        return String.format("@%s", type.name());
    }
}

package ca.ualberta.smr.model;

import lombok.Builder;
import lombok.Getter;
import lombok.experimental.Accessors;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.Collection;
import java.util.List;
import java.util.stream.Collectors;

@Builder
@Getter
@Accessors(fluent = true)
public class Parameter {
    private final Type type;
    private final String name;
    @Builder.Default
    private final Collection<Annotation> annotations = new ArrayList<>();

    @Override
    public String toString() {
        String t = type.name();
        String n = name == null ? "" : name;
        return String.join(" ", List.of(t, n));
    }
}
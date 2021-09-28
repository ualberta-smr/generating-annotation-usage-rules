package ca.ualberta.smr.model;

import lombok.Builder;
import lombok.Getter;
import lombok.ToString;
import lombok.experimental.Accessors;

import java.util.ArrayList;
import java.util.Collection;

@Builder
@Getter
@Accessors(fluent = true)
@ToString
public final class Method implements AnalysisItem{
    private final Type returnType;
    @Builder.Default
    private final Collection<Annotation> annotations = new ArrayList<>();
    @Builder.Default
    private final Collection<Parameter> parameters = new ArrayList<>();
}
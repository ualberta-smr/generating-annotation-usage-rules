package ca.ualberta.smr.model.javaelements;

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
public final class Method implements AnalysisItem, ProgramElement {
    @Builder.Default
    private final Condition<Type> returnType = Condition.empty(Type.class);
    @Builder.Default
    private final Collection<Condition<Annotation>> annotations = new ArrayList<>();
    @Builder.Default
    private final Collection<Condition<Parameter>> parameters = new ArrayList<>();
}
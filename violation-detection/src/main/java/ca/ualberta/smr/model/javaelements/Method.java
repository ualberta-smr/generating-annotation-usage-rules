package ca.ualberta.smr.model.javaelements;

import lombok.EqualsAndHashCode;
import lombok.Getter;
import lombok.Setter;
import lombok.ToString;
import lombok.experimental.Accessors;

import java.util.ArrayList;
import java.util.Collection;

@Getter
@Setter
@Accessors(fluent = true)
@ToString
@EqualsAndHashCode
public final class Method implements AnalysisItem, ProgramElement, WithAnnotation {
    private Condition<Type> returnType = Condition.empty(Type.class);
    private final Collection<Condition<Annotation>> annotations = new ArrayList<>();
    private final Collection<Condition<MethodParameter>> parameters = new ArrayList<>();
}
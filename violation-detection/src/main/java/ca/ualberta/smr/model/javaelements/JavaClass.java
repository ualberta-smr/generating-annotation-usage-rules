package ca.ualberta.smr.model.javaelements;

import lombok.Builder;
import lombok.Getter;
import lombok.experimental.Accessors;

import java.util.ArrayList;
import java.util.Collection;

@Builder
@Getter
@Accessors(fluent = true)
public final class JavaClass implements AnalysisItem{
    @Builder.Default
    private Condition<Field> field = Condition.empty();
    @Builder.Default
    private Condition<Method> method = Condition.empty();
    @Builder.Default
    private Collection<Condition<Annotation>> annotations = new ArrayList<>();
    @Builder.Default
    private Condition<Type> extendedClass = Condition.empty();
    @Builder.Default
    private Collection<Condition<Type>> implementedInterfaces = new ArrayList<>();
    // TODO: support for configuration files
    // TODO: support for constructors (that actually can be treated like methods)
}
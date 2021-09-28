package ca.ualberta.smr.model;

import lombok.Builder;
import lombok.Getter;
import lombok.experimental.Accessors;

import java.util.ArrayList;
import java.util.Collection;

@Builder
@Getter
@Accessors(fluent = true)
public final class JavaClass implements AnalysisItem{
    private Field field;
    private Method method;
    @Builder.Default
    private Collection<Annotation> annotations = new ArrayList<>();
    private Type extendedClass;
    @Builder.Default
    private Collection<Type> implementedInterfaces = new ArrayList<>();
    // TODO: support for configuration files
    // TODO: support for constructors (that actually can be treated like methods)
}
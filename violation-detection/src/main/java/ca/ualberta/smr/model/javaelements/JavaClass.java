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
@EqualsAndHashCode
@ToString
public final class JavaClass implements AnalysisItem, ProgramElement, WithAnnotation {
    private Condition<Field> field = Condition.empty(Field.class);
    private Condition<Method> method = Condition.empty(Method.class);
    private Collection<Condition<Annotation>> annotations = new ArrayList<>();
    private Condition<Type> extendedClass = Condition.empty(Type.class);
    private Collection<Condition<Type>> implementedInterfaces = new ArrayList<>();
    // TODO: support for configuration files
    // TODO: support for constructors (that actually can be treated like methods)
}
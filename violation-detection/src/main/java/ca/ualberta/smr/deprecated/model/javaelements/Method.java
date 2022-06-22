package ca.ualberta.smr.deprecated.model.javaelements;

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
public final class Method implements AnalysisItem, ProgramElement, WithAnnotation, WithType {
    private Condition<Type> returnType = Condition.empty(Type.class);
    private final Collection<Condition<Annotation>> annotations = new ArrayList<>();
    private final Collection<Condition<MethodParameter>> parameters = new ArrayList<>();

    /**
     * It's an alias for returnType(...)
     */
    @Override
    public void type(Condition<Type> newType) {
        this.returnType = newType;
    }
}
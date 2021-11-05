package ca.ualberta.smr.model.javaelements;

import lombok.EqualsAndHashCode;
import lombok.Getter;
import lombok.Setter;
import lombok.experimental.Accessors;

import java.util.ArrayList;
import java.util.Collection;

@Getter
@Setter
@Accessors(fluent = true)
@EqualsAndHashCode
public final class Field implements AnalysisItem, ProgramElement, WithAnnotation, WithType {
    private Condition<Type> type = Condition.empty(Type.class);
    private Collection<Condition<Annotation>> annotations = new ArrayList<>();

    public void type(Condition<Type> type) {
        this.type = type;
    }

    @Override
    public String toString() {
        return "Field{" +
                "type=" + type +
                ", annotations=" + annotations +
                '}';
    }
}

package ca.ualberta.smr.model.javaelements;

import lombok.Getter;
import lombok.Setter;
import lombok.experimental.Accessors;

import java.util.ArrayList;
import java.util.Collection;

@Getter
@Setter
@Accessors(fluent = true)
public final class Field implements AnalysisItem, ProgramElement {
    private Condition<Type> type = Condition.empty(Type.class);
    private Collection<Condition<Annotation>> annotations = new ArrayList<>();

    @Override
    public String toString() {
        return "Field{" +
                "type=" + type +
                ", annotations=" + annotations +
                '}';
    }
}

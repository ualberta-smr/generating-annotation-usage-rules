package ca.ualberta.smr.model.javaelements;

import lombok.Builder;
import lombok.Getter;
import lombok.experimental.Accessors;

import java.util.ArrayList;
import java.util.Collection;

@Builder
@Getter
@Accessors(fluent = true)
public final class Field implements AnalysisItem, ProgramElement {
    @Builder.Default
    private final Condition<Type> type = Condition.empty(Type.class);
    @Builder.Default
    private final Collection<Condition<Annotation>> annotations = new ArrayList<>();

    @Override
    public String toString() {
        return "Field{" +
                "type=" + type +
                ", annotations=" + annotations +
                '}';
    }
}

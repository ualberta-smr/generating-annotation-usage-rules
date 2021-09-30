package ca.ualberta.smr.model.javaelements;

import lombok.Builder;
import lombok.Getter;
import lombok.experimental.Accessors;

import java.util.ArrayList;
import java.util.Collection;

@Builder
@Getter
@Accessors(fluent = true)
public final class Field implements AnalysisItem {
    @Builder.Default
    private final Condition<Type> type = Condition.empty();
    @Builder.Default
    private final Collection<Condition<Annotation>> annotations = new ArrayList<>();
}

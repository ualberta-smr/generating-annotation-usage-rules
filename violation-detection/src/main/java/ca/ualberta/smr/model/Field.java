package ca.ualberta.smr.model;

import lombok.Builder;
import lombok.Getter;
import lombok.experimental.Accessors;

import java.util.ArrayList;
import java.util.Collection;

@Builder
@Getter
@Accessors(fluent = true)
public final class Field implements AnalysisItem {
    private final Type type;
    private final Collection<Annotation> annotations = new ArrayList<>();
}

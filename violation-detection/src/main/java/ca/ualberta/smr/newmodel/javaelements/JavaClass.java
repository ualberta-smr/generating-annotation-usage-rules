package ca.ualberta.smr.newmodel.javaelements;

import lombok.EqualsAndHashCode;
import lombok.Getter;
import lombok.RequiredArgsConstructor;
import lombok.ToString;
import lombok.experimental.Accessors;

@Getter
@RequiredArgsConstructor
@Accessors(fluent = true)
@EqualsAndHashCode
@ToString
public final class JavaClass implements AnalysisItem, ProgramElement {
    private final AggregateCondition annotations;
    private final AggregateCondition field;
    private final AggregateCondition method;
    private final AggregateCondition extendedClass;
    private final AggregateCondition implementedInterfaces;
    // TODO: support for configuration files
    // TODO: support for constructors (that actually can be treated like methods)
}

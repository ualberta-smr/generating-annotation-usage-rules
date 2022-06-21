package ca.ualberta.smr.newmodel.javaelements;

import ca.ualberta.smr.newmodel.ViolationCombination;
import ca.ualberta.smr.newmodel.ViolationInfo;
import lombok.EqualsAndHashCode;
import lombok.Getter;
import lombok.RequiredArgsConstructor;
import lombok.experimental.Accessors;

import java.util.Collection;

import static java.util.Collections.emptyList;
import static java.util.Collections.singleton;

@RequiredArgsConstructor
@Getter
@Accessors(fluent = true)
@EqualsAndHashCode(callSuper = false)
public class Value extends ProgramElement {
    private final String expr;

    public static AggregateCondition of(String name) {
        return AggregateCondition.single(new Value(name));
    }

    @Override
    public boolean matches(Object bd) {
        String valueExpression = (String) bd;
        return expr.equals(valueExpression);
    }

    @Override
    public ViolationCombination getMissing(Object bd) {
        if (this.matches(bd)) return ViolationCombination.EMPTY;
        return new ViolationInfo(null, expr);
    }

    @Override
    public String description() {
        return expr;
    }

}

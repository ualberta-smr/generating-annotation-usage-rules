package ca.ualberta.smr.newmodel.javaelements;

import ca.ualberta.smr.newmodel.StaticAnalysisRule;
import ca.ualberta.smr.newmodel.violationreport.ViolationCombination;
import ca.ualberta.smr.newmodel.violationreport.ViolationInfo;
import lombok.EqualsAndHashCode;
import lombok.Getter;
import lombok.RequiredArgsConstructor;
import lombok.experimental.Accessors;

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
    public ViolationCombination getMissing(Object bd, StaticAnalysisRule rule) {
        if (this.matches(bd)) return ViolationCombination.EMPTY;
        return new ViolationInfo(null, expr);
    }

    @Override
    public String description() {
        return expr;
    }

}

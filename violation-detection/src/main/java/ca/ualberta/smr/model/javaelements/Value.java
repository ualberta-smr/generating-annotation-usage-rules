package ca.ualberta.smr.model.javaelements;

import ca.ualberta.smr.model.StaticAnalysisRule;
import ca.ualberta.smr.model.violationreport.ViolationCombination;
import ca.ualberta.smr.model.violationreport.ViolationInfo;
import lombok.EqualsAndHashCode;
import lombok.Getter;
import lombok.RequiredArgsConstructor;
import lombok.experimental.Accessors;
import lombok.val;

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
        val valueExpression = (String) bd;
        // if the value is in quotation marks, remove them
        if (valueExpression.startsWith("\"") && valueExpression.endsWith("\"")
                || valueExpression.startsWith("'") && valueExpression.endsWith("'")) {
            return expr.equals(valueExpression.substring(1, valueExpression.length() - 1));
        }
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

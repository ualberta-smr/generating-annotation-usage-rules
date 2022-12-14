package ca.ualberta.smr.model.javaelements;

import ca.ualberta.smr.model.StaticAnalysisRule;
import ca.ualberta.smr.model.violationreport.ViolationCombination;
import ca.ualberta.smr.model.violationreport.ViolationInfo;
import lombok.EqualsAndHashCode;
import lombok.Getter;
import lombok.RequiredArgsConstructor;
import lombok.experimental.Accessors;

@RequiredArgsConstructor
@Getter
@Accessors(fluent = true)
@EqualsAndHashCode(callSuper = false)
public class Name extends ProgramElement {
    private final String name;

    public static AggregateCondition of(String name) {
        return AggregateCondition.single(new Name(name));
    }

    @Override
    public boolean matches(Object bd) {
        String nameString = (String) bd;
        return name.equals(nameString);
    }

    @Override
    public ViolationCombination getMissing(Object bd, StaticAnalysisRule rule) {
        if (this.matches(bd)) return ViolationCombination.EMPTY;
        return new ViolationInfo(null, name);
    }

    @Override
    public String description() {
        return name;
    }
}

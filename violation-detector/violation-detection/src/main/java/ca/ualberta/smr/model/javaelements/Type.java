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
public class Type extends ProgramElement {
    private final String name;

    public static AggregateCondition of(String name) {
        return AggregateCondition.single(new Type(name));
    }

    @Override
    public boolean matches(Object bd) {
        String typeString = (String) bd;
        return name.equals(typeString);
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

    public static class InterfaceType extends Type {

        public InterfaceType(String name) {
            super(name);
        }

        public static AggregateCondition of(String name) {
            return AggregateCondition.single(new InterfaceType(name));
        }

        @Override
        public ViolationCombination getMissing(Object bd, StaticAnalysisRule rule) {
            if (this.matches(bd)) return ViolationCombination.EMPTY;
            return new ViolationInfo(null, String.format("implementation of interface %s", super.name()));
        }
    }

    public static class ClassType extends Type {

        public ClassType(String name) {
            super(name);
        }

        public static AggregateCondition of(String name) {
            return AggregateCondition.single(new ClassType(name));
        }


        @Override
        public ViolationCombination getMissing(Object bd, StaticAnalysisRule rule) {
            if (this.matches(bd)) return ViolationCombination.EMPTY;
            return new ViolationInfo(null, String.format("extension of class %s", super.name()));
        }
    }
}
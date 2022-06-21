package ca.ualberta.smr.newmodel.javaelements;

import ca.ualberta.smr.newmodel.ViolationCombination;
import ca.ualberta.smr.newmodel.ViolationInfo;
import lombok.EqualsAndHashCode;
import lombok.Getter;
import lombok.RequiredArgsConstructor;
import lombok.experimental.Accessors;

import java.util.Collection;
import java.util.Collections;

import static java.util.Collections.emptyList;
import static java.util.Collections.singleton;

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
    public ViolationCombination getMissing(Object bd) {
        if (this.matches(bd)) return ViolationCombination.EMPTY;
        return new ViolationInfo(null, name);
    }

    @Override
    public String description() {
        return name;
    }
}

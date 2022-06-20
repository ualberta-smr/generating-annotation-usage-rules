package ca.ualberta.smr.newmodel.javaelements;

import lombok.EqualsAndHashCode;
import lombok.Getter;
import lombok.RequiredArgsConstructor;
import lombok.experimental.Accessors;

import static ca.ualberta.smr.utils.Utils.listOf;

@Getter
@Accessors(fluent = true)
@RequiredArgsConstructor
@EqualsAndHashCode
public class AnnotationParameter implements ProgramElement {

    private final AggregateCondition type;
    private final AggregateCondition name;
    private final AggregateCondition value;

    @Override
    public String toString() {
        String t = type.toString();
        String n = name.toString();
        String v = value.toString();
        return "<" + String.join(" ", listOf(t, n, v)) + ">";
    }

}

package ca.ualberta.smr.deprecated.model.javaelements;

import lombok.EqualsAndHashCode;
import lombok.Getter;
import lombok.RequiredArgsConstructor;
import lombok.Setter;
import lombok.experimental.Accessors;

import static ca.ualberta.smr.parsing.utils.GeneralUtility.listOf;

@Getter
@Setter
@Accessors(fluent = true)
@RequiredArgsConstructor
@EqualsAndHashCode
public class AnnotationParameter implements ProgramElement, WithType {

    private Condition<Type> type = Condition.empty(Type.class);
    private String name;

    public void type(Condition<Type> type) {
        this.type = type;
    }

    @Override
    public String toString() {
        String t = type.toString();
        String n = name == null ? "" : name;
        return String.join(" ", listOf(t, n));
    }

}
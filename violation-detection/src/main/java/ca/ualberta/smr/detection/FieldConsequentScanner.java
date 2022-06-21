package ca.ualberta.smr.detection;

import ca.ualberta.smr.newmodel.ViolationCombination;
import ca.ualberta.smr.newmodel.javaelements.AggregateCondition;
import com.github.javaparser.ast.body.FieldDeclaration;

import java.util.Collection;
import java.util.stream.Collectors;

public class FieldConsequentScanner {

    public static Collection<ViolationCombination> findViolations(Collection<FieldDeclaration> fieldDeclarations,
                                                                  AggregateCondition field) {
        return fieldDeclarations.stream()
                .map(md -> findViolations(md, field))
                .filter(v -> !v.isEmpty())
                .collect(Collectors.toList());
    }

    private static ViolationCombination findViolations(FieldDeclaration fieldDeclaration, AggregateCondition field) {
        return field.getMissing(fieldDeclaration);
    }

}

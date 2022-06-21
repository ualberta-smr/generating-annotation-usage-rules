package ca.ualberta.smr.detection;

import ca.ualberta.smr.newmodel.ViolationCombination;
import ca.ualberta.smr.newmodel.javaelements.AggregateCondition;
import com.github.javaparser.ast.body.ClassOrInterfaceDeclaration;

import java.util.Collection;
import java.util.stream.Collectors;

public class ClassConsequentScanner {

    public static Collection<ViolationCombination> findViolations(Collection<ClassOrInterfaceDeclaration> classDeclarations,
                                                                  AggregateCondition clazz) {
        return classDeclarations.stream()
                .map(md -> findViolations(md, clazz))
                .filter(v -> !v.isEmpty())
                .collect(Collectors.toList());
    }

    private static ViolationCombination findViolations(ClassOrInterfaceDeclaration classDeclaration, AggregateCondition clazz) {
        return clazz.getMissing(classDeclaration);
    }

}

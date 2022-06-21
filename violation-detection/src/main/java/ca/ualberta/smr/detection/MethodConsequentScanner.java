package ca.ualberta.smr.detection;

import ca.ualberta.smr.newmodel.violationreport.ViolationCombination;
import ca.ualberta.smr.newmodel.javaelements.AggregateCondition;
import com.github.javaparser.ast.body.MethodDeclaration;

import java.util.Collection;
import java.util.stream.Collectors;

public class MethodConsequentScanner {

    public static Collection<ViolationCombination> findViolations(Collection<MethodDeclaration> methodDeclarations,
                                                                  AggregateCondition method) {
        return methodDeclarations.stream()
                .map(md -> findViolations(md, method))
                .filter(v -> !v.isEmpty())
                .collect(Collectors.toList());
    }

    private static ViolationCombination findViolations(MethodDeclaration methodDeclaration, AggregateCondition method) {
        return method.getMissing(methodDeclaration);
    }

}
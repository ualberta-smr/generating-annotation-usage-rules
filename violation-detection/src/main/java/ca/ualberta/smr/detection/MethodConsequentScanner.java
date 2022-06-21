package ca.ualberta.smr.detection;

import ca.ualberta.smr.newmodel.StaticAnalysisRule;
import ca.ualberta.smr.newmodel.violationreport.ViolationCombination;
import ca.ualberta.smr.newmodel.javaelements.AggregateCondition;
import com.github.javaparser.ast.body.MethodDeclaration;

import java.util.Collection;
import java.util.stream.Collectors;

public class MethodConsequentScanner {

    public static Collection<ViolationCombination> findViolations(Collection<MethodDeclaration> methodDeclarations,
                                                                  StaticAnalysisRule rule) {
        return methodDeclarations.stream()
                .map(md -> findViolations(md, rule))
                .filter(v -> !v.isEmpty())
                .collect(Collectors.toList());
    }

    private static ViolationCombination findViolations(MethodDeclaration methodDeclaration, StaticAnalysisRule rule) {
        return rule.consequent().getMissing(methodDeclaration, rule);
    }

}

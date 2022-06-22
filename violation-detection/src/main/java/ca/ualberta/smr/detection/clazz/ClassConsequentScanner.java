package ca.ualberta.smr.detection.clazz;

import ca.ualberta.smr.model.StaticAnalysisRule;
import ca.ualberta.smr.model.violationreport.ViolationCombination;
import com.github.javaparser.ast.body.ClassOrInterfaceDeclaration;

import java.util.Collection;
import java.util.stream.Collectors;

public class ClassConsequentScanner {

    public static Collection<ViolationCombination> findViolations(Collection<ClassOrInterfaceDeclaration> classDeclarations,
                                                                  StaticAnalysisRule rule) {
        return classDeclarations.stream()
                .map(md -> findViolations(md, rule))
                .filter(v -> !v.isEmpty())
                .collect(Collectors.toList());
    }

    private static ViolationCombination findViolations(ClassOrInterfaceDeclaration classDeclaration, StaticAnalysisRule rule) {
        return rule.consequent().getMissing(classDeclaration, rule);
    }

}

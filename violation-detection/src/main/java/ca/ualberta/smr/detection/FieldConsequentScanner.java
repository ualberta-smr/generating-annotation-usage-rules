package ca.ualberta.smr.detection;

import ca.ualberta.smr.newmodel.StaticAnalysisRule;
import ca.ualberta.smr.newmodel.violationreport.ViolationCombination;
import ca.ualberta.smr.newmodel.javaelements.AggregateCondition;
import com.github.javaparser.ast.body.FieldDeclaration;

import java.util.Collection;
import java.util.stream.Collectors;

public class FieldConsequentScanner {

    public static Collection<ViolationCombination> findViolations(Collection<FieldDeclaration> fieldDeclarations,
                                                                  StaticAnalysisRule rule) {
        return fieldDeclarations.stream()
                .map(md -> findViolations(md, rule))
                .filter(v -> !v.isEmpty())
                .collect(Collectors.toList());
    }

    private static ViolationCombination findViolations(FieldDeclaration fieldDeclaration, StaticAnalysisRule rule) {
        return rule.consequent().getMissing(fieldDeclaration, rule);
    }

}

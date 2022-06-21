package ca.ualberta.smr.detection;

import ca.ualberta.smr.newmodel.StaticAnalysisRule;
import ca.ualberta.smr.newmodel.ViolationCombination;
import ca.ualberta.smr.newmodel.javaelements.Method;
import com.github.javaparser.ast.CompilationUnit;
import lombok.val;

import java.util.Collection;

import static java.util.Collections.emptyList;

public class MethodAnalyzer implements Analyzer {

    @Override
    public Collection<ViolationCombination> analyze(CompilationUnit cu, StaticAnalysisRule rule) {
        val methodDeclarations = MethodAntecedentScanner.findMethods(cu, rule.antecedent());
        if (methodDeclarations.isEmpty()) return emptyList();

        return MethodConsequentScanner.findViolations(methodDeclarations, rule.consequent());
    }

    @Override
    public boolean supports(Class<?> item) {
        return item.equals(Method.class);
    }
}


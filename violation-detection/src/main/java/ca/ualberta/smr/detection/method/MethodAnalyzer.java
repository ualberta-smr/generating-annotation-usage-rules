package ca.ualberta.smr.detection.method;

import ca.ualberta.smr.detection.Analyzer;
import ca.ualberta.smr.model.StaticAnalysisRule;
import ca.ualberta.smr.model.javaelements.ProgramElement;
import ca.ualberta.smr.model.violationreport.ViolationCombination;
import com.github.javaparser.ast.CompilationUnit;
import lombok.val;

import java.util.Collection;

import static java.util.Collections.emptyList;

public class MethodAnalyzer implements Analyzer {

    @Override
    public Collection<ViolationCombination> analyze(CompilationUnit cu, StaticAnalysisRule rule) {
        val methodDeclarations = MethodAntecedentScanner.findMethods(cu, rule.antecedent());
        if (methodDeclarations.isEmpty()) return emptyList();

        return MethodConsequentScanner.findViolations(methodDeclarations, rule);
    }

    @Override
    public boolean supports(ProgramElement.ProgramElementType type) {
        return type == ProgramElement.ProgramElementType.METHOD;
    }
}


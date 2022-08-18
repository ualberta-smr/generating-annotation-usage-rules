package ca.ualberta.smr.detection.clazz;

import ca.ualberta.smr.detection.Analyzer;
import ca.ualberta.smr.model.StaticAnalysisRule;
import ca.ualberta.smr.model.javaelements.ProgramElement;
import ca.ualberta.smr.model.violationreport.ViolationCombination;
import com.github.javaparser.ast.CompilationUnit;
import lombok.val;

import java.util.Collection;

import static java.util.Collections.emptyList;

public class ClassAnalyzer implements Analyzer {

    @Override
    public Collection<ViolationCombination> analyze(CompilationUnit cu, StaticAnalysisRule rule) {
        val classDeclarations = ClassAntecedentScanner.findClasses(cu, rule.antecedent());
        if (classDeclarations.isEmpty()) return emptyList();

        return ClassConsequentScanner.findViolations(classDeclarations, rule);
    }

    @Override
    public boolean supports(ProgramElement.ProgramElementType type) {
        return type == ProgramElement.ProgramElementType.CLASS;
    }
}


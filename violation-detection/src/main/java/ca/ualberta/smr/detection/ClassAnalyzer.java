package ca.ualberta.smr.detection;

import ca.ualberta.smr.newmodel.StaticAnalysisRule;
import ca.ualberta.smr.newmodel.javaelements.ProgramElement;
import ca.ualberta.smr.newmodel.violationreport.ViolationCombination;
import ca.ualberta.smr.newmodel.javaelements.JavaClass;
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


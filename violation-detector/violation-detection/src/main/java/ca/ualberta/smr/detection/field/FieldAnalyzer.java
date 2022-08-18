package ca.ualberta.smr.detection.field;

import ca.ualberta.smr.detection.Analyzer;
import ca.ualberta.smr.model.StaticAnalysisRule;
import ca.ualberta.smr.model.javaelements.ProgramElement;
import ca.ualberta.smr.model.violationreport.ViolationCombination;
import com.github.javaparser.ast.CompilationUnit;
import lombok.val;

import java.util.Collection;

import static java.util.Collections.emptyList;

public class FieldAnalyzer implements Analyzer {

    @Override
    public Collection<ViolationCombination> analyze(CompilationUnit cu, StaticAnalysisRule rule) {
        val fieldDeclarations = FieldAntecedentScanner.findFields(cu, rule.antecedent());
        if (fieldDeclarations.isEmpty()) return emptyList();

        return FieldConsequentScanner.findViolations(fieldDeclarations, rule);
    }

    @Override
    public boolean supports(ProgramElement.ProgramElementType type) {
        return type == ProgramElement.ProgramElementType.FIELD;
    }
}


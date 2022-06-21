package ca.ualberta.smr.detection;

import ca.ualberta.smr.newmodel.StaticAnalysisRule;
import ca.ualberta.smr.newmodel.ViolationCombination;
import ca.ualberta.smr.newmodel.javaelements.Field;
import com.github.javaparser.ast.CompilationUnit;
import lombok.val;

import java.util.Collection;

import static java.util.Collections.emptyList;

public class FieldAnalyzer implements Analyzer {

    @Override
    public Collection<ViolationCombination> analyze(CompilationUnit cu, StaticAnalysisRule rule) {
        val fieldDeclarations = FieldAntecedentScanner.findFields(cu, rule.antecedent());
        if (fieldDeclarations.isEmpty()) return emptyList();

        return FieldConsequentScanner.findViolations(fieldDeclarations, rule.consequent());
    }

    @Override
    public boolean supports(Class<?> item) {
        return item.equals(Field.class);
    }
}


package ca.ualberta.smr.analyzer;

import ca.ualberta.smr.antecedent.FieldAntecedentFilter;
import ca.ualberta.smr.consequent.FieldConsequentFilter;
import ca.ualberta.smr.model.javaelements.AnalysisItem;
import ca.ualberta.smr.model.javaelements.Field;
import ca.ualberta.smr.model.StaticAnalysisRule;
import ca.ualberta.smr.model.ViolationInfo;
import com.github.javaparser.ast.CompilationUnit;
import lombok.val;

import java.util.Collection;

import static ca.ualberta.smr.model.javaelements.Condition.single;

final public class FieldAnalyzer implements AnalysisRunner {

    @Override
    public Collection<ViolationInfo> analyze(CompilationUnit cu, StaticAnalysisRule rule) {
        val fieldDeclarations = FieldAntecedentFilter.doFilter(cu, single((Field) rule.antecedent()));
        return rule.consequent()
                .evaluate(r -> FieldConsequentFilter.filterFromFieldDeclarations(fieldDeclarations, single((Field) r)));
    }

    @Override
    public boolean supports(AnalysisItem item) {
        return item instanceof Field;
    }
}


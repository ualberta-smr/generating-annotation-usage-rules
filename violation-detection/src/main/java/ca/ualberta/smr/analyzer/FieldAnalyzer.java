package ca.ualberta.smr.analyzer;

import ca.ualberta.smr.antecedent.FieldAntecedentFilter;
import ca.ualberta.smr.consequent.FieldConsequentFilter;
import ca.ualberta.smr.model.javaelements.AnalysisItem;
import ca.ualberta.smr.model.javaelements.Condition;
import ca.ualberta.smr.model.javaelements.Field;
import ca.ualberta.smr.model.StaticAnalysisRule;
import ca.ualberta.smr.model.ViolationInfo;
import com.github.javaparser.ast.CompilationUnit;

import java.util.Collection;

final public class FieldAnalyzer implements AnalysisRunner {

    @Override
    public Collection<ViolationInfo> analyze(CompilationUnit cu, StaticAnalysisRule rule) {
        var fieldDeclarations = FieldAntecedentFilter.doFilter(cu, Condition.single((Field) rule.antecedent()));
        return FieldConsequentFilter.doFilter(fieldDeclarations, Condition.single((Field) rule.consequent()));
    }

    @Override
    public boolean supports(AnalysisItem item) {
        return item instanceof Field;
    }
}


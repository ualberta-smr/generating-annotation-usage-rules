package ca.ualberta.smr.analyzer;

import ca.ualberta.smr.antecedent.FieldAntecedentFilter;
import ca.ualberta.smr.consequent.FieldConsequentFilter;
import ca.ualberta.smr.model.javaelements.*;
import ca.ualberta.smr.model.*;
import com.github.javaparser.ast.CompilationUnit;
import lombok.val;

import java.util.Collection;

import static ca.ualberta.smr.model.javaelements.Condition.single;
import static java.util.Collections.emptyList;

final public class FieldAnalyzer implements AnalysisRunner {

    @Override
    @SuppressWarnings("unchecked")
    public Collection<ViolationInfo> analyze(CompilationUnit cu, StaticAnalysisRule rule) {
        val fieldDeclarations = FieldAntecedentFilter.doFilter(cu, (Condition<Field>) rule.antecedent());
        if (fieldDeclarations.isEmpty()) return emptyList();
        return rule.consequent()
                .evaluate(r -> FieldConsequentFilter.filter(fieldDeclarations, single((Field) r)));
    }

    @Override
    public boolean supports(AnalysisItem item) {
        return item instanceof Field;
    }

    @Override
    public boolean supports(Class<?> item) {
        return item.equals(Field.class);
    }
}


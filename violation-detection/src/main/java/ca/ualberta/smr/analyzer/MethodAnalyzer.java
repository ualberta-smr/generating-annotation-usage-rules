package ca.ualberta.smr.analyzer;

import ca.ualberta.smr.antecedent.MethodAntecedentFilter;
import ca.ualberta.smr.consequent.MethodConsequentFilter;
import ca.ualberta.smr.model.javaelements.*;
import ca.ualberta.smr.model.*;
import com.github.javaparser.ast.CompilationUnit;
import lombok.val;

import java.util.Collection;

import static java.util.Collections.emptyList;

final public class MethodAnalyzer implements AnalysisRunner {

    @Override
    @SuppressWarnings("unchecked")
    public Collection<ViolationInfo> analyze(CompilationUnit cu, StaticAnalysisRule rule) {
        val methodDeclarations = MethodAntecedentFilter.doFilter(cu, (Condition<Method>) rule.antecedent());
        if (methodDeclarations.isEmpty()) return emptyList();

        return rule.consequent()
                .evaluate(m -> MethodConsequentFilter.filter(methodDeclarations, Condition.single(m)));
    }

    @Override
    public boolean supports(Class<?> item) {
        return item.equals(Method.class);
    }
}
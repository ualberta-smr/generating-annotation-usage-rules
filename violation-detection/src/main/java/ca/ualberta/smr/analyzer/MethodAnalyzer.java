package ca.ualberta.smr.analyzer;

import ca.ualberta.smr.antecedent.MethodAntecedentFilter;
import ca.ualberta.smr.consequent.MethodConsequentFilter;
import ca.ualberta.smr.model.javaelements.AnalysisItem;
import ca.ualberta.smr.model.javaelements.Condition;
import ca.ualberta.smr.model.javaelements.Method;
import ca.ualberta.smr.model.StaticAnalysisRule;
import ca.ualberta.smr.model.ViolationInfo;
import com.github.javaparser.ast.CompilationUnit;
import lombok.val;

import java.util.Collection;

final public class MethodAnalyzer implements AnalysisRunner {

    @Override
    public Collection<ViolationInfo> analyze(CompilationUnit cu, StaticAnalysisRule rule) {
        val methodDeclarations = MethodAntecedentFilter.doFilter(cu, Condition.single((Method) rule.antecedent()));
        // TODO: actually it should not be flatmap, we need to consider the operation too
        return rule.consequent()
                .evaluate(m -> MethodConsequentFilter.filterFromMethodDeclarations(methodDeclarations, Condition.single((Method) m)));
    }

    @Override
    public boolean supports(AnalysisItem item) {
        return item instanceof Method;
    }
}
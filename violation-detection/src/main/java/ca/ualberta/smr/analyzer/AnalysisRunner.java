package ca.ualberta.smr.analyzer;

import ca.ualberta.smr.model.javaelements.AnalysisItem;
import ca.ualberta.smr.model.StaticAnalysisRule;
import ca.ualberta.smr.model.ViolationInfo;
import com.github.javaparser.ast.CompilationUnit;

import java.util.Collection;

public interface AnalysisRunner {
    Collection<ViolationInfo> analyze(CompilationUnit cu, StaticAnalysisRule rule);
    boolean supports(AnalysisItem item);
    boolean supports(Class<?> item);
}

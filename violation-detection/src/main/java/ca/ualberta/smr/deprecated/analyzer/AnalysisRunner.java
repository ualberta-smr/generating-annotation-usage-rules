package ca.ualberta.smr.deprecated.analyzer;

import ca.ualberta.smr.deprecated.model.StaticAnalysisRule;
import ca.ualberta.smr.deprecated.model.ViolationInfo;
import com.github.javaparser.ast.CompilationUnit;

import java.util.Collection;

public interface AnalysisRunner {
    Collection<ViolationInfo> analyze(CompilationUnit cu, StaticAnalysisRule rule);
    boolean supports(Class<?> item);
}

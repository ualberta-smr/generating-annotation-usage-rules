package ca.ualberta.smr.detection;

import ca.ualberta.smr.newmodel.StaticAnalysisRule;
import ca.ualberta.smr.newmodel.ViolationCombination;
import ca.ualberta.smr.newmodel.ViolationInfo;
import com.github.javaparser.ast.CompilationUnit;

import java.util.Collection;

public interface Analyzer {
    Collection<ViolationCombination> analyze(CompilationUnit cu, StaticAnalysisRule rule);
    boolean supports(Class<?> item);
}

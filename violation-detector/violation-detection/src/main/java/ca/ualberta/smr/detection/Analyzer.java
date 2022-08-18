package ca.ualberta.smr.detection;

import ca.ualberta.smr.model.StaticAnalysisRule;
import ca.ualberta.smr.model.javaelements.ProgramElement;
import ca.ualberta.smr.model.violationreport.ViolationCombination;
import com.github.javaparser.ast.CompilationUnit;

import java.util.Collection;

public interface Analyzer {
    Collection<ViolationCombination> analyze(CompilationUnit cu, StaticAnalysisRule rule);
    boolean supports(ProgramElement.ProgramElementType type);
}

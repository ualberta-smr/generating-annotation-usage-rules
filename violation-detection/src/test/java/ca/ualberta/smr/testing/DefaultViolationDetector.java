package ca.ualberta.smr.testing;

import ca.ualberta.smr.ViolationDetector;
import ca.ualberta.smr.analyzer.AnalysisRunner;
import ca.ualberta.smr.analyzer.ClassAnalyzer;
import ca.ualberta.smr.analyzer.FieldAnalyzer;
import ca.ualberta.smr.analyzer.MethodAnalyzer;
import ca.ualberta.smr.model.StaticAnalysisRule;
import ca.ualberta.smr.model.ViolationInfo;
import ca.ualberta.smr.typeresolution.TypeResolver;

import java.io.IOException;
import java.util.Collection;
import java.util.List;
import java.util.Map;

import static ca.ualberta.smr.utils.Utils.listOf;

class DefaultViolationDetector {

    private final ViolationDetector violationDetector;

    public DefaultViolationDetector() throws IOException {
        final TypeResolver typeResolver = new TypeResolver(System.getenv("JAR_FILES"));
        final List<AnalysisRunner> analyzers = listOf(new ClassAnalyzer(), new MethodAnalyzer(), new FieldAnalyzer());
        this.violationDetector = new ViolationDetector(typeResolver, RuleProvider.getRules(), analyzers);
    }

    public Map<StaticAnalysisRule, Collection<ViolationInfo>> analyze(String filename) {
        return violationDetector.detectViolations(filename);
    }

}

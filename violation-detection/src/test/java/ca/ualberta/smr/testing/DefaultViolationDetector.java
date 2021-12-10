package ca.ualberta.smr.testing;

import ca.ualberta.smr.ViolationDetector;
import ca.ualberta.smr.analyzer.AnalysisRunner;
import ca.ualberta.smr.analyzer.ClassAnalyzer;
import ca.ualberta.smr.analyzer.FieldAnalyzer;
import ca.ualberta.smr.analyzer.MethodAnalyzer;
import ca.ualberta.smr.model.StaticAnalysisRule;
import ca.ualberta.smr.model.ViolationInfo;
import ca.ualberta.smr.rules.RuleParser;
import ca.ualberta.smr.typeresolution.TypeResolver;
import lombok.SneakyThrows;

import java.io.InputStream;
import java.util.Collection;
import java.util.List;
import java.util.Map;

import static ca.ualberta.smr.utils.Utils.listOf;

class DefaultViolationDetector {

    private final ViolationDetector violationDetector;

    @SneakyThrows
    public DefaultViolationDetector(String jarPath) {
        final TypeResolver typeResolver = new TypeResolver(jarPath);
        final List<AnalysisRunner> analyzers = listOf(new ClassAnalyzer(), new MethodAnalyzer(), new FieldAnalyzer());
        final Collection<StaticAnalysisRule> rules = getRules();
        this.violationDetector = new ViolationDetector(typeResolver, rules, analyzers);
    }

    public Map<StaticAnalysisRule, Collection<ViolationInfo>> analyze(String filename) {
        return violationDetector.detectViolations(filename);
    }

    @SneakyThrows
    private static Collection<StaticAnalysisRule> getRules() {
        final InputStream is = DefaultViolationDetector.class.getResourceAsStream("/rules.json");
        return RuleParser.parseRules(is);
    }

}

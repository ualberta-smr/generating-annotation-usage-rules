package ca.ualberta.smr.testing;

import ca.ualberta.smr.detection.ViolationDetector;
import ca.ualberta.smr.detection.*;
import ca.ualberta.smr.detection.clazz.ClassAnalyzer;
import ca.ualberta.smr.detection.field.FieldAnalyzer;
import ca.ualberta.smr.detection.method.MethodAnalyzer;
import ca.ualberta.smr.model.StaticAnalysisRule;
import ca.ualberta.smr.model.violationreport.ViolationCombination;
import ca.ualberta.smr.parsing.rules.RuleParser;
import ca.ualberta.smr.typeresolution.TypeResolver;
import lombok.SneakyThrows;

import java.io.InputStream;
import java.util.Collection;
import java.util.List;
import java.util.Map;

import static ca.ualberta.smr.parsing.utils.GeneralUtility.listOf;

class DefaultViolationDetector {

    private final ViolationDetector violationDetector;

    @SneakyThrows
    public DefaultViolationDetector(String jarPath) {
        final TypeResolver typeResolver = new TypeResolver(jarPath);
        final List<Analyzer> analyzers = listOf(new ClassAnalyzer(), new MethodAnalyzer(), new FieldAnalyzer());
        final Collection<StaticAnalysisRule> rules = getRules();
        this.violationDetector = new ViolationDetector(typeResolver, rules, analyzers);
    }

    public Map<StaticAnalysisRule, Collection<ViolationCombination>> analyze(String filename) {
        return violationDetector.detectViolations(filename);
    }

    @SneakyThrows
    private static Collection<StaticAnalysisRule> getRules() {
        final InputStream is = DefaultViolationDetector.class.getResourceAsStream("/rules.json");
        return RuleParser.parseRules(is);
    }

}

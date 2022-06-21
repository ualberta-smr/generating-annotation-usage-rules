package ca.ualberta.smr.testing2.testing;

import ca.ualberta.smr.RealViolationDetector;
import ca.ualberta.smr.detection.*;
import ca.ualberta.smr.newmodel.StaticAnalysisRule;
import ca.ualberta.smr.newmodel.violationreport.ViolationCombination;
import ca.ualberta.smr.newrule.RuleParser;
import ca.ualberta.smr.typeresolution.TypeResolver;
import lombok.SneakyThrows;

import java.io.InputStream;
import java.util.Collection;
import java.util.List;
import java.util.Map;
import java.util.stream.Collectors;

import static ca.ualberta.smr.utils.Utils.listOf;

class DefaultViolationDetector {

    private final RealViolationDetector violationDetector;

    @SneakyThrows
    public DefaultViolationDetector(String jarPath) {
        final TypeResolver typeResolver = new TypeResolver(jarPath);
        final List<Analyzer> analyzers = listOf(new ClassAnalyzer(), new MethodAnalyzer(), new FieldAnalyzer());
        final Collection<StaticAnalysisRule> rules = getRules();
        this.violationDetector = new RealViolationDetector(typeResolver, rules, analyzers);
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

package ca.ualberta.smr.testing;

import ca.ualberta.smr.model.StaticAnalysisRule;
import ca.ualberta.smr.model.violationreport.ViolationCombination;
import ca.ualberta.smr.parsing.rules.Rule;
import ca.ualberta.smr.parsing.rules.RuleParser;
import jdk.nashorn.internal.ir.annotations.Ignore;
import org.junit.jupiter.api.Test;

import java.util.Collection;
import java.util.Map;
import java.util.stream.Collectors;

/**
 * Useful for testing against real files that reside somewhere in the file system
 */
public class DummyClassTest {

    final DefaultViolationDetector defaultDetector = new DefaultViolationDetector("src/test/data/jarfiles");

    @Test
    @Ignore
    public void test() {
        final Map<StaticAnalysisRule, Collection<ViolationCombination>> violations = defaultDetector.analyze(
                ""
        );

        final Collection<String> actualViolations = violations.entrySet().stream()
                .filter(e -> !e.getValue().isEmpty())
                .map(Map.Entry::getKey)
                .map(StaticAnalysisRule::toString)
                .collect(Collectors.toSet());

        System.out.println(actualViolations.size());
    }

}

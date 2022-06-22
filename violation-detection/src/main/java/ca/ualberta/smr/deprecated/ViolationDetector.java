package ca.ualberta.smr.deprecated;

import ca.ualberta.smr.deprecated.analyzer.AnalysisRunner;
import ca.ualberta.smr.deprecated.model.StaticAnalysisRule;
import ca.ualberta.smr.deprecated.model.ViolationInfo;
import ca.ualberta.smr.typeresolution.TypeResolver;
import ca.ualberta.smr.parsing.utils.Pair;
import com.github.javaparser.ast.CompilationUnit;
import lombok.RequiredArgsConstructor;
import lombok.var;

import java.util.*;
import java.util.stream.Collectors;

import static java.util.Collections.emptyMap;

@RequiredArgsConstructor
public class ViolationDetector {

    private final TypeResolver typeResolver;
    private final Collection<StaticAnalysisRule> rules;
    private final Collection<AnalysisRunner> analyzers;

    public Map<StaticAnalysisRule, Collection<ViolationInfo>> detectViolations(final String filename) {
        final Optional<CompilationUnit> maybeCU = typeResolver.getResolvedCompilationUnit(filename);

        // TODO: maybe should throw an exception because file could not be compiled?
        if (!maybeCU.isPresent()) return emptyMap();

        final var cu = maybeCU.get();

        return rules.stream()
                .map(rule -> {
                    var violations = findAnalyzer(rule)
                            .map(e -> e.analyze(cu, rule))
                            .orElseThrow(() -> new RuntimeException("Could not find an analyzer"));
                    return new Pair<>(rule, violations);
                }).collect(Collectors.toMap(Pair::key, Pair::value));
    }

    private Optional<AnalysisRunner> findAnalyzer(StaticAnalysisRule rule) {
        return analyzers.stream()
                .filter(a -> a.supports(rule.antecedent().getType()))
                .findFirst();
    }

}

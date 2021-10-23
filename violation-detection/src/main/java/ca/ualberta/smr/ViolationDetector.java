package ca.ualberta.smr;

import ca.ualberta.smr.analyzer.*;
import ca.ualberta.smr.model.*;
import ca.ualberta.smr.typeresolution.TypeResolver;
import ca.ualberta.smr.utils.Pair;
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
                .filter(a -> a.supports(rule.antecedent()))
                .findFirst();
    }

}

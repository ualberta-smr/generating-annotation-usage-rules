package ca.ualberta.smr;

import ca.ualberta.smr.antecedent.*;
import ca.ualberta.smr.consequent.*;
import ca.ualberta.smr.model.*;
import com.github.javaparser.ast.CompilationUnit;
import com.github.javaparser.ast.body.*;
import lombok.RequiredArgsConstructor;

import java.util.*;
import java.util.function.BiFunction;
import java.util.function.Function;

import static java.util.Collections.emptyMap;

@RequiredArgsConstructor
public class ViolationDetector {

    private final TypeResolver typeResolver;
    private final Collection<StaticAnalysisRule> rules;

    public Map<StaticAnalysisRule, Collection<ViolationInfo>> detectViolations(String filename) {
        final Optional<CompilationUnit> maybeCU = typeResolver
                .getResolvedCompilationUnit(filename);

        // TODO: maybe should throw an exception
        if (maybeCU.isEmpty()) return emptyMap();

        final var cu = maybeCU.get();
        var results = new HashMap<StaticAnalysisRule, Collection<ViolationInfo>>();
        for (var rule : rules) {
            var res = runAnalysis(rule).apply(cu);
            for (Map.Entry<? extends BodyDeclaration<?>, Collection<ViolationInfo>> collectionEntry : res.entrySet()) {
                for (ViolationInfo violationInfo : collectionEntry.getValue()) {
                    System.out.println(violationInfo.treeElement() == collectionEntry.getKey());
                    System.out.println(violationInfo.missingElements());
                    System.out.println("=======");
                }
            }
        }

        return results;
    }

    private AnalysisFunction runAnalysis(final StaticAnalysisRule rule) {
        Map<Class<? extends AnalysisItem>, AnalysisFunction> map = new HashMap<>();

        map.put(JavaClass.class, cu -> runAnalysisOnClass(cu, rule));
        map.put(Method.class, cu -> runAnalysisOnMethod(cu, rule));
        map.put(Field.class, cu -> runAnalysisOnField(cu, rule));

        return map.get(rule.antecedent().getClass());
    }

    private Map<? extends BodyDeclaration<? extends BodyDeclaration<?>>, Collection<ViolationInfo>> runAnalysisOnClass(CompilationUnit cu, StaticAnalysisRule rule) {
        var classDeclarations = ClassAntecedentFilter.doFilter(cu, (JavaClass) rule.antecedent());
        return classDelegator(rule.consequent()).apply(classDeclarations, rule.consequent());
    }

    private Map<? extends BodyDeclaration<? extends BodyDeclaration<?>>, Collection<ViolationInfo>> runAnalysisOnMethod(CompilationUnit cu, StaticAnalysisRule rule) {
        var methodDeclarations = MethodAntecedentFilter.doFilter(cu, (Method) rule.antecedent());
        return MethodConsequentFilter.doFilter(methodDeclarations, (Method) rule.consequent());
    }

    private Map<? extends BodyDeclaration<? extends BodyDeclaration<?>>, Collection<ViolationInfo>> runAnalysisOnField(CompilationUnit cu, StaticAnalysisRule rule) {
        var fieldDeclarations = FieldAntecedentFilter.doFilter(cu, (Field) rule.consequent());
        return FieldConsequentFilter.doFilter(fieldDeclarations, (Field) rule.consequent());
    }

    private ConsequentFilterFunction classDelegator(AnalysisItem consequent) {
        return CLASS_CONSEQUENT_FILTER_MAP.get(consequent.getClass());
    }

    private static final Map<Class<? extends AnalysisItem>, ConsequentFilterFunction> CLASS_CONSEQUENT_FILTER_MAP = initializeClassConsequentFilterMap();

    private static Map<Class<? extends AnalysisItem>, ConsequentFilterFunction> initializeClassConsequentFilterMap() {
        Map<Class<? extends AnalysisItem>, ConsequentFilterFunction> map = new HashMap<>();

        map.put(JavaClass.class, (items, consequent) -> ClassConsequentFilter.doFilter(items, (JavaClass) consequent));
        map.put(Method.class, (items, consequent) -> MethodConsequentFilter.doFilter(items, (Method) consequent));
        map.put(Field.class, (items, consequent) -> FieldConsequentFilter.doFilter(items, (Field) consequent));

        return map;
    }

    @FunctionalInterface
    interface ConsequentFilterFunction extends BiFunction<Collection<ClassOrInterfaceDeclaration>, AnalysisItem, Map<? extends BodyDeclaration<? extends BodyDeclaration<?>>, Collection<ViolationInfo>>> {

    }

    @FunctionalInterface
    interface AnalysisFunction extends Function<CompilationUnit, Map<? extends BodyDeclaration<? extends BodyDeclaration<?>>, Collection<ViolationInfo>>> {

    }
}


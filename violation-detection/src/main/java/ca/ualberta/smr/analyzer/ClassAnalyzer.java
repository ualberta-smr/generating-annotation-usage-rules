package ca.ualberta.smr.analyzer;

import ca.ualberta.smr.antecedent.ClassAntecedentFilter;
import ca.ualberta.smr.consequent.ClassConsequentFilter;
import ca.ualberta.smr.consequent.FieldConsequentFilter;
import ca.ualberta.smr.consequent.MethodConsequentFilter;
import ca.ualberta.smr.model.*;
import ca.ualberta.smr.model.javaelements.*;
import com.github.javaparser.ast.CompilationUnit;
import com.github.javaparser.ast.body.ClassOrInterfaceDeclaration;

import java.util.Collection;
import java.util.HashMap;
import java.util.Map;
import java.util.function.BiFunction;

final public class ClassAnalyzer implements AnalysisRunner {

    @Override
    public Collection<ViolationInfo> analyze(CompilationUnit cu, StaticAnalysisRule rule) {
        var classDeclarations = ClassAntecedentFilter.doFilter(cu, (JavaClass) rule.antecedent());
        return classConsequentDelegator(rule.consequent())
                .apply(classDeclarations, rule.consequent());
    }

    @Override
    public boolean supports(AnalysisItem item) {
        return item instanceof JavaClass;
    }

    private ConsequentFilterFunction classConsequentDelegator(AnalysisItem consequent) {
        return CLASS_CONSEQUENT_FILTER_MAP.get(consequent.getClass());
    }

    private static final Map<Class<? extends AnalysisItem>, ConsequentFilterFunction> CLASS_CONSEQUENT_FILTER_MAP = initializeClassConsequentFilterMap();

    private static Map<Class<? extends AnalysisItem>, ConsequentFilterFunction> initializeClassConsequentFilterMap() {
        Map<Class<? extends AnalysisItem>, ConsequentFilterFunction> map = new HashMap<>();

        map.put(JavaClass.class, (items, consequent) -> ClassConsequentFilter.doFilter(items, Condition.single((JavaClass) consequent)));
        map.put(Method.class, (items, consequent) -> MethodConsequentFilter.doFilter(items, Condition.single((Method) consequent)));
        map.put(Field.class, (items, consequent) -> FieldConsequentFilter.doFilter(items, Condition.single((Field) consequent)));

        return map;
    }

    @FunctionalInterface
    interface ConsequentFilterFunction extends BiFunction<Collection<ClassOrInterfaceDeclaration>, AnalysisItem, Collection<ViolationInfo>> {
        // acts like a type alias
    }
}
package ca.ualberta.smr.analyzer;

import ca.ualberta.smr.antecedent.ClassAntecedentFilter;
import ca.ualberta.smr.consequent.ClassConsequentFilter;
import ca.ualberta.smr.consequent.FieldConsequentFilter;
import ca.ualberta.smr.consequent.MethodConsequentFilter;
import ca.ualberta.smr.model.*;
import ca.ualberta.smr.model.javaelements.*;
import com.github.javaparser.ast.CompilationUnit;
import com.github.javaparser.ast.body.ClassOrInterfaceDeclaration;
import lombok.val;

import java.util.Collection;
import java.util.HashMap;
import java.util.Map;
import java.util.function.BiFunction;

import static java.util.Collections.emptyList;

final public class ClassAnalyzer implements AnalysisRunner {

    @Override
    public Collection<ViolationInfo> analyze(CompilationUnit cu, StaticAnalysisRule rule) {
        val classDeclarations = ClassAntecedentFilter.doFilter(cu, (JavaClass) rule.antecedent());
        if (classDeclarations.isEmpty()) return emptyList();

        val consequentType = rule.consequent().getType();
        return findCorrectConsequentFilter(consequentType)
                .filter(classDeclarations, rule.consequent());
    }

    @Override
    public boolean supports(AnalysisItem item) {
        return item instanceof JavaClass;
    }

    private ConsequentFilterFunction findCorrectConsequentFilter(Class<? extends AnalysisItem> consequentType) {
        return CLASS_CONSEQUENT_FILTER_MAP.get(consequentType);
    }

    private static final Map<Class<? extends AnalysisItem>, ConsequentFilterFunction> CLASS_CONSEQUENT_FILTER_MAP = initializeClassConsequentFilterMap();

    @SuppressWarnings("unchecked")
    private static Map<Class<? extends AnalysisItem>, ConsequentFilterFunction> initializeClassConsequentFilterMap() {
        Map<Class<? extends AnalysisItem>, ConsequentFilterFunction> map = new HashMap<>();

        map.put(JavaClass.class, (items, consequent) -> ClassConsequentFilter.filterFromClassDeclarations(items, (Condition<JavaClass>) consequent));
        map.put(Method.class, (items, consequent) -> MethodConsequentFilter.filterFromClassDeclarations(items, (Condition<Method>) consequent));
        map.put(Field.class, (items, consequent) -> FieldConsequentFilter.filterFromClassDeclarations(items, (Condition<Field>) consequent));

        return map;
    }

    @FunctionalInterface
    interface ConsequentFilterFunction extends BiFunction<Collection<ClassOrInterfaceDeclaration>, Condition<? extends AnalysisItem>, Collection<ViolationInfo>> {
        // acts like a type alias

        default Collection<ViolationInfo> filter(Collection<ClassOrInterfaceDeclaration> t, Condition<? extends AnalysisItem> u) {
            return apply(t, u);
        }
    }
}
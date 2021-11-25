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

import static ca.ualberta.smr.model.javaelements.Condition.single;
import static java.util.Collections.emptyList;

final public class ClassAnalyzer implements AnalysisRunner {

    @Override
    @SuppressWarnings("unchecked")
    public Collection<ViolationInfo> analyze(CompilationUnit cu, StaticAnalysisRule rule) {
        val classDeclarations = ClassAntecedentFilter.doFilter(cu, (Condition<JavaClass>) rule.antecedent());
        if (classDeclarations.isEmpty()) return emptyList();

        val consequentType = rule.consequent().getType();
        return findCorrectConsequentFilter(consequentType)
                .filter(classDeclarations, rule);
    }

    @Override
    public boolean supports(AnalysisItem item) {
        return item instanceof JavaClass;
    }

    @Override
    public boolean supports(Class<?> item) {
        return item.equals(JavaClass.class);
    }

    /**
     * Based on the consequent type, the filtering process can be delegated to 3 different consequent filters, <br>
     * and this method decides which one it will be.
     * @param consequentType type of the consequent element
     * @return function that will do the analysis/filtering
     */
    private ConsequentFilterFunction findCorrectConsequentFilter(Class<? extends AnalysisItem> consequentType) {
        return CLASS_CONSEQUENT_FILTER_MAP.get(consequentType);
    }

    private static final Map<Class<? extends AnalysisItem>, ConsequentFilterFunction> CLASS_CONSEQUENT_FILTER_MAP = initializeClassConsequentFilterMap();

    @SuppressWarnings("unchecked")
    private static Map<Class<? extends AnalysisItem>, ConsequentFilterFunction> initializeClassConsequentFilterMap() {
        Map<Class<? extends AnalysisItem>, ConsequentFilterFunction> map = new HashMap<>();

        map.put(JavaClass.class, ClassConsequentFilter::filterFromClassDeclarations);
        map.put(Method.class, (items, rule) -> MethodConsequentFilter.filterFromClassDeclarations(items, (Condition<Method>) rule.consequent()));
        map.put(Field.class, (items, rule) -> FieldConsequentFilter.filterFromClassDeclarations(items, (Condition<Field>) rule.consequent()));

        return map;
    }

    /**
     * Represents consequent filters <br>
     * It's used to simplify complicated BiFunction signature
     */
    @FunctionalInterface
    interface ConsequentFilterFunction extends BiFunction<Collection<ClassOrInterfaceDeclaration>, StaticAnalysisRule, Collection<ViolationInfo>> {

        /**
         * This function just gives more context to the apply function of BiFunction class
         */
        default Collection<ViolationInfo> filter(Collection<ClassOrInterfaceDeclaration> t, StaticAnalysisRule u) {
            return apply(t, u);
        }

    }
}
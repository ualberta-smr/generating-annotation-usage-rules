package ca.ualberta.smr.utils;

import ca.ualberta.smr.model.StaticAnalysisRule;
import ca.ualberta.smr.model.javaelements.AnalysisItem;
import ca.ualberta.smr.model.javaelements.Condition;
import ca.ualberta.smr.model.javaelements.JavaClass;
import lombok.val;

import java.util.Collection;

/**
 * WIP
 * <p>
 * The purpose: Optimizing the generated rules
 */
public class StaticRuleOptimizer {

    // FIXME:
    public static StaticAnalysisRule optimize(StaticAnalysisRule rule) {
//        final AnalysisItem rawAntecedent = rule.antecedent();
//        AnalysisItem antecedent = rawAntecedent;
//        if (rawAntecedent instanceof JavaClass) {
//            antecedent = optimize((JavaClass) rawAntecedent);
//        }
//        return new StaticAnalysisRule(rule.name(), antecedent, rule.consequent(), rule.description());
        return null;
    }

    private static AnalysisItem optimize(JavaClass jc) {
        boolean onlyMethod = jc.method().isNotEmpty()
                && jc.field().isEmpty()
                && jc.annotations().isEmpty()
                && jc.extendedClass().isEmpty()
                && jc.implementedInterfaces().isEmpty();

        if (onlyMethod) {
            if (jc.method().isSingle()) {
                return jc.method().map(m -> m).stream().findFirst().get();
            }
        }

        boolean onlyField = jc.field().isNotEmpty()
                && jc.method().isEmpty()
                && jc.annotations().isEmpty()
                && jc.extendedClass().isEmpty()
                && jc.implementedInterfaces().isEmpty();

        if (onlyField) {
            if (jc.field().isSingle()) {
                return jc.field().map(m -> m).stream().findFirst().get();
            }
        }

        return jc;
    }

    public static Condition<JavaClass> optimize(Condition<JavaClass> classCondition) {
        final Collection<JavaClass> elements = classCondition.getElements();

        val classesOnlyContainAnnotations = classCondition.isNotEmpty() && elements.stream().allMatch(jc ->
                !jc.annotations().isEmpty()
                        && jc.method().isEmpty()
                        && jc.field().isEmpty()
                        && jc.extendedClass().isEmpty()
                        && jc.implementedInterfaces().isEmpty());

        if (classesOnlyContainAnnotations) {
            val annotations = elements.stream()
                    .map(JavaClass::annotations)
                    .flatMap(Collection::stream)
                    .filter(Condition::isNotEmpty)
                    .reduce((a1, a2) -> a1.plus(a2, classCondition.getOperation()))
                    .get(); // surely, the stream isn't empty to yield no results

            // create the new Java class object
            final JavaClass javaClass = new JavaClass();
            javaClass.annotations().add(annotations);
            return Condition.single(javaClass);
        }

        return classCondition;
    }


}

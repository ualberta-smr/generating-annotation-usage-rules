package ca.ualberta.smr.utils;

import ca.ualberta.smr.model.javaelements.Condition;
import ca.ualberta.smr.model.javaelements.JavaClass;
import org.junit.jupiter.api.Test;

import static ca.ualberta.smr.model.javaelements.Annotation.annotation;
import static ca.ualberta.smr.model.javaelements.Condition.any;
import static ca.ualberta.smr.model.javaelements.Condition.single;
import static org.junit.jupiter.api.Assertions.*;

class StaticRuleOptimizerTest {

    @Test
    void test1() {
        final JavaClass jc1 = new JavaClass();
        jc1.annotations().add(single(annotation("A")));

        final JavaClass jc2 = new JavaClass();
        jc2.annotations().add(single(annotation("B")));

        final Condition<JavaClass> actualOptimizedClassCondition = StaticRuleOptimizer.optimize(Condition.any(
                jc1, jc2
        ));

        final JavaClass javaClass = new JavaClass();
        javaClass.annotations().add(
                any(
                        annotation("A"), annotation("B")
                )
        );
        final Condition<JavaClass> expected = single(javaClass);

        assertEquals(expected, actualOptimizedClassCondition);

    }

}